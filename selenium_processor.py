from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


data = {'code':[], 'code_name':[], 'issuer':[], 'listing':[], 'IPO_date':[]}
df = pd.read_csv('ISIN_codes.csv')
codes = [f for f in df[' codes']]
print( len(codes))
url = 'http://isin.krx.co.kr/srch/srch.do?method=srchList'
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('./chromedriver', chrome_options=options)
#driver.maximize_window() #화면에 꽉 채우는 옵션

driver.get(url)
#codes = ['KR7246720007','KR7245710009','KR7005930003']
cnt=0
for i in range(len(codes)):
    keyword = codes[i]
    cnt += 1
    data['code'].append(keyword)
    search = driver.find_element_by_id('isur_nm1')
    search.clear()
    search.send_keys(keyword)
    search.send_keys(Keys.ENTER)

    time.sleep(0.2)
    tmp_page_source = driver.page_source
    tmp_soup = BeautifulSoup(tmp_page_source,'html.parser')

    tr_first_last = tmp_soup.find('tr',attrs={'class':'first last'})

    for i, value in enumerate(tr_first_last.find_all('td')):
        if i == 2:
            data['code_name'].append(value.text)
            print("num : ",cnt , ", name : ", value.text)
        elif i ==3:
            data['issuer'].append(value.text)
        elif i ==6:
            data['listing'].append(value.text.strip())
        elif i == 7:
            data['IPO_date'].append(value.text.strip())
    #time.sleep(1)
driver.close()
print(len(data['code']))

data_df = pd.DataFrame(data)
data_df.to_excel('stock_info.xlsx')
#total_count = int(tr_first_last.find('span',attrs={'class':'cnt'}).text)

#body = driver.find_element_by_tag_name('body')



# for n in range(0,20):
#     body.send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.3)
#
# if total_count > 80 :
#     #더보기 버튼 클릭 # . tag
#     more_button = driver.find_element_by_css_selector('.search_deallist button')
#     more_button.send_keys(Keys.ENTER)
#     time.sleep(2)
#
#     for n in range(0,10):
#         body.send_keys(Keys.PAGE_DOWN)
#         time.sleep(0.3)
#
# page_source = driver.page_source
# driver.close()
#
# soup = BeautifulSoup(page_source,'html.parser')
# div = soup.find('div',attrs={'class':'infinite-scroll-component'})
# for item in div.find_all('li',attrs={'class':'item'}):
#     if item.find('span',attrs={'class':'soldout'}) == None :
#         name = item.find('p',attrs={'class':'title'}).find('strong').text
#         price = item.find('span',attrs={'class':'sale'}).find('i').text.replace(',','')
#         thumb = item.find('div',attrs={'class':'thumb'}).get('style')
#         code = item.find('a',attrs={'class':'anchor'}).get('href')
#         org_price = item.find('span',attrs={'class':'original'})
#         if org_price == None :
#             org_price = -1
#         else :
#             org_price = org_price.find('i').text.replace(',','')
#
#         discount = item.find('strong',attrs={'class':'num'})
#         if discount == None :
#             discount = -1
#         elif discount.text == '균일가' :
#             discount = 0
#         else :
#             discount = discount.text
#
#         print(name,price,org_price,discount)
#         print(thumb.replace('background-image: url("','').replace('");',''))
#         #http://www.ticketmonster.co.kr/deal/1031189834?keyword=xxxx
#         print(code.split('?')[0].split('/')[-1])
#
#         q = 'INSERT INTO timon_crawling_product(code, name, thumbnail, org_price, discount, sale_price, crawling_date)'
#         q += 'VALUES (%s, %s, %s, %s, %s, %s, now())'
#         d = []
#         d.append(code.split('?')[0].split('/')[-1])
#         d.append(name)
#         d.append(thumb.replace('background-image: url("','').replace('");',''))
#         d.append(org_price)
#         d.append(discount)
#         d.append(price)
#         cur.execute(q,d)
#
#
#
#
#
