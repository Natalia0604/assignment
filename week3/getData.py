import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(src) as response:
    data=json.load(response) #利用json 模組處理 json 資料格式

#取得景點名稱，經度，緯度，第一張圖檔網址
spotList=data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file: #將資料寫入data.txt
    for spot in spotList:
        picSplit=spot["file"].split("http://") #將照片的網址分開
        file.write(spot["stitle"]+ "," + spot["longitude"] + "," + spot["latitude"] + "," + "http://"+picSplit[1]+"\n")


