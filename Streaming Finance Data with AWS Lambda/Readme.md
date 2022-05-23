## Project Description

First of all, our project schema has plan of provisioning a Lambda function to generate near real time finance data records for interactive querying.
Initially, I received data through Yfinance module by using AWS Lambda Function and streamed in Kinesis which will save data to the S3 Buckets. 
Lastly, i categorized data with AWS Glue with crawlers and extract data through AWS Athena query.

This data is used for making Analysis in stock data.

![Picture1](https://user-images.githubusercontent.com/82815882/169748078-c033f73c-a42c-4044-9e5a-49d16496dd7e.png)



## Built With

Python
AWS Lambda
Kinesis
AWS S3 Buckets
AWS Glue
AWS Athena



## Forder Structure

project03

+-- results.csv

+-- results.jpeg

+-- query.sql

+-- data_transformer.py

+-- Analysis.ipynb 	

+-- Analysis.pdf 	

+-- finance_data.zip 

+-- assets

+-- +-- kinesis_config.jpeg

+-- +-- screenshot_of_s3_bucket.jpeg

+-- README.md

## Steps

### 1, Using AWS Lambda, we received data

![lambda code](https://user-images.githubusercontent.com/82815882/169748783-bdb95f36-21b9-4e6c-b0ef-a89249575312.png)

![lambda resul;t](https://user-images.githubusercontent.com/82815882/169748785-8bf541a7-18a5-4d7b-971c-686f4108c87e.png)

### 2, Streamlined data through kinesis

![kinesis_config](https://user-images.githubusercontent.com/82815882/169749037-553fbd12-3f14-423b-b9e9-24250b9b65d7.jpg)
815882/169748785-8bf541a7-18a5-4d7b-971c-686f4108c87e.png)

### 3, Save data in S3 Bucket

![screenshot_of_S3_bucket](https://user-images.githubusercontent.com/82815882/169749101-ac539df0-1822-4146-b3a9-34c26f77df50.jpg)

### 4, 

