from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from home.forms import ClientForm
from home.models import ClientModel
from django.contrib import messages

@login_required(login_url='home:loginUser')
def createClient(request):
    form_action = reverse('home:createClient')

    if request.method == 'POST':
        formClient = ClientForm(request.POST)
        if formClient.is_valid():
            form = formClient.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('home:listClient',form.id)
        else:
            if "born" in formClient.errors:
                messages.error(request, 'Data de Nascimento Inválida!')
            if "responsiblePhone" or "phone1" or "phone2" in formClient.errors:
                messages.error(request, 'Número de telefone inválido!')
        context = {
            'form': formClient,
            'title':'Cadastro',
            'form_action': form_action,
        }

        return render(
            request,
            'home/client/client.html',
            context
        )

    context = {
            'form': ClientForm(),
            'title':'Cadastro',
            'name_screen': 'Cadastro',
            'name_module': 'Home',
            'form_action': form_action,
    }

    return render(
        request,
        'home/client/client.html',
        context
    )

@login_required(login_url='home:loginUser')
def updateClient(request, client_id):
    client = get_object_or_404(ClientModel, pk=client_id)
    form_action = reverse('home:updateClient', args=(client_id,))

    if request.method == 'POST':
        formClient = ClientForm(request.POST, instance=client)

        if formClient.is_valid():
            formClient.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('home:listClient')
        else:
            if "born" in formClient.errors:
                messages.error(request, 'Data de Nascimento inválida!')
            if "responsiblePhone" or "phone1" or "phone2" in formClient.errors:
                messages.error(request, 'Número de telefone inválido!')
        print(formClient.errors)
        context = {
            'form': formClient,
            'title':'Cadastro',
            'name_screen': 'Atualizar',
            'option_delete': 'yes',
            'client': client,
            'form_action': form_action,
        }

        return render(
            request,
            'home/client/client.html',
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
        'home/client/client.html',
        context
    )

@login_required(login_url='home:loginUser')
def deleteClient(request, client_id):
    client = get_object_or_404(ClientModel, pk=client_id)
    form_action = reverse('home:deleteClient', args=(client_id,))

    confirmation = request.POST.get('confirmation_delete', 'no')

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
        'home/client/client.html',
        context
    )



