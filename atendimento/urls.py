from django.urls import path
from atendimento import views

app_name = 'atendimento'

urlpatterns = [
    path('atendimento/', views.index ,name='index'),
    path('atendimento/dados/', views.dadosClient ,name='dadosClient'),
]