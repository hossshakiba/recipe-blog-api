from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True, unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

