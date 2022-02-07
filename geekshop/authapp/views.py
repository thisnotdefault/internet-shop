from django.contrib import auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from .forms import ShopUserEditForm, ShopUserLoginForm, ShopUserRegisterForm


def register(request):
    if request.method == "POST":
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse("auth:login"))
    else:
        register_form = ShopUserRegisterForm()
    return render(
        request,
        "authapp/register.html",
        context={
            "title": "Регистрация",
            "form": register_form,
        },
    )


def login(request):
    if request.method == "POST":
        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]

            user = auth.authenticate(request.user, username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                if 'next' in request.GET.keys():
                    return HttpResponseRedirect(request.GET['next'])
                return HttpResponseRedirect(reverse("main"))
    else:
        login_form = ShopUserLoginForm()
    return render(
        request,
        "authapp/login.html",
        context={
            "title": "Войдите в аккаунт",
            "form": login_form,
        },
    )


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main"))


@login_required
def edit(request):
    if request.method == "POST":
        edit_form = ShopUserEditForm(
            request.POST,
            request.FILES,
            instance=request.user,
        )
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("main"))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
        
    
    return render(
        request,
        "authapp/edit.html",
        context={
            "title": "Редактирование",
            "form": edit_form,
        },
    )


@login_required
def change_password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)  
            return HttpResponseRedirect(reverse("main"))
    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(
        request,
        "authapp/change_password.html",
        context={
            "title": "Смена пароля",
            "password_change_form": password_change_form,
        },
    )
        
    
    