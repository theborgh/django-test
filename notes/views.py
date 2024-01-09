from django.shortcuts import render

from .models import Notes

def list(request):
    notes = Notes.objects.all()
    return render(request, 'notes/list.html', {'notes': notes})

def detail(request, note_id):
    note = Notes.objects.get(id=note_id)
    return render(request, 'notes/detail.html', {'note': note})