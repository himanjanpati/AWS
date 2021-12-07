###


### <b> AWS IAM </b>


<i>AWS IAM best practice for EC2</i>
- We can create an IAM role for an EC2 instance and attach the role to EC2
- The aws configure way of adding the IAM credentials should not be followed while accessing AWS services from EC2, other policies could be added to same EC2 role and can be assigned to EC2 instance.







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

 Spot instnaces and Spot fleet
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
  - For a one time spot instance request the instances will be launched as soon as the request will be fullfilled and the spot request will go away a it is one time
  - For persistent spot instance request the request will remain valid until time. The instances will get relaunched if we will not cancel the spot request itself. 
  - So the best prictice to spot the presistnet spot instances is to cancel the spot request 1st and then to terminate the instances
  