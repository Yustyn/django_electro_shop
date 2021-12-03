from django.shortcuts import redirect, render
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:home')
        else:
            pass
    return render(request, 'authenticate/login.html')


# def log_out(request):
#     if request.method == "POST":
#         logout()
#     return render(request, 'authenticate/login.html')
