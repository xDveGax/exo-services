# -*- coding: utf-8 -*-
# Generated for Django 2.2.8 on 2019-12-12 15:39
from __future__ import unicode_literals

from django.core.management import call_command

from exo_changelog import change, operations


def update_exo_roles():
    call_command('update_or_create_roles')


class Change(change.Change):

    dependencies = [
    ]

    operations = [
        operations.RunPython(update_exo_roles),
    ]
