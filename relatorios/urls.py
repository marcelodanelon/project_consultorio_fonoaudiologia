from django.urls import path
from relatorios.views import relatorios

app_name = 'relatorios'

urlpatterns = [
    path('relatorios/movimentacaoinsumos', relatorios.rel_movimentacao_insumos, name='rel_movimentacao_insumos'),
    path('relatorios/atendimentos', relatorios.rel_atendimentos, name='rel_atendimentos'),
]