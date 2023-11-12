from django.urls import path
from relatorios.views import relatorios

app_name = 'relatorios'

urlpatterns = [
    path('relatorios/estoque/movimentacaoinsumos', relatorios.rel_movimentacao_insumos, name='rel_movimentacao_insumos'),
    path('relatorios/estoque/teste', relatorios.teste, name='teste'),
]