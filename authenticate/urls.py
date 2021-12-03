from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.log_in, name='login')
]
