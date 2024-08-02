
# importing all the required modules
from django.shortcuts import render
from django.http import JsonResponse
import yt_dlp
from django.shortcuts import render, redirect
from pytube import *
from django.http import JsonResponse, HttpResponse
from pytube import YouTube
import logging



def index(request):
    return render(request, 'youtube.html')

# defining function


# Set up logging
logger = logging.getLogger(__name__)


def youtube(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        if not link:
            return JsonResponse({'error': 'No link provided'}, status=400)

        try:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': 'downloads/%(title)s.%(ext)s',
                'noplaylist': True,  # Download only the single video
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=True)
                title = info_dict.get('title', 'Video')
            return JsonResponse({'message': f'Download completed successfully for {title}'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'youtube.html')
