from fileinput import hook_encoded
from os import access
from urllib import request, response
from wsgiref import headers
from django.shortcuts import HttpResponse, render, redirect
from django.conf import settings
import requests
import os
import subprocess
import json

session = {'PHPSESSID': 'ol3kmcc6s3kq25hb0bj4mdr72m'}
user_login = 'none'

def get_needed_blackhole(overseer_data):
    user_y = overseer_data['student'][0]['y']
    user_x = overseer_data['student'][0]['x']
    user_stats = {} if user_x > 614 else overseer_data['plotData']['plots'][user_x]
    small_wire = user_stats.get('Min. of double ETA') or user_stats.get('Max blackhole')

    if user_y < small_wire:
        return small_wire - user_y
    else:
        return 0

def api_get_project_exp(request, project_id):
    print("hey")
    payload={}
    ft_token = request.COOKIES.get('42_access_token')
    headers = { 'Authorization': f'Bearer {ft_token}' }
    url = f"https://api.intra.42.fr/v2/projects/{project_id}/project_sessions?filter[campus_id]=21"

    response = requests.request("GET", url, headers=headers, data=payload)
    res_json = json.dumps(json.loads(response.text))

    return HttpResponse(res_json, content_type="application/json")

def api_get_projects(request):
    payload={}
    ft_token = request.COOKIES.get('42_access_token')
    user_id = request.session['42_me']['id']
    headers = { 'Authorization': f'Bearer {ft_token}' }
    url = f"https://api.intra.42.fr/v2/users/{user_id}/projects_users?filter[status]=in_progress"

    response = requests.request("GET", url, headers=headers, data=payload)
    res_json = json.dumps(json.loads(response.text))

    return HttpResponse(res_json, content_type="application/json")

def getIntegers(string):
        numbers = [int(x) for x in string.split() if x.isnumeric()]
        return numbers

def get_overseer_id(login):
    response = requests.get(f'https://overseer.1337.ma/api/users?page=1&username={login}', cookies = session).json()
    user_id = response['hydra:member'][0]['student']['id']
    return user_id

def get_overseer_data(login):
    user_id = get_overseer_id(login)
    res_body = requests.get(f"https://overseer.1337.ma/_next/data/QLfn6qnLowKAK_ZiVhg8E/user/{user_id}.json?id=0", cookies = session).json()
    overseer_data = res_body['pageProps']['data']
    return overseer_data

def get_user_status(overseer_data):
    user_y = overseer_data['student'][0]['y']
    user_x = overseer_data['student'][0]['x']
    user_stats = {} if user_x > 614 else overseer_data['plotData']['plots'][user_x]
    big_wire = user_stats.get('Avg. teams')
    small_wire = user_stats.get('Min. of double ETA') or user_stats.get('Max blackhole')

    print(overseer_data['student'][0]['login'])
    if user_x > 614:
    	return "Finshed 💼"
    elif user_y >= big_wire:
    	return "Oustanding 😎"
    elif user_y < big_wire and user_y >= small_wire:
    	return 'Good Pace 🙂'
    else:
    	return 'More Effort 😥'

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
    data_42 = request.session['42_me']
    full_name = data_42['first_name'] + ' ' + data_42['last_name']
    photo = data_42['image_url']
    login_42 = data_42['login']
    user_login = login_42
    overseer_data = get_overseer_data(login_42)
    time_spent = overseer_data['student'][0]['x']
    blackhole = overseer_data['student'][0]['y']
    status = get_user_status(overseer_data)
    needed_bh = get_needed_blackhole(overseer_data)
    # test = get_projects(login_42)
    # print(test.text)
    context = {
        'full_name': full_name,
        'photo': photo,
        'time_spent' : time_spent,
        'blackhole':blackhole,
        'status': status,
        'needed_bh': needed_bh
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
    expire = access_token['expires_in']
    access_token = access_token['access_token']
    response = redirect(login)
    response.set_cookie('42_access_token', access_token, max_age=expire)
    return response

def calulate_bh(request):
    pass

def logout(request):
    res = redirect(login)
    res.delete_cookie('42_access_token')
    print(request.COOKIES.get('42_access_token', 'none'))
    return res