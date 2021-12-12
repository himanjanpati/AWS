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
```

