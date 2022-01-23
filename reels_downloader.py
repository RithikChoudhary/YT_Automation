
from instascrape import Reel
import time

def download(link):
    try:
        if (link):
            SESSIONID = "18614737527%3ApTLwFoXv5BZohu%3A4"
            headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
            "cookie":f'sessionid={SESSIONID};'
            }
            google_reel=Reel(link)
            google_reel.scrape(headers=headers)
            google_reel.download(fp=f"\\reel{int(time.time())}.mp4")
            print("successfully downloaded")
            
    except Exception as e:
        print("Not downloaded successfully")

download("https://www.instagram.com/reel/CY-5my0LtLB/?utm_source=ig_web_copy_link")


