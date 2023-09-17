import requests
import time
# from urllib.request import urlopen
from bs4 import BeautifulSoup
from confluent_kafka import Producer

def gallery_crawl(domain, base_url, gallery_id, headers, recent_read, isProduct):
    server = 'kafka.lwu.me:9093'  if isProduct else 'localhost:9092'

    # print(server)

    producer = Producer({
        'bootstrap.servers':  server,  
        'client.id': gallery_id  
    })

    topic = 'posts'

    params={'id':gallery_id}
    while(1):
        resp = requests.get(base_url, params=params, headers=headers)
        bsObject = BeautifulSoup(resp.content, "html.parser")

        gallery_name_wrapper = bsObject.find('div', attrs={'class': 'fl clear'})
        gallery_name = gallery_name_wrapper.find('a').text

        for post in reversed(bsObject.find_all(attrs={'class':'ub-content us-post'})):
            try:
                post_num = int(post.find('td', class_='gall_num').text)
                if(recent_read >= post_num):
                    continue
                recent_read = post_num
                post_title = post.find('td', class_='gall_tit ub-word').find('a').text
                post_title = post.find('td', class_='gall_tit ub-word').find('a').text
                post_link = domain + post.find('td', class_='gall_tit ub-word').find('a').get('href')
                post_writer = post.find('td', class_='gall_writer ub-writer').text.strip()
                message = "{'id':%d, 'title':'%s', 'writer':'%s' 'link':'%s'}" %(post_num, post_title, post_writer, post_link)

                # print(gallery_name+ '=' +message)
                producer.produce(topic, key=gallery_name, value=message)
            except Exception as e:
                pass

        time.sleep(2)

__all__ = ['gallery_crawl']