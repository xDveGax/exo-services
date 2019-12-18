from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

from actstream import action
from model_utils.models import TimeStampedModel
from ratings.models import Rating

from ..rating_enum import ProjectEnum
from ..signals_define import signal_post_overall_rating_team_step_save


class TeamStep(TimeStampedModel):
    team = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
        related_name='steps',
    )
    step = models.ForeignKey(
        'project.Step',
        on_delete=models.CASCADE,
        related_name='teams',
    )
    ratings = GenericRelation(
        'ratings.OverallRating',
        content_type_field='context_content_type',
        object_id_field='context_object_id',
        related_query_name='team_steps')

    def __str__(self):
        return '{} - {}'.format(self.step.name, self.team.name)

    @property
    def project(self):
        return self.team.project

    @property
    def ratings_user(self):
        rating = self.ratings.first()
        if not rating:
            return {}
        return dict(rating.ratings.values_list('user_id', 'rating'))

    @property
    def feedbacks_user(self):
        return dict(
            self.action_object_actions.filter(
                verb=settings.TEAM_ACTION_FEEDBACK_WEEKLY,
            ).values_list('actor_object_id', 'description'))

    def target_rating(self, user_from):
        if self.team.user_is_basic(user_from):
            return ProjectEnum.COACH, self.team.coaches.first()
        elif self.team.user_is_admin(user_from):
            return ProjectEnum.HEAD, self.project.head_coaches.first()
        return None, None

    def check_user_can_rate(self, user_from, raise_exceptions=True):
        _, user = self.target_rating(user_from)
        if user is None and raise_exceptions:
            raise ValidationError("User can't rate")
        return user is not None

    def do_feedback(self, user_from, rating, comment=None):
        action.send(
            user_from,
            verb=settings.TEAM_ACTION_FEEDBACK_WEEKLY,
            action_object=self,
            description=str(rating))
        action.send(
            user_from,
            verb=settings.TEAM_ACTION_COMMENT_WEEKLY,
            action_object=self,
            description=comment)

    def do_rating(self, user_from, rating, comment=None):
        self.check_user_can_rate(user_from)
        relation_type, user = self.target_rating(user_from)

        category = settings.RATINGS_STEP_FEEDBACK
        Rating.update(
            rating_context=self,
            rating_object=user,
            user=user_from,
            rating=rating,
            category=category,
            comment=comment,
        )
        signal_post_overall_rating_team_step_save.send(
            sender=self.__class__,
            team_step=self,
            user=user,
            relation_type=relation_type)
        return rating

    def get_rating_for_user(self, user):
        try:
            return self.ratings_user.get(user.pk)
        except TypeError:
            return None

    def get_feedback_for_user(self, user):
        try:
            return eval(self.feedbacks_user.get(str(user.pk)))
        except TypeError:
            return None

    def get_last_action_feedback(self, user, verb):
        ct = ContentType.objects.get_for_model(user)
        return self.action_object_actions.filter(
            verb=verb,
            actor_content_type=ct,
            actor_object_id=user.id).last()
