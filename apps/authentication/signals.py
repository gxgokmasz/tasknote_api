from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User


@receiver(pre_save, sender=User)
def create_default_group(sender, instance, **kwargs):
    if Group.objects.filter(name="regular_users").exists():
        return

    regular_users_group = Group.objects.create(name="regular_users")

    notes_app_note = ContentType.objects.get(app_label="notes", model="note")
    notes_app_folder = ContentType.objects.get(app_label="notes", model="folder")

    notes_app_note_permissions = Permission.objects.filter(content_type=notes_app_note)
    notes_app_folder_permissions = Permission.objects.filter(content_type=notes_app_folder)

    permissions = [
        *notes_app_note_permissions,
        *notes_app_folder_permissions,
    ]

    regular_users_group.permissions.set(permissions)
    regular_users_group.save()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        instance.groups.add(Group.objects.get(name="regular_users"))
