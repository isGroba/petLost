from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from core import models

# Sample data for Colors
COLORS_DATA = [
    ('Negro', 'black'),
    ('Blanco', 'white'),
    ('Marron', 'brown'),
    ('Rojo', 'red'),
    ('Naranja', 'orange'),
    ('Amarillo', 'yellow'),
    ('Gris', 'gray'),
    ('Azul', 'blue'),
    ('Verde', 'green'),
]


class Command(BaseCommand):

    help = 'Fill the DB models with sample data for develop'

    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise CommandError(
                '\n\nWarning! Running in production mode. Aborting.')

        self.stdout.write(self.style.SUCCESS('Populating DB with dummy data...'))

        # First truncate any data in DB
        self.stdout.write(self.style.ERROR('Please truncate manually the DB before populating it.'))

        # Create a super user
        User.objects.create_superuser(
            username='admin', password='adminadmin', email='dev@petlost.com')
        self.stdout.write(self.style.SUCCESS('[\u2713] Created SuperUser'))

        # Populate colors
        self.populate_colors()

        self.stdout.write(self.style.SUCCESS('[\u2713] Populated DB succesfully'))

    def populate_colors(self):
        colors = []

        for color_data in COLORS_DATA:
            color = models.Color()
            color.name = color_data[0]
            color.code_color = color_data[1]
            color.save()
            colors.append(color)

        self.stdout.write(self.style.SUCCESS('[\u2713] Populated DB with colors...'))
