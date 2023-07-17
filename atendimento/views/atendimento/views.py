from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.urls import reverse
from atendimento.forms import AtendimentoForm, AnamneseForm
from home.models import ClientModel
from atendimento.models import AtendimentoModel, AnamneseModel

def atendimento(request):
    form_action = reverse('atendimento:atendimento')
    order_forms = AtendimentoModel()
    item_order_formset = inlineformset_factory(AtendimentoModel, AnamneseModel, form=AnamneseForm, extra=0, can_delete=False, min_num=1)

    if request.method == 'POST':
        try:
            search = int(request.POST.get('clientId'))
            client = ClientModel.objects.filter(pk=search)
        except:
            search = None
            client = None

        updateAtend = int(request.POST.get('updateAtendimento'))
        forms = AtendimentoForm(request.POST, request.FILES, instance=order_forms)
        formset = item_order_formset(request.POST, request.FILES, instance=order_forms)

        if updateAtend == 1:
            atendimento = AtendimentoModel.objects.filter(aClient=search).filter(aSituaca='Em Andamento').get()
            forms = AtendimentoForm(request.POST, instance=atendimento)

            formset = item_order_formset(request.POST, instance=atendimento)

            if forms.is_valid() and formset.is_valid():
                forms = forms.save()    
                formset.save()  
                return redirect('home:index') 
            
        if forms.is_valid() and formset.is_valid():
            forms = forms.save()    
            formset.save()  
            return redirect('home:index')
    else:
        forms = AtendimentoForm(instance=order_forms)
        formset = item_order_formset(instance=order_forms)

        #inicio de um novo atendimento | BUSCA MÉTODO GET
        try:
            search = int(request.GET.get('searchClient'))
            client = ClientModel.objects.filter(pk=search)
        except:
            search = None
            client = None

        #verifica se há atendimento em andamento
        try:
            atendimento = AtendimentoModel.objects.filter(aClient=search).filter(aSituaca='Em Andamento').get()
            if atendimento.aSituaca != 'Concluído':
                updateAtend = 1
                forms = AtendimentoForm(instance=atendimento)
                anams = AnamneseModel.objects.filter(aIDAtend=atendimento)
                formset = item_order_formset(instance=atendimento, queryset=anams)
            else:
                updateAtend = 0
        except AtendimentoModel.DoesNotExist:
            updateAtend = 0

    context = {
        'form': forms,
        'formAnamSet': formset,
        'name_module': 'Atendimento',
        'form_action': form_action,
        'title': 'Atendimento',
        'client': client,
        'updateAtend': updateAtend,
    }

    return render(request, 'atendimento/atendimento.html', context)

