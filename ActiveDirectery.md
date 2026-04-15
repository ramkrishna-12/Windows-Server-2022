# Setup Active Directory on Windows Server 2022
# Active Directery 
Active Directory (AD) is a directory service developed by Microsoft for managing users, computers, and other resources in a network. Windows Server 2022 provides robust tools for deploying and managing AD.

# Installing Active Directory Domain Services (AD DS)

In the windoes server VM go to `Server Manager` --> Local Server 
on the right hand side clickon "manage" tab and "Add Roles and Features"

![manage](<images/Screenshot 2026-04-15 132208.png>)

then following will pop up

![pop](<images/Screenshot 2026-04-15 132218.png>)

click on next
Select "Role-based or feature-based installation" and next

![role](<images/Screenshot 2026-04-15 132258.png>)

select the server from server pull 
and next

![role2](<images/Screenshot 2026-04-15 132311.png>)

# AD
to install active directery we will select "Active Directery Domain Services" and "DNS Server" for active directery and name server  
when the popup shows click add feature

![roles3](<images/Screenshot 2026-04-15 132325.png>)
![role4](<images/Screenshot 2026-04-15 132333.png>)
![role5](<images/Screenshot 2026-04-15 132432.png>)

after all the features selected click on install
it might take from few seconds to minute 

![final](<images/Screenshot 2026-04-15 132510.png>)

and close it.
when finished on the top righr corner yellow notification flag pop up 

![flag](images/snap.png)

to begain AD click on it and promote AD 

![promote](<images/Screenshot 2026-04-15 135204.png>)

![set](<images/Screenshot 2026-04-15 135256.png>)