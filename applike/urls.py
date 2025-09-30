# myproject/myapp/urls.py

from django.urls import path
from .views import (home,auth,
compress,convert,editpdf, merge,
pdftojpg,price,pdftoword,protect,unlock,signpdf,split

)

app_name ='applike'

urlpatterns = [
    path('', home, name='home'),
    path('auth/', auth, name='auth'),
    path('compress/', compress, name='compress'),
    path('convert/', convert, name='convert'),
    path('editpdf/', editpdf, name='editpdf'),
    path('merge/', merge, name='merge'),
    path('pdftojpg/', pdftojpg, name='pdftojpg'),
    path('price/', price, name='price'),
    path('pdftoword/', pdftoword, name='pdftoword'),
    path('protect/', protect, name='protect'),
    path('unlock/', unlock, name='unlock'),
    path('signpdf/', signpdf, name='signpdf'),
    path('split/', split, name='split'),
]
