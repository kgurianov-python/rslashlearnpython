"""
https://www.reddit.com/r/learnpython/comments/12a2zmp/comment/jes5omj/?utm_source=share&utm_medium=web2x&context=3

Beginner here. I found this exercise which seems interesting, but I haven't been able to solve it:

Given 2 dates as a string ('yyyy-mm-dd'), get a list with the beginning and another list with the ending of the months between those two dates, i.e:

start_date = '2022-06-01'
end_date = '2023-05-31'

start_dates = ['2022-06-01', '2022-07-01', '...', '2023-04-01', '2023-05-01']

end_datess  = ['2022-06-30', '2022-07-31', '...', '2023-04-30', '2023-05-31']
I don't even know where to start lol.
"""

from dateutil.relativedelta import relativedelta
from datetime import datetime
from dateutil.rrule import rrule, MONTHLY


def get_first_days(st_dt: str, end_dt: str) -> [str]:
    """
    Generate a list of 1 days of mant in the range btween start_date and end_date
    """
    st_dt = datetime.strptime(st_dt, '%Y-%m-%d')
    end_dt = datetime.strptime(end_dt, '%Y-%m-%d')
    result = map(lambda x: x.strftime('%Y-%m-%d'),
                 [dt for dt in rrule(MONTHLY, dtstart=(st_dt + relativedelta(day=1)), until=end_dt)])
    return list(result)


def get_last_days(st_dt: str, end_dt: str) -> [str]:
    """
    Generate a list of 1 days of mant in the range btween start_date and end_date
    """
    st_dt = datetime.strptime(st_dt, '%Y-%m-%d')
    end_dt = datetime.strptime(end_dt, '%Y-%m-%d')
    result = map(lambda x: (x + relativedelta(day=31)).strftime('%Y-%m-%d'),
                 [dt for dt in rrule(MONTHLY, dtstart=st_dt, until=end_dt)])
    return list(result)


if __name__ == '__main__':
    start_date = '2022-06-01'
    end_date = '2023-05-31'
    print(f"{get_first_days(start_date, end_date) = }")
    print(f"{get_last_days(start_date, end_date) = }")
