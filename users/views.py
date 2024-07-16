from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, LoginForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homePage')
        else:
            return render(request, 'register.html', {'form': form, 'error_message': form.errors})
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigir al usuario a una página de éxito, por ejemplo:
                return redirect('homePage')  # Cambia 'home' por la URL a la que deseas redirigir
            else:
                # Mostrar un mensaje de error indicando que las credenciales son incorrectas
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_View(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('homePage')
