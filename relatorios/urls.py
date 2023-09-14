from django.urls import path
from relatorios.views import relatorios

app_name = 'relatorios'

urlpatterns = [
    path('relatorios/', relatorios.index, name='index'),

    # exemplo para relatorios url
    path('pdf/', relatorios.sua_view_de_relatorio_pdf, name='pdf'),
]