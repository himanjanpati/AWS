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

def delete_file(bucket_name, object_key):

    s3 = boto3.resource('s3')
    s3_bucket = s3.Bucket(bucket_name)

    response = s3_bucket.delete_objects(
        Delete={
            'Objects': [
                {
                    'Key': object_key
                },
            ],
            'Quiet': True
        }
    )
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        print("failed to delete file")
    else:
        print("deletion success!!")

upload_file_s3("<path to file>", "<bucket_name>")

delete_file('<bucket_name>', '<file_name with ext>')