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