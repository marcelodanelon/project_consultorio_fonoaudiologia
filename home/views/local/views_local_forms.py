from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from home.forms import LocalForm
from home.models import LocalModel
from django.contrib import messages

@login_required(login_url='home:loginUser')
def createLocal(request):
    form_action = reverse('home:createLocal')

    if request.method == 'POST':
        formLocal = LocalForm(request.POST)

        if formLocal.is_valid():
            form = formLocal.save()
            messages.success(request, 'Unidade cadastrada com sucesso!')
            return redirect('home:updateLocal',form.id)

        context = {
            'form': formLocal,
            'title':'Cadastro',
            'name_module': 'Home',
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
            'name_module': 'Home',
            'form_action': form_action,
    }

    return render(
        request,
        'home/local/local.html',
        context
    )

@login_required(login_url='home:loginUser')
def updateLocal(request, local_id):
    local = get_object_or_404(LocalModel, pk=local_id)
    form_action = reverse('home:updateLocal', args=(local_id,))

    if request.method == 'POST':
        formLocal = LocalForm(request.POST, instance=local)

        if formLocal.is_valid():
            formLocal.save()
            messages.success(request, 'Local atualizado com sucesso!')
            return redirect('home:listLocal')

        context = {
            'form': formLocal,
            'title':'Cadastro',
            'name_screen': 'Atualizar',
            'name_module': 'Home',
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
            'name_module': 'Home',
            'option_delete': 'yes',
            'local': local,
            'form_action': form_action,
    }

    return render(
        request,
        'home/local/local.html',
        context
    )

@login_required(login_url='home:loginUser')
def deleteLocal(request, local_id):
    local = get_object_or_404(LocalModel, pk=local_id)
    form_action = reverse('home:deleteLocal', args=(local_id,))

    confirmation = request.POST.get('confirmation_delete', 'no')

    if confirmation == 'yes':
        local.delete()
        messages.success(request, 'Local deletado com sucesso!')
        return redirect ('home:listLocal')

    context = {
        'form': LocalForm(instance=local),
        'title':'Cadastro',
        'name_screen': 'Atualizar',
        'name_module': 'Home',
        'option_delete': 'yes',
        'local': local,
        'confirmation_delete': confirmation,
        'form_action': form_action,
    }

    return render(
        request,
        'home/local/local.html',
        context
    )



