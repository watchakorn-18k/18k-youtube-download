import json
from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('ชีวิตเธอดีอยู่แล้ว', limit = 1)
dict_data = videosSearch.result()
json_data = json.dumps(videosSearch.result())

for i in dict_data["result"]:
    print(i["link"])
