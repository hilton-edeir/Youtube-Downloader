from django.shortcuts import render
from pytube import YouTube


def home(request):
    return render(request, "home.html")


def download(request):
    if request.method == "POST":
        link = request.POST['link']
        yt = YouTube(link)
        videos = yt.streams.all()
        video = list(enumerate(videos))

        for i in video:
            print(i)

    return render(request, "home.html")
