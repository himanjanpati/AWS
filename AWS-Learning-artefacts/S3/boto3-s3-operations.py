import boto3
import os
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')

# Lists all the S3 buckets
for s3_bucket in s3.buckets.all():
    print(s3_bucket.name)

# Upload a file to S3 bucket
# Will use extra modules os, botocore.exceptions

def upload_file_s3(file_path, bucket_name, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_path)

    s3_client = boto3.client('s3')


    try:
        s3_client.upload_file(file_path,bucket_name,object_name)
        print('File successfully uploaded to bucket!!')
                    
    except ClientError as e:
        logging.error(e)
        return False
    return True
    
upload_file_s3("<path to file>", "<bucket_name>")