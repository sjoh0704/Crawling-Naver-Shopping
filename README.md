# Crawling-Naver-Shopping

네이버 쇼핑몰에서 원하는 카테고리 선택후, 원하는 조건의 상품 리스트를 크롤링하여 엑셀파일로 저장합니다.  
####
리뷰가 많은 순, 최근 올라온 상품을 기준으로 크롤링합니다. 




</br>

# How to use

### 1. 크롬 드라이버 설치 
- C:\chromedriver_win32\chromedriver 경로가 만족되어야 합니다.  
- chrome driver는 브라우저로 사용중인 chrome version과 같은 버전을 설치합니다.   
- 디렉토리명은 chromedriver_win32, chromedriver명은 chromedriver와 같아야 합니다. 

</br>

### 2. 어플리케이션 동작
- 크롤링하고 싶은 카테고리와 필요사항을 적어준 후 크롤링합니다. 
- 크롤링이 끝나면 크롬 브라우저가 알아서 닫힙니다. 
![image](https://user-images.githubusercontent.com/66519046/116504536-73e77500-a8f3-11eb-916a-e91ae656aa60.png)

</br>


### 3. Excel 파일 확인

- 크롤링이 끝나면 상품리스트를 모아둔 엑셀파일의 경로가 나타납니다.

![image](https://user-images.githubusercontent.com/66519046/116503782-ddff1a80-a8f1-11eb-930e-37603ed56c9a.png)

</br>


# Libraries
- tkinter
- openyxl
- bs4
- selenium


