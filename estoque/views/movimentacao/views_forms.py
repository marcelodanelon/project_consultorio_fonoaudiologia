from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from babel.numbers import format_currency
from django.http import JsonResponse
from estoque.forms import MovimentacaoInsumoForm, ItensMovimentacaoInsumoForm, ItensInsumoForm
from estoque.models import MovimentacaoInsumoModel, ItensMovimentacaoInsumoModel, ItensInsumoModel

@login_required(login_url='home:loginUser')
def getJSONitem(request):
    if request.GET.get('searchLocal'):
        q = int(request.GET.get('searchLocal'))
        model = list(ItensInsumoModel.objects.filter(local=q).exclude(quantidade=0).values())
        return JsonResponse(data={'results': model})

@login_required(login_url='home:loginUser')
def movimentacaoInsumoEntrada(request):
    try:
        search = int(request.GET.get('searchLocal'))
        items = ItensMovimentacaoInsumoModel.objects.filter(local=search)
    except:
        search = None
        items = None

    form_action = reverse('estoque:movimentacaoInsumoEntrada')
    modelMov = MovimentacaoInsumoModel()
    formMov=MovimentacaoInsumoForm()
    formIte=inlineformset_factory(MovimentacaoInsumoModel, ItensMovimentacaoInsumoModel, form=ItensMovimentacaoInsumoForm, extra=0, can_delete=True, min_num=1)
    formIteInsumo=inlineformset_factory(MovimentacaoInsumoModel, ItensInsumoModel, form=ItensInsumoForm, extra=0, can_delete=True, min_num=1)

    if request.method == 'POST':
        form = MovimentacaoInsumoForm(request.POST, request.FILES, instance=modelMov)
        formset = formIte(request.POST, request.FILES, instance=modelMov)
        formsetInsumo = formIteInsumo(request.POST, request.FILES, instance=modelMov)

        if formset.is_valid() and form.is_valid():
            success = True
            model = form.save()
            modelSet = formset.save(commit=False)
            modelSetInsumo = formsetInsumo.save(commit=False)

            # replica para o Itens no cadastro do Insumo
            for item in modelSet:
                novo_item_insumo = ItensInsumoModel(
                    movimentacao=item.movimentacao,  
                    insumo=item.insumo,
                    valorUnitario=item.valorUnitario,  
                    valorTotal=item.valorTotal,  
                    quantidade=item.quantidade,
                    dataValidade=item.dataValidade,  
                    dataEntrada=item.dataEntrada,  
                    serie=item.serie,  
                    local=item.local,  
                )
                modelSetInsumo.append(novo_item_insumo)

            # verifica se há lote existente
            for item in modelSet:
                try:
                    insumo = ItensMovimentacaoInsumoModel.objects.filter(insumo=item.insumo.pk).filter(serie=item.serie).get()
                    # retira pontos e virgulas e converte em reais
                    insumo_valorUnitario = float(insumo.valorUnitario.replace(",","").replace(".",""))
                    insumo_valorUnitario = format_currency(insumo_valorUnitario / 100, 'BRL', locale='pt_BR')
                except:
                    insumo = None

                # retira pontos e virgulas e converte em reais
                item_valorUnitario = float(item.valorUnitario.replace(",","").replace(".",""))                
                item_valorUnitario = format_currency(item_valorUnitario / 100, 'BRL', locale='pt_BR')

                # verifica valor unitario divergente
                if insumo != None and item_valorUnitario != insumo_valorUnitario:
                    messages.error(request, f'Valor Unitário para o {insumo}, diferente da série/lote existente.')
                    success = False
                    break

            if success == True:
                for item in modelSet:
                    # controle inclusão de entrada para lote existente ou novo 
                    if insumo:                    
                        totalQuantidade = insumo.quantidade + item.quantidade
                        totalValor = float(insumo.valorTotal) + float(item.valorTotal)
                        ItensMovimentacaoInsumoModel.objects.filter(insumo=item.insumo.pk).update(quantidade=totalQuantidade)
                        ItensMovimentacaoInsumoModel.objects.filter(insumo=item.insumo.pk).update(valorTotal=totalValor)
                        messages.success(request, f'Lote para {insumo} já existente, adicionado quantidade na Data de Entrada: {insumo.dataEntrada}')
                    else:
                        item_valorUnitario = float(item.valorUnitario.replace(",","").replace(".",""))
                        item.valorUnitario = format_currency(item_valorUnitario / 100, 'BRL', locale='pt_BR')
                        item_valorTotal = float(item.valorTotal.replace(",","").replace(".",""))
                        item.valorTotal = format_currency(item_valorTotal / 100, 'BRL', locale='pt_BR')
                        item_valorCompra = float(item.valorCompra.replace(",","").replace(".",""))
                        item.valorCompra = format_currency(item_valorCompra / 100, 'BRL', locale='pt_BR')
                        item.local = model.local
                        item.dataEntrada = model.data
                        item.save()

                for item in modelSetInsumo:
                    # controle inclusão de entrada para lote existente ou novo 
                    if insumo:                    
                        totalQuantidade = insumo.quantidade + item.quantidade
                        totalValor = float(insumo.valorTotal) + float(item.valorTotal)
                        ItensInsumoModel.objects.filter(insumo=item.insumo.pk).update(quantidade=totalQuantidade)
                        ItensInsumoModel.objects.filter(insumo=item.insumo.pk).update(valorTotal=totalValor)
                        messages.success(request, f'Lote para {insumo} já existente, adicionado quantidade na Data de Entrada: {insumo.dataEntrada}')
                    else:
                        item_valorUnitario = float(item.valorUnitario.replace(",","").replace(".",""))
                        item.valorUnitario = format_currency(item_valorUnitario / 100, 'BRL', locale='pt_BR')
                        item_valorTotal = float(item.valorTotal.replace(",","").replace(".",""))
                        item.valorTotal = format_currency(item_valorTotal / 100, 'BRL', locale='pt_BR')
                        item.local = model.local
                        item.dataEntrada = model.data
                        item.save()
                return redirect('estoque:index')

        context = {
        'title': 'Estoque',
        'name_module': 'Estoque',
        'name_screen': 'Movimentação de Insumos',
        'groups_user': request.user.groups.values_list('name', flat=True),
        'form_action': form_action,
        'formMov': form,
        'formIte': formset,
        'items_saida': items,
        }

        return render(
            request,
            'estoque/movimentacao/movimentacaoEntrada.html',
            context
        )

    context = {
        'title': 'Estoque',
        'name_module': 'Estoque',
        'name_screen': 'Movimentação de Insumos',
        'groups_user': request.user.groups.values_list('name', flat=True),
        'form_action': form_action,
        'items_saida': items,
        'formMov': formMov,
        'formIte': formIte(instance=MovimentacaoInsumoModel()),
    }

    return render(
        request,
        'estoque/movimentacao/movimentacaoEntrada.html',
        context
    )

@login_required(login_url='home:loginUser')
def movimentacaoInsumoSaida(request):
    try:
        search = int(request.GET.get('searchLocal'))
        items = ItensMovimentacaoInsumoModel.objects.filter(local=search)
    except:
        search = None
        items = None

    form_action = reverse('estoque:movimentacaoInsumoSaida')
    modelMov = MovimentacaoInsumoModel()
    formMov=MovimentacaoInsumoForm()
    formIte=inlineformset_factory(MovimentacaoInsumoModel, ItensMovimentacaoInsumoModel, form=ItensMovimentacaoInsumoForm, extra=0, can_delete=True, min_num=1)

    if request.method == 'POST':
        form = MovimentacaoInsumoForm(request.POST, request.FILES, instance=modelMov)
        formset = formIte(request.POST, request.FILES, instance=modelMov)

        if formset.is_valid() and form.is_valid():
            success=None
            model = form.save(commit=False)
            modelSet = formset.save(commit=False)

            # verifica se há saldo para saída
            for item in modelSet:
                insumo = ItensInsumoModel.objects.filter(insumo=item.insumo.pk).filter(serie=item.serie).get()                   
                if insumo.quantidade >= item.quantidade:
                    success=True
                else:
                    success=False
                    break
            # realiza ação e verificação
            if success:
                form.save()
                for item in modelSet:
                    insumo = ItensInsumoModel.objects.filter(insumo=item.insumo.pk).filter(serie=item.serie).get() 
                    totalQuantidade = insumo.quantidade - item.quantidade
                    totalValor = float(insumo.valorTotal) - float(item.valorTotal)
                    ItensInsumoModel.objects.filter(insumo=item.insumo.pk).filter(serie=item.serie).update(quantidade=totalQuantidade)
                    ItensInsumoModel.objects.filter(insumo=item.insumo.pk).filter(serie=item.serie).update(valorTotal=totalValor)
                    item.local = model.local
                    item.dataEntrada = model.data
                    item.save()
                return redirect('estoque:index')
            else:
                messages.error(request, f'Saldo insuficiente para insumo {insumo}!')

            context = {
            'title': 'Estoque',
            'name_module': 'Estoque',
            'name_screen': 'Movimentação de Insumos',
            'groups_user': request.user.groups.values_list('name', flat=True),
            'form_action': form_action,
            'formMov': form,
            'formIte': formIte,
            'isUpdate': 0,
            'items_saida': items,
            }

            return render(
                request,
                'estoque/movimentacao/movimentacaoSaida.html',
                context
            )

    context = {
        'title': 'Estoque',
        'name_module': 'Estoque',
        'name_screen': 'Movimentação de Insumos',
        'groups_user': request.user.groups.values_list('name', flat=True),
        'form_action': form_action,
        'items_saida': items,
        'formMov': formMov,
        'formIte': formIte(instance=MovimentacaoInsumoModel()),
        'isUpdate': 0,
    }

    return render(
        request,
        'estoque/movimentacao/movimentacaoSaida.html',
        context
    )

@login_required(login_url='home:loginUser')
def movimentacaoInsumoUpdate(request, movimentacao_id):
    try:
        search = int(request.GET.get('searchLocal'))
        items = ItensMovimentacaoInsumoModel.objects.filter(local=search)
    except:
        search = None
        items = None

    form_action = reverse('estoque:movimentacaoInsumoUpdate', kwargs={'movimentacao_id':movimentacao_id})
    movimentacao = get_object_or_404(MovimentacaoInsumoModel, pk=movimentacao_id)
    formMov=MovimentacaoInsumoForm(instance=movimentacao)
    formIte=inlineformset_factory(MovimentacaoInsumoModel, ItensMovimentacaoInsumoModel, form=ItensMovimentacaoInsumoForm, extra=0, can_delete=True, min_num=1)

    context = {
        'title': 'Estoque',
        'name_module': 'Estoque',
        'name_screen': 'Movimentação de Insumos',
        'groups_user': request.user.groups.values_list('name', flat=True),
        'items_saida': items,
        'formMov': formMov,
        'form_action': form_action,
        'isUpdate': 1,
        'formIte': formIte(instance=movimentacao),
    }

    if movimentacao.operacao == "Entrada":
        url = 'estoque/movimentacao/movimentacaoEntrada.html' 
    else:
        url = 'estoque/movimentacao/movimentacaoSaida.html'
        
    return render(
        request,
        url,
        context
    )