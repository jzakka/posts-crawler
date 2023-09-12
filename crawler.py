import crawl
import threading

DOMAIN="https://gall.dcinside.com"
BASE_URL=DOMAIN +"/board/lists/"
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

with open("gallery_list.txt", "r") as file:
    for gallery_id in file:
        threading.Thread(target=crawl.gallery_crawl, args=(DOMAIN, BASE_URL, gallery_id.strip(), headers, 0)).start()