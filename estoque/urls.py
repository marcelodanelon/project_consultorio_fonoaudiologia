from django.urls import path
from estoque.views import movimentacao, insumo, grupo, marca

app_name = 'estoque'

urlpatterns = [
    path('estoque/', insumo.index, name='index'),

    path('listInsumo/', insumo.listInsumo, name='listInsumo'),
    path('createInsumo/', insumo.createInsumo, name='createInsumo'),
    path('searchInsumo/', insumo.searchInsumo, name='searchInsumo'),
    path('<int:insumo_id>/updateInsumo/', insumo.updateInsumo, name='updateInsumo'),

    path('listGrupo/', grupo.listGrupo, name='listGrupo'),
    path('createGrupo/', grupo.createGrupo, name='createGrupo'),
    path('searchGrupo/', grupo.searchGrupo, name='searchGrupo'),
    path('<int:grupo_id>/updateGrupo/', grupo.updateGrupo, name='updateGrupo'),

    path('listMarca/', marca.listMarca, name='listMarca'),
    path('createMarca/', marca.createMarca, name='createMarca'),
    path('searchMarca/', marca.searchMarca, name='searchMarca'),
    path('<int:marca_id>/updateMarca/', marca.updateMarca, name='updateMarca'),

    path('listMovimentacaoInsumo/', movimentacao.listMovimentacaoInsumo, name='listMovimentacaoInsumo'),
    path('movimentacaoInsumoEntrada/', movimentacao.movimentacaoInsumoEntrada, name='movimentacaoInsumoEntrada'),
    path('movimentacaoInsumoSaida/', movimentacao.movimentacaoInsumoSaida, name='movimentacaoInsumoSaida'),
    path('<int:movimentacao_id>/movimentacaoInsumoUpdate/', movimentacao.movimentacaoInsumoUpdate, name='movimentacaoInsumoUpdate'),

    path('getJSONitem/', movimentacao.getJSONitem, name='getJSONitem'),
    path('getJSONinsumo/', movimentacao.getJSONinsumo, name='getJSONinsumo'),
    path('getJSONgrupo/', movimentacao.getJSONgrupo, name='getJSONgrupo'),
    path('getJSONclient/', movimentacao.getJSONclient, name='getJSONclient'),
]
