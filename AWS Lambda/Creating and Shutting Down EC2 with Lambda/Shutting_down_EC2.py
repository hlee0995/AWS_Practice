import os
import boto3

INSTANCE_ID = os.environ['INSTANCE_ID']
INSTANCE_ID =[INSTANCE_ID]
REGION = os.environ['REGION']

ec2 = boto3.client('ec2', region_name=REGION)
def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=REGION)
    ec2.stop_instances(InstanceIds=INSTANCE_ID)
    print(INSTANCE_ID, "stopped")
