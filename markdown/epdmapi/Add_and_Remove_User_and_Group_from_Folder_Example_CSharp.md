---
title: "Add and Remove User and Group from Folder Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Add_and_Remove_User_and_Group_from_Folder_Example_CSharp.htm"
---

# Add and Remove User and Group from Folder Example (C#)

This example shows how to:

- add and remove users to and from a vault.
- add a user of a group to a folder in a vault.
- remove a user of a group from a folder and from a vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//--------------------------------------------------------------------
// Preconditions:
//  1. Start Microsoft Visual Studio.
//     a. Click File > New > Project > C#, Desktop, Windows > Windows Forms Application.
//     b. Type AddRemoveUsersGroupsCSharp in Project name.
//     c. For Location, click ... and navigate to the folder where to
create the project.
//     d. Click Next.
//     e. Select Framework.
//     f. Click Create.

//     g. Click Show All Files in the Solution Explorer
toolbar and expand

//       Form1.cs in the Solution Explorer.
//     h. Replace the code in Form1.cs with this code.
//     i. To create the form, replace the code in Form1.Designer.cs with
//        this code.
//  2. Add dependencies and safely pass arrays of structures.
//  3. Ensure that the following folder and group exist in the targeted vault:
//     * Folder in the vault root named Test.
//     * Group named Management.
//  4. Click Debug > Start Debugging or press F5.
//
//Postconditions:
// 1. Displays a dialog.
// 2. Select a vault.
// 3. Perform these user actions. Click OK to close each message box.
//    a. Click Traverse users.
//       Displays a message box showing the users in the vault.
//    b. Click Add users.
//       Displays a message box informing you that rrabbit
//       and efudd were added as users to the vault.
//    c. Click Traverse users to verify that rrabbit and efudd
//       were added to the vault.
//       Displays a message box showing the users in the vault.
//    d. Click Remove user.
//       Displays a message box informing you that rrabbit was
//       removed from the vault.
//    e. Click Traverse users to verify that rrabbit was removed
//       from the vault.
//       Displays a message box showing the users in the vault.
// 4. Perform these group actions. Click OK to close each message box.
//    a. Click Traverse groups.
//       Displays a message box showing the groups in the vault.
//    b. Click Traverse group members.
//       Displays a message box showing the users in the groups
//       in the vault.
//    c. Click Add group member.
//       Displays a message box informing you that efudd
//       was added to the Management group.
//    d. Click Traverse group members to verify that
//       efudd is shown in the Management group.
//       Displays a message box showing the users in the groups
//       in the vault.
//    e. Click Add group member to folder.
//       Displays a message box informing you that efudd in
//       the Management group was added to the Test folder.
//    f. To verify the previous step:
//       1. Open a File Explorer window.
//       2. Right-click the Test folder in the selected vault
//          and click Properties to open the Test Properties
//          dialog box.
//       3. Click Group Memberships.
//       4. Click Management to verify that efudd is selected.
//       5. Click OK to close the Test Properties dialog box.
//    g. Click Remove group member and user.
//       Displays a message box informing you that efudd was
//       removed from the vault.
//    h. Click Traverse group members to verify that
//       efudd was removed from the Management group.
//       Displays a message box showing the users in the
//       groups in the vault.
//    i. Click Traverse users to verify that efudd was
//       removed as a user from the vault.
//       Displays a message box showing the users in the vault.
// 5. Close the dialog.
//    Sends two SOLIDWORKS PDM Professional messages
//    to logged-in users and group members who have
//    permission to update users and groups.
// 6. To open these messages, click:
//    * the SOLIDWORKS PDM Professional tray icon.
//     - or -
//    * Tools > Inbox in File Explorer.
//--------------------------------------------------------------------
```

```
//Form1.cs
```

```
using System;
using System.Windows.Forms;
using EPDM.Interop.epdm;

namespace AddRemoveUsersGroupsCSharp
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}
			IEdmVault8 vault;
			EdmVault5 vault1;
			EdmUserData2[] UserData = new EdmUserData2[2];
			IEdmUserMgr10 UsrMgr;
			IEdmUser9 user;
			IEdmUserGroup8 mngmtGroup;
			EdmMemberFolder[] folderMembers = new EdmMemberFolder[1];

	private void AddRemoveUsersGroupsCSharp_Load(System.Object sender, System.EventArgs e)
	{

		vault1 = new EdmVault5();
		vault = (IEdmVault8)vault1;
		EdmViewInfo[] Views = {};

		vault.GetVaultViews(out Views, false);
		VaultsComboBox.Items.Clear();
		foreach (EdmViewInfo View in Views) {
			VaultsComboBox.Items.Add(View.mbsVaultName);
		}
		if (VaultsComboBox.Items.Count > 0) {
			VaultsComboBox.Text = (string)VaultsComboBox.Items[0];
		}
	}

	private void TraverseUsersButton_Click(System.Object sender, System.EventArgs e)
	{
		try {

			if (!vault.IsLoggedIn) {
				//Log into selected vault as the current user
				vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
			}

			UsrMgr = (IEdmUserMgr10)vault;

			//Traverse users
			string Users = "";
			IEdmPos5 UserPos = default(IEdmPos5);
			UserPos = UsrMgr.GetFirstUserPosition();
			while (!UserPos.IsNull) {
				user = (IEdmUser9)UsrMgr.GetNextUser(UserPos);
				Users = Users + user.Name + "\n";
			}
			MessageBox.Show(Users, vault.Name + " Vault Users", MessageBoxButtons.OK, MessageBoxIcon.Information);

		} catch (System.Runtime.InteropServices.COMException ex) {
			MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
		} catch (Exception ex) {
			MessageBox.Show(ex.Message);

		}
	}

	private void TraverseGroupsButton_Click(System.Object sender, System.EventArgs e)
	{
		try {

			if (!vault.IsLoggedIn) {
				//Log into selected vault as the current user
				vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
			}

			UsrMgr = (IEdmUserMgr10)vault;

			//Traverse groups
			string Groups = "";
			IEdmPos5 UserGroupPos = default(IEdmPos5);
			UserGroupPos = UsrMgr.GetFirstUserGroupPosition();
			while (!UserGroupPos.IsNull) {
				mngmtGroup = (IEdmUserGroup8)UsrMgr.GetNextUserGroup(UserGroupPos);
				Groups = Groups + mngmtGroup.Name + "\n";
			}
			MessageBox.Show(Groups, vault.Name + " Vault Groups", MessageBoxButtons.OK, MessageBoxIcon.Information);

		} catch (System.Runtime.InteropServices.COMException ex) {
			MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
		} catch (Exception ex) {
			MessageBox.Show(ex.Message);

		}
	}

	private void TraverseGroupMembersButton_Click(System.Object sender, System.EventArgs e)
	{
		try {

			if (!vault.IsLoggedIn) {
				//Log into selected vault as the current user
				vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
			}

			UsrMgr = (IEdmUserMgr10)vault;

			//Traverse group members
			string Groups = "";
			IEdmPos5 UserGroupPos = default(IEdmPos5);
			UserGroupPos = UsrMgr.GetFirstUserGroupPosition();
			while (!UserGroupPos.IsNull)
			{
				mngmtGroup = (IEdmUserGroup8)UsrMgr.GetNextUserGroup(UserGroupPos);
				Groups = Groups + mngmtGroup.Name + " Members:" + "\n";
				Groups = Groups + GetMembers(mngmtGroup);
			}
			MessageBox.Show(Groups, vault.Name + " Vault Group Users", MessageBoxButtons.OK, MessageBoxIcon.Information);

		} catch (System.Runtime.InteropServices.COMException ex) {
			MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
		} catch (Exception ex) {
			MessageBox.Show(ex.Message);

		}
	}

	private string GetMembers(IEdmUserGroup8 UserGroup)
	{
		string functionReturnValue = null;
		try {

			if (!vault.IsLoggedIn) {
				//Log into selected vault as the current user
				vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
			}

			//Get group members
			functionReturnValue = "";
			string Users = "";
			IEdmPos5 UserPos = default(IEdmPos5);
			UserPos = UserGroup.GetFirstUserPosition();
			while (!UserPos.IsNull) {
				user = (IEdmUser9)UserGroup.GetNextUser(UserPos);
				Users = Users + " " + user.Name + "\n";
			}
			functionReturnValue = Users;

		} catch (System.Runtime.InteropServices.COMException ex) {
			MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
		} catch (Exception ex) {
			MessageBox.Show(ex.Message);
		}
		return functionReturnValue;

	}

	private void AddUsersButton_Click(System.Object sender, System.EventArgs e)
	{
		try {
			if (!vault.IsLoggedIn) {
				//Log into selected vault as the current user
				vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
			}

			UsrMgr = (IEdmUserMgr10)vault;

			//Add users to EdmUserData2
			UserData[0].mbsCompleteName = "Roger Rabbit";
			UserData[0].mbsEmail = "rrabbit@animatedcharacters.com";
			UserData[0].mbsInitials = "RR";
			UserData[0].mbsUserName = "rrabbit";

			UserData[1].mbsCompleteName = "Elmer J. Fudd";
			UserData[1].mbsEmail = "efudd@animatedcharacters.com";
			UserData[1].mbsInitials = "EJF";
			UserData[1].mbsUserName = "efudd";

			//Return user's interface in mpoUser
			UserData[0].mlFlags = (int)EdmUserDataFlags.Edmudf_GetInterface;
			UserData[1].mlFlags = (int)EdmUserDataFlags.Edmudf_GetInterface;

			//Add these users even if other users in the array cannot be added
			UserData[0].mlFlags += (int)EdmUserDataFlags.Edmudf_ForceAdd;
			UserData[1].mlFlags += (int)EdmUserDataFlags.Edmudf_ForceAdd;

			//Set permissions
			EdmSysPerm[] perms = new EdmSysPerm[2];
			perms[0] = EdmSysPerm.EdmSysPerm_EditReportQuery;
			perms[1] = EdmSysPerm.EdmSysPerm_MandatoryVersionComments;
			UserData[0].moSysPerms = perms;
			UserData[1].moSysPerms = perms;

			//Add the users to the vault
			UsrMgr.AddUsers3(ref UserData, (int)EdmUserType.EdmUser_PDM);

			string msg = "";
			foreach (EdmUserData2 usr in UserData) {
				if (usr.mhStatus == 0) {
					msg += "Added user " + usr.mpoUser.Name + ". ID = " + usr.mpoUser.ID.ToString() + "." + "\n";
				} else {
					IEdmVault11 vault3 = (IEdmVault11)vault;
					msg += "Error adding user " + usr.mbsUserName + ". " + vault3.GetErrorMessage(usr.mhStatus) + "\n";
				}
			}

			MessageBox.Show(msg);

		} catch (System.Runtime.InteropServices.COMException ex) {
			MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
		} catch (Exception ex) {
			MessageBox.Show(ex.Message);

		}

	}

	private void RemoveUsersButton_Click(System.Object sender, System.EventArgs e)
	{
		try {
			if (!vault.IsLoggedIn) {
				//Log into selected vault as the current user
				vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
			}

			//Remove the rrabbit from the vault
			UsrMgr = (IEdmUserMgr10)vault1.CreateUtility(EdmUtility.EdmUtil_UserMgr);
			user = (IEdmUser9)UsrMgr.GetUser("rrabbit");
			if ((user == null)) {
				MessageBox.Show("No user set to remove. Click Add users.");
				return;
			}

			int[] users = new int[1];
			users[0] = user.ID;
			UsrMgr.RemoveUsers(users);

			MessageBox.Show("User " + user.Name + " removed.");

			//Send message to all users with permission
			//to update users and groups
			IEdmPos5 UserPos = default(IEdmPos5);
			UserPos = UsrMgr.GetFirstUserPosition();
			while (!UserPos.IsNull) {
				IEdmUser9 userWithPerm = default(IEdmUser9);
				userWithPerm = (IEdmUser9)UsrMgr.GetNextUser(UserPos);
				if (userWithPerm.IsLoggedIn) {
					if (userWithPerm.HasSysRightEx(EdmSysPerm.EdmSysPerm_EditUserMgr)) {
						userWithPerm.SendMsg("ALERT: user removed", "User " + user.Name + " removed.");
					}
				}
			}

		} catch (System.Runtime.InteropServices.COMException ex) {
			MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
		} catch (Exception ex) {
			MessageBox.Show(ex.Message);

		}
	}

	private void RemoveGroupMembersButton_Click(System.Object sender, System.EventArgs e)
	{
		try {
			if (!vault.IsLoggedIn) {
				//Log into selected vault as the current user
				vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
			}

			if ((mngmtGroup == null)) {
				MessageBox.Show("No group set from which to remove group member. Click Add group member.");
				return;
			}

			//Remove user efudd from Test folder, Management group, and vault
			mngmtGroup.RemoveMembers(folderMembers);
			user = (IEdmUser9)UsrMgr.GetUser("efudd");

			if ((user == null)) {
				MessageBox.Show("No user set to remove from group. Click Add users.");
				return;
			}

			int[] users = new int[1];
			users[0] = user.ID;
			UsrMgr.RemoveUsers(users);

			MessageBox.Show("User " + user.Name + " removed from group and vault.");

		} catch (System.Runtime.InteropServices.COMException ex) {
			MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
		} catch (Exception ex) {
			MessageBox.Show(ex.Message);

		}
	}

	private void AddGroupMembersWithFoldersButton_Click(System.Object sender, System.EventArgs e)
	{
		try {
			if (!vault.IsLoggedIn) {
				//Log into selected vault as the current user
				vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
			}

			UsrMgr = (IEdmUserMgr10)vault;

			//Add efudd to Test folder
			IEdmFolder6 folder = default(IEdmFolder6);
			folder = (IEdmFolder6)vault.RootFolder.GetSubFolder("Test");

			//Get user interface for user efudd
			user = (IEdmUser9)UsrMgr.GetUser("efudd");

			if ((user == null)) {
				MessageBox.Show("No user set to add to group. Click Add users.");
				return;
			}

			//Get the group interface for Management
			mngmtGroup = (IEdmUserGroup8)UsrMgr.GetUserGroup("Management");

			//Find out if the Management user group has
			//permission to update users and groups
			if (mngmtGroup.HasSysRightEx(EdmSysPerm.EdmSysPerm_EditUserMgr)) {
				mngmtGroup.SendMsg("PERMISSIONS INFO", "Management group has permission to update groups and users.", false);
			} else {
				mngmtGroup.SendMsg("PERMISSIONS INFO", "Management group does not have permission to update groups and users.", false);
				return;
			}

			//Add efudd as member of Management for Test folder
			EdmMemberFolder[] folderMembers = new EdmMemberFolder[1];
			folderMembers[0].mlFolderID = folder.ID;
			folderMembers[0].mlUserID = user.ID;
			mngmtGroup.AddMembersWithFolders(folderMembers);

			//Verify that efudd in Management group was added to
			//Test folder
			object[] groups = null;
			IEdmUserGroup8 groupName = null;
			groups = user.GetGroupMembershipsInFolder(folder.ID);
			int i = 0;
			i = groups.GetUpperBound(0);
			int j = 0;

			groupName = (IEdmUserGroup8)groups[i];

			IEdmPos5 UserGroupPos = default(IEdmPos5);
			UserGroupPos = UsrMgr.GetFirstUserGroupPosition();
			while (!UserGroupPos.IsNull) {
				mngmtGroup = (IEdmUserGroup8)UsrMgr.GetNextUserGroup(UserGroupPos);
				if ((mngmtGroup.Name == groupName.Name))
				{
					if (j <= i)
					{
						MessageBox.Show("User " + user.Name + " in the " + mngmtGroup.Name + " group was added to the " + folder.Name + " folder.");
						j = j + 1;
					}
				}
			}

		} catch (System.Runtime.InteropServices.COMException ex) {
			MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
		} catch (Exception ex) {
			MessageBox.Show(ex.Message);

		}
	}

	private void AddGroupMembersButton_Click(System.Object sender, System.EventArgs e)
	{
		try {
			if (!vault.IsLoggedIn) {
				//Log into selected vault as the current user
				vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
			}

			UsrMgr = (IEdmUserMgr10)vault;

			//Add efudd to Management group
			mngmtGroup = (IEdmUserGroup8)UsrMgr.GetUserGroup("Management");

			if ((mngmtGroup == null)) {
				MessageBox.Show("Management group does not exist. Create a Management group.");
				return;
			}

			user = (IEdmUser9)UsrMgr.GetUser("efudd");

			if ((user == null)) {
				MessageBox.Show("No user set to add to group. Click Add users.");
				return;
			}

			int[] groupMbrIDs = new int[1];
			groupMbrIDs[0] = user.ID;
			mngmtGroup.AddMembers(groupMbrIDs);

			MessageBox.Show("User " + user.Name + " added to " + mngmtGroup.Name + " group.");

		} catch (System.Runtime.InteropServices.COMException ex) {
			MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
		} catch (Exception ex) {
			MessageBox.Show(ex.Message);

		}
	}

     }
}
```

```
Back to top
```

//Form1.Designer.cs

```
namespace AddRemoveUsersGroupsCSharp
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
		        this.VaultsComboBox = new System.Windows.Forms.ComboBox();
		        this.VaultsLabel = new System.Windows.Forms.Label();
		        this.TraverseUsersButton = new System.Windows.Forms.Button();
		        this.TraverseGroupsButton = new System.Windows.Forms.Button();
		        this.TraverseGroupMembersButton = new System.Windows.Forms.Button();
		        this.AddUsersButton = new System.Windows.Forms.Button();
		        this.RemoveUsersButton = new System.Windows.Forms.Button();
		        this.AddGroupMembersButton = new System.Windows.Forms.Button();
		        this.RemoveGroupMembersButton = new System.Windows.Forms.Button();
		        this.UserActionLabel = new System.Windows.Forms.Label();
		        this.GroupActionLabel = new System.Windows.Forms.Label();
		        this.AddGroupMembersWithFoldersButton = new System.Windows.Forms.Button();
		        this.SuspendLayout();
		        //
		        //VaultsComboBox
		        //
		        this.VaultsComboBox.FormattingEnabled = true;
		        this.VaultsComboBox.Location = new System.Drawing.Point(121, 11);
		        this.VaultsComboBox.Margin = new System.Windows.Forms.Padding(2);
		        this.VaultsComboBox.Name = "VaultsComboBox";
		        this.VaultsComboBox.Size = new System.Drawing.Size(176, 21);
		        this.VaultsComboBox.TabIndex = 10;
		        //
		        //VaultsLabel
		        //
		        this.VaultsLabel.AutoSize = true;
		        this.VaultsLabel.Location = new System.Drawing.Point(12, 9);
		        this.VaultsLabel.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
		        this.VaultsLabel.Name = "VaultsLabel";
		        this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
		        this.VaultsLabel.TabIndex = 11;
		        this.VaultsLabel.Text = "Select vault view:";
		        //
		        //TraverseUsersButton
		        //
		        this.TraverseUsersButton.Location = new System.Drawing.Point(124, 59);
		        this.TraverseUsersButton.Margin = new System.Windows.Forms.Padding(2);
		        this.TraverseUsersButton.Name = "TraverseUsersButton";
		        this.TraverseUsersButton.Size = new System.Drawing.Size(173, 25);
		        this.TraverseUsersButton.TabIndex = 15;
		        this.TraverseUsersButton.Text = "Traverse users";
		        this.TraverseUsersButton.UseVisualStyleBackColor = true;
                	        this.TraverseUsersButton.Click += new System.EventHandler(TraverseUsersButton_Click);
		        //
		        //TraverseGroupsButton
		        //
		        this.TraverseGroupsButton.Location = new System.Drawing.Point(121, 166);
		        this.TraverseGroupsButton.Margin = new System.Windows.Forms.Padding(2);
		        this.TraverseGroupsButton.Name = "TraverseGroupsButton";
		        this.TraverseGroupsButton.Size = new System.Drawing.Size(176, 25);
		        this.TraverseGroupsButton.TabIndex = 16;
		        this.TraverseGroupsButton.Text = "Traverse groups";
		        this.TraverseGroupsButton.UseVisualStyleBackColor = true;
                	        this.TraverseGroupsButton.Click += new System.EventHandler(TraverseGroupsButton_Click);
		        //
		        //TraverseGroupMembersButton
		        //
		        this.TraverseGroupMembersButton.Location = new System.Drawing.Point(121, 197);
		        this.TraverseGroupMembersButton.Margin = new System.Windows.Forms.Padding(2);
		        this.TraverseGroupMembersButton.Name = "TraverseGroupMembersButton";
		        this.TraverseGroupMembersButton.Size = new System.Drawing.Size(176, 27);
		        this.TraverseGroupMembersButton.TabIndex = 17;
		        this.TraverseGroupMembersButton.Text = "Traverse group members";
		        this.TraverseGroupMembersButton.UseVisualStyleBackColor = true;
                	        this.TraverseGroupMembersButton.Click += new System.EventHandler(TraverseGroupMembersButton_Click);
		        //
		        //AddUsersButton
		        //
		        this.AddUsersButton.Location = new System.Drawing.Point(124, 89);
		        this.AddUsersButton.Name = "AddUsersButton";
		        this.AddUsersButton.Size = new System.Drawing.Size(173, 23);
		        this.AddUsersButton.TabIndex = 18;
		        this.AddUsersButton.Text = "Add users";
		        this.AddUsersButton.UseVisualStyleBackColor = true;
                	        this.AddUsersButton.Click += new System.EventHandler(AddUsersButton_Click);
		        //
		        //RemoveUsersButton
		        //
		        this.RemoveUsersButton.Location = new System.Drawing.Point(124, 118);
		        this.RemoveUsersButton.Name = "RemoveUsersButton";
		        this.RemoveUsersButton.Size = new System.Drawing.Size(173, 24);
		        this.RemoveUsersButton.TabIndex = 19;
		        this.RemoveUsersButton.Text = "Remove user";
		        this.RemoveUsersButton.UseVisualStyleBackColor = true;
                	        this.RemoveUsersButton.Click += new System.EventHandler(RemoveUsersButton_Click);
		        //
		        //AddGroupMembersButton
		        //
		        this.AddGroupMembersButton.Location = new System.Drawing.Point(121, 229);
		        this.AddGroupMembersButton.Name = "AddGroupMembersButton";
		        this.AddGroupMembersButton.Size = new System.Drawing.Size(176, 23);
		        this.AddGroupMembersButton.TabIndex = 20;
		        this.AddGroupMembersButton.Text = "Add group member";
		        this.AddGroupMembersButton.UseVisualStyleBackColor = true;
                	        this.AddGroupMembersButton.Click += new System.EventHandler(AddGroupMembersButton_Click);
		        //
		        //RemoveGroupMembersButton
		        //
		        this.RemoveGroupMembersButton.Location = new System.Drawing.Point(121, 287);
		        this.RemoveGroupMembersButton.Name = "RemoveGroupMembersButton";
		        this.RemoveGroupMembersButton.Size = new System.Drawing.Size(176, 25);
		        this.RemoveGroupMembersButton.TabIndex = 21;
		        this.RemoveGroupMembersButton.Text = "Remove group member and user";
		        this.RemoveGroupMembersButton.UseVisualStyleBackColor = true;
                	        this.RemoveGroupMembersButton.Click += new System.EventHandler(RemoveGroupMembersButton_Click);
		        //
		        //UserActionLabel
		        //
		        this.UserActionLabel.AutoSize = true;
		        this.UserActionLabel.Location = new System.Drawing.Point(12, 59);
		        this.UserActionLabel.Name = "UserActionLabel";
		        this.UserActionLabel.Size = new System.Drawing.Size(69, 13);
		        this.UserActionLabel.TabIndex = 22;
		        this.UserActionLabel.Text = "User actions:";
		        //
		        //GroupActionLabel
		        //
		        this.GroupActionLabel.AutoSize = true;
		        this.GroupActionLabel.Location = new System.Drawing.Point(12, 166);
		        this.GroupActionLabel.Name = "GroupActionLabel";
		        this.GroupActionLabel.Size = new System.Drawing.Size(76, 13);
		        this.GroupActionLabel.TabIndex = 23;
		        this.GroupActionLabel.Text = "Group actions:";
		        //
		        //AddGroupMembersWithFoldersButton
		        //
		        this.AddGroupMembersWithFoldersButton.Location = new System.Drawing.Point(121, 258);
		        this.AddGroupMembersWithFoldersButton.Name = "AddGroupMembersWithFoldersButton";
		        this.AddGroupMembersWithFoldersButton.Size = new System.Drawing.Size(176, 23);
		        this.AddGroupMembersWithFoldersButton.TabIndex = 24;
		        this.AddGroupMembersWithFoldersButton.Text = "Add group member to folder";
		        this.AddGroupMembersWithFoldersButton.UseVisualStyleBackColor = true;
                	        this.AddGroupMembersWithFoldersButton.Click += new System.EventHandler(AddGroupMembersWithFoldersButton_Click);
		        //
		        //Form1
		        //
		        this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
		        this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
		        this.ClientSize = new System.Drawing.Size(333, 329);
		        this.Controls.Add(this.AddGroupMembersWithFoldersButton);
		        this.Controls.Add(this.GroupActionLabel);
		        this.Controls.Add(this.UserActionLabel);
		        this.Controls.Add(this.RemoveGroupMembersButton);
		        this.Controls.Add(this.AddGroupMembersButton);
		        this.Controls.Add(this.RemoveUsersButton);
		        this.Controls.Add(this.AddUsersButton);
		        this.Controls.Add(this.TraverseGroupMembersButton);
		        this.Controls.Add(this.TraverseGroupsButton);
		        this.Controls.Add(this.TraverseUsersButton);
		        this.Controls.Add(this.VaultsComboBox);
		        this.Controls.Add(this.VaultsLabel);
		        this.Margin = new System.Windows.Forms.Padding(2);
		        this.Name = "Form1";
                	        this.Load += new System.EventHandler(AddRemoveUsersGroupsCSharp_Load);
		        this.Text = "Add and remove users and groups";
		        this.ResumeLayout(false);
		        this.PerformLayout();

	        }

            #endregion

	        internal System.Windows.Forms.ComboBox VaultsComboBox;
	        internal System.Windows.Forms.Label VaultsLabel;
	        internal System.Windows.Forms.Button TraverseUsersButton;
	        internal System.Windows.Forms.Button TraverseGroupsButton;
	        internal System.Windows.Forms.Button TraverseGroupMembersButton;
	        internal System.Windows.Forms.Button AddUsersButton;
	        internal System.Windows.Forms.Button RemoveUsersButton;
	        internal System.Windows.Forms.Button AddGroupMembersButton;
	        internal System.Windows.Forms.Button RemoveGroupMembersButton;
	        internal System.Windows.Forms.Label UserActionLabel;
	        internal System.Windows.Forms.Label GroupActionLabel;
	        internal System.Windows.Forms.Button AddGroupMembersWithFoldersButton;

        }

}
```

[Back to top](#Top)
