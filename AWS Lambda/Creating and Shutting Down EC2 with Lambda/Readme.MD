# Creating and Shutting down an EC2 instance using a lambda function and boto3 library Project

### Step 1, Go to Lambda from AWS homepage

![Lambda aws](https://user-images.githubusercontent.com/82815882/168392413-e8c3d1e8-2902-4f32-b379-9b2dcb51fa54.png)

### Step 2, Create Function

![Create Function](https://user-images.githubusercontent.com/82815882/168392626-7786241b-163c-4d36-8210-85addec7a812.png)

Select Author from scratch, Python 3.9,
Set up execution role as create a new role with basic lambda permission and make note on new role's name

### Step 3, Go to Iam Tap

![Iam dashboard](https://user-images.githubusercontent.com/82815882/168392816-2becda5c-4f35-46ee-908b-c5e27c6fa142.png)

### Step 4, Roles - click on policy name to Change LambdaBasicExecutionRole policy 

![EC2 Permission Tap ](https://user-images.githubusercontent.com/82815882/168392835-e997df23-1c05-42d7-8d8a-12e867c935e3.png)


### Step 5, Add Environment Variable and write the code

![env](https://user-images.githubusercontent.com/82815882/168393073-31249aa3-1da1-478c-b4cc-032ec4c4ba61.png)

Key: AMI Value: ami-0c6a6b0e75b2b6ce7 (This is a random ID from Amazon Machine Image list from EC2 management console).
Key: INSTANCE_TYPE Value: t2.micro
Key: REGION Value:us-east-2


### Step 6, Run the function after take out Key values from Event JSON

![test1](https://user-images.githubusercontent.com/82815882/168393393-c09b7ca0-52b7-4f13-9a61-682ae610acc6.png)

##now your EC2 is Running!

![12](https://user-images.githubusercontent.com/82815882/168393472-51dfc9b6-4f51-4cfb-beda-f292e37333fc.png)

### Step7, Create StopEC2 Function in similar way and change iam permission again

![StopEC2](https://user-images.githubusercontent.com/82815882/168394167-e41679c9-36ac-440e-87bf-236cfefc56a6.png)

### Step 8, Add Environment Variable and write the code

![evn stop](https://user-images.githubusercontent.com/82815882/168394556-91b7eb97-5d32-485c-a515-83902b0adc51.png)


### Step 9, Result

![stop it](https://user-images.githubusercontent.com/82815882/168394481-14e58e5e-12a5-4b87-ad02-2cb5d5972813.png)
![result](https://user-images.githubusercontent.com/82815882/168394488-63507169-f15c-4991-9288-0ec24c8f0c8a.png)


### In this way, I learned how i can utilize AWS Lambda Function


