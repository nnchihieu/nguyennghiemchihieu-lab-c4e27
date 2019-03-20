import requests
from bs4 import BeautifulSoup

url = 'https://dantri.com.vn/suc-khoe.htm'

# Lấy html từ trang cần lấy:
response = requests.get(url)

# Tạo đối tượng soup từ html vừa lấy được:
soup = BeautifulSoup(response.content, 'html.parser')

# Lấy tất cả các thẻ chứa các bài viết. Sử dụng thuộc tính chung là data-boxtype:
post_elments = soup.find_all("div", {"data-boxtype": 'timelineposition'})

# In thử ra màn hình:
for v in post_elments:
    print(v.a.attrs['title'])
    print(v.a.img.attrs['src'])

# Đưa kết quả vào 1 mảng Dict:
result = []
for v in post_elments:
    result.append({'title': v.a.attrs['title'], 'src': v.a.img.attrs['src'], 'description': v.div.div.text.strip()})

# Lưu dữ liệu ra file json:
# Thông tin về json: http://freetuts.net/json-la-gi-cau-truc-chuoi-json-236.html
import json

with open('result.json', 'wt', encoding='utf-8') as f:
    f.write(json.dump(result, ensure_ascii=False))

# Lưu dữ liệu ra file excel
# Nếu chưa cài pyexcel thì cần cài: python -m pip install pyexcel
# Xong rồi cài thêm python -m pip install pyexcel-xls
# link về pyexcel: http://docs.pyexcel.org/en/latest/
import pyexcel as p 
p.save_as(records=result, dest_file_name="result.xls")


