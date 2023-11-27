from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from atendimento.forms import MotivosAtendimentoForm
from atendimento.models import MotivosAtendimentoModel

@login_required(login_url='home:loginUser')
def createMotivo(request):
    form_action = reverse('atendimento:createMotivo')

    if request.method == 'POST':
        formMotivo = MotivosAtendimentoForm(request.POST)

        if formMotivo.is_valid():
            formMotivo.save()
            messages.success(request, 'Motivo cadastrada com sucesso!')
            return redirect('atendimento:listMotivo')

        context = {
            'form': formMotivo,
            'title':'Cadastro',
            'name_module': 'Atendimento',
            'name_screen': 'Cadastro',
            'form_action': form_action,
        }

        return render(
            request,
            'motivos/motivo.html',
            context
        )

    context = {
            'form': MotivosAtendimentoForm(),
            'title':'Cadastro',
            'name_screen': 'Cadastro',
            'name_module': 'Atendimento',
            'form_action': form_action,
    }

    return render(
        request,
        'atendimento/motivos/motivo.html',
        context
    )

@login_required(login_url='home:loginUser')
def updateMotivo(request, motivo_id):
    motivo = get_object_or_404(MotivosAtendimentoModel, pk=motivo_id)
    form_action = reverse('atendimento:updateMotivo', args=(motivo_id,))
    
    if request.method == 'POST':
        formMotivo = MotivosAtendimentoForm(request.POST, instance=motivo)
        if formMotivo.is_valid():
            formMotivo.save()
            messages.success(request, 'Motivo atualizada com sucesso!')
            return redirect('atendimento:listMotivo')

        context = {
            'form' : MotivosAtendimentoForm(instance=motivo),
            'form_action': form_action,
            'motivo': motivo,
            'title':'Cadastro',
            'name_screen': 'Cadastro',
            'option_delete': 'yes',
            'name_module': 'Atendimento',
        }

        return render(
            request,
            'atendimento/motivos/motivo.html',
            context
        )

    context = {
        'form' : MotivosAtendimentoForm(instance=motivo),
        'form_action': form_action,
        'motivo': motivo,
        'title':'Cadastro',
        'name_screen': 'Cadastro',
        'option_delete': 'yes',
        'name_module': 'Atendimento',
    }

    return render(
        request,
        'atendimento/motivos/motivo.html',
        context
    )

@login_required(login_url='home:loginUser')
def deleteMotivo(request, motivo_id):
    motivo = get_object_or_404(MotivosAtendimentoModel, pk=motivo_id)
    form_action = reverse('atendimento:deleteMotivo', args=(motivo_id,))

    confirmation = request.POST.get('confirmation_delete', 'no')

    if confirmation == 'yes':
        motivo.delete()
        messages.success(request, 'Motivo deletado com sucesso!')
        return redirect ('atendimento:listMotivo')

    context = {
        'form': MotivosAtendimentoForm(instance=motivo),
        'title':'Cadastro',
        'name_screen': 'Atualizar',
        'name_module': 'Atendimento',
        'option_delete': 'yes',
        'motivo': motivo,
        'confirmation_delete': confirmation,
        'form_action': form_action,
    }

    return render(
        request,
        'atendimento/motivos/motivo.html',
        context
    )