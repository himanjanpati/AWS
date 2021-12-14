### boto3 Meta ###

meta allows to leverage the boto3 client and resource both types of apis to use together if code is already written using one of the apis.

**example:**
 Show all the regions in AWS account which has EC2 service enabled
 
 Ans : The **describe_regions()** method is client method and can not be used with boto3 resource . If code is already using boto3 resouce the **meta.client** can be used to extend the client method

 ```
 import boto3

 ec2 = boto3.resource('ec2')

 #print(dir(ec2.meta))
 #print(ec2.meta.client.describe_regions())
 for each_region in ec2.meta.client.describe_regions()['Regions']:
   print(each_region['RegionName'])
 ```
    



