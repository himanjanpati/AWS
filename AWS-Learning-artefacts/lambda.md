## <b>AWS Lambda</b> ##
</br>

<i>What is serverless?</i>

 - No need to worry about deployment infra, scaling, high available
 - pay for use
 - only focus is code

<i>What is Lambda</i>
 - AWS Lambda is an event-driven, serverless computing platform used to deploy codes in variety of langiages like java, c#, python, nodeJs, go and etc.
 - Pay for use
   - number of requests
   - duration of requests
   - memory


- Lambda function handler name should be below which depends on filename and the handler name

   example - lambda function handler name for the below would be hello-world.test_handler

   <i><b>filename.handlername<b></i>

   <b>hello-world.py</b>
   ```
   import json

   def test_handler(event, context):
     print("Hello World!!")
     return{
         'statuscode': 200,
         'body': json.dump("Hello lambda")
     }
   ```
   event - captures the events that lambda handler receives.</br>
   ex: while testing lambda using aws console the test cases "key": "value" are the events for the lambda

   context:
   sample context here while using nodeJs runtime 
   <b>getRemainingTimeInMillis()</b> context  is not availble in python 
   ```
   {
      callbackWaitsForEmptyEventLoop: [Getter/Setter],
      succeed: [Function (anonymous)],
      fail: [Function (anonymous)],
      done: [Function (anonymous)],
      functionVersion: '$LATEST',
      functionName: 'hello-lambda',
      memoryLimitInMB: '128',
      logGroupName: '/aws/lambda/hello-lambda',
      logStreamName: '2022/04/06/[$LATEST]8fa2676644ce48a2a8e95becd2960abf',
      clientContext: undefined,
      identity: undefined,
      invokedFunctionArn: 'arn:aws:lambda:us-east-1:380780315807:function:hello-lambda',
      awsRequestId: '04978e08-fa83-46e3-94d3-c097869093bb',
      getRemainingTimeInMillis: [Function: getRemainingTimeInMillis]
   }

   ```
   sample python context
   ```
    LambdaContext(
       [aws_request_id=1bc6fa59-b453-4d96-9428-60dfc7eb82fb,log_group_name=/aws/lambda/hello-lambda,log_stream_name=2022/04/06/[$LATEST]37fae17c590b45538e88524774b5b8f7,function_name=hello-lambda,memory_limit_in_mb=128,function_version=$LATEST,invoked_function_arn=arn:aws:lambda:us-east-1:380780315807:function:hello-lambda,client_context=None,identity=CognitoIdentity([cognito_identity_id=None,cognito_identity_pool_id=None])]
       )
   ```
   128mb min and 10GB maximum memory size of lambda function</br>
   15 mins maximum timeout</br>
   512mb min to 10GB max ephemeral storage
   
- 5 compoments of serverless framework
  - functions
     - unit of deployment
     - package of code
  - events 
     - triggers the function
     - automatically creates the necessary infra based on type of event ex- http event, api gateway endpoint will be created and configures function to listen to the function
     - do some task upon trigger ex- provision a resource
  - resources
     - define all resources in serverlessconfig file
     - all defined resources will be provisioned automatically along with the function deployment
  - services
     - unit of organisation
     - project file (serverless.yaml) contains all functions/endpoints/handlers 
  - plugins
     - extends the framework