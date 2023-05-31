from django.shortcuts import render, redirect
from home.models import ClientModel
from django.db.models import Q
from datetime import datetime

def isDate(var):
    try:
        d = datetime.strptime(var, '%d/%m/%Y').date()
        return True
    except:
        return False

def index(request):
    context = {
        'title': 'Home',
    }

    return render(
        request,
        'home/index.html',
        context
    )

def listClient(request):
    clients = ClientModel.objects.all()

    context = {
            'clients': clients,
            'title':'Pesquisa',
    }

    return render(
        request,
        'home/search.html',
        context
    )

def searchClient(request):
    search_client = request.GET.get('q','').strip()

    print(type(search_client))
    if search_client == "":
        return redirect('home:listClient')

    if search_client.isdigit():
        clients = ClientModel.objects.filter(document1=int(search_client))
    elif isDate(search_client):
        clients = ClientModel.objects.filter(born=datetime.strptime(search_client, '%d/%m/%Y').date())
    else:        
        clients = ClientModel.objects.filter(
            Q(first_name=search_client) | 
            Q(last_name=search_client)
        )


    context = {
            'clients': clients,
            'title':'Pesquisa',
    }

    return render(
        request,
        'home/search.html',
        context
    )