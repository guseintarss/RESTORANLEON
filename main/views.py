from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def menu(request):
    return render(request, 'main/menu.html')

def bakets(request):
    return render(request, 'main/bakets.html')

def blog(request):
    return render(request, 'main/blog.html')

def inter(request):
    return render(request, 'main/inter.html')

def otvz(request):
    return render(request, 'main/otzv.html')

def korp(request):
    return render(request, 'main/korp.html')