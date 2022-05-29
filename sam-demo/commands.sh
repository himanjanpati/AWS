#create an S3 bucket
aws s3 mb s3://himanjan-code-sam

aws cloudformation package --s3-bucket himanjan-code-sam --template-file template.yaml --output-template-file gen/template-generated.yaml

aws cloudformation deploy --template-file gen/template-generated.yaml --stack-name hello-world-sam --capabilities CAPABILITY_IAM