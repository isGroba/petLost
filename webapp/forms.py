from django import forms

from core import models


class CreatePublication(forms.ModelForm):
    class Meta:
        model = models.Publication
        fields = ('title', 'description', 'pet')

        widgets = {
            'title': forms.TextInput(),
            'description': forms.TextInput(),
        }


class EditPublication(forms.ModelForm):
    class Meta:
        model = models.Publication
        fields = ('title', 'description', 'pet')

        widgets = {
            'title': forms.TextInput(),
            'description': forms.TextInput(),
            'pet': forms.HiddenInput(),
        }

class CreatePet(forms.ModelForm):
    class Meta:
        model = models.Pet
        fields = ('name', 'type_animal', 'breed', 'description', 'color', 'picture')


class NewPet(forms.Form):

    CATEGORIES = [
        ('dog', 'Perro'),
        ('cat', 'Gato'),
        ('bird', 'Pájaro'),
        ('reptile', 'Reptil'),
        ('other', 'Otro'),
    ]

    name = forms.CharField(label='Nombre')
    type_animal = forms.ChoiceField(label='Tipo', choices=CATEGORIES)
    breed = forms.CharField(label='Raza')
    description = forms.CharField(label='Descripción')
    picture = forms.ImageField(label='Foto', required=False)
    color = forms.MultipleChoiceField(choices = models.Color.objects.values_list('id','name') , widget=forms.CheckboxSelectMultiple)

    def execute(self):
        cleaned_data = self.cleaned_data
        pet = models.Pet.objects.create(
                name = cleaned_data['name'],
                type_animal = cleaned_data['type_animal'],
                breed = cleaned_data['breed'],
                description = cleaned_data['description'],
                picture = cleaned_data['picture'],
            )
        pet.color = cleaned_data['color']
        publication = models.Publication.objects.create(title = '', description = '', pet = pet)
        return publication