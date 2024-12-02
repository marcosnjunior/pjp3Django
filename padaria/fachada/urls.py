
from django.urls import path
from .views import balcao, caixa, detalhes, pesquisa

urlpatterns = [
    path('balcao/', balcao,name='balcao'),
    path('caixa/', caixa, name='caixa'),
    path('detalhes/<uuid:id_produto>', detalhes, name='detalhes'),
    path('pesquisa', pesquisa, name='pesquisa'),
]
