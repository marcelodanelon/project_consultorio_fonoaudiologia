from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from home.forms import ProfessionalForm
from home.models import ProfessionalModel
from django.contrib import messages

def createProfessional(request):
    form_action = reverse('home:createProfessional')

    if request.method == 'POST':
        formProfessional = ProfessionalForm(request.POST)

        if formProfessional.is_valid():
            form = formProfessional.save()
            messages.success(request, 'Unidade cadastrada com sucesso!')
            return redirect('home:updateProfessional',form.id)

        context = {
            'form': formProfessional,
            'title':'Cadastro',
            'form_action': form_action,
        }

        return render(
            request,
            'home/professional/professional.html',
            context
        )

    context = {
            'form': ProfessionalForm(),
            'title':'Cadastro',
            'name_screen': 'Cadastro',
            'form_action': form_action,
    }

    return render(
        request,
        'home/professional/professional.html',
        context
    )

def updateProfessional(request, professional_id):
    professional = get_object_or_404(ProfessionalModel, pk=professional_id)
    form_action = reverse('home:updateLocal', args=(professional_id,))

    if request.method == 'POST':
        formProfessional = ProfessionalForm(request.POST, instance=professional)

        if formProfessional.is_valid():
            formProfessional.save()
            messages.success(request, 'Profissional atualizado com sucesso!')
            return redirect('home:listLocal')

        context = {
            'form': formProfessional,
            'title':'Cadastro',
            'name_screen': 'Atualizar',
            'option_delete': 'yes',
            'professional': professional,
            'form_action': form_action,
        }

        return render(
            request,
            'home/professional/professional.html',
            context
        )

    context = {
            'form': ProfessionalForm(instance=professional),
            'title':'Cadastro',
            'name_screen': 'Atualizar',
            'option_delete': 'yes',
            'professional': professional,
            'form_action': form_action,
    }

    return render(
        request,
        'home/professional/professional.html',
        context
    )

def deleteProfessional(request, professional_id):
    professional = get_object_or_404(ProfessionalModel, pk=professional_id)
    form_action = reverse('home:deleteLocal', args=(professional_id,))

    confirmation = request.POST.get('confirmation_delete', 'no')

    if confirmation == 'yes':
        professional.delete()
        messages.success(request, 'Profissional deletado com sucesso!')
        return redirect ('home:listLocal')

    context = {
        'form': ProfessionalForm(instance=professional),
        'title':'Cadastro',
        'name_screen': 'Atualizar',
        'option_delete': 'yes',
        'professional': professional,
        'confirmation_delete': confirmation,
        'form_action': form_action,
    }

    return render(
        request,
        'home/professional/professional.html',
        context
    )



