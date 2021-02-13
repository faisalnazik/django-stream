from __future__ import unicode_literals
from django.shortcuts import render, redirect
from web.datasource import DataSource
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from . import messages

ds = DataSource()

@login_required
@csrf_exempt 
def addToList(request):
    resp = {}
    
    if (request.method == "POST"):
        resp = ds.addToList(request.POST, request.user)

    return JsonResponse(resp)

@csrf_exempt 
def doLogin(request):
    resp = {}

    if (request.method == "POST"):
        user = ds.auth(request)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return JsonResponse(messages.errors["invalid_user"])

    return JsonResponse(resp)

@csrf_exempt 
def doRegister(request):
    resp = {}

    if (request.method == "POST"):
        user = ds.register(request)

        if user is not None:
            user = ds.auth(request)
            login(request, user)
            return redirect("/")
        else:
            return JsonResponse(messages.errors["error_register_user"])

    return JsonResponse(resp)