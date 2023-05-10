from django.shortcuts import render, redirect
from authentification.models import Utilisateur
from .forms import RapportForm, ClientForm
from .models import Rapport, Client
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




def getRapport(request, *args, **kwargs):
    rapports = Rapport.objects.all()
    # context['rapport'] = rapport


    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    print(request.rapport.date)
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

    return render(request, 'données/rapport.html', {'rapports' : rapports})


def client(request, *args, **kwargs):
    
    form = ClientForm()
    if request.method =="POST":
        form = ClientForm(request.POST)
        if form.is_valid():
           form.save()    
    return render(request, 'données/client.html', {'form':form})  


# def client(request, *args, **kwargs):
#     nom = request.POST.get('username'),
#     adresse = request.POST.get('adresse'),
#     mail = request.POST.get('mail'),
#     date_naiss = request.POST.get('date_naiss'),
#     tel = request.POST.get('tel'),
#     typeAssur = request.POST.get('type'),
#     autre = request.POST.get('autre'),
#     client = Client(nom=nom, adresse=adresse, email=mail, date_naiss=date_naiss, 
#     tel=tel, typeAssur=typeAssur, autre=autre)
          

#     client.save()    
#     return render(request, 'données/client.html', {'client':client})  




# def signup(request, *args, **kwargs):

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('pwd')
#         mail = request.POST.get('mail')
#         poste = request.POST.get('poste')
#         tel = request.POST.get('tel')
         
#         user = User.objects.create_user(username = username, password = password) 
#         login(request, user)
#         return redirect('login')
#     return render(request, 'authentification/signup.html')       