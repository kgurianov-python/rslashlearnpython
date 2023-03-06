import calendar
from datetime import date, timedelta


def all_weekday_year(year: int, weekday: int):
    result = date(year, 1, 1)
    result += timedelta(days=weekday - result.weekday() + 7)
    while result.year == year:
        yield result
        result += timedelta(days=7)


for day in all_weekday_year(2023, calendar.FRIDAY):
    print(day.strftime('%d %b %Y, %A'))
