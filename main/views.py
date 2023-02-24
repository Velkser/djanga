from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Главная страница',
        'values':['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 22,
            'hobby': 'Programming'
        }
    }
    return render(request, 'page1.html', data)

def about(request):
    data = {
        'title': 'Про нас'
    }
    return render(request,'about.html', data)

def login(request):
    data = {
        'title': 'Страница Логина'
    }
    return render(request,'login.html', data)





