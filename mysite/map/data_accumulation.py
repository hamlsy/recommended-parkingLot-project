import requests
import pandas as pd
import sqlite3
from datetime import datetime

#api key를 통해 json_data 추출
def get_data(api_key):
    url = "http://openapi.seoul.go.kr:8088/"+api_key+"/json/GetParkingInfo/1/800/"
    response = requests.get(url)
    json_data = response.json()
    return json_data

#json data -> 정규화 및 dataframe화
def set_dataframe(api_data):
    df = pd.json_normalize(api_data['GetParkingInfo']['row'])
    return df

api_key = "755152686c6c73793131346e4b747859"
api_data = get_data(api_key)
df = set_dataframe(api_data)

#DB접근
connect = sqlite3.connect("test1.db")

#현재 시간
now = datetime.now()

#테이블 name 현재 시간으로 설정함.. 추후 수정 필요
table_name = now.strftime('%m-%d %H:%M:%S')

#sql 방식으로 DATAFRAME 해당 table에 저장
df.to_sql(table_name, connect)

#저장
connect.commit()

#DB 연결 종료
connect.close()
