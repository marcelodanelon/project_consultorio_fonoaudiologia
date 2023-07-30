from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='home:loginUser')
def index(request):
    context = {
        'name_module': 'Estoque',
    }

    return render(
        request,
        'estoque/index.html',
        context
    )