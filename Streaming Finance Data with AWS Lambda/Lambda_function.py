import json
import boto3
import random
import datetime
from time import sleep
import yfinance as yf


StreamName = os.environ['StreamName']
REGION = os.environ['REGION']

kinesis = boto3.client('kinesis', REGION)


def getdata3(i):
    a=0
    df = yf.Ticker(i).history(period = '1d', interval = '5m')
    df = df.drop(['Open','Close', 'Volume','Dividends','Stock Splits'], axis=1)
    df.insert(2,'name',i)
    df.reset_index(inplace=True)
    df = df.rename(columns = {'Datetime':'ts'})
    while a < 79:
        data = {}
        data['High'] = df['High'][a]
        data['Low'] = df['Low'][a]
        data['ts'] = df['ts'].astype(str)[a]
        data['name'] = df['name'][a]
        a += 1
        data = json.dumps(data)
        print(data)
        kinesis.put_record(
            StreamName=StreamName,
            Data=data,
            PartitionKey="partitionkey")
            
List = {"FB","SHOP","BYND","NFLX","PINS","SQ","TTD","OKTA","SNAP","DDOG"}
for i in List:
    getdata3(i)
