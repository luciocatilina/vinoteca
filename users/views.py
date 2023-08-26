from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm




def login(request):

    if request.method == 'POST':

        form_login = MyAuthForm(request, data=request.POST)

        if form_login.is_valid():

            user = form_login.cleaned_data.get('username')
            passw = form_login.cleaned_data.get('password')

            user = authenticate(username=user, password=passw)

            if user:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'index.html')
    else:
        form_login = MyAuthForm()

    return render(request, 'login.html', {'form_login': form_login})


def registration(request):

    if request.method == 'POST':
        form_registration = RegistrationForm(request.POST)

        if form_registration.is_valid():
            username = form_registration.cleaned_data['username']
            passw = form_registration.cleaned_data['password1']
            form_registration.save()
            user = authenticate(username=username,
                                password=passw)
            if user:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'index.html')

    else:
        form_registration = RegistrationForm()

    return render(request, 'registration.html', {'form_registration': form_registration})


class MyAuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': gettext_lazy(
            'Wrong username or password'
        )
    }