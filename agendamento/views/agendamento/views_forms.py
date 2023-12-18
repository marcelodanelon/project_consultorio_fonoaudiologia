from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from agendamento.forms import AgendamentoForm
from agendamento.models import AgendamentoModel

@login_required(login_url='home:loginUser')
def createAgendamento(request):
    form_action = reverse('agendamento:createAgendamento')
    form = AgendamentoForm()

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento gravado com sucesso!')
            return redirect('agendamento:listAgendamento')

        print(form.errors)  

    context = {
        'form': form,
        'name_screen': 'Agendamento',
        'name_module': 'Agendamento',
        'title': 'Agendamento',
        'updateAgendamento': 0,
        'form_action': form_action,
    }

    return render(
        request,
        "agendamento/agendamento/agendamento.html",
        context
    )

@login_required(login_url='home:loginUser')
def updateAgendamento(request, agendamento_id):
    agendamento = get_object_or_404(AgendamentoModel, pk=agendamento_id)
    form_action = reverse('agendamento:updateAgendamento', args=(agendamento_id,))
    
    if request.method == 'POST':
        formAgendamento = AgendamentoForm(request.POST, instance=agendamento)
        if formAgendamento.is_valid():
            formAgendamento.save()
            messages.success(request, 'Agendamento atualizado com sucesso!')
            return redirect('agendamento:listAgendamento')

        context = {
            'form' : AgendamentoForm(instance=agendamento),
            'form_action': form_action,
            'title': 'Agendamento',
            'name_screen': 'Consulta',
            'name_module': 'Agendamento',
            'updateAgendamento': 1,
        }

        return render(
            request,
            'agendamento/agendamento/agendamento.html',
            context
        )

    context = {
        'form' : AgendamentoForm(instance=agendamento),
        'form_action': form_action,
        'title':'Cadastro',
        'name_screen': 'Consulta',
        'name_module': 'Agendamento',
        'option_delete': 'yes',
        'horario_agendamento': str(agendamento.agHoraAg),
        'agendamento': agendamento,
        'updateAgendamento': 1,
    }

    return render(
        request,
        'agendamento/agendamento/agendamento.html',
        context
    )

@login_required(login_url='home:loginUser')
def deleteAgendamento(request, agendamento_id):
    agendamento = get_object_or_404(AgendamentoModel, pk=agendamento_id)
    form_action = reverse('agendamento:deleteAgendamento', args=(agendamento_id,))

    confirmation = request.POST.get('confirmation_delete', 'no')

    if confirmation == 'yes':
        agendamento.delete()
        messages.success(request, 'Agendamento deletado com sucesso!')
        return redirect ('agendamento:listAgendamento')

    context = {
        'form': AgendamentoForm(instance=agendamento),
        'title': 'Agendamento',
        'name_screen': 'Atualizar',
        'name_module': 'Home',
        'option_delete': 'yes',
        'updateAgendamento': 1,
        'agendamento': agendamento,
        'confirmation_delete': confirmation,
        'form_action': form_action,
    }

    return render(
        request,
        'agendamento/agendamento/agendamento.html',
        context
    )