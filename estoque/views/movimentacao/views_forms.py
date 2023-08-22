from django.shortcuts import render
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from estoque.forms import MovimentacaoInsumoForm, InsumoForm, ItemInsumoForm
from estoque.models import MovimentacaoInsumoModel, ItensInsumoModel

def MovimentacaoInsumoCreate(request):
    form_action = reverse('estoque:movimentacaoInsumoCreate')

    formMov=MovimentacaoInsumoForm()
    formIte=inlineformset_factory(MovimentacaoInsumoModel, ItensInsumoModel, form=ItemInsumoForm, extra=0, can_delete=True, min_num=1)

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