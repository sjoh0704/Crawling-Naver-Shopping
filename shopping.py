from selenium import webdriver
import time
from bs4 import BeautifulSoup
from datetime import datetime

MONTH = 50
URL_CNT = 10


def set_today():
    return datetime.today().strftime("%Y.%m.")
today = set_today()
print(set_today())
# date = list(map(int, date.split(".")))
# today = list(map(int, today.split(".")))
# date = list(map(int, date.split(".")[:-1]))
# print(date)
# # print(today)
def compute_date(today, date):
    date = list(map(int, date.split(".")[:-1]))
    today = list(map(int, today.split(".")[:-1]))
    month = (today[0] - date[0]) * 12 + (today[1] - date[1])
    return month
def set_page(url, page_number):
    url = url.split("pagingIndex=")
    url1 = url[0] + "pagingIndex=" + str(page_number)
    url2 = url[1][1:]
    return url1 + url2

category = int(input("카테고리 입력\n(패션의류: 1, 패션잡화: 2, 화장품/미용: 3, 디지털/가전: 4, 가구/인테리어: 5, 출산/육아: 6, 식품: 7, 스포츠/레저: 8, 생활/가전: 9, 여가/생활편의:10 ):"))
MONTH = int(input("몇개월내로 검색하시겠습니까? :"))
URL_CNT = int(input("몇 개의 리스트를 가져오시겠습니까? :"))


driver = webdriver.Chrome(r'C:\Users\SeungJu\Downloads\chromedriver_win32 (1)\chromedriver.exe')

#

SCROLL_PAUSE_SEC = 0.01
# 스크롤 높이 가져옴
url_list = []
title_list = []
date_list = []
selected_URL_list = []
selected_title_list = []


for i in range(1, 100):

    if category == 1: # 패션의류
        link = "https://search.shopping.naver.com/search/all?frm=NVSHOVS&origQuery=%EC%A7%81%EA%B5%AC&pagingIndex=" + str(i) + "&pagingSize=80&productSet=overseas&query=%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"
    elif category == 2: # 패션잡화
        link = "https://search.shopping.naver.com/search/category?agency=true&catId=50000000&frm=NVSHCAT&origQuery&pagingIndex=" + str(i) + "&pagingSize=40&productSet=total&query&sort=review&timestamp=&viewType=list#"
    elif category == 3: # 화장품/미용
        link = "https://search.shopping.naver.com/search/category?agency=true&catId=50000001&frm=NVSHCAT&origQuery&pagingIndex=" + str(i) + "&pagingSize=40&productSet=total&query&sort=review&timestamp=&viewType=list"
    elif category == 4: #디지털가전
        link = "https://search.shopping.naver.com/search/category?agency=true&catId=50000003&frm=NVSHCAT&origQuery&pagingIndex=" + str(i) + "&pagingSize=40&productSet=total&query&sort=review&timestamp=&viewType=list"
    elif category == 5: # 가구/인테리어
        link = "https://search.shopping.naver.com/search/category?agency=true&catId=50000004&frm=NVSHCAT&origQuery&pagingIndex=" + str(i) + "&pagingSize=40&productSet=total&query&sort=review&timestamp=&viewType=list"
    elif category == 6: # 출산/육아
        link = "https://search.shopping.naver.com/search/category?agency=true&catId=50000005&frm=NVSHCAT&origQuery&pagingIndex=" + str(i) + "&pagingSize=40&productSet=total&query&sort=review&timestamp=&viewType=list"
    elif category == 7: # 식품
        link = "https://search.shopping.naver.com/search/category?agency=true&catId=50000006&frm=NVSHCAT&origQuery&pagingIndex=" + str(i) + "&pagingSize=40&productSet=total&query&sort=rel&timestamp=&viewType=list"
    elif category == 8: # 스포츠/레저
        link = "https://search.shopping.naver.com/search/category?agency=true&catId=50000007&frm=NVSHCAT&origQuery&pagingIndex=" + str(i) + "&pagingSize=40&productSet=total&query&sort=review&timestamp=&viewType=list"
    elif category == 9: # 생활/건강
        link = "https://search.shopping.naver.com/search/category?agency=true&catId=50000008&frm=NVSHCAT&origQuery&pagingIndex=" + str(i) + "&pagingSize=40&productSet=total&query&sort=review&timestamp=&viewType=list"
    elif category == 10: # 여가/생활편의
        link = "https://search.shopping.naver.com/search/category?agency=true&catId=50000009&frm=NVSHCAT&origQuery&pagingIndex=" + str(i) + "&pagingSize=40&productSet=total&query&sort=review&timestamp=&viewType=list"
    else:
        print("exception error: 링크 없음 프로그램을 종료합니다. ")
        break
        # print(i, link)
    driver.get(link)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
    # 끝까지 스크롤 다운
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 1초 대기
        time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height



    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")


# 타이틀
    titles = soup.select('ul.list_basis div div div div  a[title] ')
    # print(str(i) + "번째")
    # print(url_items)

    for title in titles:
        text = title.get("title")
        title_list.append(text)


    # url

    url_items = soup.select('ul.list_basis div div div div  a[href]')
    # print(str(i) + "번째")
    # print(url_items)

    tmp = None
    for url in url_items:
        text = url.get("href")


        if "https://cr" in text and text != tmp:
            url_list.append(text)
            tmp = text


    # review
    date_items = soup.select(".list_basis div span.basicList_etc__2uAYO")

    for date in date_items:
        text = date.get_text()
        # print(tmp)
        if "등록일" in text:
            text = text.split(" ")[1]
            date_list.append(text)
            # print("안쪽")
    for i, date in enumerate(date_list):
        if compute_date(today, date) <= MONTH:
            selected_URL_list.append(url_list[i])
            selected_title_list.append(title_list[i])
    if len(selected_URL_list) > URL_CNT:  # 가져오려는 리스트수
        selected_URL_list = list(selected_URL_list[:URL_CNT])
        selected_title_list = list(selected_title_list[:URL_CNT])
        driver.close()
        break






    #
    # driver.close()

# for url in url_list:
#     print(url)


# for title in title_list:
#     print(title)
# print(len(title_list), len(url_list))

# for date in date_list:
#     print(date)
# url 100개
for i in range(URL_CNT):
    print(str(i + 1) + ". " + selected_title_list[i] +"\n URL: ", selected_URL_list[i] + "\n")


print()
print("< 상품 필터링하기 >")
while(True):
    tmp_list1 = []
    tmp_list2 = []
    x = input("빼고 싶은 상품 입력(-1입력시 종료): ")
    y = 0

    if x == "-1":
        print("종료합니다")

        break
    i = 0
    for i in range(len(selected_URL_list)):
        if(x not in selected_title_list[i]):
            tmp_list1.append(selected_title_list[i])
            tmp_list2.append(selected_URL_list[i])




    if y == len(selected_title_list):
        print("상품 없음")
        break
    selected_title_list =tmp_list1
    selected_URL_list =tmp_list2


print()
print("< 필터링된 상품 목록 >")
for i in range(len(selected_URL_list)):
    print(str(i + 1) + ". " + selected_title_list[i] +"\n URL: ", selected_URL_list[i] + "\n")



















