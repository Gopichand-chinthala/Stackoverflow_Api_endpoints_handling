from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.
def Question_list(request):
    response= requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
    Questions=response.json()['items']
    context={
        'Questions':Questions,
    }
    return render(request,'stack_api/questions_list.html',context)

def Posts_list(request):
    response= requests.get('https://api.stackexchange.com/2.3/posts?order=desc&sort=activity&site=stackoverflow')
    Posts=response.json()['items']
    context={
        'Posts':Posts,
    }
    return render(request,'stack_api/posts_list.html',context)

def Users_list(request):
    response= requests.get('https://api.stackexchange.com/2.3/users?order=desc&sort=reputation&site=stackoverflow')
    Users=response.json()['items']
    context={
        'Users':Users,
    }
    return render(request,'stack_api/Users_list.html',context)