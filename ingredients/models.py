from django.db import models
from django.cong import settings

class Ingredient(models.Model):

    name = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
