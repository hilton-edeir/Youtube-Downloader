from django.shortcuts import render
from pytube import YouTube


def home(request):
    return render(request, "home.html")


def download(request):
    if request.method == "POST":
        link = request.POST['link_input']
        yt = YouTube(link)
        videos = yt.streams.all()
        video = list(enumerate(videos))
    return render(request, "home.html")
