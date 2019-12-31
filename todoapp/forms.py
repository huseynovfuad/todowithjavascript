from django import forms
from .models import Todo

class TodoCreateForm(forms.ModelForm):
    text = forms.CharField(widget = forms.TextInput(attrs={
        'placeholder':'Write something',
        'class': 'form-control',
        'id': 'create_text',
        'name': 'create_text',
    }))
    class Meta:
        model = Todo
        fields = [
            'text'
        ]

class TodoUpdateForm(forms.ModelForm):
    text = forms.CharField(widget = forms.TextInput(attrs={
        'placeholder':'Write something',
        'class': 'form-control',
        'id': 'update_text',
        'name': 'update_text',
    }))
    class Meta:
        model = Todo
        fields = [
            'text'
        ]