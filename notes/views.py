from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import Notes

class NotesListView(ListView):
    model = Notes
    template_name = 'notes/list.html' # must add because default is notes/notes_list.html
    context_object_name = 'notes'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/detail.html'
