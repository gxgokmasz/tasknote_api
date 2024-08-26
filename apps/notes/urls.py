from django.urls import path
from .views import (
    FolderListCreateView,
    FolderRetrieveUpdateDestroyView,
    NoteListCreateView,
    NoteRetrieveUpdateDestroyView,
)


urlpatterns = [
    path("api/v1/notes/", NoteListCreateView.as_view(), name="note_list_create"),
    path(
        "api/v1/notes/<slug:slug>/",
        NoteRetrieveUpdateDestroyView.as_view(),
        name="note_retrieve_update_destroy",
    ),
    path("api/v1/folders/", FolderListCreateView.as_view(), name="folder_list_create"),
    path(
        "api/v1/folders/<slug:slug>/",
        FolderRetrieveUpdateDestroyView.as_view(),
        name="folder_retrieve_update_destroy",
    ),
]
