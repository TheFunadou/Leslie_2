from django.shortcuts import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import *
from django.http import Http404


def main(request):
    return render (request, 'templates_base/main.html', {'page_title': 'BODEGA AURRERA: MENU PRINCIPAL'})

