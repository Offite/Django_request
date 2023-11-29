from django.shortcuts import render
from django.http import HttpResponse

def index(request, name="Noname", age=0):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path

    return HttpResponse(f'host: {host} <br> browser: {user_agent} <br> Path: {path} <br> '
                        f'<br> user: {name}, age {age}',
                        headers={'SecretCode': '12345678'})



