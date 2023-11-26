from django.shortcuts import render

def home(request):
    return render(request,'home/index.html')

def produtos(request):
    return render(request, 'home/produtos.html')