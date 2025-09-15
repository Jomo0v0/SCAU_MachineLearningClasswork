import time
now = time.strptime('2016-07-20', '%Y-%m-%d')
print(now)
print(time.strftime('%Y-%m-%d', now))

import datetime
someDay = datetime.date(1999, 2, 10)
anotherDay = datetime.date(1999, 2, 15)
deltaDay = anotherDay - someDay
print(deltaDay.days)