from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.homepage, name='home')
]
