from django.views import generic


class Home(generic.TemplateView):
    template_name = 'webapp/home.html'
    name = 'Página principal'
