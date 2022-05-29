1- create the folder structure
project
  - src
     - app.py
  commands.sh
  template.yaml

2- create the s3 bucket</br>
3- package cloudformation</br>
4- deploy the cloudformation</br>

<b>Permissions for EC2 assume role</b>

```
lambda:UpdateFunctionCode
lambda:GetFunction
lambda:ListTags
lambda:AddPermission
lambda:RemovePermission 
apigateway:POST
apigateway:PATCH
apigateway:GET
```