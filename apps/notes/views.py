from rest_framework import generics
from core.common.permissions import GlobalPermission
from .models import Folder, Note
from .serializers import FolderSerializer, NoteSerializer


class FolderListCreateView(generics.ListCreateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = (GlobalPermission,)


class FolderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = (GlobalPermission,)
    lookup_field = "slug"


class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (GlobalPermission,)


class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (GlobalPermission,)
    lookup_field = "slug"
