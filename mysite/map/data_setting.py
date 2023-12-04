import pandas as pd
from haversine import haversine


#혼잡도 비율 색상
def set_color(current, capacity):
    degree = (int(current)/int(capacity))*100
    if degree >= 100: return 'gray'
    elif degree >= 80 and degree <100:
        # red
        return 'red'
    elif degree < 80 and degree > 60:
        #yellow
        return 'yellow'
    else:
        #green
        return 'green'
def calculate_distance(lat, lng, target_lat, target_lng):
    start = (float(lat), float(lng))
    end = (float(target_lat), float(target_lng))
    distance = haversine(start, end)
    return distance


def add_marker_set(data_select_row):
    marker_set = []
    for i in data_select_row:
        parking_code = i.find("PARKING_CODE").text
        parking_lat = i.find("LAT").text
        parking_lng = i.find("LNG").text
        parking_name = i.find("PARKING_NAME").text
        parking_addr = i.find("ADDR").text
        parking_cur = i.find("CUR_PARKING").text
        parking_capacity = i.find("CAPACITY").text
        parking_color = set_color(parking_cur, parking_capacity)
        parking_district = parking_addr.split(" ")[0]
        marker_set.append({"parking_code":parking_code, "lat":parking_lat, "lng":parking_lng, "name":parking_name, "addr": parking_addr,
                           "current": parking_cur,"capacity": int(parking_capacity),
                           "marker_color": parking_color, "parking_district": parking_district})
    marker_set_df = pd.DataFrame(marker_set)
    marker_set_filtered = marker_set_df.groupby("parking_code").agg({"parking_code":'first', "lat":'first', "lng":'first', "name":'first', "addr": 'first',
                           "current": 'first',"capacity": 'sum',
                           "marker_color": 'first', "parking_district": 'first'})

    marker_set = marker_set_filtered.to_dict('records')
    for marker_info in marker_set:
        marker_info["marker_color"] = set_color(marker_info["current"], marker_info["capacity"])

    return marker_set

def sort_distance_marker(user_lat, user_lng, marker_set):
    parking_location = []
    for parking_info in marker_set:
        parking_location.append([parking_info,
                                 calculate_distance(user_lat,user_lng, parking_info['lat'], parking_info['lng'])])
    #거리 순 정렬
    parking_location.sort(key=lambda x: x[1])
    result = []
    cnt = 0
    for parking_info in parking_location:
        # 우선순위 몇 개 표시할지 설정
        if cnt == 3: break;
        if parking_info[0]["marker_color"] != "gray":
            result.append(parking_info[0])
            cnt += 1
    return result