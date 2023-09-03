from django.urls import path
from estoque.views import movimentacao, insumo

app_name = 'estoque'

urlpatterns = [
    path('estoque/', insumo.index, name='index'),

    path('listInsumo/', insumo.listInsumo, name='listInsumo'),
    path('createInsumo/', insumo.createInsumo, name='createInsumo'),
    path('searchInsumo/', insumo.searchInsumo, name='searchInsumo'),
    path('<int:insumo_id>/updateInsumo/', insumo.updateInsumo, name='updateInsumo'),
    path('<int:insumo_id>/deleteInsumo/', insumo.deleteInsumo, name='deleteInsumo'),

    path('MovimentacaoInsumoEntrada/', movimentacao.movimentacaoInsumoEntrada, name='movimentacaoInsumoEntrada'),
    path('MovimentacaoInsumoSaida/', movimentacao.movimentacaoInsumoSaida, name='movimentacaoInsumoSaida'),
    path('getJSONitem/', movimentacao.getJSONitem, name='getJSONitem'),
]
