from django.urls import path

app_name = 'App'

from . import views

urlpatterns = [
   path('', views.home, name='home'),
]
