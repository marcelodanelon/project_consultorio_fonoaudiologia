from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from estoque.forms import MarcaForm
from estoque.models import MarcaModel
import ast

@login_required(login_url='home:loginUser')
def createMarca(request):
    form_action = reverse('estoque:createMarca')

    if request.method == 'POST':
        formMarca = MarcaForm(request.POST)

        if formMarca.is_valid():
            formMarca.save()
            messages.success(request, 'Marca cadastrada com sucesso!')
            return redirect('estoque:listMarca')

        context = {
            'form': formMarca,
            'title':'Cadastro',
            'name_module': 'Estoque',
            'name_screen': 'Cadastro',
            'form_action': form_action,
        }

        return render(
            request,
            'estoque/marca/marca.html',
            context
        )

    context = {
            'form': MarcaForm(),
            'title':'Cadastro',
            'name_screen': 'Cadastro',
            'name_module': 'Estoque',
            'form_action': form_action,
    }

    return render(
        request,
        'estoque/marca/marca.html',
        context
    )

@login_required(login_url='home:loginUser')
def updateMarca(request, marca_id):
    marca = get_object_or_404(MarcaModel, pk=marca_id)
    form_action = reverse('estoque:updateMarca', args=(marca_id,))
    
    if request.method == 'POST':
        formMarca = MarcaForm(request.POST, instance=marca)
        if formMarca.is_valid():
            formMarca.save()
            messages.success(request, 'Marca atualizada com sucesso!')
            return redirect('estoque:listMarca')

        context = {
            'form' : MarcaForm(instance=marca),
            'form_action': form_action,
            'title':'Cadastro',
            'name_screen': 'Cadastro',
            'name_module': 'Estoque',
        }

        return render(
            request,
            'estoque/marca/marca.html',
            context
        )

    context = {
        'form' : MarcaForm(instance=marca),
        'form_action': form_action,
        'title':'Cadastro',
        'name_screen': 'Cadastro',
        'name_module': 'Estoque',
    }

    return render(
        request,
        'estoque/marca/marca.html',
        context
    )