# python 3 imports
from __future__ import absolute_import, unicode_literals

# python imports
import logging

# 3rd. libraries imports
from appconf import AppConf

# django imports
from django.conf import settings  # noqa

logger = logging.getLogger(__name__)


class AssignmentConfig(AppConf):
    APP_NAME = 'assignment'

    PERMS_VIEW_ASSIGNMENT = 'team_assignment_view'
    TEAM_ALL_PERMISSIONS = (
        (PERMS_VIEW_ASSIGNMENT, 'Can see assignment'),
    )

    TAG_DONE = 'done'

    INFORMATION_BLOCK_CH_TYPE_TASK = 'T'
    INFORMATION_BLOCK_CH_TYPE_TEXT = 'E'
    INFORMATION_BLOCK_CH_TYPE_RESOURCE = 'R'
    INFORMATION_BLOCK_CH_TYPE_ADVICE = 'A'
    INFORMATION_BLOCK_CH_TYPE_DEFAULT = INFORMATION_BLOCK_CH_TYPE_TASK

    INFORMATION_BLOCK_CH_TYPES = (
        (INFORMATION_BLOCK_CH_TYPE_TASK, 'Task'),
        (INFORMATION_BLOCK_CH_TYPE_TEXT, 'Text'),
        (INFORMATION_BLOCK_CH_TYPE_RESOURCE, 'Resource'),
        (INFORMATION_BLOCK_CH_TYPE_ADVICE, 'Advice'),
    )

    INFORMATION_BLOCK_CH_SECTION_LEARN = 'L'
    INFORMATION_BLOCK_CH_SECTION_DELIVER = 'D'

    INFORMATION_BLOCK_CH_SECTIONS = (
        (INFORMATION_BLOCK_CH_SECTION_LEARN, 'Learn'),
        (INFORMATION_BLOCK_CH_SECTION_DELIVER, 'Deliver'),
    )

    INFORMATION_BLOCK_CH_SECTION_DEFAULT = INFORMATION_BLOCK_CH_SECTION_LEARN

    TASK_TEAM_CH_STATUS_TO_DO = 'T'
    TASK_TEAM_CH_STATUS_DONE = 'D'
    TASK_TEAM_CH_STATUS_DEFAULT = TASK_TEAM_CH_STATUS_TO_DO

    TASK_TEAM_CH_STATUS = (
        (TASK_TEAM_CH_STATUS_TO_DO, 'To Do'),
        (TASK_TEAM_CH_STATUS_DONE, 'Done'),
    )

    CH_RESOURCE_ITEM_STATUS_AVAILABLE = 'A'
    CH_RESOURCE_ITEM_STATUS_UVAILABLE = 'U'
    CH_RESOURCE_ITEM_STATUS_DEFAULT = CH_RESOURCE_ITEM_STATUS_AVAILABLE

    CH_RESOURCE_ITEM_STATUS = (
        (CH_RESOURCE_ITEM_STATUS_AVAILABLE, 'Available'),
        (CH_RESOURCE_ITEM_STATUS_UVAILABLE, 'Unavailable'),
    )

    CH_RESOURCE_ITEM_TYPE_PDF = 'P'
    CH_RESOURCE_ITEM_TYPE_DOC = 'D'
    CH_RESOURCE_ITEM_TYPE_SLIDES = 'S'
    CH_RESOURCE_ITEM_TYPE_FORM = 'F'
    CH_RESOURCE_ITEM_TYPE_SPREEDSHET = 'R'
    CH_RESOURCE_ITEM_TYPE_VIDEO = 'V'
    CH_RESOURCE_ITEM_TYPE_LINKS = 'L'
    CH_RESOURCE_ITEM_TYPE_IMG = 'I'
    CH_RESOURCE_ITEM_TYPE_UPLOADER = 'U'
    CH_RESOURCE_ITEM_TYPE_DEFAULT = CH_RESOURCE_ITEM_TYPE_PDF

    CH_RESOURCE_ITEM_TYPE = (
        (CH_RESOURCE_ITEM_TYPE_PDF, 'PDF'),
        (CH_RESOURCE_ITEM_TYPE_DOC, 'Document'),
        (CH_RESOURCE_ITEM_TYPE_SLIDES, 'Slides'),
        (CH_RESOURCE_ITEM_TYPE_FORM, 'Form'),
        (CH_RESOURCE_ITEM_TYPE_SPREEDSHET, 'Spreedshet'),
        (CH_RESOURCE_ITEM_TYPE_VIDEO, 'Video'),
        (CH_RESOURCE_ITEM_TYPE_LINKS, 'Link'),
        (CH_RESOURCE_ITEM_TYPE_UPLOADER, 'Uploader')
    )
