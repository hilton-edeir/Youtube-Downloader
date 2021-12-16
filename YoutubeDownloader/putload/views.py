from django.contrib import messages
from django.shortcuts import render
from pytube import YouTube


def home(request):
    if request.method == "POST":
        link = request.POST['link']

        try:
            yt = YouTube(link)
            videos = yt.streams
            list_videos = list(enumerate(videos))
            empty = False

            if len(list_videos) == 0:
                empty = True

            return render(request, "home.html", {"list_videos": list_videos, "empty": empty})

        except:
            messages.add_message(request, messages.ERROR, "We couldn't find nothing, please try again")

    return render(request, "home.html")


def download(request, video):
    if request.method == "POST":
        try:
            video.download()

        except:
            messages.add_message(request, messages.ERROR, "Download failed, please try again")

    return render(request, "home.html")
