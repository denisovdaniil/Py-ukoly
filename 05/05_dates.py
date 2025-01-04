# 05_dates.py

import datetime



for month in range(1,13):
    date = datetime.date(2024, month, 1)
    dmy = date.strftime('%d/%m/%Y')
    print(dmy)
