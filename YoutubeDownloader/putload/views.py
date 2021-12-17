from django.contrib import messages
from django.shortcuts import render
from pytube import YouTube


def home(request):
    if request.method == "POST":
        try:
            link = request.POST['yt_link']
            video = YouTube(link)

            return render(request, "video_thumbnail.html", {"video": video, "link": link})

        except:
            messages.add_message(request, messages.ERROR, "Something went wrong, please try again")

    return render(request, "home.html")


def downnload_video(request):
    if request.method == "POST":
        link = request.POST['video_link']
        print(link)
        try:
            video = YouTube(link)
            video.streams.get_highest_resolution().download()
            messages.add_message(request, messages.SUCCESS, "Download completed")
        except:
            messages.add_message(request, messages.ERROR, "Download failed, please try again")

    return render(request, "home.html")


def downnload_audio(request):
    if request.method == "POST":
        link = request.POST['video_link']

        try:
            video = YouTube(link)
            video.streams.filter(file_extension="mp3").get_highest_resolution().download()
            messages.add_message(request, messages.SUCCESS, "Download completed")
        except:
            messages.add_message(request, messages.ERROR, "Download failed, please try again")

    return render(request, "home.html")