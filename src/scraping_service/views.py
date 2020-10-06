from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now().date()
    name = 'Dave'
    value = {'date':date, 'name':name} # передача данных через словарь
    return render(request, 'home.html', value)