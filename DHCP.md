# DHCP Server Role 
A DHCP (Dynamic Host Configuration Protocol) server is a network service that automatically assigns IP addresses and other network configuration parameters to devices on a network. This eliminates the need for manual IP configuration, making network management more efficient and less error-prone.

When a device (DHCP client) connects to the network, it sends a DHCP Discover broadcast. The DHCP server responds with an Offer containing an available IP address, subnet mask, default gateway, and DNS server details. The client accepts the offer with a Request, and the server finalizes the process with an Acknowledgement.

# Key functions include:

1. Dynamic IP allocation: Assigns IP addresses for a set lease time, reclaiming them when devices disconnect.

2. Automatic configuration: Provides subnet mask, gateway, and DNS settings without user intervention.

3. Centralized management: Allows administrators to control IP assignments from a single point.

4. Error reduction: Minimizes misconfigurations common with manual IP assignment.



Code example – Check  [dhcp.py](dhcp.py)

# Important note:
 DHCP is not used for resolving domain names (that’s DNS), manually assigning static IPs, or acting as a firewall. Its primary role is dynamic IP address allocation.

 # installation of DHCP
 to install DHCP go to server manager and click on manger 

--> ADD Role and Ferature

 --> Role based install
         
 --> select the server

Server Manager dashboard displaying the Add Roles and Features Wizard interface. Left navigation pane lists options including Dashboard, Local Server, All Servers, AD DS, DNS, and File and Storage Services. The wizard window shows installation progress and configuration steps in a professional Windows administrative interface.
 ![selcet](<images/Screenshot 2026-04-15 132208.png>)

 Add Roles and Features Wizard server selection screen with a list of available servers. Users must select the target server for DHCP installation from this interface, which displays server names and their availability status in a formal administrative configuration environment.

 ![lst](<images/Screenshot 2026-04-16 124527.png>)

 after selecting click next 
 selcct the DHCP Server a pop will show and click on Add featurtes

 Server Roles selection screen with DHCP Server option highlighted and a popup dialog displaying Add Features required for DHCP Server installation including Remote Server Administration Tools and Role Administration Tools

 ![tools](<images/Screenshot 2026-04-16 124757.png>)

 click on next and install...
 it may take few miutes to install

 Confirmation page of Add Roles and Features Wizard displaying DHCP Server with associated tools ready to install, showing Install button at bottom right and optional features notice

 ![conf](<images/Screenshot 2026-04-16 125109.png>)



 # DHCP Post Configuration

 DHCP installation progress page displaying confirmation message stating Configuration required and Installation succeeded on RAM-DEMO-SERVER02.google.com. The DHCP Server section shows action items: Launch the DHCP post-install wizard and Complete DHCP configuration. Below are sections for Remote Server Administration Tools, Role Administration Tools, and DHCP Server Tools. The Results tab is highlighted on the left navigation panel of the wizard.

 ![DHCP installation progress page displaying confirmation message stating Configuration required and Installation succeeded on RAM-DEMO-SERVER02.google.com. The DHCP Server section shows action items: Launch the DHCP post-install wizard and Complete DHCP configuration. Below are sections for Remote Server Administration Tools, Role Administration Tools, and DHCP Server Tools. The Results tab is highlighted on the left navigation panel of the wizard.](<images/Screenshot 2026-04-16 125823.png>)

 in this we are log in admin so no need to change anything click on "commit
 " button and done 
 ![commit](<images/Screenshot 2026-04-16 130335.png>)