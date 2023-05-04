from django.urls import path
from . import views

app_name = 'authentification'

urlpatterns = [
     path('', views.login_page, name='login'),
     path('logout/', views.logout, name='logout'),
     path('signup/', views.signup, name='signup'),
     
    

]