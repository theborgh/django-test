from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import Notes
from .forms import NotesForm

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/notes/list'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'notes/list.html' # must add because default is notes/notes_list.html
    context_object_name = 'notes'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/detail.html'

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/notes/list'

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/notes/list'
    template_name = 'notes/notes_delete.html'
