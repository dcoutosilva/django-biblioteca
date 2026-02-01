from django.db import models


class Livros(models.Model):
    nome = models.CharField(max_length=100) 
    autor = models.CharField(max_length=100)                   
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()      
    isbn = models.CharField(max_length=13)
    quantidade = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    
