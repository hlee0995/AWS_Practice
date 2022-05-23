import json
import boto3
import random
import datetime
import os
from time import sleep
import yfinance as yf

StreamName = os.environ['StreamName']
REGION = os.environ['REGION']
kinesis = boto3.client('kinesis',REGION)

def lambda_handler(event, context):
    List = ["FB","SHOP","BYND","NFLX","PINS","SQ","TTD","OKTA","SNAP","DDOG"]
    #List = ["FB"]
    for i in List:
        df = yf.Ticker(i).history(start='2022-05-02', end='2022-05-03', period = '1d', interval = '5m')
        df = df.drop(['Open','Close', 'Volume'], axis=1)
        df.insert(2,'name',i)
        df.reset_index(inplace=True)
        print(df)
        df = df.rename(columns = {'Datetime':'ts'})
        df['ts'] = df['ts'].astype('str')
        for i in range(len(df)):
            data = {}
            data['High'] = df['High'][i]
            data['Low'] = df['Low'][i]
            data['ts'] = df['ts'][i] 
            data['name'] = df['name'][i]
            dataj = json.dumps(data)+"\n"
            print(dataj)
            kinesis.put_record(
                StreamName=StreamName,
                Data=dataj,
                PartitionKey="partitionkey")
            sleep(0.5)
    return {
        'statusCode': 200,
        'body': json.dumps("Run Complete!")
    }    