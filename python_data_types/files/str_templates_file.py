from dateutil.utils import today

with open('str_date.txt') as f:
    for line in f:
        print(line.format(date=today().strftime('%Y-%m-%d')))
