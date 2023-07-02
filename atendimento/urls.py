from django.urls import path
from atendimento import views

app_name = 'atendimento'

urlpatterns = [
    path('atendimento/', views.atendimento ,name='atendimento'),
    path('atendimento/dados/', views.dadosClient ,name='dadosClient'),
]