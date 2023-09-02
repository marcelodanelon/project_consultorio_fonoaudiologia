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
        print('passou')
        return JsonResponse(data={'results': model})

def movimentacaoInsumoCreate(request):
    try:
        search = int(request.GET.get('searchLocal'))
        items = ItensInsumoModel.objects.filter(local=search)
    except:
        search = None
        items = None

    form_action = reverse('estoque:movimentacaoInsumoCreate')
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
            'estoque/movimentacao/movimentacao.html',
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
        'estoque/movimentacao/movimentacao.html',
        context
    )