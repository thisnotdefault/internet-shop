from django.contrib import auth
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
