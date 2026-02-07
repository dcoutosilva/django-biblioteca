from django.db import models
from datetime import date


class Livros(models.Model):
    nome = models.CharField(max_length=100) 
    autor = models.CharField(max_length=100)    
    co_autor = models.CharField(max_length=100, blank = True)  # Campo opcional para co-autor                
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()      
    isbn = models.CharField(max_length=13)
    quantidade = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    data_cadastro = models.DateField(default = date.today)
    emprestado = models.BooleanField(default=False)
    data_emprestimo = models.DateField(blank = True)
    data_devolucao = models.DateField(blank = True, null=True)
    nome_emprestimo = models.CharField(max_length=100, blank = True)
    tempo_duracao = models.DateField(blank = True, null=True)   
    
    class Meta:
        verbose_name = "Livro"
        