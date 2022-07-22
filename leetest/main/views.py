from fileinput import hook_encoded
from os import access
from urllib import request, response
from wsgiref import headers
from django.shortcuts import HttpResponse, render, redirect
from django.conf import settings
import requests
import os
import subprocess

def getIntegers(string):
        numbers = [int(x) for x in string.split() if x.isnumeric()]
        return numbers

def is_authenticated(request):
    url = 'https://api.intra.42.fr/v2/me'
    data = request.COOKIES.get('42_access_token', 'none')
    if (data == 'none'):
        return False
    headers = {
        'Authorization': 'Bearer ' + data,
    }
    response = requests.get(url=url, headers=headers)
    request.session['42_me'] = response.json()
    if (response.status_code == 200):
        return True
    return False

def home(request):
    if (not is_authenticated(request)):
        return redirect(login)
    data = request.session['42_me']
    print(data)
    full_name = data['first_name'] + ' ' + data['last_name']
    photo = data['image_url']
    output = subprocess.check_output("node /workspace/leetmove/allo/test.js", shell=True)
    # directories = os.system("node /workspace/leetmove/allo/test.js")
    encoding = 'utf-8'
    test = str(output, encoding)
    time_spent = getIntegers(test)[0]
    context = {
        'full_name': full_name,
        'photo': photo,
        'time_spent' : time_spent
    }
    return render(request, "home/index.html", context)

def login(request):
    if (is_authenticated(request)):
        return redirect(home)
    return render(request, "home/login.html")

def get_access_token(code):
    headers = {
        'grant_type':'authorization_code',
        'client_id':settings.CLIENT_ID,
        'client_secret': settings.SECRET_ID,
        'code': code,
        'redirect_uri': settings.REDIRECT_URI
    }
    response = requests.post(url=settings.OAUTH_ENDPOINT, params=headers)
    return response.json()
    
def oauth2_callback(request):
    code = request.GET['code']
    access_token = get_access_token(code)
    access_token = access_token['access_token']
    response = redirect(login)
    response.set_cookie('42_access_token', access_token)
    return response


def logout(request):
    res = redirect(login)
    res.delete_cookie('42_access_token')
    print(request.COOKIES.get('42_access_token', 'none'))
    return res