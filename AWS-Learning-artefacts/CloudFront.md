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
