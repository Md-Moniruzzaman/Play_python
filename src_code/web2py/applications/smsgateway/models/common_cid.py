import datetime
import urllib
db = DAL('mysql://root:@localhost/smsgateway', decode_credentials=True)
mreporting_http_pass='abC321'
date_fixed=datetime.datetime.now()+datetime.timedelta(hours=6)