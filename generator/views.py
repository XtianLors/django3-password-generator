from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password':'1034alACMEksjdc8'})

def password(request):

    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('@!#$%&/()=?+*-_,.;:<>~¬'))

    if request.GET.get('accentuated'):
        characters.extend(list('áéíóúäëïöüâêîôûàèìòù'))

    length = int(request.GET.get('length', 12))
    for x in range(length):
        thepassword += random.choice(characters )
    return render(request, 'generator/password.html',{'password':thepassword})


def birds(request):
    return HttpResponse('birds')

def aboutpg(request):
    return render(request, 'generator/info.html')
