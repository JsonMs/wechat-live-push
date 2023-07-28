import json
import os
import sys
from datetime import datetime, date
from time import localtime

import yaml
from requests import get, post
from zhdate import ZhDate


# 获取颜色,等待颜色开启的那天
def get_random_color():
    return "#173177"

# Get 请求
def request_get(get_url):
    try:
        # headers = {
        #     'Content-Type': 'application/json',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        #                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        # }
        return get(get_url).json()
    except Exception as e:
        print("GET request fail！", e)
        os.system("pause")
        sys.exit(1)


# Post 请求
def request_post(post_url, headers, payload):
    try:
        return post(post_url, headers=headers, json=payload).json()
    except Exception as e:
        print("POST request fail！", e)
        os.system("pause")
        sys.exit(1)


# 读取yaml文件
def read_yaml(file_name):
    try:
        with open(file_name, encoding='utf-8') as file:
            return yaml.load(stream=file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        print("文件路径不对，请填写正确文件路径 %s" % file_name)
        os.system("pause")
        sys.exit(1)
    except SyntaxError:
        print("%s文件格式不正确" % file_name, SyntaxError)
        os.system("pause")
        sys.exit(1)


# 获取下一个生日
def get_next_birthday(birthday, next_year):
    year = localtime().tm_year
    birthday_year = birthday.split("-")[0]
    birthday_mouth = int(birthday.split("-")[1])
    birthday_day = int(birthday.split("-")[2])

    if next_year:
        year += 1
    # 今年生日
    if birthday_year[0] == "r":
        return ZhDate(year, birthday_mouth, birthday_day).to_datetime().date()
    else:
        return date(year, birthday_mouth, birthday_day)


# 获取生日
def get_birthday(birthday):
    year = localtime().tm_year
    month = localtime().tm_mon
    day = localtime().tm_mday
    today = datetime.date(datetime(year=year, month=month, day=day))

    year_birthday = get_next_birthday(birthday, False)
    # 计算生日年份，如果还没过，按当年减，如果过了需要+1
    if today == year_birthday:
        return 0

    if today > year_birthday:
        year_birthday = get_next_birthday(birthday, True)
    return year_birthday.__sub__(today).days


def get_now():
    year = localtime().tm_year
    month = localtime().tm_mon
    day = localtime().tm_mday
    today = datetime.date(datetime(year=year, month=month, day=day))
    return today, year, month, day


# 获取开始时间到今天的天数
def get_since_day_to_today(since_day):
    today, year, month, day = get_now()
    since_year = int(since_day.split("-")[0])
    since_month = int(since_day.split("-")[1])
    since_day = int(since_day.split("-")[2])
    since_date = date(since_year, since_month, since_day)
    return today.__sub__(since_date).days
