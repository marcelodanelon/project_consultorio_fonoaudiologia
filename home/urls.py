from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('createClient/', views.createClient, name='createClient'),
    path('listClient/', views.listClient, name='listClient'),
    path('<int:client_id>/searchClient/', views.listClient, name='listClient'),
]