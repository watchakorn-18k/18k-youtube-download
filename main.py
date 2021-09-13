from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
# i need GridLayout
from kivy.properties import StringProperty,BooleanProperty,NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.progressbar import ProgressBar
import youtube_dl
import os
from kivy.core.window import Window
from kivy.animation import Animation
import time




class gridlayout_Screen(GridLayout):
    check_input = BooleanProperty(False)
    my_text = StringProperty("")
    success_download = StringProperty("")
    process_download = StringProperty("")
    count = 0
    process_download_value = NumericProperty(0)
    def on_button_click(self):
        self.ids.my_button_1.disabled = True
        print(self.ids.my_button_1.disabled)
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
                'outtmpl': PATH +u'%(title)s - 18k.mp3',    #name the file the ID of the video
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
                self.my_text = f"{video_title}"
                import re
                def listToString(s):
                    str1 = " "
                    for ele in s: 
                        str1 += ele
                    return str1
                self.my_text = f"{listToString(re.split(' ',self.my_text[0:30]))}..... - {int(video_duration)} นาที"

                if self.my_text != "":
                    ydl.download([link])
                
                    
        except :
            print("-----------")
            print(self.ids.my_text_input.text.find("youtube.com"))
            if self.ids.my_text_input.text.find("youtube.com") == -1 :
                self.process_download = " "
            elif self.ids.my_text_input.text.find("youtube.com") >= 0 :
                self.process_download = "ดาวน์โหลดเสร็จแล้ว"

    def on_open_dir_mp3(self):
        import os
        path = "Download MP3"
        path = os.path.realpath(path)
        os.startfile(path)
    def animate_it(self):
        
        animate = Animation(opacity=0,duration=0.1)
        animate += Animation(opacity=1,)
        animate.start(self.ids.btn_1)


        
    
    


class YoutubeDownloadApp(App):
    def build(self):
        self.title = 'ดาวน์โหลดเพลงจากยูทูป'
        self.icon = 'logo.png'
        self.title_color = 1,0,0,1
        Window.size = (400, 600)




        

       

        

YoutubeDownloadApp().run()
        

