from django.contrib import messages
from django.shortcuts import render
from pytube import YouTube


def home(request):
    if request.method == "POST":
        try:
            link = request.POST['yt_link']
            video = YouTube(link)
            video_streams = video.streams
            video_thumbnail = YouTube(link).thumbnail_url

            return render(request, "video_thumbnail.html", {"video_thumbnail": video_thumbnail, "video_streams": video_streams})

        except:
            messages.add_message(request, messages.ERROR, "Something went wrong, please try again")

    return render(request, "home.html")


def downnload_video(request, video):
    pass


def downnload_audio(request, video):
    pass

