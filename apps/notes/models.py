from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.authentication.models import User
from core.common.models import CommonInfo


class Folder(CommonInfo):
    name = models.CharField(_("nome"), max_length=60)
    user = models.ForeignKey(
        User, models.CASCADE, related_name="folders", verbose_name=_("usuário")
    )

    def __str__(self):
        return self.name


class Note(CommonInfo):
    title = models.CharField(_("título"), max_length=60)
    content = models.TextField(_("conteúdo"))
    folder = models.ForeignKey(
        Folder, models.CASCADE, related_name="notes", verbose_name=_("pasta")
    )

    def __str__(self):
        return self.title
