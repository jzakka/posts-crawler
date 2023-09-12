import crawl
import threading

DOMAIN="https://gall.dcinside.com"
BASE_URL=DOMAIN +"/board/lists/"
headers={'User-Agent':'Chrome/'}

with open("gallery_list.txt", "r") as file:
    for gallery_id in file:
        threading.Thread(target=crawl.gallery_crawl, args=(DOMAIN, BASE_URL, gallery_id.strip(), headers, 0)).start()