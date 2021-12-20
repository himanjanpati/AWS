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