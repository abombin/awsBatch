import os
import boto3
import pandas as pd
from io import StringIO
#import s3fs


s3 = boto3.client('s3')

def bucketList():
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')



#bucketList()

#print(os.getcwd())


# read data from the server
df=pd.read_csv('/home/ubuntu/github/shinyApp/shinyVizApps/uploadDatCov/data/metaData.tsv', sep='\t')

#print(df.columns)

# write data to s3
bucket = 'abombin' 
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)
s3_resource = boto3.resource('s3')
s3_resource.Object(bucket, 'df.csv').put(Body=csv_buffer.getvalue())


#df.to_csv(
#    "s3://abombin/metaDat.csv",
#    index=False,
#)
