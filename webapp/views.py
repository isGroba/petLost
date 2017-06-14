from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import reverse, redirect, render_to_response, render
from django.views import generic
from registration.views import RegistrationView

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from core import models
from webapp import forms


class Option:
    def __init__(self, name, viewname, args=None, kwargs=None, menu=None):
        self.name = name
        self.url = reverse(viewname, args, kwargs) if viewname else False
        self.menu = menu

    def is_current(self):
        return self.menu.current == self.name


class MenuBar:
    def __init__(self, current):
        self.current = current

    def get_options(self):
        return [
            Option('Publicaciones', 'publication-list', menu=self),
            Option('Mascotas', 'pet-list', menu=self),
            Option('Nueva publicación', None, menu=self),
            Option('Mis publicaciones', None, menu=self),
            Option('Configuracion cuenta', None, menu=self),
        ]

    def __iter__(self):
        return iter(self.get_options())


class MenuMixin:
    name = ''

    def get_context_data(self, **kwargs):
        if 'menu' not in kwargs:
            kwargs['menu'] = MenuBar(self.name)
            kwargs['pet_lost'] = models.Pet.objects.count()
            kwargs['publi'] = models.Publication.objects.count()
        return super().get_context_data(**kwargs)


class Register(MenuMixin, RegistrationView):
    pass


class Login(MenuMixin, LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = 'home'


class Logout(LogoutView):
    pass


class Home(MenuMixin, generic.ListView):
    template_name = 'webapp/home.html'
    name = 'Página principal'
    paginate_by = 5
    model = models.Publication

    def get_queryset(self):
        return models.Publication.objects.all().order_by('-date')


class PublicationList(MenuMixin, generic.ListView):
    template_name = 'webapp/publication/list.html'
    name = 'Publicaciones'
    model = models.Publication
    paginate_by = 5

    def get_queryset(self):
        return models.Publication.objects.all()


class PublicationCreate(LoginRequiredMixin, MenuMixin, SuccessMessageMixin, generic.CreateView):
    model = models.Publication
    form_class = forms.CreatePublication
    template_name = 'webapp/publication/create.html'
    success_message = ('Publicacion creada correctamente')
    name = 'Crear publicacion'

    def get_success_url(self):
        return reverse('publication-detail', args=[self.object.id])


class PublicationEdit(MenuMixin, generic.UpdateView):
    model = models.Publication
    form_class = forms.EditPublication
    template_name = 'webapp/publication/edit.html'
    name = 'Crear Publicación'

    def get_success_url(self):
        return reverse('publication-detail', args=[self.object.id])


class PublicationDetail(MenuMixin, generic.DetailView):
    model = models.Publication
    template_name = 'webapp/publication/detail.html'
    name = 'Detalle publicacion'


class PetList(MenuMixin, generic.ListView):
    template_name = 'webapp/pet/list.html'
    name = 'Mascotas'
    model = models.Pet
    paginate_by = 5

    def get_queryset(self):
        return models.Pet.objects.all()


class NewPet(MenuMixin, generic.FormView):
    form_class = forms.NewPet
    template_name = 'webapp/pet/create.html'
    name = 'Nueva mascota creada'

    def form_valid(self, form):
        publication = form.execute()
        print(publication.id)
        print('llega3')
        return redirect('publication-edit', publication.id)


class PetDetail(MenuMixin, generic.DetailView):
    model = models.Pet
    template_name = 'webapp/pet/detail.html'
    name = 'Detalle mascota'
