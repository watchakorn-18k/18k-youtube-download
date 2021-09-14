from moviepy.editor import *

clip = AudioFileClip('Download MP3\Mattafix - Big City Life (Lyrics) (Best Version) - 18k.mp3')
clip.write_audiofile('testfile.mp3')
clip.close()