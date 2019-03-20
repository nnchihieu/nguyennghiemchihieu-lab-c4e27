from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode('utf-8')
# with open('milk.html','wb') as f:
#     f.write(raw_data)
soup = BeautifulSoup(html_content,'html.parser')
div = soup.find('div', style = 'overflow:hidden;width:100%;border-bottom:solid 1px #cecece;')
ls_tr = div.table.find_all('tr')
bang_doanh_thu = []
for tr in ls_tr:
    ls_td = tr.find_all('td')
    list = {}
    for i in range(len(ls_td)):
        thong_ke = ls_td[i].string
        if i == 0:
            list['danh mục'] = thong_ke
        elif i == 1:
            list['Quý 4-2016'] = thong_ke
        elif i == 2:
            list['Quý 1-2017'] = thong_ke
        elif i == 3:
            list['Quý 2-2017'] = thong_ke
        elif i == 4:
            list['Quý 3-2017'] = thong_ke
    if list != {}:
        bang_doanh_thu.append(OrderedDict(list))

pyexcel.save_as(records=bang_doanh_thu, dest_file_name='milk.xlsx')

