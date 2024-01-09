from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Notes
from .forms import NotesForm

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/notes/list'

class NotesListView(ListView):
    model = Notes
    template_name = 'notes/list.html' # must add because default is notes/notes_list.html
    context_object_name = 'notes'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/detail.html'

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/notes/list'
