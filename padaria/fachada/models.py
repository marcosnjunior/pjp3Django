from django.db import models
import uuid


class Produto(models.Model):
    
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)
    nome = models.CharField(max_length=200)
    preco = models.IntegerField()
    descricao = models.TextField(default='Não preenchido')
    imagem = models.ImageField(upload_to='imagens', null=True, blank=True)
    
    
    def __str__(self):
        return self.nome
    
    
class Dados_usuario(models.Model):
    
    CARGOS = {
    "Gerente": "Gerente",
    "Vendedor":"Vendedor",
    "Ajudante":"Ajudante"
    }   

    nome = models.CharField(max_length=50)
    funcao = models.CharField(max_length=50)
    cargo = models.CharField(max_length=25, blank=True, choices=CARGOS)
    salario = models.IntegerField()
    

    def __str__(self):
        return self.nome

    

    
