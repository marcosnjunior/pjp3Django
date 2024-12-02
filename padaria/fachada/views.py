from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto
from django.db.models import Q


def balcao(request):
    return HttpResponse("Opa!! Tu chegasse no balcão")



def caixa(request):
    
    #produto = Produto.objects.all()
    produto = Produto.objects.filter(preco__lte=1350)
    return render(request, 'fachada/lista_produtos.html',{'produto':produto})



def detalhes(request, id_produto):
    
    if request.method == 'POST':
        
        id = request.POST.get('id_produto')
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')
        
        produto = Produto.objects.get(id=id)
        produto.nome = nome
        produto.preco = preco
        produto.descricao = descricao
        produto.save()
        
        produto = Produto.objects.all()
        return render(request, 'fachada/lista_produtos.html',{'produto':produto})

    produto = Produto.objects.get(id=id_produto)
    return render(request, 'fachada/detalhes.html',{'produto':produto})



def pesquisa(request):
    
    if request.method == 'POST':
        pesquisa = request.POST.get('pesquisa')
        
        produto = Produto.objects.filter(Q(nome__contains=pesquisa) | Q(descricao__contains=pesquisa))
        return render(request, 'fachada/lista_produtos.html',{'produto':produto})
        