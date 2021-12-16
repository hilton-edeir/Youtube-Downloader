from django.shortcuts import render
from pytube import YouTube


def home(request, link):

    return render(request, "home.html")


def download():
    pass