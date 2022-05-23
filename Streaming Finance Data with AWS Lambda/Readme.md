

First of all, our project schema has plan of provisioning a Lambda function to generate near real time finance data records for interactive querying.
Initially, I received data through Yfinance module by using AWS Lambda Function and streamed in Kinesis which will save data to the S3 Buckets. 
Lastly, i categorized data with AWS Glue with crawlers and extract data through AWS Athena query.

This data is used for making Analysis in stock data.

![Picture1](https://user-images.githubusercontent.com/82815882/169748078-c033f73c-a42c-4044-9e5a-49d16496dd7e.png)



##Built With

Python
AWS Lambda
Kinesis
AWS S3 Buckets
AWS Glue
AWS Athena



Forder Structure
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
