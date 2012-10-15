from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def control(request):
    return render(request, "control.html")

def contingencia(request):
    return render(request, "contingencia.html")
