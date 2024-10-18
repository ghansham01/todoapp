from django import path
from . import views

urlpatterns =[
    path('', views.tasklist, name='tasks'),
    
]