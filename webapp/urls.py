from django.conf.urls import include, url
from django.views.generic import RedirectView

from . import views

publications = [
    url(r'^$', views.PublicationList.as_view(), name='publication-list'),
    url(r'^new/$', views.PublicationCreate.as_view(), name='publication-create'),
    url(r'^(?P<pk>[^/]+)/$', views.PublicationDetail.as_view(), name='publication-detail'),
]

pet = [
    url(r'^$', views.PetList.as_view(), name='pet-list'),
    url(r'^new/$', views.PetCreate.as_view(), name='pet-create'),
    url(r'^(?P<pk>[^/]+)/$', views.PetDetail.as_view(), name='pet-detail'),
]


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='home/')),
    url(r'^home/$', views.Home.as_view(), name='home'),
    url(r'^publications/', include(publications)),
    url(r'^pet/', include(pet)),
]
