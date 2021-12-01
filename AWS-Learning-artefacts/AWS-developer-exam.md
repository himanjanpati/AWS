### <b>AWS EC2</b>

<i>EC2 public and private IP</i>

- public ip accessible over internet
- private ip address are internal to corporate network
- Two public IPs can not be same
- In two different corporate network can have same private IP address
- Each EC2 instance is assigned with a private IP and public IPs are not mandatory
- Auto assignment of a public IP address to an EC2 instance can be enabled/disabled while creating the subnect/associting the subnet to the EC2
- If EC2 instance public IP is not associated as an elastic IP then the public IP address will be lost when the instance is stopped but private IP remains same.
- To attach a fix public IP to an EC2 instance elastic IP has to be created and associated
- Elastic IP can be associted to one instance at a time. Only 5 elastic IPs can be created per account
- Elastic IP creation and association is not a good architecture consideration.
- The alteranative option is to have random public IP and a DNS registered to the same (Route 53)
- Best case is to use LB (load balancer) without a public ip at all.
