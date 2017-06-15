from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, reverse
from django.views import generic

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
            Option('Nueva publicación', 'pet-create', menu=self),
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


class NewPet(LoginRequiredMixin, MenuMixin, generic.FormView):
    form_class = forms.NewPet
    template_name = 'webapp/pet/create.html'
    name = 'Datos del animal'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, request):
        publication = form.execute(request.user)
        return redirect('publication-edit', publication.id)


class PetDetail(MenuMixin, generic.DetailView):
    model = models.Pet
    template_name = 'webapp/pet/detail.html'
    name = 'Detalle mascota'
