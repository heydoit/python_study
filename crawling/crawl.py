# title : 경제뉴스 크롤링
# creater : kimyujin
# dev date : 2022/11/22
# Update date : 2022/12/08
# updater : kimyujin
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from bs4 import BeautifulSoup

#웹드라이버 설정
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwiches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension",False)

def makePgnum(num):
    if num == 1:
        return num
    elif num == 0 :
        return num+1
    else:
        return num + 9*(num-1)

def makeUrl(search, start_pg, end_pg):
    if start_pg == end_pg:
        start_page = makePgnum(start_pg)
        url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101" +search + "&start=" + str(start_page)
        print("생성url: ", url)
        return url
    else:
        urls = []
        for i in range(start_pg, end_pg+1):
            page = makePgnum(i)
            url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101" + search + "&start" + str(page)
            urls.append(url)
        print("생성url: ",urls)
        return urls
# driver = webdriver.Chrome('C:/study_alone/chromedriver')
# url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'
# driver.get(url)
# time.sleep(1)