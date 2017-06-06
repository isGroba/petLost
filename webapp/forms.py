from django import forms

from core import models


class CreatePublication(forms.ModelForm):
    class Meta:
        model = models.Publication
        fields = ('title', 'description')

        widgets = {
            'title': forms.TextInput(),
            'description': forms.TextInput(),
        }
