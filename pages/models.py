from pyexpat import model
from django.db import models
from django.contrib.auth.models import User 


class Post(models.Model):
    titulo = models.CharField( max_length=50)
    conteudo = models.TextField()
    data_publicacao = models.DateField(auto_now_add=True)
    image = models.CharField( max_length=125)
    image = models.ImageField(upload_to='images',null=True)
    

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data_publicacao = models.DateField(auto_now_add=True)
    


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title 
        