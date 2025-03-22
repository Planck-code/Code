import time

import requests
from lxml import etree
import re

#href = //div[@class="content__list--item--main"]/p[1]/a[1]/@href

# 定义翻页
pg = 1

# 起始页面URL
start_urls = f"https://hf.lianjia.com/zufang/pg{pg}"
print(start_urls)

# 设置请求头参数
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "cookie":"SECKEY_ABVK=1paWqbEYOjh+uo2Ut54lzFrVbbh3d52xlaA9LigIegU%3D; BMAP_SECKEY=1paWqbEYOjh-uo2Ut54lzH_N4B0PPFeeOn3a6hEWr7L2ySXhkchafQuxwwk9ohHjr7KGhZo1a9Fg0a8fyYyEIc8nFbyNXU84-ppwigvv6QzebarrpwgojU5lYGyThqgZ-s9k6qR2ZvRwTJMkaRRZsRcBCm6_MY6cxakCCyDHchTgOEc5c35KrjuSSAqMhlFd; lianjia_uuid=8bdf8687-3a50-48c4-ad2c-ecf10ad9998b; _jzqy=1.1730461011.1730461011.1.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6%E7%BD%91%E5%AE%98%E7%BD%91.-; _ga=GA1.2.1500932845.1730461023; lfrc_=7d91df54-c10b-458c-8d5e-91b533ee3a7b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22192daf77056581-08db59f3d1149-26011951-921600-192daf770589e1%22%2C%22%24device_id%22%3A%22192daf77056581-08db59f3d1149-26011951-921600-192daf770589e1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wyhf%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoxau%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; select_city=340100; Hm_lvt_46bf127ac9b856df503ec2dbf942b67e=1735263205,1735283839,1736726781; Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e=1736726781; HMACCOUNT=2ABB3EB82A9B5C49; _jzqa=1.3967762617377708500.1730461011.1735283839.1736726781.7; _jzqc=1; _jzqckmp=1; _qzja=1.388439764.1730461011112.1735283838848.1736726781504.1735283873691.1736726781504.0.0.0.12.7; _qzjc=1; _qzjto=1.1.0; GUARANTEE_POPUP_SHOW=true; GUARANTEE_BANNER_SHOW=true; _gid=GA1.2.359243232.1736726793; beikeBaseData=%7B%22parentSceneId%22:%2271661273677885185%22%7D; lianjia_ssid=61936292-b86a-425b-9d2c-dc8d0d29b52a; login_ucid=2000000456265214; lianjia_token=2.0014b8686f4311087d0515415ed048ebd6; lianjia_token_secure=2.0014b8686f4311087d0515415ed048ebd6; security_ticket=tIl2KESHvgoigoBBcQw61LH9ARj4nB1RO+8miSmMOk3Xsi/qm/mrUKwklBZ71avxiALrYsrEbI7sR+DLk5qjusT0yB9erQMS/JtwMQ/q+UHSjBZtGOPykhLsg3K6x8d0SB39APP6YguWGngh2WVNT25qF7OLU1CxhrL2R9/xtow=; ftkrc_=a476c6a1-d47b-42d6-a47e-49e995847a32; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNmE1ZjE3YmQ1YTQ4MDk3YmIxNDRmOTJkNWI3MDA1ZjcwYzJlZmZhMDBjNTFhMzUzNjM1ZWZkM2E3ZTBhZjM2MjFlMzhiNzk3YzdhYzQwMjNiNDMxYWE3MDYyZThmMzkxYmU2ZmE5ZjAzNjE5OTQ0ZjlmN2Y3YTZlZmYyOWJlNzMxYjA0MTI3MTlkMjRlZTA5NWJlMWRhYWEwOWZjOTFhOWNiZDZmZTVkNTRiNDM3MDhjMDAyMGFiNGVhMWM2OGQyY2U2MjhlMDA1MjAwNGUwOTYwMzY3Mzg5NjYxNTI2NGYwNzQ0MTExYjI4NWVlYzhjMzk4OGU0MGIzNTUxOTY2ZFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI5NGNiNmQxMVwifSIsInIiOiJodHRwczovL2hmLmxpYW5qaWEuY29tL3p1ZmFuZyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9"
}

# 获取response对象
response = requests.get(url=start_urls,headers=headers)
content = response.content.decode('utf-8')

# 通过lxml库解析content内容
html = etree.HTML(content)

# 获取href属性
urls = html.xpath('//div[@class="content__list--item--main"]/p[1]/a[1]/@href')


housebasic = []
for url in urls :
    new_url = "https://hf.lianjia.com/zufang"+url
    print(new_url)

    # 获取response对象
    response = requests.get(url=new_url, headers=headers)
    content = response.content.decode('utf-8')

    # 通过lxml库解析content内容
    html = etree.HTML(content)

    # 核验码
    verification_code = html.xpath('//i[@class="gov_title"]/text()[2]')[0]
    verification_code = re.findall("([a-zA-Z0-9]+)", verification_code, re.DOTALL)[0]
    print(verification_code)

    # 房源标题
    title = html.xpath('//div[@class="content clear w1150"]/p[1]/text()')[0].strip()
    print(title)

    # 维护时间
    maintain_time = html.xpath('//div[@class="content__subtitle"]/text()')[0].strip()
    print(maintain_time)

    # 所在区
    district = html.xpath('//p[@class="bread__nav__wrapper oneline"]/a[2]/text()')[0].strip()
    district = district.split("租")[0]
    print(district)

    # 所在路
    street = html.xpath('//p[@class="bread__nav__wrapper oneline"]/a[3]/text()')[0].strip()
    street = street.split("租")[0]
    print(street)

    # 小区名
    community_name = html.xpath('//div[@class="bread__nav w1150 bread__nav--bottom"]/h1/a/text()')[0].strip()
    community_name = community_name.split("租")[0]
    print(community_name)

    # 出租方式
    lease_type = html.xpath('//ul[@class="content__aside__list"]/li[1]/text()')[0].strip()
    print(lease_type)

    # 户型
    house_type = html.xpath('//ul[@class="content__aside__list"]/li[2]/text()')[0].strip()
    house_type = house_type.split(" ")[0]
    print(house_type)

    eg = {
        'verification_code': verification_code,
        'title': title,
        'maintain_time': maintain_time,
        'district': district,
        'street': street,
        'community_name': community_name,
        'lease_type': lease_type,
        'house_type': house_type
    }

    housebasic.append(eg)
    time.sleep(10)

import csv
with open("zufang.csv","w",encoding='utf-8',newline="") as f:
    #字段名
    filenames = ['verification_code','title','maintain_time','district',
                 'street','community_name','lease_type','house_type']
    writer = csv.DictWriter(f,fieldnames=filenames)
    writer.writeheader()
    writer.writerows(housebasic)
    print("数据写入成功")

