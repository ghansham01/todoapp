from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tasklist(request):
    return HttpResponse("Hello, You're at the task list page.")
