from django.shortcuts import render
from django.http import HttpResponse
    def index(request):
        host = request.get_host()
        user_agent = request.META.get('HTTP_USER_AGENT')
        ip_address = request.META.get('REMOTE_ADDR')
        return render(request, 'index.html', {'host': host, 'user_agent': user_agent, 'ip_address': ip_address})

    def error(request):
        status_code = 500
        message = 'К сожалению произошла ошибка'
        return render(request, 'error.html', {'status_code': status_code, 'message': message})

    def user(request):
        login = request.GET.get('login', 'default_login')
        folder_name = request.GET.get('folder_name', 'default_folder')
        post_number = request.GET.get('post_number', 1)
        return render(request, 'user.html', {'login': login, 'folder_name': folder_name, 'post_number': post_number})