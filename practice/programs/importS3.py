import os
import boto3


s3 = boto3.client('s3')

def bucketList():
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')


#bucketList()

print(os.getcwd())