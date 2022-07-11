import datetime

current_date = datetime.datetime.now()
print(current_date)  # Normal date and time printer
# Modified date and time print:
print(current_date.strftime("Date: %Y-%m-%d, Time: %H:%M:%S "))
print(current_date.strftime("Date: %Y-%h-%d, Time: %H:%M:%S "))
