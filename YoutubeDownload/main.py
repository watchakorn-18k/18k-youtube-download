from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
# i need GridLayout
from kivy.properties import StringProperty,BooleanProperty
from kivy.uix.gridlayout import GridLayout
import webbrowser
from kivy.uix.widget import Widget
import youtube_dl
import os
from kivy.core.window import Window


class gridlayout_Screen(GridLayout):
    success_text = StringProperty("")
    my_text = StringProperty("")
    line_yt_text = StringProperty("")
    check_offline_text = BooleanProperty(True)
    def on_button_click(self):
        if os.path.isdir("Download MP3"):
            PATH = '/Download MP3/'
        elif os.path.isdir("Download MP3") != True:
            os.mkdir("Download MP3")
            PATH = '/Download MP3/'


        try:
            link = self.ids.my_text_input.text
            ydl_opts = {
                'format':'worstaudio',
                'extractaudio':True,
                'audioformat':'mp3',
                'outtmpl': PATH +u'%(title)s - %(artist)s.mp3',    #name the file the ID of the video
                'noplaylist':True,
                'nocheckcertificate':True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '128',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                meta = ydl.extract_info(link, download=False) 
                info_dict = ydl.extract_info(link, download=False)
                video_title = info_dict.get('title', None)
                video_duration = info_dict.get('duration', None)/60
                print(video_title)
                self.my_text = f"{video_title} - {int(video_duration)} นาที ดาวน์โหลดสำเร็จสมบูรณ์ "
                if self.my_text != "":
                    ydl.download([link])
                    self.success_text = StringProperty("Success")

                
                
        except:
            print("Error")
        
    
    


class YoutubeDownloadApp(App):
    def build(self):
        self.title = 'ดาวน์โหลดเพลงจากยูทูป'
        self.icon = 'logo.png'
        self.title_color = 1,0,0,1
        Window.size = (500, 600)
        

       

        

YoutubeDownloadApp().run()
        

