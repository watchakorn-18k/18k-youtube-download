import os,winshell,sys

desktop = winshell.desktop()
files = os.listdir(desktop)
print()
# exit()
for f in files:
    if f != "18k-youtube-download.lnk":
        print(f)
        winshell.CreateShortcut(
  Path=os.path.join(desktop(), "18k-youtube-download.lnk"),
  Target=f"{os.getcwd()}\python.exe",
  Icon=(r"c:\python\python.exe", 0),
  Description="Python Interpreter"
)
# from pytube import YouTube


# previousprogress = 0
# def on_progress(stream, chunk, bytes_remaining):
#     global previousprogress
#     total_size = stream.filesize
#     bytes_downloaded = total_size - bytes_remaining 

#     liveprogress = (int)(bytes_downloaded / total_size * 100)
#     if liveprogress > previousprogress:
#         previousprogress = liveprogress
#         print(liveprogress)

# yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
# yt.register_on_progress_callback(on_progress)
# yt.streams.filter(progressive=True, file_extension='mp3')
# print(yt.streams.get_by_itag(140))

# import ffmpeg


# video = ffmpeg.input("Downloads\YouTube Rewind 2019 For the Record  YouTubeRewind.mp4")
# audio = video.audio
# stream = ffmpeg.output(audio, "Successful/test.mp3")
# ffmpeg.run(stream)

# import subprocess

# cmd="ffmpeg -i YouTubeRewind2019FortheRecordYouTubeRewind.mp4 -y test.mp3"
# process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
# for line in process.stdout:
#     data = line[8:15].strip("pmov, , abcdefghijlnoqrstuvwxyzACDEFGHIJLNOQRSTUVWXYZmp : ,-_#-][ , mp")
#     print(data)


# import yt_dlp
# import os
# link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# try:
#     ydl_opts = {
#         'format':'worstaudio',
#         'extractaudio':True,
#         'audioformat':'mp3',
#         'outtmpl': u'%(title)s - 18K.mp3',    #name the file the ID of the video
#         'noplaylist':True,
#         'keepvideo': True,
#         'nocheckcertificate':True,
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '128',
#         },
#             {
#         'key': 'FFmpegMetadata'
#             }
#         ],
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         meta = ydl.extract_info(link, download=False) 
#         info_dict = ydl.extract_info(link, download=False)
#         video_title = info_dict.get('title', None)
#         video_duration = info_dict.get('duration', None)/60
#         video_title[0:30]
#         ydl.download([link])
        
# except :
#     pass