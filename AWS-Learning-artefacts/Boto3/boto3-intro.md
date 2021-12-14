### What is Boto3?

Boto3 is the Amazon Web Services (AWS) SDK for Python which enables to create, configure, and manage AWS services(EC2,S3 and etc.)

Boto3 is built on the top of a library called Botocore, which the AWS CLI shares. Botocore provides the low-level clients, session and credentials, and configuration data which is configured in aws cli (aws confiure --profile)</br>

Boto3 is built on the top of Botocore by providing its own <b>session, resources, collections, waiters, and paginators.</b>

### Installing Boto3

```
pip3 install boto3 --user
```
By default, pip install packages to a system directory(e.g. /usr/local/lib/python3.9) and this requires root privilege. This will install the package in /usr/local/lib/python3.7/site-packages
```
sudo pip3 install boto3
```
By using --user flag, this will make pip install packages in the home directory instead, which doesn’t require any special privileges.

configure the aws command line by proving your aws account security credentials, region name, and default output format. In case if you don’t have awscli installed you can install it using the below command.

```
sudo pip3 install awscli
```
```
$ aws configure
AWS Access Key ID [****************XXXX]:
AWS Secret Access Key [****************XXXX]:
Default region name [eu-west-2]:
Default output format [json]:
```
To verify the above working</br>
This will show the configured user's profile
```
aws sts get-caller-identity

{
    "UserId": "XXXXXXXXXXXXXXXXXX",
    "Account": "123456789",
    "Arn": "arn:aws:iam::123456789:user/aws-cli-admin"
}
```
boto3 sessions

default session
```
session = boto3.session.Session()
```
custom session
```
custom_session = boto3.session.Session(profile_name="aws-cli-admin")
print(custom_session)
```

**boto3 resource and client
 - boto3 client is the original AWS API abstraction provides low level access to AWS services
 - boto3 resource is the newer AWS API abstraction provides high level access to AWS servicess
 - client supports all kind of service operations, resouce does not provide all opearations</br>

getting all s3 buckets using resouce api
```
import boto3
s3_resource = boto3.resource('s3')
#This resuns a collection and could be iterated to get the bucket names 
all_s3_buckets = s3_resource.buckets.all()
#returns collection of bucket names and each bucket name could be retieved using '.' operator
for each_s3 in all_s3_buckets:
  print(each_s3.name)

#simplifying above
for s3_bucket in s3_resource.buckets.all():
  print(s3_bucket.name)
```
getting all s3 buckets using client api

```
import boto3

s3_client = boto3.client('s3')
dir(s3_client)
#will show allavileble methods and props 
#list_buckets methods will show the list of buckets
#this will return a dictonary which will have all buckets inside 'Buckets' list
for each_s3 in s3_client.list_buckets()['Buckets']:
  print(each_s3['Name'])
```

