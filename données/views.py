from django.shortcuts import render, redirect
from authentification.models import Utilisateur

    
def index(request, *args, **kwargs):
    users = Utilisateur.objects.all()

    context = {
        'users' : users
    }

    # print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    # print(request.Presence.utilisateur.username)
    # print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

    return render(request, 'données/index.html', context)