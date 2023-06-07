from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from home.forms import ClientForm
from home.models import ClientModel
from django.contrib import messages

def createClient(request):
    form_action = reverse('home:createClient')

    if request.method == 'POST':
        formClient = ClientForm(request.POST)

        if formClient.is_valid():
            form = formClient.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('home:updateClient',form.id)

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
            'name_screen': 'Cadastro',
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
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('home:listClient')

        context = {
            'form': formClient,
            'formErrors': formClient.errors.items(),
            'title':'Cadastro',
            'name_screen': 'Atualizar',
            'option_delete': 'yes',
            'client': client,
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
            'name_screen': 'Atualizar',
            'option_delete': 'yes',
            'client': client,
            'form_action': form_action,
    }

    return render(
        request,
        'home/client.html',
        context
    )

def deleteClient(request, client_id):
    client = get_object_or_404(ClientModel, pk=client_id)
    form_action = reverse('home:deleteClient', args=(client_id,))

    confirmation = request.POST.get('confirmation_delete', 'no')

    print(confirmation)
    if confirmation == 'yes':
        client.delete()
        messages.success(request, 'Cliente deletado com sucesso!')
        return redirect ('home:listClient')

    context = {
        'form': ClientForm(instance=client),
        'title':'Cadastro',
        'name_screen': 'Atualizar',
        'option_delete': 'yes',
        'client': client,
        'confirmation_delete': confirmation,
        'form_action': form_action,
    }

    return render(
        request,
        'home/client.html',
        context
    )



