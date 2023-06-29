from django.shortcuts import render
from atendimento.forms import AtendimentoForm
from home.models import ClientModel
from atendimento.models import AtendimentoModel

def index(request):
    form = AtendimentoForm()

    context = {
        'form': form,
        'name_screen': 'Atendimento'
    }

    return render(
        request,
        'atendimento/atendimento.html',
        context
    )

def dadosClient(request):
    search = request.GET.get('searchClient')
    client = ClientModel.objects.filter(pk=search)

    form = AtendimentoForm()

    context = {
        'client': client,
        'form': form,
        'name_screen': 'Atendimento'
    }

    return render(
        request,
        'atendimento/atendimento.html',
        context
    )