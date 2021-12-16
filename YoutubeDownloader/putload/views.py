from django.shortcuts import render
from pytube import YouTube


def home(request):
    return render(request, "home.html")


def download(request, link):
    yt = YouTube(link)
    videos = yt.streams.all()
    video = list(enumerate(videos))
    return render(request, "home.html", {"video_list": video})
