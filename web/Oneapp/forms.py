from django import forms
from .models import Movies_table


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies_table
        fields = ['name', 'desc', 'img']
