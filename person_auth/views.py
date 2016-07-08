from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib import auth

from person_auth.models import Number


def reg(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        return render(request, 'person_auth/answer.html', context={'message': 'something wrong'})
    return render(request, 'person_auth/reg.html', context={'form': UserCreationForm()})


def login(request):
    if request.POST and not auth.get_user(request).is_authenticated():
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        if user is not None:
            return render(request, 'person_auth/answer.html', context={'message': 'success'})
        return render(request, 'person_auth/answer.html', context={'message': 'something wrong'})
    if auth.get_user(request).is_authenticated():
        return redirect('phone')
    return render(request, 'person_auth/login.html', context={'form': AuthenticationForm()})


def phone(request):
    if auth.get_user(request).is_authenticated():
        user = auth.get_user(request)
        if request.POST:
            new_phone = request.POST.get('phone', '')
            Number(phone_number=new_phone, user=user).save()
        all_number = Number.objects.filter(user=user)
        context = {
            'all_number': all_number[::-1],
            'user_name': user.username,
        }
        return render(request, 'person_auth/num_page.html', context=context)
    return redirect('login')


def logout(request):
    auth.logout(request)
    return redirect('login')
