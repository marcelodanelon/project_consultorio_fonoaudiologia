from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name_module': 'Estoque',
    }

    return render(
        request,
        'storage/index.html',
        context
    )