from rest_framework import serializers
from .models import Folder, Note


class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = ("id", "slug", "name", "user", "created_at", "updated_at")


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ("id", "slug", "title", "folder", "content", "created_at", "updated_at")
