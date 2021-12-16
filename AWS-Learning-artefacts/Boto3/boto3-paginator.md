### Paginator: ###

In the case of AWS **clients**, certain operations return the incomplete result, requiring subsequent requests to obtain the entire result set. The process of sending the subsequent requests to continue where a previous request left off is called pagination. 

***example:*** in the case of the IAM list_users operation, it only returns the 1st 100 objects while using the aws boto3 client, so we need to send the subsequent requests with the appropriate marker to retrieve the next page of results.

The advantage of the pagination approach is, results can be fetched more quick rather than waiting for the entire result. 

Example:
Retriving all IAM users using boto3 client

Note - for better illustration, 200 IAM users have been created using below script

```

```