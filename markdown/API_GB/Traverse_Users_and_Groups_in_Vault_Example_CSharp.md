---
title: "Traverse Users and Groups in Vault Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Traverse_Users_and_Groups_in_Vault_Example_CSharp.htm"
---

# Traverse Users and Groups in Vault Example (C#)

This example shows how to traverse the users and groups in a vault and send a message, also called a notification, to all logged-in users of the vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 //    a. Click File > New > Project > C# > Windows Forms Application.
 //    b. Type UsersAndGroupsCSharp in Name.
 //    c. Click Browse and navigate to the folder where to create the project.
 //    d. Click OK.
 //    e. Click Show All Files in the Solution Explorer toolbar and expand
 //       Form1.cs in the Solution Explorer.
 //    f. Replace the code in Form1.cs with this code.
 //    g. Replace the code in Form1.Designer.cs with this code.
 // 2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 //    name in the Solution Explorer, click Add Reference, click
 //    Assemblies > Framework in the left-side panel, browse to the top folder
 //    of your SOLIDWORKS PDM Professional installation, locate and click
 //    EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
 // 3. Right-click EPDM.Interop.epdm in References, click Properties, and set
 //    Embed Interop Types to False to handle methods that pass arrays of
 //    structures.
 // 4. Ensure that the vault contains one or more users and one or more
 //    workflows.
 // 5. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 //  1. Displays a dialog.
 //  2. Select a vault.
 //  3. Click Traverse users.
 //     Three message boxes report:
 //     * users in the vault,
 //     * state permissions for a user in the vault,
 //       - and -
 //     * transition permissions for a user in the vault.
 //  4. Click OK to close each message box.
 //  5. Click Traverse groups.
 //     A message box reports the groups in the vault.
 //  6. Click OK to close the message box.
 //  7. Click Traverse group members.
 //     A message box reports the users of each group in the vault.
 //  8. Click OK to close the message box.
 //  9. Click Send consultation request.
 //     After several minutes, a SOLIDWORKS PDM Professional notification
 //     appears only to logged-in users.
 // 10. To open the the message, click:
 //     * the notification while it is displayed,
 //     * the SOLIDWORKS PDM Professional tray icon,
 //       - or -
 //     * Tools > Inbox in the vault view.
 // 11. Close the dialog.
 //----------------------------------------------------------------------------
 //Form1.cs
 using System.IO;
 using System.Xml.Serialization;
 using EPDM.Interop.epdm;
 using System.Windows.Forms;
 using System.Runtime.InteropServices;

 namespace UsersAndGroupsCSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }

         void UsersAndGroupsCSharp_Load(System.Object sender, System.EventArgs e)
         {

             IEdmVault8 vault = (IEdmVault8)new EdmVault5();
             EdmViewInfo[] Views = { };

             vault.GetVaultViews(out Views, false);
             VaultsComboBox.Items.Clear();
             foreach (EdmViewInfo View in Views)
             {
                 VaultsComboBox.Items.Add(View.mbsVaultName);
             }
             if (VaultsComboBox.Items.Count > 0)
             {
                 VaultsComboBox.Text = (string)VaultsComboBox.Items[0];
             }
         }

         private void TraverseUsersButton_Click(System.Object sender, System.EventArgs e)

        {
                IEdmVault5 vault = new EdmVault5();
                IEdmVault7 vault1 = null;

                if (vault == null)
                {
                    vault = new EdmVault5();
                }

                vault1 = (IEdmVault7)vault;

                //Log into selected vault as the current user
                vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());

                //Declare an IEdmUserMgr9 object
                IEdmUserMgr9 UserMgr = default(IEdmUserMgr9);
                UserMgr = vault1.CreateUtility(EdmUtility.EdmUtil_UserMgr);

                EdmStatePermission[] ppoPermissions = {

    };
                EdmTransitionPermission[] ppoTransitionPermissions = {

    };

                string Users = null;
                IEdmPos5 UserPos = default(IEdmPos5);
                IEdmUser5 User = default(IEdmUser5);
                UserPos = UserMgr.GetFirstUserPosition();
                while (!UserPos.IsNull)
                {
                    User = UserMgr.GetNextUser(UserPos);
                    Users = Users + User.Name + " ID: " + User.ID + "\n";
                }

                MessageBox.Show(Users, vault1.Name + " Vault Users", MessageBoxButtons.OK, MessageBoxIcon.Information);

                //Get permissions for all states for a user
                UserMgr.GetStatePermissions(User.ID, EdmObjectType.EdmObject_User, 0, out ppoPermissions);
                string str = null;
                str = "EdmStatePermissions for a user in the vault" + "\n";
                str = str + "\n";
                foreach (EdmStatePermission item in ppoPermissions)
                {

                   str = str + "mlOwnerID: " + item.mlOwnerID + "\n";
                    str = str + "meOwnerType (EdmObjectType.EdmObject_User (7) or EdmObjectType.EdmObject_UserGroup (8)): " + item.meOwnerType + "\n";
                    str = str + "mlStateID: " + item.mlStateID + "\n";
                    str = str + "mlEdmRightFlag as defined in EdmRightFlags: " + item.mlEdmRightFlag + "\n";
                    str = str + "\n";

                }
                MessageBox.Show(str);

                //Get permissions for all transitions for a user
                UserMgr.GetTransitionPermissions(User.ID, EdmObjectType.EdmObject_User, 0, out ppoTransitionPermissions);
                str = "EdmTransitionPermissions for a user in the vault" + "\n";
                str = str + "\n";
                foreach (EdmTransitionPermission item in ppoTransitionPermissions)
                {

                    str = str + "mlOwnerID: " + item.mlOwnerID + "\n";
                    str = str + "meOwnerType (EdmObjectType.EdmObject_User (7) or EdmObjectType.EdmObject_UserGroup (8)): " + item.meOwnerType + "\n";
                    str = str + "mlTransitionID: " + item.mlTransitionID + "\n";
                    str = str + "mlEdmRightFlag as defined in EdmTransitionRightFlags: " + item.mlEdmRightFlag + "\n";
                    str = str + "\n";

                }
                MessageBox.Show(str);
         }

         private void TraverseGroupsButton_Click(System.Object sender, System.EventArgs e)
        {

            //Declare and create an instance of IEdmVault5 object
             IEdmVault5 vault = new EdmVault5();
             //Log into selected vault as the current user
            vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());

             //Declare an IEdmUserMgr5 object
             IEdmUserMgr5 UserMgr = default(IEdmUserMgr5);
             //The IEdmUserMgr5 interface is implemented by the
             //same class as the IEdmVault5 interface,
             //so assign the value of the IEdmVault5 object
            UserMgr = (IEdmUserMgr5)vault;

             string Groups = "";
             IEdmPos5 UserGroupPos = default(IEdmPos5);
            UserGroupPos = UserMgr.GetFirstUserGroupPosition();
             while (!UserGroupPos.IsNull)
            {
                IEdmUserGroup5 UserGroup = default(IEdmUserGroup5);
                UserGroup = UserMgr.GetNextUserGroup(UserGroupPos);
                Groups = Groups + UserGroup.Name + "\n";
            }
            MessageBox.Show(Groups, vault.Name + " Vault Groups", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void TraverseGroupMembersButton_Click(System.Object sender, System.EventArgs e)
        {

            //Declare and create an instance of IEdmVault5 object
             IEdmVault5 vault = new EdmVault5();
             //Log into selected vault as the current user
            vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());

             //Declare an IEdmUserMgr5 object
             IEdmUserMgr5 UserMgr = default(IEdmUserMgr5);
             //The IEdmUserMgr5 interface is implemented by the
             //same class as the IEdmVault5 interface,
             //so assign the value of the IEdmVault5 object
            UserMgr = (IEdmUserMgr5)vault;

             string Groups = "";
             IEdmPos5 UserGroupPos = default(IEdmPos5);
            UserGroupPos = UserMgr.GetFirstUserGroupPosition();
             while (!UserGroupPos.IsNull) {
                 IEdmUserGroup5 UserGroup = default(IEdmUserGroup5);
                UserGroup = UserMgr.GetNextUserGroup(UserGroupPos);
                Groups = Groups + UserGroup.Name + ":\n";
                Groups = Groups + GetMembers(UserGroup);
            }
            MessageBox.Show(Groups, vault.Name + " Vault Group and Users", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }

        private string GetMembers(IEdmUserGroup5 UserGroup)
        {
            string functionReturnValue = null;

            functionReturnValue = "";
             string Users = "";
             IEdmPos5 UserPos = default(IEdmPos5);
            UserPos = UserGroup.GetFirstUserPosition();
             while (!UserPos.IsNull)
            {
                IEdmUser5 User = default(IEdmUser5);
                User = UserGroup.GetNextUser(UserPos);
                Users = Users + " " + User.Name + "\n";
            }
            functionReturnValue = Users;
            return functionReturnValue;
        }

        private void SendConsultationRequestButton_Click(System.Object sender, System.EventArgs e)
        {

            //Declare and create an instance of IEdmVault5 object
             IEdmVault5 vault = new EdmVault5();
             //Log into selected vault as the current user
            vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());

             //Declare an IEdmUserMgr5 object
             IEdmUserMgr5 UserMgr = default(IEdmUserMgr5);
             //The IEdmUserMgr5 interface is implemented by the
             //same class as the IEdmVault5 interface,
             //so assign the value of the IEdmVault5 object
            UserMgr = (IEdmUserMgr5)vault;

             IEdmUserGroup5 UserGroup = default(IEdmUserGroup5);
            UserGroup = UserMgr.GetUserGroup("All Users");
             if ((UserGroup != null))
            {
                IEdmPos5 UserPos = default(IEdmPos5);
                UserPos = UserGroup.GetFirstUserPosition();
                 while (!UserPos.IsNull)
                {
                    IEdmUser5 User = default(IEdmUser5);
                    User = UserGroup.GetNextUser(UserPos);
                     if (User.IsLoggedIn)
                    {
                        User.SendMsg("Informal review request", "Please stop by my office sometime " + "this morning for a quick informal " + "review of my design changes before " + "I submit them for approval.");
                    }
                }
            }
        }
    }
}
```

```
Back to top
```

```
\\Form1.Designer.cs
```

```
namespace UsersAndGroupsCSharp
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
        /// <param name="disposing">True if managed resources should be disposed; otherwise, false.</param>
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
            this.VaultsLabel = new System.Windows.Forms.Label();
            this.VaultsComboBox = new System.Windows.Forms.ComboBox();
            this.TraverseUsersButton = new System.Windows.Forms.Button();
            this.TraverseGroupsButton = new System.Windows.Forms.Button();
            this.TraverseGroupMembersButton = new System.Windows.Forms.Button();
            this.SendConsultationRequestButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            //
            // VaultsLabel
            //
            this.VaultsLabel.AutoSize = true;
            this.VaultsLabel.Location = new System.Drawing.Point(26, 24);
            this.VaultsLabel.Name = "VaultsLabel";
            this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
            this.VaultsLabel.TabIndex = 0;
            this.VaultsLabel.Text = "Select vault view:";
            //
            // VaultsComboBox
            //
            this.VaultsComboBox.FormattingEnabled = true;
            this.VaultsComboBox.Location = new System.Drawing.Point(29, 51);
            this.VaultsComboBox.Name = "VaultsComboBox";
            this.VaultsComboBox.Size = new System.Drawing.Size(168, 21);
            this.VaultsComboBox.TabIndex = 1;
            //
            // TraverseUsersButton
            //
            this.TraverseUsersButton.Location = new System.Drawing.Point(29, 92);
            this.TraverseUsersButton.Name = "TraverseUsersButton";
            this.TraverseUsersButton.Size = new System.Drawing.Size(168, 36);
            this.TraverseUsersButton.TabIndex = 2;
            this.TraverseUsersButton.Text = "Traverse users";
            this.TraverseUsersButton.UseVisualStyleBackColor = true;
            this.TraverseUsersButton.Click += new System.EventHandler(this.TraverseUsersButton_Click);
            //
            // TraverseGroupsButton
            //
            this.TraverseGroupsButton.Location = new System.Drawing.Point(29, 151);
            this.TraverseGroupsButton.Name = "TraverseGroupsButton";
            this.TraverseGroupsButton.Size = new System.Drawing.Size(168, 39);
            this.TraverseGroupsButton.TabIndex = 3;
            this.TraverseGroupsButton.Text = "Traverse groups";
            this.TraverseGroupsButton.UseVisualStyleBackColor = true;
            this.TraverseGroupsButton.Click += new System.EventHandler(this.TraverseGroupsButton_Click);
            //
            // TraverseGroupMembersButton
            //
            this.TraverseGroupMembersButton.Location = new System.Drawing.Point(29, 210);
            this.TraverseGroupMembersButton.Name = "TraverseGroupMembersButton";
            this.TraverseGroupMembersButton.Size = new System.Drawing.Size(168, 41);
            this.TraverseGroupMembersButton.TabIndex = 4;
            this.TraverseGroupMembersButton.Text = "Traverse group members";
            this.TraverseGroupMembersButton.UseVisualStyleBackColor = true;
            this.TraverseGroupMembersButton.Click += new System.EventHandler(this.TraverseGroupMembersButton_Click);
            //
            // SendConsultationRequestButton
            //
            this.SendConsultationRequestButton.Location = new System.Drawing.Point(29, 279);
            this.SendConsultationRequestButton.Name = "SendConsultationRequestButton";
            this.SendConsultationRequestButton.Size = new System.Drawing.Size(168, 35);
            this.SendConsultationRequestButton.TabIndex = 5;
            this.SendConsultationRequestButton.Text = "Send consultation request";
            this.SendConsultationRequestButton.UseVisualStyleBackColor = true;
            this.SendConsultationRequestButton.Click += new System.EventHandler(this.SendConsultationRequestButton_Click);
            //
            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 342);
            this.Controls.Add(this.SendConsultationRequestButton);
            this.Controls.Add(this.TraverseGroupMembersButton);
            this.Controls.Add(this.TraverseGroupsButton);
            this.Controls.Add(this.TraverseUsersButton);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.VaultsLabel);
            this.Name = "Form1";
            this.Text = "Traverse users and groups";
            this.Load += new System.EventHandler(this.UsersAndGroupsCSharp_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label VaultsLabel;
        private System.Windows.Forms.ComboBox VaultsComboBox;
        private System.Windows.Forms.Button TraverseUsersButton;
        private System.Windows.Forms.Button TraverseGroupsButton;
        private System.Windows.Forms.Button TraverseGroupMembersButton;
        private System.Windows.Forms.Button SendConsultationRequestButton;
    }
}
```

```
Back to top
```
