from django.shortcuts import render, redirect
from home.forms import ClientForm
from home.models import ClientModel
from django.db.models import Q
from datetime import datetime

def isDate(var):
    try:
        d = datetime.strptime(var, '%d/%m/%Y').date()
        return True
    except:
        return False

def createClient(request):
    formClient = ClientForm()

    if request.method == 'POST':
        formClient = ClientForm(request.POST)

        if formClient.is_valid():
            formClient.save()
            return redirect('home:index')

        context = {
            'form': formClient,
            'formErrors': formClient.errors.items(),
            'title':'Cadastro',
        }

        return render(
            request,
            'home/client.html',
            context
        )

    context = {
            'form': ClientForm(),
            'title':'Cadastro',
    }

    return render(
        request,
        'home/client.html',
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