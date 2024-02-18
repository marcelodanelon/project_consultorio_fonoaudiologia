from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from atendimento.forms import AudiometriaForm
from atendimento.models import AudiometriaModel
from django.http import HttpResponse
from django.http import JsonResponse
import base64
import os

@login_required(login_url='home:loginUser')
def audiometria(request):
    form_action = reverse('atendimento:audiometria')
    form = AudiometriaForm()

    if request.method == 'POST':
        form = AudiometriaForm(request.POST)
        if form.is_valid():
            formAud_instance = form.save()
            messages.success(request,'Audiometria gravada com sucesso!')

            response = HttpResponse(status=204)
            response['id_registro'] = str(formAud_instance.id)
            return response

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
            formAud_instance = formAudiometria.save()
            messages.success(request, 'Audiometria atualizada com sucesso!')
            
            response = HttpResponse(status=204)
            response['id_registro'] = str(formAud_instance.id)
            return response
        
        context = {
            'form': formAudiometria,
            'title':'Cadastro',
            'name_screen': 'Atualizar',
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
            'update': 'yes',
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

def save_images_planos_audiometria(request):
    if request.method == 'POST':
        image_data = request.POST.get('image')
        formid = request.POST.get('formId')
        componentId = request.POST.get('componentId')
        print(componentId)
        if image_data:
            image_data_bytes = base64.b64decode(image_data.split(',')[1])

            directory = 'utils/data_files/temp_images_audiometria/'

            os.makedirs(directory, exist_ok=True)

            file_path = os.path.join(directory, f"{formid}_{componentId}.png")

            with open(file_path, 'wb') as f:
                f.write(image_data_bytes)
            return JsonResponse({'message': 'Imagem salva com sucesso!', 'file_path': file_path})
    return JsonResponse({'error': 'Erro ao salvar a imagem.'}, status=400)