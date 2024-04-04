from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from home.forms import ClientForm
from home.models import ClientModel
from django.contrib import messages
from datetime import date
from datetime import datetime
from django.utils.formats import get_format

@login_required(login_url='home:loginUser')
def createClient(request):
    form_action = reverse('home:createClient')
    
    if request.method == 'POST':
        formClient = ClientForm(request.POST)

        if formClient.is_valid():
            form = formClient.save(commit=False)

            # inclusão de idade no field age
            today = date.today()
            date_born = None
            for item in get_format('DATE_INPUT_FORMATS'):
                try:
                    date_born = datetime.strptime(formClient['born'].value(), item).date()
                    form.age = today.year - date_born.year - ((today.month, today.day) < (date_born.month, date_born.day))
                except (ValueError, TypeError):
                    continue            

            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('home:listClient')
        else:
            if "born" in formClient.errors:
                messages.error(request, 'Data de Nascimento Inválida!')
            if "responsiblePhone" or "phone1" or "phone2" in formClient.errors:
                messages.error(request, 'Número de telefone inválido!')
            else:
                messages.error(request, formClient.errors)
        
        context = {
            'form': formClient,
            'title':'Cadastro',
            'name_screen': 'Cadastro',
            'form_action': form_action,
            'name_module': 'Home',
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
            'form_action': form_action,
            'name_module': 'Home',
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

    today = date.today()
    try:
        client.age = today.year - client.born.year - ((today.month, today.day) < (client.born.month, client.born.day))
    except AttributeError:
        print("Sem data de nascimento informada!")


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
            'name_module': 'Home',
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
            'name_module': 'Home',
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
        'name_module': 'Home',
    }

    return render(
        request,
        'home/client/client.html',
        context
    )



