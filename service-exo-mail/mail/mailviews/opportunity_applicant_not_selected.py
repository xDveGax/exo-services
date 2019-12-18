from django.utils.translation import ugettext_lazy as _

from utils.faker_factory import faker

from ..mails import BaseMailView


class OpportunityApplicantNotSelectedMailView(BaseMailView):
    """
    """
    template_name = 'mails/opportunity/opportunity_applicant_not_selected.html'

    mandatory_mail_args = [
        'title',
        'applicant_name',
        'created_by_name',
        'public_url',
    ]

    subject = _('Sorry, the opportunity has been assigned')
    section = 'opportunities'

    def get_mock_data(self, optional=True):
        mock_data = {
            'title': '[Role] for [Project Name]',
            'applicant_name': '[EM Name]',
            'created_by_name': '[SDM Name]',
            'disable_notification_url': None,
            'public_url': '/{}'.format(faker.uri_path()),
        }
        return mock_data
