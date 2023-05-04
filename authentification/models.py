from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Utilisateur(AbstractUser):

    choices = (
    (0, 'DGA'),
    (1, 'Secretaire'),
    (2, 'Caissière'),
    (3, 'Productrice'),
    (4, 'Informaticienne')
    )
    code = models.CharField(max_length=5, null=False)
    poste = models.IntegerField(default=0, choices=choices )
    tel = models.CharField(default=0, max_length=20)

    def __str__(self):
        return self.username 