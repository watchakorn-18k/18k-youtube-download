from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.set('kivy','window_icon','Assets/logo.png')
Config.set('input', 'mouse', 'mouse,disable_multitouch')

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
from pytube import YouTube
import os
from youtubesearchpython import VideosSearch
import asyncio
import shutil
import sys
from threading import Thread



def split_text(text):
    import re
    string_to_split = text
    res = re.split('[^a-zA-Zก-ฮ0-9.ะาิืี๊่้ึ ุูแโเะั ำไใฤฤาฦฦา่้๊๋ๆ-]', string_to_split)
    res = ''.join(res)
    res = re.split('\s+', res)
    res = ''.join(res)
    res = re.split('.mp4', res)
    res = ''.join(res)
    return res


def search_youtube(self,input_search):
    def check_data():
        if dict_data['result'] != []:
            self.ids.notice_text.text = ""
            self.ids.title_youtube.text = " " + load_title_youtube()
            self.ids.image_youtube.source = load_thumbnail_url()
            self.ids.duration_youtube.text = load_duration_youtube()
            self.ids.copy_link.value = load_link_youtube()
            self.ids.copy_link.opacity = 1
            self.ids.title_youtube.opacity = 1
            self.ids.image_youtube.opacity = 1
            self.ids.duration_youtube.opacity = 1
        else:
            self.ids.label_youtube.text = "ไม่พบข้อมูล"
            self.ids.copy_link.opacity = 0
            self.ids.title_youtube.opacity = 0
            self.ids.image_youtube.opacity = 0
            self.ids.duration_youtube.opacity = 0
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
    check_data()


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

def check_youtube_music(text):
    t1 = text.split("https://music.youtube.com/")[1]
    text_res = "https://youtube.com/"+t1
    return text_res

def start_youtube_download(self):
    if self.ids.my_text_input.text.find("https://music.youtube.com/") == 0:
        self.ids.my_text_input.text = check_youtube_music(self.ids.my_text_input.text)
        create_dir_download()
        async def main(self):
            await download_music(self)
            await convert_mp3(self)
        asyncio.run(main(self))

    elif self.ids.my_text_input.text.find("www.youtube.com/watch?v=") == self.ids.my_text_input.text.find("youtu.be/"):
        search_youtube(self,self.ids.my_text_input.text)
    elif self.ids.my_text_input.text.find("www.youtube.com/watch?v=") or self.ids.my_text_input.text.find("youtu.be/") >= 0:
        # print(self.ids.my_text_input.text.find("www.youtube.com/watch?v="))
        # print(self.ids.my_text_input.text.find("youtu.be/"))
        create_dir_download()
        async def main(self):
            await download_music(self)
            await convert_mp3(self)
        asyncio.run(main(self))

previousprogress = 0
def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 
    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previousprogress:
        previousprogress = liveprogress
        progress_update.value = liveprogress
        # print(liveprogress)
async def download_music(self):
    try:
        self.ids.my_button_1.disabled = True
        PATH_CACHE = create_dir_cache_music()
        link = self.ids.my_text_input.text
        self.ids.copy_link.opacity = 0
        self.ids.title_youtube.opacity = 0
        self.ids.image_youtube.opacity = 0
        self.ids.duration_youtube.opacity = 0
        yt = YouTube(link)
        yt.register_on_progress_callback(on_progress)
        global progress_update
        progress_update = self.ids.progress_bar_status
        yt.streams.filter(progressive=True,abr='128kbps').first()
        test = yt.streams.get_by_itag(140)
        test.download('cache_MP3')
    except:
        self.ids.notice_text.text = "ดาวน์โหลดไม่สำเร็จพบข้อผิดพลาด"
        sys.exit()

async def convert_mp3(self):
    try:
        dir = "cache_MP3"
        for count, filename in enumerate(os.listdir(dir)):
            dst = os.path.join(dir, f"{split_text(filename)}")
            src = os.path.join(dir, filename)
            os.rename(src, dst)
        for filename in os.listdir("cache_MP3"):
            music_name = str(filename)
            # print(music_name)
        import subprocess
        cmd= f'ffmpeg -i "cache_MP3\{music_name}" -y "Download MP3\{music_name} - 18k.mp3"'
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True,encoding="utf8")
        for line in process.stdout:
            data = line.strip("")
            self.ids.notice_text.text = "กำลังแปลงไฟล์"
            self.ids.test.text = "อย่าปิดโปรแกรมจนกว่าจะเสร็จ"
            self.process_download = data[2:38]
        self.ids.progress_bar_status.value = 100
        self.my_text = f"{music_name[0:30]} - 18k"
        self.process_download = "ดาวน์โหลดเสร็จเรียบร้อย"
        shutil.rmtree('cache_MP3')
        self.ids.notice_text.text = "เปิดโฟลเดอร์เพลงตรง Logo 18K "
        self.ids.notice_text.font_size = 25
    except:
        self.ids.notice_text.text = "แปลงไฟล์ไม่สำเร็จพบข้อผิดพลาด"
        sys.exit()
        


class gridlayout_Screen(GridLayout):
    check_input = BooleanProperty(False)
    my_text = StringProperty("")
    success_download = StringProperty("")
    process_download = StringProperty("")
    count = 0
    process_download_value = NumericProperty(0)
    def on_button_click(self):
        self.ids.label_youtube.text = ' '
        self.ids.notice_text.text = 'รอสักครู่...'
        self.ids.progress_bar_status.value = 0
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
            # print("right mouse clicked")
            pos = touch.pos
            self._show_cut_copy_paste(
                pos, EventLoop.window, mode='paste')
                
class YoutubeDownloadApp(App):
    def build(self):
        self.title = 'ดาวน์โหลดเพลงจากยูทูป'
        self.title_color = 1,0,0,1
    
YoutubeDownloadApp().run()


