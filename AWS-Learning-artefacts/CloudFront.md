### <b> CloudFront </b> ###

- AWS Cloud front is a CDN with 216 POP/edge locations accross globe
- can expose external https and can talk to internal https backends

- <b>cloudfront origins</b>
   - s3 bucket
     - caching static contents at the edge
     - OAI (origin access identity) allows s3 bucket to allow traffic from cloudfront and no where else
     principal block will be added with OAI ID in s3 bucket policy
     - cloudfront acts as an ingress to allow traffic from anywhere
  - Custom Origin
    - ALB
    - EC2 instance
    - s3 website
    - HTTP backend(onprem)
- Working use case
  - client makes an http request to CloudFront (edge loaction)
  - cloudfront forwards the request along with the query string and header to the origin 
  - origin responds to the edge location
  - edge location caches the static contents or conetnts based on the caching setting defined in edge locations
  - edge location responds back to client, any future request with similar request edge location will review the request before forwarding to origin
  - edge location could serve the request without sening the request to origin if all contnets are aviable in cache (example - a static document or media file )


- <b> CloudFront Caching</b>
  - caching could be used for below
    - headers (Http)
    - Query strings
    - Session cookies
  - cache lives in each edge locations
  - Use longer TTL (min 1 sec, could be 1 day to 1 year) for maximum cache hit
  - maximize hit by separating the static and dynamic distributions
  - cloudfront invalodations could is used to update the contents/cache when static file changes are made to S3 contents
- <b>CloudFront Security</b>
  - Georestriction - access based on region/countries
  - only allowing over HTTPS
    - redirect http to https or allow only https
  - Origin protocol policy
    - Htpps only and match viewer
    - S3 or https origin
  - S3 bucket webseite does not support https
- CloudFront signed URLs, signed cookie
  - signed url used for paid shared contenets/ users having the signed in URL can have access to contents via cloudfront. Access each file could be given using one signed URL
  - key group is used for signed URLs to encry
  - signed cookie - used for giving access to private content (private to user) and only one signed cookie is needed for multiple contents
- S3 presigned url is used direct acess to S3 bucket contents when user have the pre-signed URLs for s3 (valid for short time)
