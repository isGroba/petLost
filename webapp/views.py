from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import reverse
from django.views import generic

from core import models
from webapp import forms


class Home(generic.TemplateView):
    template_name = 'webapp/home.html'
    name = 'Página principal'


class PublicationList(generic.ListView):
    template_name = 'webapp/publication/list.html'
    name = 'Publicaciones'
    model = models.Publication

    def get_queryset(self):
        return models.Publication.objects.all()


class PublicationCreate(SuccessMessageMixin, generic.CreateView):
    model = models.Publication
    form_class = forms.CreatePublication
    template_name = 'webapp/publication/create.html'
    success_message = ('Publicacion creada correctamente')
    name = 'Crear publicacion'

    def get_success_url(self):
        return reverse('publication-detail', args=[self.object.id])


class PublicationDetail(generic.DetailView):
    model = models.Publication
    template_name = 'webapp/publication/detail.html'
    name = 'Detalle publicacion'
