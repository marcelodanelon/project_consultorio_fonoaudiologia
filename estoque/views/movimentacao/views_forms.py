from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from estoque.forms import MovimentacaoInsumoForm, InsumoForm, ItemInsumoForm
from estoque.models import MovimentacaoInsumoModel, InsumoModel, ItensInsumoModel

def MovimentacaoInsumoCreate(request):
    form_action = reverse('estoque:movimentacaoInsumoCreate')
    modelMov = MovimentacaoInsumoModel()
    formMov=MovimentacaoInsumoForm()
    formIte=inlineformset_factory(MovimentacaoInsumoModel, ItensInsumoModel, form=ItemInsumoForm, extra=0, can_delete=True, min_num=1)

    if request.method == 'POST':
        form = MovimentacaoInsumoForm(request.POST, request.FILES, instance=modelMov)
        formset = formIte(request.POST, request.FILES, instance=modelMov)

        print(form.errors)
        print(formset.errors)
        if formset.is_valid() and form.is_valid():
            success=True
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

            # realiza ação e verificação
            if success:
                form.save()
                for item in modelSet:
                    insumo = InsumoModel.objects.filter(pk=item.insumo.pk).get()
                    if model.operacao=='Entrada':                    
                        totalQuantidade = insumo.quantidade + item.quantidade
                        InsumoModel.objects.filter(pk=item.insumo.pk).update(quantidade=totalQuantidade)
                    else:
                        totalQuantidade = insumo.quantidade - item.quantidade
                        InsumoModel.objects.filter(pk=item.insumo.pk).update(quantidade=totalQuantidade)
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
        'formMov': formMov,
        'formIte': formIte(instance=MovimentacaoInsumoModel()),
    }

    return render(
        request,
        'estoque/movimentacao/movimentacao.html',
        context
    )