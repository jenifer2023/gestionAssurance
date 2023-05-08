from django.shortcuts import render, redirect
from authentification.models import Utilisateur
from .forms import RapportForm
from .models import Rapport
from . import models  
from django import forms

    
def index(request, *args, **kwargs):
    users = Utilisateur.objects.all()

    context = {
        'users' : users
    }

    return render(request, 'données/index.html', context)


def rapport(request, *args, **kwargs):
    
    form = RapportForm()
    if request.method =="POST":
        form = RapportForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request, 'données/rapport.html', {'form':form})  


# def getRapport(request, *args, **kwargs):
#     rapport = Rapport.objects.all()
#     context = {[
#         'libelle' : libelle,
#         'date' : date
#     ]}

#     re