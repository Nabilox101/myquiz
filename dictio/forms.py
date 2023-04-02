from django import forms
from .models import Example
from django_summernote.widgets import SummernoteWidget


class ExampleForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = ('english_to_darija', 'example_text',)
        widgets = {
            'example_text': SummernoteWidget(),
        }