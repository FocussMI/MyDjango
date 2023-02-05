from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

def index(request):
    return HttpResponse("Main Page")

def categories(request, catid):
    if request.POST:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request,year):
    if int(year) > 2020:
        return HttpResponseBadRequest("Некорректные данные(400)")
    else:
        return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
   return HttpResponseNotFound('<h1>Страница не найдена(404)</h1>')

def access(request,age):
    if (age > 18):
        return HttpResponse("Доступ разрешен")
    else:
        return HttpResponseForbidden("Доступ заблокирован")
