import requests
import datetime
import calendar

url = "https://iapi.bot.or.th/Stat/BondAuction/bond_auction_v1/"
querystring = {"start_period":"2017-07-17","end_period":"2017-06-17"}
headers = {
    'api-key': "U9G1L457H6DCugT7VmBaEacbHV9RX0PySO05cYaGsm"
    }
print(datetime.datetime.now())
response = requests.request("GET", url, headers=headers, params=querystring)
#print(datetime.datetime.now())
print(response.text)


for d_year in range(2016,2017): 
    for d_month in range(11,12):
        s_year = str(d_year)
        s_month = str(d_month).zfill(2)
        s_lastday = str(calendar.monthrange(d_year,d_month)[1]) #last day of each month
        print(s_year+"-"+s_month)
        querystring = {"start_period":'"'+s_year+"-"+s_month+"-01"+'"',"end_period":'"'+s_year+"-"+s_month+"-"+s_lastday+'"'}
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
