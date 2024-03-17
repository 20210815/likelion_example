from django.db import models

# Create your models here.
class Category(models.Model):
  title = models.CharField(max_length=50, unique=True)
  slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
  
  def __str__(self):
    return f'[{self.title}]'