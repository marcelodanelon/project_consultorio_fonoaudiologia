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
            return redirect('agendamento:index')

    context = {
        'form': form,
        'name_screen': 'Agendamento',
        'name_module': 'Agendamento',
        'updateAgendamento': 0,
        'form_action': form_action,
    }

    return render(
        request,
        "agendamento/agendamento/agendamento.html",
        context
    )

# @login_required(login_url='home:loginUser')
# def updateAgenda(request, agenda_id):
#     agenda = get_object_or_404(AgendamentoModel, pk=agenda_id)
#     form_action = reverse('agendamento:updateAgenda', args=(agenda_id,))
    
#     if request.method == 'POST':
#         formMarca = AgendamentoForm(request.POST, instance=agenda)
#         if formMarca.is_valid():
#             formMarca.save()
#             messages.success(request, 'Agenda atualizada com sucesso!')
#             return redirect('agendamento:listAgenda')

#         context = {
#             'form' : AgendamentoForm(instance=agenda),
#             'form_action': form_action,
#             'title':'Cadastro',
#             'name_screen': 'Consulta',
#             'name_module': 'Agendamento',
#             'updateAgendamento': 1,
#         }

#         return render(
#             request,
#             'agendamento/agenda/agenda.html',
#             context
#         )

#     context = {
#         'form' : AgendamentoForm(instance=agenda),
#         'form_action': form_action,
#         'title':'Cadastro',
#         'name_screen': 'Consulta',
#         'name_module': 'Agendamento',
#         'updateAgendamento': 1,
#     }

#     return render(
#         request,
#         'agendamento/agenda/agenda.html',
#         context
#     )