from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from atendimento.forms import AtendimentoForm, AnamneseFormSet
from home.models import ClientModel
from atendimento.models import AtendimentoModel

def atendimento(request):
    form_action = reverse('atendimento:atendimento')
    formAnamSet = AnamneseFormSet(request.GET or None)

    if request.method == 'POST':
        updateAtend = request.POST.get('updateAtendimento', 0)
        if updateAtend == 0:
            form = AtendimentoForm(request.POST)
            formAnamSet = AnamneseFormSet(request.POST)
        else:
            #verificar
            search = request.POST.get('searchClient')
            atendimento = AtendimentoModel.objects.get(aClient=search)
            form = AtendimentoForm(request.POST, instance=atendimento)

        if form.is_valid():
            obj1 = form.save()
            if formAnamSet.is_valid():
                for formA in formAnamSet:
                    obj2 = formA.save(commit=False)
                    obj2.aIDAtend = obj1.id
                    formA.save() 

                return redirect('home:index')

    context = {
        'form': AtendimentoForm(),
        'formAnamSet': formAnamSet,
        'name_module': 'Atendimento',
        'form_action': form_action,
        'title': 'Atendimento',
    }

    return render(
        request,
        'atendimento/atendimento.html',
        context
    )

def dadosClient(request):
    form_action = reverse('atendimento:atendimento')

    search = request.GET.get('searchClient')
    client = ClientModel.objects.filter(pk=search)
    try:
        atendimento = AtendimentoModel.objects.get(aClient=search)
        if atendimento.aSituaca != 'Concluído':
            updateAtend = 1
            form = AtendimentoForm(instance=atendimento)
        else:
            form = AtendimentoForm()
            updateAtend = 0
    except AtendimentoModel.DoesNotExist:
        form = AtendimentoForm()
        updateAtend = 0

    context = {
        'client': client,
        'form': form,
        'formAnamSet': AnamneseFormSet,
        'name_module': 'Atendimento',
        'form_action': form_action,
        'title': 'Atendimento',
        'updateAtend': updateAtend,
    }

    return render(
        request,
        'atendimento/atendimento.html',
        context
    )