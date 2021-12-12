###


### <b> AWS IAM </b>


<i>AWS IAM best practice for EC2</i>
- We can create an IAM role for an EC2 instance and attach the role to EC2
- The aws configure way of adding the IAM credentials should not be followed while accessing AWS services from EC2, other policies could be added to same EC2 role and can be assigned to EC2 instance.







### <b>AWS EC2</b>

**developer exam essentials**</br>
<i>EC2 fundamentals</i>
- EC2: Elastic compute cloud(IAAS AWS)
- Provides the below aws workload integration
    - Renting VMs
    - Storing data in virtual drives (EBS)
    - distributing load accross machines (ELB)
    - Scale services (ASG)

**user data**
- Custom script can be run before provisioning EC2 instances using **User data ** script which is called bootsraping and that will be run using root user privilege
- bootstraping - running commands while the instance starts
- The script will be run once while instance starts first
- what we can do with user data script
   - installing updates
   - installing softwares
   - downloading common files from internet
   - ex: installing apache server and hosting a custom html page to show

   ```
   #!/bin/bash
   #install httpd
   yum update
   yum install -y httpd
   systemctl start httpd
   systemctl enable httpd
   echo "<h1> Hello From EC2 </h1>" > /var/www/html/index.html
   ````
**EC2 instance types**
- Types of EC2 instances
   - genral purpose
   - compute optimised: C series instances(c4.large, c5.large etc) high perfomance computing, high CPU then memory ex: Scientific modeling, ML, Batch processing workloads
   - storage optimised: (D2, D3 instances) high storage i/o operations, High frequency online transaction processing (OLTP) systems, Distributed file systems
   - memory optimised: R (R6g, R6gd etc.) and X (X1, X1e etc)(instance family(high memory cache operations, in memory operatiosn ex: redis cache), High-performance databases (relational and NoSQL)
   - GPU optimised (graphices processing workloads ex: media services)
- t2micro (free tier), t2.xlarge, c5d.4xlarge, r5.16xlarge, m5.8xlarge</br>
  t - instance family</br>
  2 - generation (AWS changes based on new h/w upgrade improvements in each generation)</br>
  micro - size (nano< micro< small< medium< large< xlrage)</br>
  as size increses the compute(CPU, GPU), memory capability increases
- To create an EC2 instance in a particular AZ, a subnet has to created in the AZ and the EC2 instance has to be placed in that subnet
- **EC2 metadata and dynamic data**
  EC2 instance metadata can be accessed using below
  ex - to show AMI ID, IAM, hostname, mac, local-ipv4, instance type and etc.
  ```
   curl http://169.254.169.254/latest/meta-data
  ```
  EC2 instance idenity details :
  ```
   curl http://169.254.169.254/latest/dynamic/instance-identity/document
  ```
- **EC2 security groups**</br>
  - acts as virtual firewall to control incoming and outgoing traffic to/from AWS resources (EC2 instances, DBs etc.)
  - security groups are default deny, if no rules configured then no inbound/outbound traffic will be allowed
  - only allowed traffic can be sepecified, everything else will be denied
  - separate rules can be configured for inbound and outbound traffic
  - Upto 5 SGs can be attched to an EC2 instance
  - SGs are stateful: if a outbound request is allowed then incoming request will be allowed and vice versa
  - SGs are lock down to a region/VPC combination (confined to one region and VPC in that region)
  
- AWS elastic IPs are a quick and dirty way of attaching a constant IP/ static IP to an EC2 instance
- elastic IPs should be released if not attached to any EC2 instance else AWS will charge for allocated elsatic IPs







**Solution Architect**</br>
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

- Three types of EC2 instance purchase options; On-demand, Reserved, Spot and dedicated host</br>
<b>On-demand</b>:
    - pay for what you use
    - Windows and Linux machine - billed per sec after the 1st min 
    - all other machine types/os - billing per hour
    - high cost, no upfront 
    - No long term commitment
    - </b> recommended for short-term, un-interrupted and unpredictable workloads</b>

- <b>Reserved</b> (min 1 year)
  
    - <b>Reserved instances</b> : long runnig/stable workloads (ex- DB)
    - 75% discount compared to other pricing plans
  Reserve a specific instance type (ex: t2micro, c5xlarge etc)
    - used for steady state used applications (ex: self manged k8s cluster using EC2 instance, database)
    - <b>Convertible reserved instances</b>
        - long workloads with flexible instances (can change the EC2 instance type t2micro - large etc.)
        - upto 54% discount
    - Scheduled reserved instances (deprecated): we can schedule based on need (ex- every thu between 3-6PM)

- <b>Spot Instances</b>
    - short workloads, can be taken by AWS any time based on demand (if max price is less than the current price) cheap pricing (less reliable)
    - upto 90% discount
    - most cost-efficient
    - useful for workloads resilient to failure (ex: batch jobs, image processing, distributed workloads)
- <b>dedcicated host</b> 
    - book the entire physical server and control over instance placement
    - compliance requirement and existing server bound license
    - More expensive
    - At least 3 yrs reservation
    - useful for org having strong regulatory and compliance need
- <b> Dedicated instance</b>
    - instance running on dedicated h/w
    - may share h/w with other instnace in same account
    - no control over placement

 ### <b><u>Spot instnaces and Spot fleet</u></b>
  - define max spot price, get instance when current price < max price
  - when current price > max price, we can choose either to stop/terminate the instance within 2mins grace period
  - <b>Spot block</b>: block spot during a specified time frame (1-6hr) without interruptions (wont be avilable post july 2021, wont be supported post 2022)
 
 <b> Request and terminate Spot instances </b>
  
    Spot instance req
    - Max price
    - Desired nos of instances
    - Launch spec
    - Request type: one time | Persistent valid from, valid until

  - two types of request for spot instances : <b>One time and persistent request</b>
  - For a one time spot instance request the instances will be launched as soon as the request will be fullfilled and the spot request will go away after the instances are launched.
  - For persistent spot instance request the request will remain valid even after the instances are launched (valid unitl). The instances will get relaunched if we will not cancel the spot request itself. 
  - So the best prictice to stop the presistnet spot instances is to cancel the spot request 1st and then to terminate the instances
  - we can only cancel spot requests with status open, active or disabled

 ### <u>Spot Fleets</u>
 - set of spot instances + (optional) On demand instances
 - try to meet target capacity with optimal pricing




 
  