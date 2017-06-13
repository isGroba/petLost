from django import forms

from core import models

from django.contrib.auth.models import User
from registration.forms import RegistrationForm


class CreatePublication(forms.ModelForm):
    class Meta:
        model = models.Publication
        fields = ('title', 'description', 'pet')

        widgets = {
            'title': forms.TextInput(),
            'description': forms.TextInput(),
        }


class CreatePet(forms.ModelForm):
    class Meta:
        model = models.Pet
        fields = ('name', 'type_animal', 'breed', 'description', 'color', 'picture')
