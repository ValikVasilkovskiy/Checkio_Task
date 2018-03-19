# Input: Two dates as tuples of integers.
# Output: The difference between the dates in days as an integer.
# Example: days_diff((1982, 4, 19), (1982, 4, 22)) == 3
# Example: days_diff((2014, 1, 1), (2014, 8, 27)) == 238
# Example: days_diff((2014, 8, 27), (2014, 1, 1)) == 238

from datetime import datetime

def days_diff(date1, date2):
    if datetime(date2[0], date2[1], date2[2]) >= datetime(date1[0], date1[1], date1[2]):
        # get object timedelta
        delta = datetime(date2[0], date2[1], date2[2]) - datetime(date1[0], date1[1], date1[2])
    else:
        delta = datetime(date1[0], date1[1], date1[2]) - datetime(date2[0], date2[1], date2[2])
    return delta.days # timedelta.days
print(days_diff((2014, 8, 27), (2014, 1, 1)))


