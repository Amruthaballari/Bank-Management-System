from django.shortcuts import render


def home(request):
    return render(request, 'bank/home.html')


def services(request):
    return render(request, 'bank/services.html')


def about(request):
    return render(request, 'bank/about.html')


def contact(request):
    return render(request, 'bank/contact.html')


def login(request):
    return render(request, 'bank/login.html')


def register(request):
    return render(request, 'bank/register.html')