from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from estoque.forms import MovimentacaoInsumoForm, InsumoForm, ItemInsumoForm
from estoque.models import MovimentacaoInsumoModel, ItensInsumoModel

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
            model = form.save()
            modelSet = formset.save(commit=False)
            print(modelSet)
            for item in modelSet:
                print(item)
                item.local = model.local
                item.dataEntrada = model.data
                item.save()
                # print(member)
            
                # formset.save()
        # if forms.is_valid() and formset.is_valid():
        #     forms = forms.save()    
        #     formset.save()  
            # return redirect('estoque:index')

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