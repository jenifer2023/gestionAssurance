from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model, login

from . import forms

# # Create your views here.

User = get_user_model()
def login_page(request, *args, **kwargs):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                
            )
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'authentification/login.html', context={'form': form, 'message': message})    
     
                  
def logout_user(request):
    logout(request)
    return redirect(login)

# def index(request, *args, **kwargs):
#     users = Utilisateur.objects.all()

#     context = {
#         'users' : users
#     }

#     return render(request, 'authentification/index.html')






User = get_user_model()

def signup(request, *args, **kwargs):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        mail = request.POST.get('mail')
        poste = request.POST.get('poste')
        tel = request.POST.get('tel')
         
        user = User.objects.create_user(username = username, password = password) 
        login(request, user)
        return redirect('login')
    return render(request, 'authentification/signup.html')