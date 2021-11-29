### <b>AWS EC2</b>

<i>EC2 public and private IP</i>

- public ip accessible over internet
- private ip address are internal to corporate network
- Two public IPs can not be same
- In two different corporate network can have same private IP address
- Each EC2 instance is assigned with a private IP and public IPs are not mandatory
- Auto assignment of a public IP address to an EC2 instance can be enabled/disabled while creating the subnect/associting the subnet to the EC2
- If EC2 instance public IP is not associated as an elastic IP then the public IP address will be lost when the instance is stopped but private IP remains same.

