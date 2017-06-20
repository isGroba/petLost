from django.conf.urls import include, url
from django.views.generic import RedirectView

from . import views

publications = [
    url(r'^$', views.PublicationList.as_view(), name='publication-list'),
    url(r'^own/$', views.MyPublications.as_view(), name='own-publication-list'),
    url(r'^own/(?P<pk>[^/]+)/$', views.MyPublicationDetail.as_view(), name='own-publication-detail'),
    url(r'^(?P<pk>[^/]+)/$', views.PublicationDetail.as_view(), name='publication-detail'),
    url(r'^(?P<pk>[^/]+)/edit/$', views.PublicationEdit.as_view(), name='publication-edit'),
]

pet = [
    url(r'^$', views.PetList.as_view(), name='pet-list'),
    url(r'^new/$', views.NewPet.as_view(), name='pet-create'),
    url(r'^(?P<pk>[^/]+)/$', views.PetDetail.as_view(), name='pet-detail'),
]

email = [
    url(r'^(?P<pk>[^/]+)/$', views.NewEmail.as_view(), name='new-email'),
]

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='home/')),
    url(r'^home/$', views.Home.as_view(), name='home'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url(r'^publications/', include(publications)),
    url(r'^pet/', include(pet)),
    url(r'^email/', include(email)),
]
