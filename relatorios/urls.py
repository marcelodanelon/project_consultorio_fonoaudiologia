from django.urls import path
from relatorios.views import relatorios

app_name = 'relatorios'

urlpatterns = [
    path('pdf/', relatorios.sua_view_de_relatorio_pdf, name='pdf'),
]