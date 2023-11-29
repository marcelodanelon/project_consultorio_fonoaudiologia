from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from datetime import date
from atendimento.forms import AudiometriaForm
from atendimento.models import AudiometriaModel

@login_required(login_url='home:loginUser')
def audiometria(request):
    form_action = reverse('atendimento:audiometria')
    form = AudiometriaForm()

    if request.method == 'POST':
        form = AudiometriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Audiometria gravada com sucesso!')
            return redirect('atendimento:listAudiometria')

    context = {
        'form' : form,
        'name_screen': 'Audiometria',
        'name_module': 'Atendimento',
        'form_action': form_action,
    }

    return render(
        request, 
        'atendimento/audiometria/audiometria.html', 
        context
    )

@login_required(login_url='home:loginUser')
def updateAudiometria(request, audiometria_id):
    audiometria = get_object_or_404(AudiometriaModel, pk=audiometria_id)
    form_action = reverse('atendimento:updateAudiometria', args=(audiometria_id,))

    if request.method == 'POST':
        formAudiometria = AudiometriaForm(request.POST, instance=audiometria)

        if formAudiometria.is_valid():
            print(formAudiometria['auCoordenadas_planoI_Linha1'])
            formAudiometria.save()
            messages.success(request, 'Audiometria atualizada com sucesso!')
            return redirect('atendimento:listAudiometria')
        
        context = {
            'form': formAudiometria,
            'title':'Cadastro',
            'name_screen': 'Atualizar',
            'option_delete': 'yes',
            'audiometria': audiometria,
            'form_action': form_action,
            'name_module': 'Atendimento',
        }

        return render(
            request,
            'atendimento/audiometria/audiometria.html',
            context
        )

    context = {
            'form': AudiometriaForm(instance=audiometria),
            'title':'Cadastro',
            'name_screen': 'Atualizar',
            'option_delete': 'yes',
            'audiometria': audiometria,
            'form_action': form_action,
            'name_module': 'Atendimento',
    }

    return render(
        request,
        'atendimento/audiometria/audiometria.html',
        context
    )

@login_required(login_url='home:loginUser')
def deleteAudiometria(request, audiometria_id):
    audiometria = get_object_or_404(AudiometriaModel, pk=audiometria_id)
    form_action = reverse('atendimento:deleteAudiometria', args=(audiometria_id,))

    confirmation = request.POST.get('confirmation_delete', 'no')

    if confirmation == 'yes':
        audiometria.delete()
        messages.success(request, 'Audiometria deletada com sucesso!')
        return redirect ('atendimento:listAudiometria')

    context = {
        'form': AudiometriaForm(instance=audiometria),
        'title':'Cadastro',
        'name_screen': 'Atualizar',
        'option_delete': 'yes',
        'audiometria': audiometria,
        'confirmation_delete': confirmation,
        'form_action': form_action,
        'name_module': 'Atendimento',
    }

    return render(
        request,
        'atendimento/audiometria/audiometria.html', 
        context
    )