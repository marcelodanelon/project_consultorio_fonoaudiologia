from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from estoque.forms import MovimentacaoInsumoForm, InsumoForm, ItemInsumoForm
from estoque.models import MovimentacaoInsumoModel, InsumoModel, ItensInsumoModel
from django.template.loader import render_to_string
from django.http import HttpResponse

def getJSONitem(request):
    if request.GET.get('searchLocal'):
        q = int(request.GET.get('searchLocal'))
        model = list(ItensInsumoModel.objects.filter(local=q).exclude(quantidade=0).values())
        return JsonResponse(data={'results': model})

def movimentacaoInsumoEntrada(request):
    try:
        search = int(request.GET.get('searchLocal'))
        items = ItensInsumoModel.objects.filter(local=search)
    except:
        search = None
        items = None

    form_action = reverse('estoque:movimentacaoInsumoEntrada')
    modelMov = MovimentacaoInsumoModel()
    formMov=MovimentacaoInsumoForm()
    formIte=inlineformset_factory(MovimentacaoInsumoModel, ItensInsumoModel, form=ItemInsumoForm, extra=0, can_delete=True, min_num=1)

    if request.method == 'POST':
        form = MovimentacaoInsumoForm(request.POST, request.FILES, instance=modelMov)
        formset = formIte(request.POST, request.FILES, instance=modelMov)

        if formset.is_valid() and form.is_valid():
            success = True
            model = form.save()
            modelSet = formset.save(commit=False)

            # verifica se há lote existente
            for item in modelSet:
                try:
                    insumo = ItensInsumoModel.objects.filter(insumo=item.insumo.pk).filter(serie=item.serie).get()
                except:
                    insumo = None

                # verifica valor unitario divergente
                if insumo != None and float(item.valorUnitario) != float(insumo.valorUnitario.replace(",",".")):
                    messages.error(request, f'Valor Unitário para o {insumo}, diferente da série/lote existente.')
                    success = False
                    break

            if success == True:
                for item in modelSet:
                    # controle inclusão de entrada para lote existente ou novo 
                    if insumo:                    
                        totalQuantidade = insumo.quantidade + item.quantidade
                        totalValor = float(insumo.valorTotal) + float(item.valorTotal)
                        ItensInsumoModel.objects.filter(insumo=item.insumo.pk).update(quantidade=totalQuantidade)
                        ItensInsumoModel.objects.filter(insumo=item.insumo.pk).update(valorTotal=totalValor)
                    else:
                        item.local = model.local
                        item.dataEntrada = model.data
                        item.save()
                return redirect('estoque:index')

            # realiza ação e verificação
            # if success:
            #     form.save()
            #     for item in modelSet:
            #         insumo = InsumoModel.objects.filter(pk=item.insumo.pk).get()
            #         if model.operacao=='Entrada':                    
            #             totalQuantidade = insumo.quantidade + item.quantidade
            #             print(item.valorTotal)
            #             totalValor = insumo.valor + float(item.valorTotal)
            #             InsumoModel.objects.filter(pk=item.insumo.pk).update(quantidade=totalQuantidade)
            #             InsumoModel.objects.filter(pk=item.insumo.pk).update(valor=totalValor)
            #         else:
            #             totalQuantidade = insumo.quantidade - item.quantidade
            #             totalValor = insumo.valor - float(item.valorTotal)
            #             InsumoModel.objects.filter(pk=item.insumo.pk).update(quantidade=totalQuantidade)
            #             InsumoModel.objects.filter(pk=item.insumo.pk).update(valor=totalValor)
            #         item.local = model.local
            #         item.dataEntrada = model.data
            #         item.save()
            #     return redirect('estoque:index')
            # else:
            #     messages.error(request, f'Saldo insuficiente para insumo {insumo}!')

        context = {
        'title': 'Estoque',
        'name_module': 'Estoque',
        'name_screen': 'Movimentação de Insumos',
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


def movimentacaoInsumoSaida(request):
    try:
        search = int(request.GET.get('searchLocal'))
        items = ItensInsumoModel.objects.filter(local=search)
    except:
        search = None
        items = None

    form_action = reverse('estoque:movimentacaoInsumoSaida')
    modelMov = MovimentacaoInsumoModel()
    formMov=MovimentacaoInsumoForm()
    formIte=inlineformset_factory(MovimentacaoInsumoModel, ItensInsumoModel, form=ItemInsumoForm, extra=0, can_delete=True, min_num=1)

    if request.method == 'POST':
        form = MovimentacaoInsumoForm(request.POST, request.FILES, instance=modelMov)
        formset = formIte(request.POST, request.FILES, instance=modelMov)

        if formset.is_valid() and form.is_valid():
            success=None
            model = form.save(commit=False)
            modelSet = formset.save(commit=False)

            # verifica se há saldo para saída
            for item in modelSet:
                insumo = InsumoModel.objects.filter(pk=item.insumo.pk).get()
                if model.operacao!='Entrada':                    
                    if insumo.quantidade >= item.quantidade:
                        success=True
                    else:
                        success=False
                        break

            # realiza ação e verificação
            if success:
                form.save()
                for item in modelSet:
                    insumo = InsumoModel.objects.filter(pk=item.insumo.pk).get()
                    if model.operacao=='Entrada':                    
                        totalQuantidade = insumo.quantidade + item.quantidade
                        print(item.valorTotal)
                        totalValor = insumo.valor + float(item.valorTotal)
                        InsumoModel.objects.filter(pk=item.insumo.pk).update(quantidade=totalQuantidade)
                        InsumoModel.objects.filter(pk=item.insumo.pk).update(valor=totalValor)
                    else:
                        totalQuantidade = insumo.quantidade - item.quantidade
                        totalValor = insumo.valor - float(item.valorTotal)
                        InsumoModel.objects.filter(pk=item.insumo.pk).update(quantidade=totalQuantidade)
                        InsumoModel.objects.filter(pk=item.insumo.pk).update(valor=totalValor)
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
        'form_action': form_action,
        'formMov': form,
        'formIte': formset,
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
        'form_action': form_action,
        'items_saida': items,
        'formMov': formMov,
        'formIte': formIte(instance=MovimentacaoInsumoModel()),
    }

    return render(
        request,
        'estoque/movimentacao/movimentacaoSaida.html',
        context
    )