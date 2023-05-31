from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from home.forms import ClientForm
from home.models import ClientModel

def createClient(request):
    form_action = reverse('home:createClient')

    if request.method == 'POST':
        formClient = ClientForm(request.POST)

        if formClient.is_valid():
            formClient.save()
            return redirect('home:index')

        context = {
            'form': formClient,
            'formErrors': formClient.errors.items(),
            'title':'Cadastro',
            'form_action': form_action,
        }

        return render(
            request,
            'home/client.html',
            context
        )

    context = {
            'form': ClientForm(),
            'title':'Cadastro',
            'form_action': form_action,
    }

    return render(
        request,
        'home/client.html',
        context
    )

def updateClient(request, client_id):
    client = get_object_or_404(ClientModel, pk=client_id)
    form_action = reverse('home:updateClient', args=(client_id,))

    if request.method == 'POST':
        formClient = ClientForm(request.POST, instance=client)

        if formClient.is_valid():
            formClient.save()
            return redirect('home:index')

        context = {
            'form': formClient,
            'formErrors': formClient.errors.items(),
            'title':'Cadastro',
            'form_action': form_action,
        }

        return render(
            request,
            'home/client.html',
            context
        )

    context = {
            'form': ClientForm(instance=client),
            'title':'Cadastro',
            'form_action': form_action,
    }

    return render(
        request,
        'home/client.html',
        context
    )

