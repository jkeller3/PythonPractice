import datetime
import pytz

# PRINTS OUT LIST OF ALL TIME ZONES!
# for tz in pytz.all_timezones:
# 	print(tz)

tday = datetime.date.today()
print(tday)
print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)

print(tday - tdelta)

# date 2 = date 1 + timedelta

# timedelta = date1 + date2

bday = datetime.date(2024, 5, 21)

till_bday = bday - tday
print(till_bday.days)


# testing datetime functionality without pytz functionality (OLD)
# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.now(datetime.UTC)

dt = datetime.datetime(2024, 4, 30, 20, 46, tzinfo=pytz.UTC)
print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_pcf = dt_utcnow.astimezone(pytz.timezone('US/Pacific'))
print(dt_pcf)


dt = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')

print(dt.strftime('%B %d, %Y'))

dt_str = 'April 30, 2024'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime