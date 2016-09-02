# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from django.db import models


class AbstractPootleData(models.Model):

    class Meta(object):
        abstract = True

    # last unit updated
    last_updated_unit = models.OneToOneField(
        "pootle_store.Unit",
        db_index=True,
        null=True,
        blank=True,
        related_name="last_updated_for_%(class)s")
    # last untranslated unit created
    last_created_unit = models.OneToOneField(
        "pootle_store.Unit",
        db_index=True,
        null=True,
        blank=True,
        related_name="last_created_for_%(class)s")
    # the mtime of the last unit to be changed - used to order Stores
    max_unit_mtime = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=False,
        db_index=True)
    # the revision of the last unit to be changed - used to order Stores
    max_unit_revision = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        db_index=True)
    # last submission made
    last_submission = models.OneToOneField(
        "pootle_statistics.Submission",
        null=True,
        blank=True,
        db_index=True,
        related_name="%(class)s_stats_data")
    # the total number of failing critical checks
    critical_checks = models.IntegerField(
        null=False,
        blank=False,
        default=0,
        db_index=True)
    # the number of pending suggestions
    pending_suggestions = models.IntegerField(
        null=False,
        blank=False,
        default=0,
        db_index=True)
    # the total number of words in the store
    total_words = models.IntegerField(
        null=False,
        blank=False,
        default=0,
        db_index=True)
    # the number of translated words
    translated_words = models.IntegerField(
        null=False,
        blank=False,
        default=0,
        db_index=True)
    # the number of fuzzy words
    fuzzy_words = models.IntegerField(
        null=False,
        blank=False,
        default=0,
        db_index=True)