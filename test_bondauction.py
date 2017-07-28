import requests
import datetime

url = "https://iapi.bot.or.th/Stat/BondAuction/bond_auction_v1/"
querystring = {"start_period":"2000-07-17","end_period":"2017-06-17"}
headers = {
    'api-key': "U9G1L457H6DCugT7VmBaEacbHV9RX0PySO05cYaGsm"
    }
print(datetime.datetime.now())
response = requests.request("GET", url, headers=headers, params=querystring)
print(datetime.datetime.now())
print(response.text)
