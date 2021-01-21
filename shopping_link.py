def get_category(category, i):
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
        return
    return link