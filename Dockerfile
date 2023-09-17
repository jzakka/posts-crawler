# 사용할 베이스 이미지를 선택합니다.
FROM python:3.8

# 작업 디렉터리를 설정합니다.
WORKDIR /app

# 필요한 라이브러리를 설치합니다.
RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install confluent-kafka

# 소스 코드 및 crawl 모듈을 복사합니다.
COPY . /app

EXPOSE 9092

# 파이썬 스크립트를 실행합니다.
CMD ["python", "crawler.py", "product"]