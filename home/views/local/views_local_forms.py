from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from home.forms import LocalForm
from home.models import LocalModel
from django.contrib import messages

def createLocal(request):
    form_action = reverse('home:createLocal')

    if request.method == 'POST':
        formClient = LocalForm(request.POST)

        if formClient.is_valid():
            form = formClient.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('home:updateClient',form.id)
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
            'home/local/local.html',
            context
        )

    context = {
            'form': LocalForm(),
            'title':'Cadastro',
            'name_screen': 'Cadastro',
            'form_action': form_action,
    }

    return render(
        request,
        'home/local/local.html',
        context
    )

def updateLocal(request, local_id):
    local = get_object_or_404(LocalModel, pk=local_id)
    form_action = reverse('home:updateClient', args=(local_id,))

    if request.method == 'POST':
        formClient = LocalForm(request.POST, instance=local)

        if formClient.is_valid():
            formClient.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('home:listLocal')
        else:
            if "born" in formClient.errors:
                messages.error(request, 'Data de Nascimento inválida!')
            if "responsiblePhone" or "phone1" or "phone2" in formClient.errors:
                messages.error(request, 'Número de telefone inválido!')

        context = {
            'form': formClient,
            'title':'Cadastro',
            'name_screen': 'Atualizar',
            'option_delete': 'yes',
            'local': local,
            'form_action': form_action,
        }

        return render(
            request,
            'home/local/local.html',
            context
        )

    context = {
            'form': LocalForm(instance=local),
            'title':'Cadastro',
            'name_screen': 'Atualizar',
            'option_delete': 'yes',
            'local': local,
            'form_action': form_action,
    }

    return render(
        request,
        'home/local/local.html',
        context
    )

def deleteLocal(request, local_id):
    client = get_object_or_404(LocalModel, pk=local_id)
    form_action = reverse('home:deleteLocal', args=(local_id,))

    confirmation = request.POST.get('confirmation_delete', 'no')

    if confirmation == 'yes':
        client.delete()
        messages.success(request, 'Cliente deletado com sucesso!')
        return redirect ('home:listLocal')

    context = {
        'form': LocalForm(instance=client),
        'title':'Cadastro',
        'name_screen': 'Atualizar',
        'option_delete': 'yes',
        'client': client,
        'confirmation_delete': confirmation,
        'form_action': form_action,
    }

    return render(
        request,
        'home/local/local.html',
        context
    )



