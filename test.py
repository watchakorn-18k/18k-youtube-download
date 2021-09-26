text = "https://music.youtube.com/watch?v=f02mOEt11OQ&list=RDAMVMf02mOEt11OQ"

if text.find("https://music.youtube.com/") == 0:
    t1 = text.split("https://music.youtube.com/")[1]
    text_res = "https://youtube.com/"+t1

