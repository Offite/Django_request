from django.urls import path, re_path
from .views import index


urlpatterns = [
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)', index),
    # path('user/<str:name>/<int:age>', index, name='home'), #http://127.0.0.1:8000/app/user/TOM
    path('user/<str:name>', index, name='home'),
    path('user', index, name='home'),
]