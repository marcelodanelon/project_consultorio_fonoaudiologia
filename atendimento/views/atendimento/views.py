from django.shortcuts import render, redirect
from django.urls import reverse
from atendimento.forms import AtendimentoForm, AnamneseFormSet
from home.models import ClientModel

def atendimento(request):
    form_action = reverse('atendimento:atendimento')
    formAnamSet = AnamneseFormSet(request.GET or None)

    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        formAnamSet = AnamneseFormSet(request.POST)
        
        if form.is_valid():
            obj1 = form.save()
            print(formAnamSet)
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

    form = AtendimentoForm()

    context = {
        'client': client,
        'form': form,
        'formAnamSet': AnamneseFormSet,
        'name_module': 'Atendimento',
        'form_action': form_action,
        'title': 'Atendimento',
    }

    return render(
        request,
        'atendimento/atendimento.html',
        context
    )