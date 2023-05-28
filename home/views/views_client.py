from django.shortcuts import render
from home.forms import ClientForm

def Create(request):
    form = ClientForm()

    if request.method == 'POST':
        ...

    context = {
        'form': form
    }

    return render(
        request,
        'home/client.html',
        context
    )