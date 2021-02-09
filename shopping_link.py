def get_category(main, sub, i):

    if main == 1: #해외


        if sub == 1: # 패션의류
            link = "https://search.shopping.naver.com/search/all?catId=50000000&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8&sort=review&timestamp=&viewType=list"
        elif sub == 2:
            link = "https://search.shopping.naver.com/search/all?catId=50000004&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8&sort=review&timestamp=&viewType=list"
        elif sub == 3:
            link = "https://search.shopping.naver.com/search/all?catId=50000008&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8&sort=review&timestamp=&viewType=list"
        elif sub == 4:
            link = "https://search.shopping.naver.com/search/all?catId=50000007&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8&sort=review&timestamp=&viewType=list"
        elif sub == 5:
            link = "https://search.shopping.naver.com/search/all?catId=50000006&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8&sort=review&timestamp=&viewType=list"
        elif sub == 6:
            link = "https://search.shopping.naver.com/search/all?catId=50000001&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8&sort=review&timestamp=&viewType=list"
        elif sub == 7:
            link = "https://search.shopping.naver.com/search/all?catId=50000002&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8&sort=review&timestamp=&viewType=list"
        elif sub == 8:
            link = "https://search.shopping.naver.com/search/all?catId=50000003&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8&sort=review&timestamp=&viewType=list"
        elif sub == 9:
            link = "https://search.shopping.naver.com/search/all?catId=50000005&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8&sort=review&timestamp=&viewType=list"
        elif sub == 10:
            link = "https://search.shopping.naver.com/search/all?catId=50000009&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8&sort=review&timestamp=&viewType=list"



        else:
            raise Exception("ERROR: 존재하지 않는 카테고리")




    elif main == 2: #해외직구

        if sub == 1:
           link = "https://search.shopping.naver.com/search/all?catId=50000000&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"
        if sub == 2:
           link = "https://search.shopping.naver.com/search/all?catId=50000004&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"
        if sub == 3:
           link = "https://search.shopping.naver.com/search/all?catId=50000008&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"
        if sub == 4:
           link = "https://search.shopping.naver.com/search/all?catId=50000007&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"

        if sub == 5:
           link = "https://search.shopping.naver.com/search/all?catId=50000006&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"

        if sub == 6:
           link = "https://search.shopping.naver.com/search/all?catId=50000001&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"

        if sub == 7:
           link = "https://search.shopping.naver.com/search/all?catId=50000002&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"
        if sub == 8:
           link = "https://search.shopping.naver.com/search/all?catId=50000003&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"
        if sub == 9:
           link = "https://search.shopping.naver.com/search/all?catId=50000005&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"
        if sub == 10:
           link = "https://search.shopping.naver.com/search/all?catId=50000009&frm=NVSHCAT&origQuery=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%ED%95%B4%EC%99%B8%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"


        else:
            raise Exception("ERROR: 존재하지 않는 카테고리")


    elif main == 3:  # 직구

        if sub == 1:
            link = "https://search.shopping.naver.com/search/all?catId=50000000&frm=NVSHCAT&origQuery=%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"
        if sub == 2:
            link = "https://search.shopping.naver.com/search/all?catId=50000004&frm=NVSHCAT&origQuery=%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"
        if sub == 3:
            link = "https://search.shopping.naver.com/search/all?catId=50000008&frm=NVSHCAT&origQuery=%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"
        if sub == 4:
            link = "https://search.shopping.naver.com/search/all?catId=50000007&frm=NVSHCAT&origQuery=%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"

        if sub == 5:
            link = "https://search.shopping.naver.com/search/all?catId=50000006&frm=NVSHCAT&origQuery=%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"

        if sub == 6:
            link = "https://search.shopping.naver.com/search/all?catId=50000001&frm=NVSHCAT&origQuery=%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"

        if sub == 7:
            link = "https://search.shopping.naver.com/search/all?catId=50000002&frm=NVSHCAT&origQuery=%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"
        if sub == 8:
            link = "https://search.shopping.naver.com/search/all?catId=50000003&frm=NVSHCAT&origQuery=%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"
        if sub == 9:
            link = "https://search.shopping.naver.com/search/all?catId=50000005&frm=NVSHCAT&origQuery=%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"
        if sub == 10:
            link = "https://search.shopping.naver.com/search/all?catId=50000009&frm=NVSHCAT&origQuery=%EC%A7%81%EA%B5%AC&pagingIndex="+str(i)+"&pagingSize=40&productSet=overseas&query=%EC%A7%81%EA%B5%AC&sort=review&timestamp=&viewType=list"

        else:
            raise Exception("ERROR: 존재하지 않는 카테고리")


    return link