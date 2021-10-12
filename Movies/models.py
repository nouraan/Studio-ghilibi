from django.db import models
from django.db.models.base import Model

# Create your models here.
class Films(models.Model):
    Film=models.CharField( max_length=100)




    def __str__(self):
        return self.Film

class People(models.Model):
    films = models.ForeignKey(Films,related_name='person', on_delete=models.CASCADE)
    person=models.CharField( max_length=100)


    def __str__(self):
        return self.person

