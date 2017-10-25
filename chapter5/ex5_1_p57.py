import time

epoch = time.time()
seconds_in_a_day = 24 * 60 * 60
seconds_in_an_hour = 60 * 60
seconds_in_a_minute = 60

days = epoch // seconds_in_a_day
hours = (epoch % seconds_in_a_day) // seconds_in_an_hour
minutes = (epoch % seconds_in_a_day) % seconds_in_an_hour // seconds_in_a_minute
seconds = (epoch % seconds_in_a_day) % seconds_in_an_hour % seconds_in_a_minute
print("%s: %s: %s: %s" %(days, hours, minutes, seconds))
print("Current time is %d: %d: %d: %d" %(days, hours, minutes, seconds))
