import ffmpeg
import sys

sys.path.append(r'bin') # your ffmpeg file path
stream = ffmpeg.input('sea-video.mp4')

stream = ffmpeg.output(stream, 'output.mp3')
