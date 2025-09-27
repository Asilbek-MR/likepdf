# myproject/myapp/urls.py

from django.urls import path
from .views import home,auth

app_name ='applike'

urlpatterns = [
    path('', home, name='home'),
    path('auth/', auth, name='auth'),
]
