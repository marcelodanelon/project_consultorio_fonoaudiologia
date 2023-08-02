from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from estoque.forms import InsumoForm
from estoque.models import InsumoModel

@login_required(login_url='home:loginUser')
def createInsumo(request):
    form_action = reverse('estoque:createInsumo')

    if request.method == 'POST':
        formInsumo = InsumoForm(request.POST)

        if formInsumo.is_valid():
            form = formInsumo.save()
            messages.success(request, 'Insumo cadastrado com sucesso!')
            return redirect('estoque:updateInsumo',form.id)

        context = {
            'form': formInsumo,
            'title':'Cadastro',
            'name_module': 'Estoque',
            'form_action': form_action,
        }

        return render(
            request,
            'estoque/insumo/insumo.html',
            context
        )

    context = {
            'form': InsumoForm(),
            'title':'Cadastro',
            'name_screen': 'Cadastro',
            'name_module': 'Estoque',
            'form_action': form_action,
    }

    return render(
        request,
        'estoque/insumo/insumo.html',
        context
    )

@login_required(login_url='home:loginUser')
def updateInsumo(request, insumo_id):
    insumo = get_object_or_404(InsumoModel, pk=insumo_id)
    form_action = reverse('estoque:updateInsumo', args=(insumo_id,))

    context = {
        'form' : InsumoForm(instance=insumo),
        'form_action': form_action,
        'insumo': insumo,
        'title':'Cadastro',
        'name_screen': 'Atualizar',
        'name_module': 'Estoque',
        'option_delete': 'yes',
    }

    return render(
        request,
        'estoque/insumo/insumo.html',
        context
    )

@login_required(login_url='home:loginUser')
def deleteInsumo(request, insumo_id):
    insumo = get_object_or_404(InsumoModel, pk=insumo_id)
    form_action = reverse('estoque:deleteInsumo', args=(insumo_id,))

    confirmation = request.POST.get('confirmation_delete', 'no')

    if confirmation == 'yes':
        insumo.delete()
        messages.success(request, 'Cliente deletado com sucesso!')
        return redirect ('estoque:listInsumo')

    context = {
        'form': InsumoForm(instance=insumo),
        'title':'Cadastro',
        'name_screen': 'Atualizar',
        'option_delete': 'yes',
        'client': insumo,
        'confirmation_delete': confirmation,
        'form_action': form_action,
    }

    return render(
        request,
        'estoque/insumo/insumo.html',
        context
    )