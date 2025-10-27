from datetime import datetime

def get_days_from_today(date):
    date_n = datetime.strptime(date, '%Y-%m-%d')
    now = datetime.now ()
    difference = now - date_n
    return difference.days
f =  get_days_from_today ('2020-9-10')
print(f)
