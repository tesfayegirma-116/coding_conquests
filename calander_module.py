import calendar
import datetime


def get_day_name(day, month, year):
    day_name = calendar.day_name[datetime.date(year, month, day).weekday()]
    return day_name


day, month, year = map(int, input().split())

print(get_day_name(month, day , year).upper())
