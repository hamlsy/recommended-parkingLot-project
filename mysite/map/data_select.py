import requests
from bs4 import BeautifulSoup
api_key = "755152686c6c73793131346e4b747859"

def data_select(select_gu):
    url1 = "http://openapi.seoul.go.kr:8088/" + api_key + "/xml/GetParkingInfo/1/1000/"+select_gu
    url2 = "http://openapi.seoul.go.kr:8088/" + api_key + "/xml/GetParkingInfo/1001/1972/"+select_gu
    rq1 = requests.get(url1)
    rq2 = requests.get(url2)
    soup1 = BeautifulSoup(rq1.text, "xml")
    soup2 = BeautifulSoup(rq2.text, "xml")
    combine_row = soup1.find_all("row") + soup2.find_all("row")
    return combine_row
