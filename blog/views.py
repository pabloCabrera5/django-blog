from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
# vistas que cargaran nuestras paginas html

def post_list(request):
    return render(request, 'blog/post_list.html', {})