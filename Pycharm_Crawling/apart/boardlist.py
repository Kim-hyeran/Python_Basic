import requests
from bs4 import BeautifulSoup

cnt=0

#한 페이지의 게시글 제목, 내용, 작성자, 날짜 수집 코드
list_url='http://news.sarangbang.com/bbs.html?tab=story&p=2'

resp=requests.get(list_url)

if resp.status_code!=200:
    print('WARNING : 잘못된 URL 접근입니다')

soup=BeautifulSoup(resp.text, 'html.parser')

board_list=soup.select('tbody#bbsResult > tr > td > a')

for i, href in enumerate(board_list):
    #print(i, href)
    if(i%2==0):
        cnt+=1
        #한 건의 게시글 제목, 내용, 작성자, 날짜 수집 코드
        url='http://news.sarangbang.com'+href['href']

        resp=requests.get(url)

        if resp.status_code!=200:
            print('WARNING : 잘못된 URL 접근입니다')

        soup=BeautifulSoup(resp.text, 'html.parser')

        title=soup.select('h3.tit_view')[0].text.strip()
        contents=soup.select('div.bbs_view p')
        reg_dt=soup.select('span.tit_cat')[1].text.strip()[:10] #페이지 구조가 같을 경우에만 사용 가능
        writer=soup.select('a.name_more')[0].text.strip()

        print('TITLE : ', title)
        print('WRITHER : ', writer)
        print('DATE : ', reg_dt)

        text=''
        for i in contents:
            text+=i.text.strip()
        print('CONTENTS : ', text)
        print()

print('사랑방 부동산에서 {}개의 데이터가 수집되었습니다'.format(cnt))