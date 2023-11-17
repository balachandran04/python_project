from .views import *
from django.urls import path

urlpatterns =[
    path('', inbox_view,name='inbox'),
    path('c/<conversation_id>/', inbox_view, name='inbox'),


]