from django.shortcuts import render


def homepage(request):
    return render(request, 'pages/index.html')
# Create your views here.
