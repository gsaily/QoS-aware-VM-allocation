# QoS-aware-VM-allocation
Priority queuing and scheduling of VMs for QoS on OpenStack

# Objective and Description
Cloud computing has been typically characterized by growing demands for scalability, fault tolerance and cost-effectiveness, which has lead researches to extensively research the area of virtualization. The different VMs that handle the cloud’s workflow have to be allocated in such a manner that takes into consideration QoS requirements of the users.

This project has been developed over the OpenStack infrastructure and tests different VM allocation policies for the purpose of establishing certain QoS assurance.

# Project Goals
1. Configure DevStack
2. Launch VM instances
3. VM Allocation

# Installation Guide
1. Use vagrant and ubuntu to build a VM

2. Set the host IP address to 171.168.33.10 to log in to DevStack web console

3. Forward port 80 to 8080

4. Clone devstack from  https://git.openstack.org/openstackdev/devstack

5. Run stack.sh. This installs and configures the required Nova, Glance, Swift, Neutron components.

6. DevStack can be configured by the local.conf file. Note : The “local.conf” file must be in devstack directory before you run stack.sh

7. Source DevStack by  $ source ~/devstack/openrc

8. Create RSA key by $cd ~/.ssh and $ssh-keygen -t rsa and $nova keypair-add --pub-key id_rsa.pub devkey 

9. Switch to horizon web console and go to 171.168.33.10
 
# Network Configuration
1. Create a new security group from Access & Security

2. Go to Manage rules and rules for Ingress and Egress ports for ICMP and TCP traffic

3. Go to Access & Security and Floating Tabs and allocate IP to project

4. Get ubuntu image with wget and store it in the OpenStack directory

5. From the Wen Console, create image with the image file downloaded in step 4 above

6. Create / select a flavor for the cloud instance

7. Launch the VM instance

8. Create and launch as many instances as required

# Open vSwitch
I used Open vSwitch to connect between the VMs on Open Virtual Network. 

1. Get the Open vSwitch

2. From the vSphere, select the host or server that hosts the VMs

3. Create a new vSwitch and configure it's network settings to set the VLAN ID to "All"

# VM allocation policy
Part I - I implemented three priority queues for a low priority, medium priority and high priority, respectively. Then I added the VMs to their relevant priority queues, after passing them through a classifier that identified the critically of the requests sent to users. Then I sent the VMs to a scheduler which then scheduled the VMs for execution according to the priority class they belonged to. The VM with the highest is scheduled first and the VM with the lowest priority is scheduled last.

Part II- The applications that users request, are classified by a classifier and assigned to priority queues. A scheduler then allocates resources to the VMs according to whether they have a low priority, high priority or medium priority traffic. The VMs with highest priority are given more resources and run first. The VMs with least priority run the last.

However, this approach will eventually lead to the high priority VMs consuming more resources and running for longer time, which will lead to a lower QoS for user applications running on VMs with lower priority. In order to avoid this problem, I had the VMs run in a variation of their priority order. This could be decided and configured by the users or the vendors, according to their requirements. Ex. Variation 1 could be highest priority, medium priority, lowest priority; variation 2 could be lowest priority, medium priority, high priority; variation 3 could be medium priority, lowest priority, highest priority.

# Steps for Creating my own Scheduler 
Nova responsible for handling mapping of VMs to hosts, scheduling the VM instances and applying filters. 

For the purpose of creating my own scheduler I inherited from the class "nova.scheduler.driver.Scheduler." 

1. Change directory to nova

2. Create and edit the new scheduler

3. Open the /etc/nova/nova.conf. Edit scheduler_driver variable to nova.scheduler.myScheduler

4. Restart nova scheduler

# References
[1] Chiwook Jeong, Taejin Ha, JongWon Kim et al., “Quality-of-Service Aware Resource Allocation for Virtual Machines”, IEEE International Conference  on Information Networking (ICOIN),  2017,  pp. 191-193.

[2] Chiwook Jeong, Taejin Ha, JongWon Kim et al., “Quality-of-Service Aware Resource Allocation for Virtual Machines”, IEEE International Conference  on Information Networking (ICOIN),  2017,  pp. 191-193.

[3] https://docs.openstack.org/mitaka/networking-guide/config-qos.html

[4] http://docs.openstack.org/developer/devstack/

[5] http://docs.openstack.org/developer/devstack/configuration.html
