from django.shortcuts import render

# Create your views here.
def Index(request):
    context = {
        'title': 'Home',
    }

    return render(
        request,
        'home/index.html',
        context
    )

