weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = {
    0: 'Jan',
    1: 'Feb',
    2: 'Mar',
    3: 'Apr',
    4: 'May',
    5: 'Jun',
    6: 'Jul',
    7: 'Aug',
    8: 'Sep',
    9: 'Okt',
    10: 'Nov',
    11: 'Dec'
}

days_per_month = {
    0: 31,
    1: 28,
    2: 31,
    3: 30,
    4: 31,
    5: 30,
    6: 31,
    7: 31,
    8: 30,
    9: 31,
    10: 30,
    11: 31
}

def get_days_in_month(date):
    # Check for leap year
    if date.year % 4 == 0 and (date.year % 100 == 0 or date.year % 400 == 0):
        if date.month == 1:
            return 29
    return days_per_month[date.month]

class EulerDate(object):
    def __init__(self, year, month, day, dayidx):
        self.year = year
        self.month = month
        self.day = day
        self.dayidx = dayidx

    def inc_day(self):
        self.dayidx = (self.dayidx+1) % 7
        if self.day < get_days_in_month(self) - 1:
            self.day += 1
        else:
            # Start new month
            self.day = 0
            if self.month == 11:
                self.month = 0
                self.year += 1
            else:
                self.month += 1
    def __repr__(self):
        return '%d %s %d is a %s' % (self.year, months[self.month], self.day+1, weekdays[self.dayidx])

def date_generator():
    curr_date = EulerDate(1900,0,0,0)
    while True:
        yield  curr_date
        curr_date.inc_day()

d = date_generator()
curr_date = d.next()
sunday_hits = 0
while curr_date.year < 2001:
    if curr_date.year > 1900:
        if curr_date.dayidx == 6 and curr_date.day == 0:
            sunday_hits += 1
    curr_date = d.next()

print sunday_hits

