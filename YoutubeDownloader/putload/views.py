from django.contrib import messages
from django.shortcuts import render
from pytube import YouTube


def home(request):
    if request.method == "POST":
        link = request.POST['link_yt']
        video = YouTube(link)
        video.streams.get_by_itag(137)


        '''
        list_videos = list(enumerate(videos))
        empty = False

        if len(list_videos) == 0:
            empty = True

        return render(request, "home.html", {"list_videos": list_videos, "empty": empty})
       
    except:
        messages.add_message(request, messages.ERROR, "We couldn't find nothing, please try again")
         '''

    return render(request, "home.html")


