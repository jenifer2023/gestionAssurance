from django.urls import path
from . import views

app_name = 'données'

urlpatterns = [
    path('', views.index, name='index'),
    path('rapport/', views.rapport, name='rapport'),
     

]