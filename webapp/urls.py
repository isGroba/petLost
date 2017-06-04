from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='home/')),
    url(r'^home/$', views.Home.as_view(), name='home'),
]
