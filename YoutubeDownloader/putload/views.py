from django.contrib import messages
from django.shortcuts import render
from pytube import YouTube


def home(request):
    if request.method == "POST":
        link = request.POST['link']

        try:
            yt = YouTube(link)
            videos = yt.streams
            video = list(enumerate(videos))

        except:
            messages.add_message(request, messages.ERROR, 'Download failed, please try again')


    return render(request, "home.html")

