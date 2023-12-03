import requests
from bs4 import BeautifulSoup
import pandas as pd

api_key = "755152686c6c73793131346e4b747859"
# addr = input("자치구를 입력하세요")
# cnt = input("몇 개의 값을 조회하시겠습니까?") + "/"
url1 = "http://openapi.seoul.go.kr:8088/"+api_key+"/xml/GetParkingInfo/1/1000/"
url2 = "http://openapi.seoul.go.kr:8088/"+api_key+"/xml/GetParkingInfo/1001/1972/"

#api data
# rq1 = requests.get(url1)
rq2 = requests.get(url2)
soup = BeautifulSoup(rq2.text, "xml")

parkingList = []
#set color
def setColor(capacity, current):
    percent = current/capacity * 100
    if percent == 100: return "black"
    if percent < 40:
        return "green"
    elif percent >= 40 and percent < 70:
        return "yellow"
    elif percent >= 70: return "red"
def getColor(x):
    return setColor(x['수용량'], x['현재 주차대수'])
#data append
for i in soup.find_all("row"):
    parking_code = i.find("PARKING_CODE").text
    parking_name = i.find("PARKING_NAME").text
    capacity = i.find("CAPACITY").text
    cur_parking = i.find("CUR_PARKING").text
    parkingList.append({"주차코드": parking_code, "주차장 이름":parking_name, "수용량":capacity,
                        "현재 주차대수":cur_parking})
print(len(soup.find_all("row")))
parking_df = pd.DataFrame(parkingList)
#data filter
# parking_df_filtered = parking_df.groupby("주차코드").agg({
#     '주차장 이름':'first',
#     '수용량':'sum', '현재 주차대수':'first',
#     '혼잡도':'first'}).reset_index()
#
# parking_df_filtered['혼잡도'] = parking_df_filtered.apply(getColor)
#show dataframe
# display(parking_df_filtered)
# print(parking_df_filtered['수용량'])
print(parking_df)
# parking_df_filtered.to_csv('C:\\Users\\이승영\\Desktop\\parking_data_list.csv', encoding='utf-8-sig')