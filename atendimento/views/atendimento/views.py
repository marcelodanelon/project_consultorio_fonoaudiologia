from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from atendimento.forms import AtendimentoForm, AnamneseForm
from home.models import ClientModel

def atendimento(request):
    form_action = reverse('atendimento:atendimento')

    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        formAnam = AnamneseForm(request.POST)
        
        if form.is_valid():
            obj1 = form.save()
            if formAnam.is_valid():
                obj2 = formAnam.save(commit=False)
                obj2.aIDAtend = obj1.id
                formAnam.save() 

                return redirect('home:index')

    context = {
        'form': AtendimentoForm(),
        'formAnam': AnamneseForm(),
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
    formAnam = AnamneseForm()

    context = {
        'client': client,
        'form': form,
        'formAnam': formAnam,
        'name_module': 'Atendimento',
        'form_action': form_action,
        'title': 'Atendimento',
    }

    return render(
        request,
        'atendimento/atendimento.html',
        context
    )