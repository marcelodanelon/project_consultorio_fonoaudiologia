from django.shortcuts import render, redirect
from home.forms import ClientForm
from home.models import ClientModel

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