import yt_dlp
from pytube import Playlist
from pprint import pprint
import time
import random 
def download_audio(link):
  with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': '%(title)s.mp3'}) as video:
    info_dict = video.extract_info(link, download = True)
    video_title = info_dict['title']
    print(video_title)
    video.download(link)    
    print("Successfully Downloaded - see local folder on Google Colab")
def get_playlist_urls(playlist_url):
    playlist = Playlist(playlist_url)
    video_urls = list(playlist.video_urls)
    return video_urls

playlist_url = "aici pui link playlist"

def download_playlist():
  urls = get_playlist_urls(playlist_url)
  print("start=========")
  flag=True
  lastUrl="aici pui ultimul url , last music"
  #decomentezi daca e lung playlistul
#   flag=False
  pprint(urls)
  for url in urls:
    if flag or lastUrl == url
      print(url)
      download_audio(url)
      time.sleep(30 + random.randint(0,10))

download_playlist()
