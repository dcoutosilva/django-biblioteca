from django.db import models


class Emprestimo(models.Model):
    nome_emprestimo = models.CharField(max_length=100)
    livro_emprestado = models.CharField(max_length=100)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    tempo_duracao = models.DateField()

class Livros(models.Model):
    nome = models.CharField(max_length=100) 
    autor = models.CharField(max_length=100)                   
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()      
    isbn = models.CharField(max_length=13)
    quantidade = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    data_cadastro = models.DateField()
    emprestado = models.BooleanField(default=False)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    nome_emprestimo = models.CharField(max_length=100)
    tempo_duracao = models.DateField()    
