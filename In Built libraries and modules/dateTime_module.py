
# ->  Write a program that prints the current date and time in the format YYYY-MM-DD HH:MM:SS.

from datetime import datetime

currentDate = datetime.now()

print(currentDate.strftime("%Y-%m-%d %H:%M:%S"))