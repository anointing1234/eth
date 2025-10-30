from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout,login as auth_login,authenticate



def empty(request):
    return render(request,'page.html')

def home(request):
    return render(request,'index.html')


