from django.db import models


class Location(models.Model):

    class Meta:
        verbose_name = 'Ubicación'

    lat = models.TextField(verbose_name='latitud', max_length=30)
    lng = models.TextField(verbose_name='longuitud', max_length=30)
    zoom = models.IntegerField(verbose_name='zoom')


class Member(models.Model):

    class Meta:
        verbose_name = 'Socio'

    name = models.TextField(verbose_name='Nombre')
    mail = models.EmailField()
    phone = models.IntegerField(verbose_name='Número de teléfono')
    city = models.TextField(verbose_name='Ciudad', max_length=20)


class Color(models.Model):

    class Meta:
        verbose_name = 'Color'

    name = models.TextField(verbose_name='Nombre', max_length=32)
    code_color = models.TextField(verbose_name='Código color', max_length=32)


class Pet(models.Model):

    class Meta:
        verbose_name = 'Mascota'
    CATEGORIES = [
        ('dog', 'perro'),
        ('gato', 'Gato'),
        ('bird', 'Pájaro'),
        ('reptil', 'Reptil'),
        ('other', 'Otro'),
    ]
    name = models.TextField(verbose_name='Nombre', max_length=32)
    type_animal = models.CharField('Tipo', choices=CATEGORIES, max_length=32)
    breed = models.TextField(verbose_name='Raza')
    number_color = models.IntegerField(verbose_name='Número de colores')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True, max_length=250)
    location = models.ManyToManyField(Location)
    color = models.ManyToManyField(Color)


class Publication(models.Model):

    class Meta:
        verbose_name = 'Publicación'

    title = models.TextField(verbose_name='Título', max_length=100)
    description = models.TextField(verbose_name='Descripción', null=True, blank=True, max_length=250)
    date = models.DateField(verbose_name='Fecha', auto_now=True)
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return {}.format(self.title)
