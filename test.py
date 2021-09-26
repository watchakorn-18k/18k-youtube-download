# import re
# string_to_split = "[ re - ]  ／『もう一度』  18K.mp3"

# res = re.split('[^a-zA-Zก-ฮ0-9.ะาิืี๊่้ึ ุูแโเะั ำไใฤฤาฦฦา่้๊๋ๆ-]', string_to_split)
# res = ''.join(res)
# res = re.split('\s+', res)
# res = ''.join(res)
# print(res)
# word = []
# for i in res:
#     if i != '':
#         word.append(i)
#     elif i == '':
#         i = '_'
#         word.append(i)
        
# word = ' '.join(word)
# print(word)
def split_text(text):
    import re
    string_to_split = text
    res = re.split('[^a-zA-Zก-ฮ0-9.ะาิืี๊่้ึ ุูแโเะั ำไใฤฤาฦฦา่้๊๋ๆ-]', string_to_split)
    res = ''.join(res)
    res = re.split('\s+', res)
    res = ''.join(res)
    return res
import os
dir = "cache_MP3"
for count, filename in enumerate(os.listdir(dir)):
    dst = os.path.join(dir, f"{split_text(filename)}")
    src = os.path.join(dir, filename)
    os.rename(src, dst)
