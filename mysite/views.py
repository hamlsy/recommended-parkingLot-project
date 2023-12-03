import datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt

from mysite.map import data_collect
from mysite.map.data_select import data_select
from mysite.map.data_setting import set_color, add_marker_set, sort_distance_marker


# Create your views here.
def home(request):
    return render(request, 'home.html')

# with open('home/lsy4723/recommended-parkingLot-project/newDBdjangoProject/templates/seoul_set.json', 'r', encoding='UTF8') as f:
def new_map(request):
    gu_kr_name = request.POST.get('select_gu')
    with open('C:\pycharmProject\\newDBdjangoProject\\templates\seoul_set.json', 'r', encoding='UTF8') as f:
        json_data = json.load(f)
    lat = ''
    lng = ''
    for key, value in json_data.items():
        if gu_kr_name == key:
            lat = value["lat"]
            lng = value["long"]
            break
    # data_setting -> add_marker_set function
    marker_set = add_marker_set(data_select(gu_kr_name))

    context = {'initial_lat': lat, 'initial_lng': lng, 'marker_set': marker_set}
    return render(request, "new_map.html", context)

def current_location(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        request.session['user_latitude'] = latitude
        request.session['user_longitude'] = longitude
        return JsonResponse({'success': True})
    else:
        return render(request, "current_location.html")
    return JsonResponse({'success': False})
@csrf_exempt
def new_current_map(request):
    if request.method == 'POST':
        user_lat = request.POST.get('latitude')
        user_lng = request.POST.get('longitude')
    print("현재 좌표: ",user_lat, user_lng, datetime.datetime.now())
    marker_set = sort_distance_marker(user_lat, user_lng, add_marker_set(data_select("")))
    context = {"user_lat": user_lat, "user_lng": user_lng, "marker_set": marker_set}
    return render(request, "new_current_map.html", context)

def parking_detail(request, parking_code):
    context = data_collect.get_data(int(parking_code))
    context["parking_code"] = parking_code
    return render(request, 'parking_detail.html', context)
def new_entire_map(request):
    lat = '37.5642135'
    lng = '127.0016985'
    marker_set = add_marker_set(data_select(""))
    context = {'initial_lat': lat, 'initial_lng': lng, 'marker_set': marker_set}
    return render(request, "new_entire_map.html", context)