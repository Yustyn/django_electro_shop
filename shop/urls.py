from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^store$', views.store, name='store'),
    url(r'^checkout$', views.checkout, name='checkout'),
    url(r'^product$', views.product, name='product'),
]
