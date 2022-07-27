## Project Description

First of all, our project schema has plan of provisioning a Lambda function to generate near real time finance data records for interactive querying.
Initially, I received data through Yfinance module by using AWS Lambda Function and streamed in Kinesis which will save data to the S3 Buckets. 

AWS crawler connects to a data store S3 and progresses through a prioritized list of classifiers to determine the schema and then creates metadata tables in the catalog. and Lastly, extract query data through athena. I export the data in CSV file.

This data is used for making Analysis in stock data through Python Jupyter Notebook.

![Picture1](https://user-images.githubusercontent.com/82815882/169748078-c033f73c-a42c-4044-9e5a-49d16496dd7e.png)



## Built With

Python

AWS Lambdav to process stock feed data

Kinesis to streamline

AWS S3 Buckets 

AWS Glue to analyze data

AWS Athena to process query



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

### 4, Add a crawler 

![crawler](https://user-images.githubusercontent.com/82815882/169841102-9a9d7a5e-1fd3-40bf-8af0-4b33a94588a8.jpg)

### 5, Check Tables created from a crawler

![data](https://user-images.githubusercontent.com/82815882/169841320-30e2c62b-d4d6-4c61-ab00-d4c5320e8675.jpg)

### 6, Process query data through AWS Athena

![query data](https://user-images.githubusercontent.com/82815882/169841540-41cdd4e2-b400-44a0-bc46-31734bb3d1c1.jpg)

### 7, Make Analysis in Jupyter Notebook. 

## Outputs


![output3](https://user-images.githubusercontent.com/82815882/169841904-04e43dd5-21f9-4525-83dd-0e2339f882f3.png)
![output2](https://user-images.githubusercontent.com/82815882/169841905-a2f5fbaf-f42f-408e-a8a2-157377a1f1a2.png)
![output1](https://user-images.githubusercontent.com/82815882/169841908-69505386-2e4a-41d4-b09c-a7305007d20f.png)
![output4](https://user-images.githubusercontent.com/82815882/169841910-16c935dc-c85a-4214-8711-c0b8f7226bc8.png)





