from django.shortcuts import render
from atendimento.forms import AtendimentoForm

# Create your views here.
def index(request):
    form = AtendimentoForm()

    context = {
        'form': form,
    }

    return render(
        request,
        'atendimento/atendimento.html',
        context
    )