import crawl
import threading

DOMAIN="https://gall.dcinside.com"
BASE_URL=DOMAIN +"/board/lists/"
headers={'User-Agent':'Chrome/'}

def crawl_gallery(gallery_id):
    try:
        crawl.gallery_crawl(DOMAIN, BASE_URL, gallery_id.strip(), headers, 0)
    except Exception as e:
        # 스레드에서 예외 발생 시 예외 처리
        print(f"스레드에서 예외 발생: {e}")
        # 필요한 로깅 또는 기타 작업 수행
        # 스레드를 다시 시작하려면 새로운 스레드를 생성
        threading.Thread(target=crawl_gallery, args=(gallery_id,)).start()

with open("gallery_list.txt", "r") as file:
    for gallery_id in file:
        threading.Thread(target=crawl_gallery, args=(gallery_id,)).start()