from django.contrib.auth.models import User
from django.db import models


class Color(models.Model):

    class Meta:
        verbose_name = 'Color'

    name = models.TextField(verbose_name='Nombre', max_length=32)
    code_color = models.TextField(verbose_name='Código color', max_length=32)

    def __str__(self):
        return '{}'.format(self.name)


class Pet(models.Model):

    class Meta:
        verbose_name = 'Mascota'

    CATEGORIES = [
        ('dog', 'Perro'),
        ('cat', 'Gato'),
        ('bird', 'Pájaro'),
        ('reptile', 'Reptil'),
        ('other', 'Otro'),
    ]

    name = models.TextField(verbose_name='Nombre', null=True, blank=True, max_length=32)
    type_animal = models.CharField('Tipo', choices=CATEGORIES, default='', max_length=32)
    breed = models.TextField(verbose_name='Raza', null=True, blank=True,)
    description = models.TextField(verbose_name='Descripción', null=True, blank=True, max_length=250)
    picture = models.ImageField(verbose_name='Foto', upload_to='pets', blank=True, null=True)
    location = models.CharField('Ubicacion', default='', max_length=50)
    color = models.ManyToManyField(Color)

    def __str__(self):
        return '{} {}'.format(self.type_animal, self.name)


class Publication(models.Model):

    class Meta:
        verbose_name = 'Publicación'

    STATUS = [
        ('found', 'Buscando al propietario'),
        ('lost', 'Buscando mi mascota'),
        ('solved', 'Solucionado'),
    ]
    title = models.TextField(verbose_name='Título', default='', max_length=100)
    description = models.TextField(verbose_name='Descripción', null=True, blank=True, max_length=250)
    date = models.DateField(verbose_name='Fecha', auto_now=True)
    state_publication = models.CharField('Estado', choices=STATUS, default='', max_length=32)
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT)
    member = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return '{}'.format(self.title)
