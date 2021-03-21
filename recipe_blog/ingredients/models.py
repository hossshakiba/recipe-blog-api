from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Ingredient(models.Model):

    name = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(User , null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
