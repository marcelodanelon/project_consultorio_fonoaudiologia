from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from agendamento.forms import AgendaForm
from agendamento.models import AgendaModel
from django.db.models import Q

@login_required(login_url='home:loginUser')
def createAgenda(request):
    form_action = reverse('agendamento:createAgenda')
    form = AgendaForm()

    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            agendas_conflitantes = AgendaModel.objects.filter(
                Q(aProfessional=model.aProfessional) &
                Q(aLocal=model.aLocal) &
                (
                    (Q(agDatIni__lte=model.agDatIni) & Q(agDatFim__gte=model.agDatIni)) |  
                    (Q(agDatIni__lte=model.agDatFim) & Q(agDatFim__gte=model.agDatFim)) |  
                    (Q(agDatIni__gte=model.agDatIni) & Q(agDatFim__lte=model.agDatFim))    
                ) &
                (
                    (Q(agHorIni__lte=model.agHorIni) & Q(agHorFim__gte=model.agHorIni)) |  
                    (Q(agHorIni__lte=model.agHorFim) & Q(agHorFim__gte=model.agHorFim)) |  
                    (Q(agHorIni__gte=model.agHorIni) & Q(agHorFim__lte=model.agHorFim))    
                )
            )
            if agendas_conflitantes.exists():
                messages.error(request, 'Agenda com período já existente!')
            else:
                model.save()
                messages.success(request, 'Agenda criada com sucesso!')
                return redirect('agendamento:listAgenda')

    context = {
        'form': form,
        'name_screen': 'Cadastro',
        'name_module': 'Agendamento',
        'updateAgendamento': 0,
        'form_action': form_action,
    }

    return render(
        request,
        "agendamento/agenda/agenda.html",
        context
    )

@login_required(login_url='home:loginUser')
def updateAgenda(request, agenda_id):
    agenda = get_object_or_404(AgendaModel, pk=agenda_id)
    form_action = reverse('agendamento:updateAgenda', args=(agenda_id,))
    
    if request.method == 'POST':
        formMarca = AgendaForm(request.POST, instance=agenda)
        if formMarca.is_valid():
            formMarca.save()
            messages.success(request, 'Agenda atualizada com sucesso!')
            return redirect('agendamento:listAgenda')

        context = {
            'form' : AgendaForm(instance=agenda),
            'form_action': form_action,
            'title':'Cadastro',
            'name_screen': 'Consulta',
            'name_module': 'Agendamento',
            'updateAgendamento': 1,
        }

        return render(
            request,
            'agendamento/agenda/agenda.html',
            context
        )

    context = {
        'form' : AgendaForm(instance=agenda),
        'form_action': form_action,
        'title':'Cadastro',
        'name_screen': 'Consulta',
        'name_module': 'Agendamento',
        'updateAgendamento': 1,
    }

    return render(
        request,
        'agendamento/agenda/agenda.html',
        context
    )