import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
REGION = os.environ['REGION']

ec2 = boto3.client('ec2', region_name=REGION)


def lambda_handler(event, context):

    instance = ec2.run_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        MaxCount=1,
        MinCount=1
    )

    print ("New instance created:")
    instance_id = instance['Instances'][0]['InstanceId']
    print (instance_id)
