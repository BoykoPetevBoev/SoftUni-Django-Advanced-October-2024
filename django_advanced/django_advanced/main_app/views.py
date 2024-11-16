from django.shortcuts import render, redirect, resolve_url


def home(request):
    return render(request, 'common/home.html')


