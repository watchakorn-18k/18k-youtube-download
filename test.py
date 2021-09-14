# import asyncio
# import time

# async def wash(basket):
#     print(f'Washing Machine ({basket}): Put the coin')
#     print(f'Washing Machine ({basket}): Start washing...')
#     await asyncio.sleep(5)
#     print(f'Washing Machine ({basket}): Finished washing')
#     return f'{basket} is completed'

# if __name__ == '__main__':
#     t1 = time.time()
#     asyncio.run(wash('Basket A'))
#     t2 = time.time() - t1
#     print(f'Executed in {t2:0.2f} seconds.')


#                 async def main(self):
#                     await download_music(self)
#                     await convert_mp3(self)
#                 asyncio.run(main(self))








# from moviepy.audio.io.AudioFileClip import AudioFileClip

# import os

# s ="https://www.youtube.com/watch?v=iOzFmsM6BMw&ab_channel=MEXOFFICIAL"
# print(s.find("www.youtube.com/watch?v="))

# for filename in os.listdir("cache_MP3"):
#     music_name = str(filename)
# print(music_name)
# clip = AudioFileClip(f'cache_MP3\{music_name}')
# clip.write_audiofile(f'Download MP3\{music_name}')

# clip.close()
# os.remove(f'cache_MP3\{music_name}') 


    # split the file name into 3 parts
    # normal filename looks like this for mp3
    # 'Born Again - Third Day-4m_dP2n-5W8.mp3'

    # split_val = filename.split('-')
    # print(split_val)
    # new_name = f"{split_val[0][0:30]} - {split_val[1][0:4]}.mp3"
    # print(new_name)
    # os.rename(filename, new_name)
 


# video_title = "ข้าวผัดไข่สีทอง ด้วยไข่ 100 ฟอง"
# f = open("demofile2.txt", "w", encoding="utf-8")
# f.write(video_title)
# f.close()

# video_title = open("demofile2.txt", "r",encoding="utf-8")
# video_title =   video_title.read()
# print(video_title)


                # music_infile = f"{video_title} - 18k.mp3"
                # print(music_infile)
                # clip = AudioFileClip(f'Download MP3/{music_infile}')
                # clip.write_audiofile(f'Download MP3s/{music_infile}')
                # clip.close()