from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Folder, Note


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ("name", "user")
    list_per_page = 10

    fieldsets = (
        (_("Informações da pasta"), {"fields": ("name", "user")}),
        (_("Datas importantes"), {"fields": ("created_at", "updated_at")}),
        (_("Identificadores"), {"fields": ("id", "slug")}),
    )
    add_fieldsets = ((None, {"fields": ("name", "user")}),)
    readonly_fields = ("id", "slug", "created_at", "updated_at")

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "folder")
    list_per_page = 10

    fieldsets = (
        (_("Informações da nota"), {"fields": ("title", "folder", "content")}),
        (_("Datas importantes"), {"fields": ("created_at", "updated_at")}),
        (_("Identificadores"), {"fields": ("id", "slug")}),
    )
    add_fieldsets = ((None, {"fields": ("title", "folder", "content")}),)
    readonly_fields = ("id", "slug", "created_at", "updated_at")

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)
