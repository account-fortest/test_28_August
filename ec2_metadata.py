#### AWS connect and download metadata using python.

import boto3
import os

AWS_ACCESS_KEY_ID = os.environ.get['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ.get['AWS_SECRET_ACCESS_KEY']

## Function to loop through instance section to get all keys (metadata)
def loop_through_nested_loop(dict_):
    for key, value in dict_.items():
        if type(value) is dict:
            yield (key)
            yield from loop_through_nested_loop(value)
        else:
            yield (key)

## Connection to aws using boto3 package
client = boto3.client('ec2', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name='ap-south-1')
test = client.describe_instances()

## Looping through outer layers of dictionary 
for value in test['Reservations']:
    for instance_value in value['Instances']:
        for key in loop_through_nested_loop(instance_value):
            print (key)
