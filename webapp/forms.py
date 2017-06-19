from django import forms

from core import models


class EditPublication(forms.ModelForm):
    class Meta:
        model = models.Publication
        fields = ('title', 'description', 'state_publication', 'pet')

        widgets = {
            'title': forms.TextInput(),
            'description': forms.TextInput(),
            'pet': forms.HiddenInput(),
        }


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
    color = forms.MultipleChoiceField(
        choices=models.Color.objects.values_list('id', 'name'), widget=forms.CheckboxSelectMultiple)
    location = forms.CharField(label='Ubicación')

    def execute(self, usuario):
        cleaned_data = self.cleaned_data
        pet = models.Pet.objects.create(
                name=cleaned_data['name'],
                type_animal=cleaned_data['type_animal'],
                breed=cleaned_data['breed'],
                description=cleaned_data['description'],
                location=cleaned_data['location'],
                picture=cleaned_data['picture'],
            )
        pet.color = cleaned_data['color']

        member = usuario
        publication = models.Publication.objects.create(
            title='', description='', state_publication='', pet=pet, member=member)
        return publication


class NewEmail(forms.Form):

    subject = forms.CharField(label='Asunto')
    message = forms.CharField(label='Mensaje')
