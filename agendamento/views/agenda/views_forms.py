from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from agendamento.forms import AgendaForm

@login_required(login_url='home:loginUser')
def createAgenda(request):
    form_action = reverse('agendamento:createAgenda')
    form = AgendaForm()

    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agenda criada com sucesso!')
            return redirect('agendamento:index')

    context = {
        'form': form,
        'name_screen': 'Cadastro',
        'name_module': 'Agendamento',
        'form_action': form_action,
    }

    return render(
        request,
        "agendamento/agenda/agenda.html",
        context
    )