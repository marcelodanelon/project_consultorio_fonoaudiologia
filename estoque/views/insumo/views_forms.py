from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from babel.numbers import format_currency
from django.urls import reverse
from django.contrib import messages
from estoque.forms import InsumoForm, MovimentacaoInsumoForm
from estoque.models import InsumoModel, ItensInsumoModel

@login_required(login_url='home:loginUser')
def createInsumo(request):
    form_action = reverse('estoque:createInsumo')
    insumo = get_object_or_404(InsumoModel, pk=1)
    
    if request.method == 'POST':
        formInsumo = InsumoForm(request.POST)

        if formInsumo.is_valid():
            formInsumo.save()
            messages.success(request, 'Insumo cadastrado com sucesso!')
            return redirect('estoque:listInsumo')

        context = {
            'form': formInsumo,
            'title':'Cadastro',
            'name_module': 'Estoque',
            'name_screen': 'Insumo',
            'isCreate': 1,
            'insumo': insumo,
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
            'name_screen': 'Insumo',
            'isCreate': 1,
            'insumo': insumo,
            'form_action': form_action,
    }

    return render(
        request,
        'estoque/insumo/insumo.html',
        context
    )

@login_required(login_url='home:loginUser')
def updateInsumo(request, insumo_id):
    try:
        local = int(request.GET.get('localitems'))
    except:
        local = None
    insumo = get_object_or_404(InsumoModel, pk=insumo_id)
    form_action = reverse('estoque:updateInsumo', args=(insumo_id,))
    itemsComSaldo = ItensInsumoModel.objects.filter(insumo=insumo_id).filter(local=local).exclude(quantidade=0).order_by('-dataEntrada')
    itemsSemSaldo = ItensInsumoModel.objects.filter(insumo=insumo_id).filter(local=local).filter(quantidade=0).order_by('-dataEntrada')

    quantidade_total = 0
    valor_total = 0.00

    for item in itemsComSaldo:
        valor_float = item.valorTotal.replace("R$", "").replace(".", "").replace(",", ".").strip()
        valor_total += float(valor_float)
        quantidade_total += item.quantidade
    
    insumo.quantidade = str(quantidade_total)
    insumo.valor = format_currency(valor_total, 'BRL', locale='pt_BR')

    if request.method == 'POST':
        formClient = InsumoForm(request.POST, instance=insumo)

        if formClient.is_valid():
            formClient.save()
            messages.success(request, 'Insumo atualizado com sucesso!')
            return redirect('estoque:listInsumo')

        context = {
            'form' : InsumoForm(instance=insumo),
            'formLocal': MovimentacaoInsumoForm(),
            'form_action': form_action,
            'itemsComSaldo': itemsComSaldo,
            'itemsSemSaldo': itemsSemSaldo,
            'name_screen': 'Insumo',
            'insumo': insumo,
            'local': local,
            'title':'Cadastro',
            'name_module': 'Estoque',
            'option_delete': 'yes',
        }

        return render(
            request,
            'estoque/insumo/insumo.html',
            context
        )

    context = {
        'form' : InsumoForm(instance=insumo),
        'formLocal': MovimentacaoInsumoForm(),
        'form_action': form_action,
        'itemsComSaldo': itemsComSaldo,
        'itemsSemSaldo': itemsSemSaldo,
        'name_screen': 'Insumo',
        'insumo': insumo,
        'local': local,
        'title':'Cadastro',
        'name_module': 'Estoque',
        'option_delete': 'yes',
    }

    return render(
        request,
        'estoque/insumo/insumo.html',
        context
    )