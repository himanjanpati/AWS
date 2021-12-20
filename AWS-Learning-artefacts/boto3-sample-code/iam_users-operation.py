import boto3

iam_svc = boto3.resource("iam")

user_count=0
for i in range(1,200):
  user_name = "iam_user"+str(i)
  iam_svc.create_user(UserName=user_name)
  user_count+=1
  print(f"{user_name}"+"created")
print(f"{user_count}"+" users created")

count=0
for iam_user in iam_svc.users.all():
  if iam_user.name.startswith('iam_user'):
    print(iam_user.name)
    iam_svc.meta.client.delete_user(UserName=iam_user.name)
    print(f"{iam_user.name}"+"deleted")
    count+=1 
print(f"total users deleted is {count}")

count = 0

iam_client = boto3.client('iam')

paginator = iam_client.get_paginator('list_users')
all_users = paginator.paginate()
for each_user in all_users:
  for each_username in each_user['Users']:
    print(each_username['UserName'])
    count+=1
print(count)
             



# for each_user in page_iterator:
#   print(each_user)
#   count+=1
# print(count)


# count = 0

# iam_client = boto3.client('iam')
# all_users = iam_client.list_users()['Users']
# for each_user in all_users:
#   print(each_user['UserName'])
#   count+=1
# print(f"total Users {count}")

