import json
from datetime import datetime
from time import localtime

from config import global_config as base_config
from util import base_util as util


def get_access_token():
    app_id = config["appId"]
    app_secret = config["appSecret"]
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}" \
        .format(app_id, app_secret)
    return util.request_get(url)['access_token']


def get_location():
    user_city = config["userCity"]
    weather_key = config["weatherKey"]
    url = 'https://geoapi.qweather.com/v2/city/lookup?location={}&key={}'.format(user_city, weather_key)
    location_list = util.request_get(url)['location']
    if location_list:
        return location_list[0]['id']


def get_weather():
    location_id = get_location()
    weather_key = config["weatherKey"]
    daily_url = 'https://devapi.qweather.com/v7/weather/3d?location={}&key={}'.format(location_id, weather_key)
    now_url = 'https://devapi.qweather.com/v7/weather/now?location={}&key={}'.format(location_id, weather_key)
    indices_url = 'https://devapi.qweather.com/v7/indices/1d?type=0&location={}&key={}'.format(location_id, weather_key)

    weather_info = util.request_get(daily_url)['daily'][0]
    now_weather_info = util.request_get(now_url)['now']

    indices_url_info = util.request_get(indices_url)['daily']

    weather_data = {
        # 日期
        "fx_date": weather_info['fxDate'],
        # 白天天气
        "text_day": weather_info['textDay'],
        # 晚间天气
        "text_night": weather_info['textNight'],
        # 最高气温
        "temp_max": weather_info['tempMax'],
        # 最低气温
        "temp_min": weather_info['tempMin'],
        # 天气
        "weather": now_weather_info['text'],
        # 温度
        "temp": now_weather_info['temp'],
        # 体感温度
        "feels_like": now_weather_info['feelsLike']
    }
    for indices in indices_url_info:
        weather_data["index_name{}".format(indices['type'])] = indices['name']
        weather_data["index_category{}".format(indices['type'])] = indices['category']
        weather_data["index_text{}".format(indices['type'])] = indices['text']
        long_text(weather_data, "index_text{}".format(indices['type']))

    return weather_data


def long_text(json_data, key):
    limit = 19
    if key.__contains__("en"):
        limit = 32

    text1 = json_data[key]
    text2 = ""
    if len(text1) > limit:
        text2 = text1[limit:]
        text1 = text1[0:limit]

    json_data[key] = text1
    next_key = key + "x"
    if key.__contains__("index"):
        next_key = key[10:] + "x"
    json_data[next_key] = text2


def get_ciba():
    url = "http://open.iciba.com/dsapi/"
    data = util.request_get(url)
    return {
        "note_ch": data["note"],
        "note_en": data["content"]
    }


def get_rainbow():
    rainbow_key = config["rainbowKey"]
    rainbow_url = "https://apis.tianapi.com/caihongpi/index?key=%s" % rainbow_key
    return util.request_get(rainbow_url)['result']['content']


def build_basic_data():
    week_list = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
    year = localtime().tm_year
    month = localtime().tm_mon
    day = localtime().tm_mday
    today = datetime.date(datetime(year=year, month=month, day=day))

    week = week_list[today.isoweekday() % 7]
    now_date = "{} {}".format(today, week)
    nick_name = config["nickName"]
    since_date = config["sinceDate"]
    since_days = util.get_since_day_to_today(since_date)
    birthday = config["birthday"]
    birth_days = util.get_birthday(birthday)
    city = config["userCity"]
    if birth_days == 0:
        birth_text = "今天是你的生日哦，祝{}生日快乐！".format(nick_name)
    else:
        birth_text = "距离下次生日还有{}天".format(birth_days)

    return {
        "date": now_date,
        "nick_name": nick_name,
        "since_days": since_days,
        "birth_text": birth_text,
        "city": city,
    }


def change_color(change_data):
    res = {}
    for k in change_data:
        v = change_data[k]
        res[k] = {
            "value": v,
            "color": util.get_random_color()
        }
    return res


def send_message():
    access_token = get_access_token()
    url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s" % access_token

    basic_date = build_basic_data()
    weather_data = get_weather()
    note_data = get_ciba()
    basic_date.update(weather_data)
    basic_date.update(note_data)
    basic_date["rainbow"] = get_rainbow()

    long_text(basic_date, "rainbow")
    long_text(basic_date, "note_ch")
    long_text(basic_date, "note_en")

    res = change_color(basic_date)

    payload = {
        "touser": config["userId"],
        "template_id": config["templateId"],
        "topcolor": "#FF0000",
        "data": res
    }
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    response = util.request_post(url, headers=headers, payload=payload)
    if response["errcode"] == 40037:
        print("推送消息失败，请检查模板id是否正确")
    elif response["errcode"] == 40036:
        print("推送消息失败，请检查模板id是否为空")
    elif response["errcode"] == 40003:
        print("推送消息失败，请检查微信号是否正确")
    elif response["errcode"] == 0:
        print("推送消息成功")
    else:
        print(response)


if __name__ == "__main__":
    config = base_config.load_config()
    send_message()
