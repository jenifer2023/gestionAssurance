# authentication/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    choices = (
    (0, 'DGA'),
    (1, 'Secretaire'),
    (2, 'Caissière'),
    (3, 'Productrice'),
    (4, 'Informaticienne')
    )
    username = forms.CharField(max_length=63, label='Nom d’utilisateur ')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe ')
    # email = models.CharField(max_length=63, null=False, label='Email : ')
    # code = models.CharField(max_length=5, null=False, label='Code')
    # poste = models.IntegerField(default=1, choices=choices, label='Poste occupé(e) : ' )
    # tel = models.CharField(default=0, max_length=20, label='Tel : ')


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')    