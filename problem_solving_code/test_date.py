from datetime import datetime, timedelta

datetime_object = datetime.strptime('2024-05-09 04:02:36', "%Y-%m-%d %H:%M:%S")
time  = datetime.strftime(datetime_object, '%H')
print(datetime_object)
print(time)

if int(time)<5:
    business_date = datetime_object - timedelta(days=1)
else:
    business_date = datetime.strftime(datetime_object, "%Y-%m-%d")
    
print(business_date)