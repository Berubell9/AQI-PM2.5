import requests #เรียกใช้ข้อมูล
url="http://air4thai.pcd.go.th/services/getNewAQI_JSON.php"
response = requests.get(url) #ตัวเเปรดึงข้อมูลจากเว็บ
data = response.json()

import folium #เรียกใช้เเผนที่
map = folium.Map(location = [13.736,100.523],zoom_start = 8) #ตั้งหน้าเริ่มไปที่กรุงเทพ

for item in data["stations"]: #เข้าถึง stations ที่เป็นวงเล็บใหญ่
    x = item['lat'] #ดึงละติจูด
    y = item['long'] #ดึงลองติจูด
    level = item['LastUpdate']['AQI']['Level']
    aqi = int(item['LastUpdate']['AQI']['aqi'])
    pm = item['LastUpdate']['PM25']['value']

    color=''
    if(aqi>=0 and aqi<=25):
        color='lightblue'
    elif(aqi>=26 and aqi<=50):
        color='green'
    elif(aqi>=51 and aqi<=100):
        color='orange'
    elif(aqi>=101 and aqi<=200):
        color='red'
    else:
        color='purple'

    folium.Marker([x,y],
    tooltip = item['nameTH'], #ชื่อสถานที่
    popup = folium.Popup("<h5>ค่าดัชนีคุณภาพอากาศ (AQI) : "+str(aqi)+"</h5>\n<h5>ค่าPM2.5 : "+pm+" µg/m³</h5>\n<b>ระดับความรุนเเรง : "+level+"</b>",
    max_width=500), #ค่าที่ได้
    icon = folium.Icon(color = color)
    ).add_to(map)

map.save("index.html")