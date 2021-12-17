from django.contrib import messages
from django.shortcuts import render
from pytube import YouTube


def home(request):
    if request.method == "POST":
        try:
            link = request.POST['yt_link']
            video = YouTube(link)

            return render(request, "video.html", {"video": video, "link": link})

        except Exception as exception:
            print(exception)
            messages.add_message(request, messages.ERROR, "Something went wrong, please try again")

    return render(request, "home.html")


def download_video(request):
    if request.method == "POST":
        link = request.POST['video_link']

        try:
            video = YouTube(link)
            video.streams.get_highest_resolution().download('Downloads')
            messages.add_message(request, messages.SUCCESS, "Download completed")
        except Exception as exception:
            print(exception)
            messages.add_message(request, messages.ERROR, "Download failed, please try again")

    return render(request, "home.html")


def download_audio(request):
    if request.method == "POST":
        link = request.POST['video_link']

        try:
            video = YouTube(link)
            video.streams.get_audio_only().download()
            messages.add_message(request, messages.SUCCESS, "Download completed")
        except Exception as exception:
            print(exception)
            messages.add_message(request, messages.ERROR, "Download failed, please try again")

    return render(request, "home.html")
