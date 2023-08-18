from django.shortcuts import render
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from estoque.forms import MovimentacaoInsumoForm, InsumoForm, ItemInsumoForm
from estoque.models import MovimentacaoInsumoModel, ItensInsumoModel

def MovimentacaoInsumoCreate(request):
    formMov=MovimentacaoInsumoForm()
    formIns=InsumoForm()
    formIte=inlineformset_factory(MovimentacaoInsumoModel, ItensInsumoModel, form=ItemInsumoForm, extra=0, can_delete=True, min_num=1)

    context = {
        'formMov': formMov,
        'formIns': formIns,
        'formIte': formIte(instance=MovimentacaoInsumoModel()),
    }

    return render(
        request,
        'estoque/movimentacao/movimentacao.html',
        context
    )