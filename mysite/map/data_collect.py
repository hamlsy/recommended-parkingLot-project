import sqlite3
table_name = 't_11월21일09시00분08초'
db='C:\pycharmProject\\newDBdjangoProject\mysite\map\parking_data.db'
wanttime='11시'

#평일 평균 대수 구하기

def get_weekday_avg(hour,code):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    avg=0
    k=0

    # 평일 데이터 조회
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND (name LIKE '%20일{hour}%' OR name LIKE '%21일{hour}%' OR name LIKE '%22일{hour}%' OR name LIKE '%23일{hour}%' OR name LIKE '%24일{hour}%' OR name LIKE '%24일{hour}%' OR name LIKE '%27일{hour}%' OR name LIKE '%28일{hour}%' OR name LIKE '%29일{hour}%' OR name LIKE '%30일{hour}%' OR name LIKE '%1일{hour}%');")
    table_names = cursor.fetchall()
    table_names = [table[0] for table in table_names]

    # 각 테이블에서 주차 대수의 평균을 구하고 출력
    for table_name in table_names:
        query = f"SELECT PARKING_CODE, AVG(COALESCE(CUR_PARKING, 0)), CAPACITY FROM {table_name} WHERE PARKING_CODE={code} GROUP BY PARKING_CODE, CAPACITY;"
        cursor.execute(query)
        avg_parking_by_id = cursor.fetchall()
        
        for row in avg_parking_by_id:
            avg=avg+row[1]
            k=k+1
        

    conn.close()
    return avg/k if k>0 else 0
    
# 주말 평균 대수 구하기
def get_holyday_avg(hour,code):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    avg=0
    k=0

    # 주말 데이터 조회
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND (name LIKE '%25일{hour}%' OR name LIKE '%26일{hour}%' OR name LIKE '%12월2일{hour}%' OR name LIKE '%12월3일{hour}%');")
    table_names = cursor.fetchall()
    table_names = [table[0] for table in table_names]

    # 각 테이블에서 주차 대수의 평균을 구하고 출력
    for table_name in table_names:
        query = f"SELECT PARKING_CODE, AVG(COALESCE(CUR_PARKING, 0)), CAPACITY FROM {table_name} WHERE PARKING_CODE={code} GROUP BY PARKING_CODE, CAPACITY;"
        cursor.execute(query)
        avg_parking_by_id = cursor.fetchall()
        
        for row in avg_parking_by_id:
            avg=avg+row[1]
            k=k+1
        

    conn.close()
    return avg/k if k>0 else 0

#1개의 코드를 받아 그 주차장이름 출력
def get_name(code):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    query = f"SELECT PARKING_NAME " \
            f"FROM {table_name} " \
            f"WHERE PARKING_CODE={code};"
    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        rows
        
    return row[0]
#1개의 코드를 받아 그 평일 주차장운영시간 출력
def weektime(code):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    code1 = code

    query = f"SELECT WEEKDAY_BEGIN_TIME,WEEKDAY_END_TIME " \
            f"FROM {table_name} " \
            f"WHERE PARKING_CODE={code1};"
    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        time_range = f"{row[0]} ~ {row[1]}"  # 원하는 형태의 문자열 조합

    return time_range
        

def holydaytime(code):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    code1 = code

    query = f"SELECT HOLIDAY_BEGIN_TIME,HOLIDAY_END_TIME " \
            f"FROM {table_name} " \
            f"WHERE PARKING_CODE={code1};"
    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        time_range = f"{row[0]} ~ {row[1]}"  # 원하는 형태의 문자열 조합

    return time_range
    
def get_tel(code):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    code1 = code

    query = f"SELECT TEL " \
            f"FROM {table_name} " \
            f"WHERE PARKING_CODE={code1};"
    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        rows
        
    return row[0]
def get_address(code):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    code1 = code

    query = f"SELECT ADDR " \
            f"FROM {table_name} " \
            f"WHERE PARKING_CODE={code1};"
    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        rows
        
    return row[0]
        

def basic_fee(code):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    query = f"SELECT TIME_RATE, RATES " \
            f"FROM {table_name} " \
            f"WHERE PARKING_CODE={code};"
    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        if int(row[0]) != 0:
            time_range = (int(row[1]) / int(row[0])) * 5  # 원하는 형태의 문자열 조합
        else:
            time_range = int(row[1])

    return time_range

def extra_fee(code):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    query = f"SELECT ADD_TIME_RATE, ADD_RATES " \
            f"FROM {table_name} " \
            f"WHERE PARKING_CODE={code};"
    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        if int(row[0]) != 0:
            time_range = (int(row[1]) / int(row[0])) * 5  # 원하는 형태의 문자열 조합
        else:
            time_range = int(row[1])

    return time_range


def parking_type(code):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    code

    query = f"SELECT PARKING_TYPE_NM " \
            f"FROM {table_name} " \
            f"WHERE PARKING_CODE={code};"
    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        rows
        
    return row[0]
    
        

def get_data(code):
    data = {}

    data['weekday_avg'] = [get_weekday_avg('8시', code),get_weekday_avg('9시', code),get_weekday_avg('10시', code),get_weekday_avg('11시', code),get_weekday_avg('12시', code),get_weekday_avg('13시', code),get_weekday_avg('14시', code),get_weekday_avg('15시', code),get_weekday_avg('16시', code),get_weekday_avg('17시', code),get_weekday_avg('18시', code),get_weekday_avg('19시', code),get_weekday_avg('20시', code),get_weekday_avg('21시', code)]
    data['holyday_avg'] = [get_holyday_avg('8시', code),get_holyday_avg('9시', code),get_holyday_avg('10시', code),get_holyday_avg('11시', code),get_holyday_avg('12시', code),get_holyday_avg('13시', code),get_holyday_avg('14시', code),get_holyday_avg('15시', code),get_holyday_avg('16시', code),get_holyday_avg('17시', code),get_holyday_avg('18시', code),get_holyday_avg('19시', code),get_holyday_avg('20시', code),get_holyday_avg('21시', code)]
    data['weektime'] = weektime(code)
    data['holydaytime'] = holydaytime(code)
    data['tel'] = get_tel(code)
    data['address'] = get_address(code)
    data['basic_fee'] = basic_fee(code)
    data['extra_fee'] = extra_fee(code)
    data['name']=get_name(code)
    data['parking_type']=parking_type(code)

    return data

# 함수들을 활용하여 정보를 담은 딕셔너리 반환
result = get_data(1913385)
print(result)
