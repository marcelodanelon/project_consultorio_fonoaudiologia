from django.shortcuts import render, get_object_or_404
from atendimento.forms import AtendimentoForm, AnamneseForm
from home.models import ClientModel

def atendimento(request):
    form = AtendimentoForm()
    formAnam = AnamneseForm()

    context = {
        'form': form,
        'formAnam': formAnam,
        'name_module': 'Atendimento',
        'title': 'Atendimento',
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
    formAnam = AnamneseForm()

    context = {
        'client': client,
        'form': form,
        'formAnam': formAnam,
        'name_module': 'Atendimento',
        'title': 'Atendimento',
    }

    return render(
        request,
        'atendimento/atendimento.html',
        context
    )