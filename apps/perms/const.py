# -*- coding: utf-8 -*-
#
from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.db.fields import BitChoices
from common.utils.integer import bit

__all__ = ["SpecialAccount", "ActionChoices"]


class ActionChoices(BitChoices):
    connect = bit(1), _("Connect")
    upload = bit(2), _("Upload")
    download = bit(3), _("Download")
    copy = bit(4), _("Copy")
    paste = bit(5), _("Paste")

    @classmethod
    def is_tree(cls):
        return True

    @classmethod
    def branches(cls):
        return (
            (_("Transfer"), [cls.upload, cls.download]),
            (_("Clipboard"), [cls.copy, cls.paste]),
        )

    @classmethod
    def has_perm(cls, action_name, total):
        action_value = getattr(cls, action_name)
        return action_value & total == action_value


class SpecialAccount(models.TextChoices):
    ALL = "@ALL", "All"
