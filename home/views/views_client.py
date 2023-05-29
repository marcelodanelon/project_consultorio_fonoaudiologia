from django.shortcuts import render, redirect
from django.urls import reverse
from home.forms import ClientForm

def createClient(request):
    formClient = ClientForm()

    if request.method == 'POST':
        formClient = ClientForm(request.POST)

        if formClient.is_valid():
            formClient.save()
            return redirect('home:index')

        context = {
            'form': formClient,
            'formErrors': formClient.errors.items(),
            'title':'Cadastro',
        }

        return render(
            request,
            'home/client.html',
            context
        )

    context = {
            'form': ClientForm(),
            'title':'Cadastro',
    }

    return render(
        request,
        'home/client.html',
        context
    )