from django.db import models


class Member(models.Model):

    class Meta:
        verbose_name = 'Socio'

    name = models.TextField(verbose_name='Nombre')
    mail = models.EmailField()
    phone = models.IntegerField(verbose_name='Número de teléfono', null=True, blank=True,)
    city = models.TextField(verbose_name='Ciudad', null=True, blank=True, max_length=20)


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
    NUMBER = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    name = models.TextField(verbose_name='Nombre', null=True, blank=True, max_length=32)
    type_animal = models.CharField('Tipo', choices=CATEGORIES, default='', max_length=32)
    breed = models.TextField(verbose_name='Raza', null=True, blank=True,)
    number_color = models.IntegerField(verbose_name='Número de colores', choices=NUMBER, default='', max_length=32)
    description = models.TextField(verbose_name='Descripción', null=True, blank=True, max_length=250)
    color = models.ManyToManyField(Color)


class Publication(models.Model):

    class Meta:
        verbose_name = 'Publicación'

    title = models.TextField(verbose_name='Título', default='', max_length=100)
    description = models.TextField(verbose_name='Descripción', null=True, blank=True, max_length=250)
    date = models.DateField(verbose_name='Fecha', auto_now=True)
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT, default='')
    location = models.TextField(verbose_name='Localización', default='', max_length=100)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return {}.format(self.title)
