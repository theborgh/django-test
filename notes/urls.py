from django.urls import path

from . import views

urlpatterns = [
    path('list', views.NotesListView.as_view(), name='notes.list'),
    path('detail/<int:pk>', views.NotesDetailView.as_view(), name='notes.detail'),
    path('detail/<int:pk>/edit', views.NotesUpdateView.as_view(), name='notes.update'),
    path('notes/new', views.NotesCreateView.as_view(), name='notes.new'),
]