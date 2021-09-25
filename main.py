from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.set('kivy','window_icon','logo.png')
Config.set('input', 'mouse', 'mouse,disable_multitouch')
from logging import shutdown
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.base import EventLoop
from kivy.properties import StringProperty,BooleanProperty,NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.progressbar import ProgressBar
import youtube_dl
import os
from youtubesearchpython import VideosSearch
from moviepy.audio.io.AudioFileClip import AudioFileClip
import re
import asyncio
import time
from threading import Thread


def search_youtube(self,input_search):
    videosSearch = VideosSearch(input_search, limit = 1)
    dict_data = videosSearch.result()
    def load_thumbnail_url():
        for i in dict_data["result"]:
            img = next(iter(i["thumbnails"]))["url"]
            return img
    def load_title_youtube():
        for i in dict_data["result"]:
            title = i["title"][0:30]
            return title
    def load_duration_youtube():
        for i in dict_data["result"]:
            duration = f'ความยาว {i["duration"]}'
            return duration
    def load_link_youtube():
        for i in dict_data["result"]:
            link_data = i["link"]
            return link_data
    if dict_data['result'] != []:
        self.ids.title_youtube.text = "  " + load_title_youtube()
        self.ids.image_youtube.source = load_thumbnail_url()
        self.ids.duration_youtube.text = load_duration_youtube()
        self.ids.copy_link.value = load_link_youtube()
    else:
        self.ids.label_youtube.text = "ไม่พบข้อมูล"


def listToString(s):
    str1 = " "
    for ele in s: 
        str1 += ele
    return str1

def create_dir_download():
    if os.path.isdir("Download MP3"):
        PATH = '/Download MP3/'
    elif os.path.isdir("Download MP3") != True:
        os.mkdir("Download MP3")
        PATH = '/Download MP3/'
    return PATH

def create_dir_cache_music():
    if os.path.isdir("cache_MP3"):
        PATH_CACHE = '/cache_MP3/'
    elif os.path.isdir("cache_MP3") != True:
        os.mkdir("cache_MP3")
        PATH_CACHE = '/cache_MP3/'
    return PATH_CACHE

def start_youtube_download(self):
    if self.ids.my_text_input.text == '18K':
        self.ids.title_youtube.text = "  " + "18K"
        self.ids.image_youtube.source = "logo_title.png"
        self.ids.duration_youtube.text = "Radio"
    elif self.ids.my_text_input.text.find("www.youtube.com/watch?v=") == self.ids.my_text_input.text.find("youtu.be/"):
        search_youtube(self,self.ids.my_text_input.text)
    elif self.ids.my_text_input.text.find("www.youtube.com/watch?v=") or self.ids.my_text_input.text.find("youtu.be/") >= 0:
        print(self.ids.my_text_input.text.find("www.youtube.com/watch?v="))
        print(self.ids.my_text_input.text.find("youtu.be/"))
        create_dir_download()
        self.ids.my_progress_bar.value = 10
        self.ids.my_button_1.disabled = True
        async def main(self):
            await download_music(self)
            await convert_mp3(self)
        asyncio.run(main(self))


async def download_music(self):
    try:
        PATH_CACHE = create_dir_cache_music()
        link = self.ids.my_text_input.text
        ydl_opts = {
            'format':'worstaudio',
            'extractaudio':True,
            'audioformat':'mp3',
            'outtmpl': PATH_CACHE +u'%(title)s - 18K.mp3',    #name the file the ID of the video
            'noplaylist':True,
            'keepvideo': True,
            'nocheckcertificate':True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '128',
            },
                {
            'key': 'FFmpegMetadata'
                }
            ],
        }
        self.ids.my_progress_bar.value = 20
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(link, download=False) 
            info_dict = ydl.extract_info(link, download=False)
            video_title = info_dict.get('title', None)
            video_duration = info_dict.get('duration', None)/60
            self.ids.my_progress_bar.value = 30
            self.process_download = "กำลังโหลด..."
            video_title[0:30]
            self.ids.my_progress_bar.value = 50
            ydl.download([link])
            #self.my_text = f"{listToString(re.split(' ',video_title[0:30]))}..... - {int(video_duration)} นาที"
    except :
        pass

async def convert_mp3(self):
    try:
        for filename in os.listdir("cache_MP3"):
            music_name = str(filename)
        clip = AudioFileClip(f'cache_MP3\{music_name}')
        self.process_download = "กำลังแปลงไฟล์..."
        self.ids.my_progress_bar.value = 80
        clip.write_audiofile(f'Download MP3\{music_name}')
        self.process_download = "ดาวน์โหลดเสร็จแล้ว"
        self.my_text = f"{music_name[0:30]} - 18k"
        self.ids.my_progress_bar.value = 90
        clip.close()
        os.remove(f'cache_MP3\{music_name}')
        self.ids.my_progress_bar.value = 100
        self.ids.my_label_top.text = "คลิกที่โลโก้ 18K เพื่อเปิดโฟลเดอร์เพลง"
    except :
        pass



class gridlayout_Screen(GridLayout):
    check_input = BooleanProperty(False)
    my_text = StringProperty("")
    success_download = StringProperty("")
    process_download = StringProperty("")
    count = 0
    process_download_value = NumericProperty(0)
    
    def on_button_click(self):
        start_youtube_download(self)
    
    def on_open_dir_mp3(self):
        create_dir_download()
        path = "Download MP3"
        path = os.path.realpath(path)
        os.startfile(path)
    def animate_it(self):
        animate = Animation(opacity=0,duration=0.1)
        animate += Animation(opacity=1,)
        animate.start(self.ids.btn_1)





class RightClickTextInput(TextInput):   

    def on_touch_down(self, touch):

        super(RightClickTextInput,self).on_touch_down(touch)

        if touch.button == 'right':
            print("right mouse clicked")
            pos = touch.pos

            self._show_cut_copy_paste(
                pos, EventLoop.window, mode='paste')
class YoutubeDownloadApp(App):
    def build(self):
        self.title = 'ดาวน์โหลดเพลงจากยูทูป'
        self.title_color = 1,0,0,1
    
YoutubeDownloadApp().run()
        

