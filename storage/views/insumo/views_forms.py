from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from storage.forms import InsumoForm
from storage.models import InsumoModel

def createInsumo(request):
    form_action = reverse('storage:createInsumo')

    if request.method == 'POST':
        formInsumo = InsumoForm(request.POST)

        if formInsumo.is_valid():
            form = formInsumo.save()
            messages.success(request, 'Insumo cadastrado com sucesso!')
            return redirect('storage:updateInsumo',form.id)

        context = {
            'form': formInsumo,
            'title':'Cadastro',
            'form_action': form_action,
        }

        return render(
            request,
            'storage/insumo/insumo.html',
            context
        )

    context = {
            'form': InsumoForm(),
            'title':'Cadastro',
            'name_screen': 'Cadastro',
            'form_action': form_action,
    }

    return render(
        request,
        'storage/insumo/insumo.html',
        context
    )

def updateInsumo(request, insumo_id):
    insumo = get_object_or_404(InsumoModel, pk=insumo_id)
    form_action = reverse('storage:updateInsumo', args=(insumo_id,))

    context = {
        'form' : InsumoForm(instance=insumo),
        'form_action': form_action,
        'insumo': insumo,
        'title':'Cadastro',
        'name_screen': 'Atualizar',
        'option_delete': 'yes',
    }

    return render(
        request,
        'storage/insumo/insumo.html',
        context
    )