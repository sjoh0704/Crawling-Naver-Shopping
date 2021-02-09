from selenium import webdriver
import time
from bs4 import BeautifulSoup
from datetime import datetime
import shopping_link
from item import Item
from MakeExcel import make_file

MONTH = 50
URL_CNT = 10

def set_today():
    return datetime.today().strftime("%Y.%m.")
today = set_today()
print(set_today())

def compute_date(today, date):
    date = list(map(int, date.split(".")[:-1]))
    today = list(map(int, today.split(".")[:-1]))
    month = (today[0] - date[0]) * 12 + (today[1] - date[1])
    return month

# def set_page(url, page_number):
#     url = url.split("pagingIndex=")
#     url1 = url[0] + "pagingIndex=" + str(page_number)
#     url2 = url[1][1:]
#     return url1 + url2

main_category = int(input("해외: 1\t해외직구: 2\t직구: 3\n"))
sub_category = int(input("패션의류: 1, 가구/인테리어: 2, 생활/건강: 3, 스포츠/레저: 4, 식품: 5, 패션잡화: 6, 화장품/미용: 7, 디지털/가전: 8, 출산/육아: 9, 여가/생활편의:10\n"))
MONTH = int(input("몇 개월내로 검색하시겠습니까? :"))
URL_CNT = int(input("몇 개의 리스트를 가져오시겠습니까? :"))
driver = webdriver.Chrome(r'C:\Users\SeungJu\Downloads\chromedriver_win32 (3)\chromedriver.exe')



SCROLL_PAUSE_SEC = 0.01
# 스크롤 높이 가져옴
url_list = []
title_list = []
date_list = []
selected_URL_list = []
selected_title_list = []
selected_item = []

for i in range(1, 100):

    try:
        link = shopping_link.get_category(main_category, sub_category, i)

        driver.get(link)
    except Exception as e:
        print(e)
        break


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
    titles = soup.select('ul.list_basis div div div div div a[title]')

    for title in titles:
        text = title.get("title")
        title_list.append(text)
        # print(text)


    # url

    url_items = soup.select('ul.list_basis div div div div div a[href]')
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
            tmp = Item(title_list[i], url_list[i])
            selected_item.append(tmp)

    if len(selected_item) > URL_CNT:  # 가져오려는 리스트수
        driver.close()
        selected_item = selected_item[:URL_CNT]
        break
for i in range(URL_CNT):
    print(str(i + 1) + ". " + selected_item[i].title +"\n URL: ", selected_item[i].url + "\n")





print()

make_file(selected_item)


print("< 상품 필터링하기 >")
while(True):
    tmp_list = []
    x = input("빼고 싶은 상품 입력(-1입력시 종료): ")
    y = 0

    if x == "-1":
        print("종료합니다")

        break

    i = 0
    for i in range(len(selected_item)):
        if(x not in selected_item[i].title):
            tmp_list.append(selected_item[i])





    if y == len(selected_item):
        print("상품 없음")
        break
    selected_item = tmp_list


print()
print("< 필터링된 상품 목록 >")
for i in range(len(selected_item)):
    print(str(i + 1) + ". " + selected_item[i].title +"\n URL: ", selected_item[i].url + "\n")


















