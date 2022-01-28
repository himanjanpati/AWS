### Paginator: ###

In the case of AWS **clients**, certain operations return the incomplete result, requiring subsequent requests to obtain the entire result set. The process of sending the subsequent requests to continue where a previous request left off is called pagination. 

***example:*** in the case of the IAM list_users operation, it only returns the 1st 100 objects while using the aws boto3 client, so we need to send the subsequent requests with the appropriate marker to retrieve the next page of results.

The advantage of the pagination approach is, results can be fetched more quick rather than waiting for the entire result. 

Example:
Retriving all IAM users using boto3 client

Note - for better illustration, 200 IAM users have been created using below script

```
import boto3

iam_svc = boto3.resource('iam')

for user in range(1,200):
  user_name = "iam_user"+str(user)
  iam_svc.create_user(UserName=user_name)
  print(f"{user_name}"+" created successfully")

count=0
for iam_user in iam_svc.users.all():
  if iam_user.name.startswith('iam_user'):
    print(iam_user.name)
    iam_svc.meta.client.delete_user(UserName=iam_user.name)
    print(f"{iam_user.name}"+"deleted")
    count+=1

print(f"Total {count} users deleted")
```

showing all users using boto3 resource

The below will show all the iam_users

In this case it shows 202 users as I have 202 users exist in my account

```
import boto3

count = 0
iam_svc = boto3.resource('iam')
for each_user in iam_svc.users.all():
  print(each_user.name)
  count+=1

print(f"total users {count}")
```

showing the IAM users using boto3 client 
The below will show 100 users total

**Boto3 client can not retrive full list of users when it exceeds more than 100**
So We need to use paginator to handle this scnario
paginator will allow to send subsequent requests to obtain the entire resultset

```
import boto3

iam_client = boto3.client('iam')
count = 0
for each_user in iam_client.list_users()['Users']:
  print(each_user['UserName'])
  count+=1

print(f"total users {count}")
```

### using paginator
```
import boto3 as aws

iam_client = aws.client('iam')
count=0
paginator = iam_client.get_paginator('list_users')
all_users = paginator.paginate()
for each_user in all_users:
  for each_user_name in each_user['Users']:
    print(each_user_name['UserName'])
    count+=1

print(count)

```
**we can not use all_users['Users'] in above to use a single loop**
This will show below error
So we need to use two loops to get each user then to iterate over users to get user names
**TypeError: 'PageIterator' object is not subscriptable