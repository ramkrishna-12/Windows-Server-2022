# Create Home Folder for AD Users (Windows Server 2022)








# 📌 Overview

This project demonstrates how to configure Home Folders for Active Directory users in Windows Server 2022, enabling:

Centralized file storage 📂
Automatic drive mapping 🔗
Secure per-user access 🔐
🧭 Architecture Overview

User Login → Active Directory → File Server → Home Folder (H:)

* Each user gets a private folder
* Folder is mapped automatically (e.g., H: drive)
*   Permissions ensure user-only access

# 🧾 Requirements

* Windows Server 2022 (Domain Controller or File Server)
* Active Directory Domain Services (AD DS)
* Domain Admin / Delegated privileges
* File server with storage (NTFS formatted)
* Basic knowledge of:
    * ADUC (Active Directory Users and Computers)

    *File sharing & permissions

# 📖 Key Concepts



| Term              | Description                                    |
| ----------------- | ---------------------------------------------- |
| Active Directory  | Directory service for managing users/resources |
| Home Folder       | Personal storage directory for a user          |
| NTFS Permissions  | File-level security permissions                |
| Share Permissions | Network-level access control                   |
| Drive Mapping     | Assigning network path to a drive letter       |


# ⚙️ Step-by-Step Configuration

🔹 Step 1: Create Shared Folder

1. Create folder (example): 


D:\HomeFolders


2. Right-click → Properties → Sharing → Advanced Sharing
3. Enable:
    ✅ Share this folder
4. Permissions:

    * Remove Everyone
    * Add Authenticated Users
    * Grant Full Control (temporary for setup)
# 🔐 Step 2: Configure NTFS Permissions

Set the following:

| Identity            | Permission                     |
| ------------------- | ------------------------------ |
| Administrators      | Full Control                   |
| SYSTEM              | Full Control                   |
| Authenticated Users | Create Folder / Append Data    |
| CREATOR OWNER       | Full Control (Subfolders only) |

⚠️ Ensures users can only access their own folders.


# 👤 Step 3: Assign Home Folder in AD
1. Open Active Directory Users and Computers
2. Select a user → Properties
3. Go to Profile Tab
4. Under Home Folder:
5. Select:
     Connect
    Drive: H:

    Path:

    \\\ServerName\HomeFolders\%username%

# 📂 Step 4: Testing
* Log in as the user
* Open This PC
* Verify:

    * ✅ H: drive exists
    * ✅ Folder auto-created
    * ✅ Access restricted
    
# ⚡Automation (PowerShell)

Bulk assign home folders:

Set-ADUser -Identity username `
-HomeDirectory "\\ServerName\HomeFolders\username" `
-HomeDrive "H:"


# 🧩 Optional: Group Policy Method


Instead of AD profile tab, you can use Group Policy (GPO):

1. Open Group Policy Management

2. Create/Edit GPO

3. Navigate:

User Configuration → Preferences → Windows Settings → Drive Maps

4. Create new mapped drive:

* Location:

\\\ServerName\HomeFolders\%username%


 * Drive Letter: H:


# 🛡️ Best Practices
   *  Use dedicated file server
   * Enable disk quotas
   * Schedule regular backups
   * Follow least privilege principle
   * Monitor access logs


# 🚨 Troubleshooting


| Issue              | Possible Cause    | Fix                  |
| ------------------ | ----------------- | -------------------- |
| Folder not created | Permissions issue | Check NTFS + Share   |
| Access denied      | Wrong ownership   | Verify CREATOR OWNER |
| Drive not mapping  | DNS / path issue  | Check server name    |

# 📊 Example Folder Structure


HomeFolders/

├── user1/

├── user2/

└── user3/

