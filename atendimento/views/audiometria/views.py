from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from tempfile import NamedTemporaryFile
from atendimento.models import AudiometriaModel
from django.core.paginator import Paginator
from django.http import HttpResponse
from atendimento.views.atendimento import generate_word_document, save_as_pdf
import os

@login_required(login_url='home:loginUser')
def listAudiometria(request):
    form_action = reverse('atendimento:audiometria')

    audiometrias = AudiometriaModel.objects.all().order_by('id')

    paginator = Paginator(audiometrias, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'page_obj': page_obj,
            'title':'Cadastro',
            'name_module': 'Atendimento',
            'form_action': form_action,
    }

    return render(
        request,
        'atendimento/audiometria/search.html',
        context
    )

@login_required(login_url='home:loginUser')
def searchAudiometria(request):
    search_audiometria = request.GET.get('q','').strip()

    if search_audiometria == "":
        return redirect('estoque:listAudiometria')

    if search_audiometria.isdigit():
        audiometrias = AudiometriaModel.objects.filter(id=int(search_audiometria)).order_by('id')

    paginator = Paginator(audiometrias, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Atendimento',
            'page_obj': page_obj,
    }

    return render(
        request,
        'atendimento/audiometria/search.html',
        context
    )

def download_documento_audiometria(request):
    id_registro = request.GET.get('registro')
    documento = request.GET.get('documento')
    audiometria_obj = get_object_or_404(AudiometriaModel, id=id_registro)
    
    url = ''
    data = {
        'aClient': audiometria_obj.aClient,
        'aClient.age': audiometria_obj.aClient.age,
        'auAudio': audiometria_obj.auAudio,
        'auData': audiometria_obj.auData,
        'auMedSo': audiometria_obj.auMedSo,
        'auCalib': audiometria_obj.auCalib,
        'auMVaOe': audiometria_obj.auMVaOe,
        'auMVaOd': audiometria_obj.auMVaOd,
        'auMVoOe': audiometria_obj.auMVoOe,
        'auMVoOd': audiometria_obj.auMVoOd,
        'auMosPoOe': audiometria_obj.auMosPoOe,
        'auMosdBOe': audiometria_obj.auMosdBOe,
        'auSTROe': audiometria_obj.auSTROe,
        'auLDVOe': audiometria_obj.auLDVOe,
        'auMascOe': audiometria_obj.auMascOe,
        'auSpaceOe': audiometria_obj.auSpaceOe,
        'auDisPoOe': audiometria_obj.auDisPoOe,
        'auDisdBOe': audiometria_obj.auDisdBOe,
        'auMosPoOd': audiometria_obj.auMosPoOd,
        'auMosdBOd': audiometria_obj.auMosdBOd,
        'auSTROd': audiometria_obj.auSTROd,
        'auLDVOd': audiometria_obj.auLDVOd,
        'auMascOd': audiometria_obj.auMascOd,
        'auSpaceOd': audiometria_obj.auSpaceOd,
        'auDisPoOd': audiometria_obj.auDisPoOd,
        'auDisdBOd': audiometria_obj.auDisdBOd,
        'auObser': audiometria_obj.auObser
    }

    match documento:
        case 'fichaAudiometria':
            doc = 'FICHA DE AUDIOMETRIA.docx'
            url = 'utils\\docs\\FICHA DE AUDIOMETRIA.docx'

    word_document = generate_word_document(data, url, id_registro)

    temp_file = NamedTemporaryFile(delete=False, suffix='.docx')
    temp_file.write(word_document.getvalue())
    temp_file.close()

    pdf_file_path = save_as_pdf(temp_file.name)

    with open(pdf_file_path, "rb") as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={doc.replace(".docx", ".pdf")}'

    # Remove o arquivo temporário
    os.remove(temp_file.name)

    return response