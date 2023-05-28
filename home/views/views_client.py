from django.shortcuts import render, redirect
from home.forms import ClientForm

def Create(request):
    form = ClientForm()

    if request.method == 'POST':
        form = ClientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home:index')

    context = {
        'title': 'Cadastro',
        'form': form
    }

    return render(
        request,
        'home/client.html',
        context
    )