from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #para cualquier url carga la vista que genera la llamda a post_list
]