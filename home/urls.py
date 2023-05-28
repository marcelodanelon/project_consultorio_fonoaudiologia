from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.Index, name='index'),
    path('client/create', views.Create, name='create'),
]