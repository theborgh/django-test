from typing import Any
from django import forms

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'content': forms.Textarea(attrs={'class': 'form-control mb-5', 'cols': 80, 'rows': 20})
        }
        labels = {
            'title': 'Title',
            'content': 'Write your note here'
        }

    def clean_title(self):
        data = self.cleaned_data['title']
        if len(data) < 5:
            raise forms.ValidationError('Title must be at least 5 characters long')
        return data