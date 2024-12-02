from django.contrib import admin
from .models import Produto, Dados_usuario

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'descricao']

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Dados_usuario)
