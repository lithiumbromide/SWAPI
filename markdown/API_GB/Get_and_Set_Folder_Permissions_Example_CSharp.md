---
title: "Get and Set Folder Permissions Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Get_and_Set_Folder_Permissions_Example_CSharp.htm"
---

# Get and Set Folder Permissions Example (C#)

This example shows how to create an application that displays a form in which a user can assign permissions to folders for users and groups in a vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
//----------------------------------------------------------------------------
 // Preconditions:
//  1. Start Microsoft Visual Studio.
//  2. Click File > New > Project > Visual Basic > Windows Forms Application.
 //  3. Type CallingCSharp in Name.
//  4. Click Browse and navigate to the folder where to create the project.
//  5. Click OK.
//  6. Create a form similar to the form shown above with the following names for the form controls:
//     a. Label1 (label control with text, "Select vault:")
//     b. comboVault (combo box control)
//     c. buttonLogIn (button with text, "Log In")
//     d. Label2 (label with text, "Users")
 //     e. buttonRefresh (button with text, "Refresh Permissions")
 //     f. listViewUsers (list view control)
 //        ColumnHeader1 (ID)
 //        ColumnHeader2 (Name)
 //        ColumnHeader3 (Folder ID)
 //        ColumnHeader7 (Folder)
 //        ColumnHeader8 (Folder Permissions)
 //     g. Label3 (label with text, "Groups")
 //     h. listViewGroups (list view control)
 //        ColumnHeader4 (ID)
 //        ColumnHeader5 (Name)
 //        ColumnHeader6 (Folder ID)
 //        ColumnHeader9 (Folder)
 //        ColumnHeader10 (Folder Permissions)
 //     i. listViewPermissions (list view control)
 //     j. checkboxReverseOrder (check box with text, "Reverse Order")
 //     k. buttonApply (button with text, "Apply Permissions")
  //  7. Replace the code in Form1.cs with this code.
 //  8. Replace the code in Form1.Designer.cs with this code.
//  9. Add  EPDM.Interop.epdm.dll as a reference (right-click the project
 //     name in the Solution Explorer, click Add Reference, click Assemblies > Framework in the
 //     left-side panel, browse to the top folder of your SOLIDWORKS PDM Professional installation,
 //     locate and click EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
 // 10. Right-click References > EPDM.Interop.epdm, click Properties, and set
 //     Embed Interop Types to False to handle methods
 //     that pass arrays of structures.
// 11. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. In the Form1 dialog, select a vault and click Log In.
 //    Wait for the application to populate the Users and Groups list boxes.
 // 2. Click permissions in the list box located left of the Reverse Order check box.
 // 3. Optionally select the Reverse Order check box.
 // 4. Select the check boxes in front of the users and folders to which to assign permissions.
 // 5. Click Apply Permissions.
 //    Wait for the application to populate the Users list.
 //    The folder permissions are updated for the selected users.
 // 6. Select the check boxes in front of the groups and folders to which to assign permissions.
 // 7. Click Apply Permissions.
 //    Wait for the application to populate the Groups list.
 //    The folder permissions are updated for the selected groups.
 //----------------------------------------------------------------------------

 // Form1.cs
 using System;
 using System.Collections.Generic;
 using System.ComponentModel;
 using System.Data;
 using System.Drawing;
 using System.Linq;
 using System.Text;
 using System.Windows.Forms;
 using EPDM.Interop.epdm;

 namespace CallingCSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         IEdmVault5 vault1;
         IEdmVault8 vault;
         private Dictionary<int, string> folders;
         String val;
         private enum MyEdmRightsFlags : int
         {
             MyRight_All = EdmRightFlags.EdmRight_All,
             MyRight_None = EdmRightFlags.EdmRight_None,
             MyRight_Read = EdmRightFlags.EdmRight_Read,
             MyRight_Lock = EdmRightFlags.EdmRight_Lock,
             MyRight_Delete = EdmRightFlags.EdmRight_Delete,
             MyRight_AddRename = EdmRightFlags.EdmRight_Add,
             MyRight_Share = EdmRightFlags.EdmRight_Share,
             MyRight_IncrementRevision = EdmRightFlags.EdmRight_IncrementRevision,
             MyRight_AddDeleteFolder = EdmRightFlags.EdmRight_AddFolder,
             MyRight_RecoverTrash = EdmRightFlags.EdmRight_RecoverTrash,
             MyRight_DestroyTrash = EdmRightFlags.EdmRight_DestroyTrash,
             MyRight_EditFolderCard = EdmRightFlags.EdmRight_EditFolderCard,
             MyRight_BomActivate = EdmRightFlags.EdmRight_BomActivate,
             MyRight_MaySeeComputedBOM = EdmRightFlags.EdmRight_MaySeeComputedBOM,
             MyRight_AssignGroupMembership = 0x1000,
             MyRightAssignFilePermissions = 0x2000,
             MyRight_PermitGroupAccess = 0x4000,
             MyRight_ReadNamedBOM = 0x8000,
             MyRight_ChangeCard = EdmRightFlags.EdmRight_ChangeCard,
             MyRight_ShowWorkingVersion = EdmRightFlags.EdmRight_ShowWorkingVersion,
             MyRight_Rollback = EdmRightFlags.EdmRight_Rollback,
             MyRight_ColdStoreRestore = EdmRightFlags.EdmRight_ColdStoreRestore,
             MyRight_EditVerFreeVarData = EdmRightFlags.EdmRight_EditVerFreeVarData
         }

         private void Form1_Load(System.Object sender, System.EventArgs e)
         {
             try
             {
                 vault1 = new EdmVault5();
                 vault = (IEdmVault8)vault1;
                 EdmViewInfo[] aViews = null;
                 vault.GetVaultViews(out aViews, false);
                 comboVault.Items.Clear();
                 if (aViews != null)
                 {
                     foreach (EdmViewInfo View in aViews)
                     {
                         comboVault.Items.Add(View.mbsVaultName);
                     }
                     comboVault.SelectedIndex = 0;
                 }

                 Dictionary<MyEdmRightsFlags, String> RightLabels = new Dictionary<MyEdmRightsFlags, String>()
             {{MyEdmRightsFlags.MyRight_Read, "Read file contents"}, {MyEdmRightsFlags.MyRight_Lock, "Check out file"}, {MyEdmRightsFlags.MyRight_Delete, "Delete file"}, {MyEdmRightsFlags.MyRight_AddRename, "Add or rename file"},{MyEdmRightsFlags.MyRight_Share, "Share file to another folder"}, {MyEdmRightsFlags.MyRight_IncrementRevision, "Increment revision of a file"}, {MyEdmRightsFlags.MyRight_AddDeleteFolder, "Add or delete a folder"}, {MyEdmRightsFlags.MyRight_RecoverTrash, "Recover files from recycle bin"}, {MyEdmRightsFlags.MyRight_DestroyTrash, "Destroy"}, {MyEdmRightsFlags.MyRight_EditFolderCard, "Edit folder card data"}, {MyEdmRightsFlags.MyRight_BomActivate, "Activate computed BOM"}, {MyEdmRightsFlags.MyRight_MaySeeComputedBOM, "See computed BOM"}, {MyEdmRightsFlags.MyRight_AssignGroupMembership, "Assign group membership"}, {MyEdmRightsFlags.MyRightAssignFilePermissions, "Assign File permissions"}, {MyEdmRightsFlags.MyRight_PermitGroupAccess, "Permit or deny group-level access to files"}, {MyEdmRightsFlags.MyRight_ReadNamedBOM, "Read named bill of materials"}, {MyEdmRightsFlags.MyRight_ChangeCard, "Can update the design of cards"}, {MyEdmRightsFlags.MyRight_ShowWorkingVersion, "Show working versions of files"}, {MyEdmRightsFlags.MyRight_Rollback, "Rollback"},{MyEdmRightsFlags.MyRight_ColdStoreRestore, "Restore file from cold storage"}, {MyEdmRightsFlags.MyRight_EditVerFreeVarData, "Edit version free variable data"}};

                 foreach (MyEdmRightsFlags flag in Enum.GetValues(typeof(MyEdmRightsFlags)))
                 {
                     if (RightLabels.ContainsKey(flag))
                     {
                         String val;
                         RightLabels.TryGetValue(flag, out val);
                         ListViewItem rightItem = listViewPermissions.Items.Add(val);
                         rightItem.Tag = flag;
                     }
                 }
             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

         private void buttonLogIn_Click(object sender, System.EventArgs e)
         {
             try {
             vault.LoginAuto(comboVault.Text, (int)this.Handle);
             comboVault.Enabled = false;
             buttonLogIn.Enabled = false;
             buttonApply.Enabled = true;
             buttonRefresh.Enabled = true;

             folders = new Dictionary<int, string>();

             IEdmFolder7 rootFolder = (IEdmFolder7)vault.RootFolder;
             BuildFolderDictionary(rootFolder);

             ShowAllUserPermissions();
             ShowAllGroupPermissions();
             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

         private void BuildFolderDictionary(IEdmFolder7 folder)
         {
             folders.Add(folder.ID, folder.LocalPath);

             IEdmPos5 posSubFolder = folder.GetFirstSubFolderPosition();
             while (!(posSubFolder.IsNull))
             {
                 IEdmFolder7 subFolder = (IEdmFolder7)folder.GetNextSubFolder(posSubFolder);
                 BuildFolderDictionary(subFolder);
             }
         }

         private void ShowAllUserPermissions()
         {
             listViewUsers.Items.Clear();
             IEdmUserMgr7 userMgr = (IEdmUserMgr7)vault;
             IEdmPos5 userPos = userMgr.GetFirstUserPosition();
             while (!(userPos.IsNull))
             {
                 IEdmUser5 user = (IEdmUser5)userMgr.GetNextUser(userPos);

                 foreach (int folderID in folders.Keys)
                 {
                     EdmFolderPermission[] aPermissions = null;
                     userMgr.GetFolderPermissions(user.ID, user.ObjectType, folderID, (int)EdmGetPermFlag.EdmGetPerm_OnlyExplicitlySet, out aPermissions);

                     if (aPermissions != null && aPermissions.Length > 0)
                     {
                         ListViewItem itemUser = listViewUsers.Items.Add(user.ID.ToString());
                         itemUser.SubItems.Add(user.Name);
                         itemUser.SubItems.Add(folderID.ToString());
                         folders.TryGetValue(folderID, out val);
                         itemUser.SubItems.Add(val);
                         EdmFolderPermission folderPermission = (EdmFolderPermission)aPermissions.GetValue(0);
                         itemUser.SubItems.Add(folderPermission.mlEdmRightFlag.ToString());
                     }
                 }
             }
         }

         private void ShowAllGroupPermissions()
         {
             listViewGroups.Items.Clear();
             IEdmUserMgr7 userMgr = (IEdmUserMgr7)vault;
             IEdmPos5 groupPos = userMgr.GetFirstUserGroupPosition();
             while (!(groupPos.IsNull))
             {
                 IEdmUserGroup5 @group = (IEdmUserGroup5)userMgr.GetNextUserGroup(groupPos);

                 foreach (int folderID in folders.Keys)
                 {
                     EdmFolderPermission[] aPermissions = null;
                     userMgr.GetFolderPermissions(@group.ID, @group.ObjectType, folderID, 0, out aPermissions);

                     if (aPermissions != null && aPermissions.Length > 0)
                     {
                         ListViewItem itemGroup = listViewGroups.Items.Add(@group.ID.ToString());
                         itemGroup.SubItems.Add(@group.Name);
                         itemGroup.SubItems.Add(folderID.ToString());
                         folders.TryGetValue(folderID, out val);
                         itemGroup.SubItems.Add(val);
                         EdmFolderPermission folderPermission = (EdmFolderPermission)aPermissions.GetValue(0);
                         itemGroup.SubItems.Add(folderPermission.mlEdmRightFlag.ToString());
                     }
                 }
             }
         }

         private void buttonApply_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 int assignedRights = 0;
                 foreach (ListViewItem rightItem in listViewPermissions.Items)
                 {
                     if (rightItem.Checked)
                     {
                         assignedRights = assignedRights | (int)rightItem.Tag;
                     }
                 }

                 IEdmUserMgr7 userMgr = (IEdmUserMgr7)vault;

                 List<EdmFolderPermission> listPermissions = new List<EdmFolderPermission>();
                 foreach (ListViewItem itemUser in listViewUsers.Items)
                 {
                     if (itemUser.Checked)
                     {
                         int folderID = Convert.ToInt32(itemUser.SubItems[2].Text);
                         EdmFolderPermission permission = default(EdmFolderPermission);
                         {
                             permission.mlFolderID = folderID;
                             permission.mlOwnerID = Convert.ToInt32(itemUser.SubItems[0].Text);
                             permission.meOwnerType = EdmObjectType.EdmObject_User;
                             permission.mlEdmRightFlag = assignedRights;
                         }
                         listPermissions.Add(permission);
                     }
                 }

                 foreach (ListViewItem itemGroup in listViewGroups.Items)
                 {
                     if (itemGroup.Checked)
                     {
                         int folderID = Convert.ToInt32(itemGroup.SubItems[2].Text);
                         EdmFolderPermission permission = default(EdmFolderPermission);
                         {
                             permission.mlFolderID = folderID;
                             permission.mlOwnerID = Convert.ToInt32(itemGroup.SubItems[0].Text);
                             permission.meOwnerType = EdmObjectType.EdmObject_UserGroup;
                             permission.mlEdmRightFlag = assignedRights;
                         }
                         listPermissions.Add(permission);
                     }
                 }

                 if (checkboxReverseOrder.Checked)
                     listPermissions.Reverse();

                 EdmFolderPermission[] permissions = listPermissions.ToArray();
                 userMgr.SetFolderPermissions(permissions);

                 ShowAllGroupPermissions();
                 ShowAllUserPermissions();
             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

         private void buttonRefresh_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 ShowAllGroupPermissions();
                 ShowAllUserPermissions();
             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

     }

 }

 // Form1.Designer.cs
  namespace CallingCSharp
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
             this.buttonLogIn = new System.Windows.Forms.Button();
             this.label2 = new System.Windows.Forms.Label();
             this.buttonRefresh = new System.Windows.Forms.Button();
             this.label3 = new System.Windows.Forms.Label();
             this.checkboxReverseOrder = new System.Windows.Forms.CheckBox();
             this.buttonApply = new System.Windows.Forms.Button();
             this.listViewUsers = new System.Windows.Forms.ListView();
             this.columnHeader1 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
             this.columnHeader2 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
             this.columnHeader3 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
             this.columnHeader7 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
             this.columnHeader8 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
             this.listViewGroups = new System.Windows.Forms.ListView();
             this.columnHeader4 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
             this.columnHeader5 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
             this.columnHeader6 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
             this.columnHeader9 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
             this.columnHeader10 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
             this.listViewPermissions = new System.Windows.Forms.ListView();
             this.comboVault = new System.Windows.Forms.ComboBox();
             this.label4 = new System.Windows.Forms.Label();
             this.SuspendLayout();
             //
             // buttonLogIn
             //
             this.buttonLogIn.Location = new System.Drawing.Point(518, 27);
             this.buttonLogIn.Name = "buttonLogIn";
             this.buttonLogIn.Size = new System.Drawing.Size(75, 23);
             this.buttonLogIn.TabIndex = 2;
             this.buttonLogIn.Text = "Log In";
             this.buttonLogIn.UseVisualStyleBackColor = true;
             this.buttonLogIn.Click += new System.EventHandler(this.buttonLogIn_Click);
             //
             // label2
             //
             this.label2.AutoSize = true;
             this.label2.Location = new System.Drawing.Point(38, 85);
             this.label2.Name = "label2";
             this.label2.Size = new System.Drawing.Size(37, 13);
             this.label2.TabIndex = 3;
             this.label2.Text = "Users";
             //
             // buttonRefresh
             //
             this.buttonRefresh.Location = new System.Drawing.Point(518, 75);
             this.buttonRefresh.Name = "buttonRefresh";
             this.buttonRefresh.Size = new System.Drawing.Size(126, 23);
             this.buttonRefresh.TabIndex = 4;
             this.buttonRefresh.Text = "Refresh Permissions";
             this.buttonRefresh.UseVisualStyleBackColor = true;
             this.buttonRefresh.Click += new System.EventHandler(this.buttonRefresh_Click);
             //
             // label3
             //
             this.label3.AutoSize = true;
             this.label3.Location = new System.Drawing.Point(38, 227);
             this.label3.Name = "label3";
             this.label3.Size = new System.Drawing.Size(44, 13);
             this.label3.TabIndex = 6;
             this.label3.Text = "Groups";
             //
             // checkboxReverseOrder
             //
             this.checkboxReverseOrder.AutoSize = true;
             this.checkboxReverseOrder.Location = new System.Drawing.Point(518, 368);
             this.checkboxReverseOrder.Name = "checkboxReverseOrder";
             this.checkboxReverseOrder.Size = new System.Drawing.Size(95, 17);
             this.checkboxReverseOrder.TabIndex = 9;
             this.checkboxReverseOrder.Text = "Reverse Order";
             this.checkboxReverseOrder.UseVisualStyleBackColor = true;
             //
             // buttonApply
             //
             this.buttonApply.Location = new System.Drawing.Point(518, 407);
             this.buttonApply.Name = "buttonApply";
             this.buttonApply.Size = new System.Drawing.Size(126, 23);
             this.buttonApply.TabIndex = 10;
             this.buttonApply.Text = "Apply Permissions";
             this.buttonApply.UseVisualStyleBackColor = true;
             this.buttonApply.Click += new System.EventHandler(buttonApply_Click);
             //
             // listViewUsers
             //
             this.listViewUsers.CheckBoxes = true;
             this.listViewUsers.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
             this.columnHeader1,
             this.columnHeader2,
             this.columnHeader3,
             this.columnHeader7,
             this.columnHeader8});
             this.listViewUsers.Location = new System.Drawing.Point(38, 112);
             this.listViewUsers.Name = "listViewUsers";
             this.listViewUsers.Size = new System.Drawing.Size(501, 97);
             this.listViewUsers.TabIndex = 11;
             this.listViewUsers.UseCompatibleStateImageBehavior = false;
             this.listViewUsers.View = System.Windows.Forms.View.Details;
             //
             // columnHeader1
             //
             this.columnHeader1.Text = "ID";
             this.columnHeader1.Width = 41;
             //
             // columnHeader2
             //
             this.columnHeader2.Text = "Name";
             this.columnHeader2.Width = 137;
             //
             // columnHeader3
             //
             this.columnHeader3.Text = "Folder ID";
             //
             // columnHeader7
             //
             this.columnHeader7.Text = "Folder";
             this.columnHeader7.Width = 152;
             //
             // columnHeader8
             //
             this.columnHeader8.Text = "Folder Permissions";
             this.columnHeader8.Width = 108;
             //
             // listViewGroups
             //
             this.listViewGroups.CheckBoxes = true;
             this.listViewGroups.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
             this.columnHeader4,
             this.columnHeader5,
             this.columnHeader6,
             this.columnHeader9,
             this.columnHeader10});
             this.listViewGroups.Location = new System.Drawing.Point(38, 257);
             this.listViewGroups.Name = "listViewGroups";
             this.listViewGroups.Size = new System.Drawing.Size(501, 97);
             this.listViewGroups.TabIndex = 12;
             this.listViewGroups.UseCompatibleStateImageBehavior = false;
             this.listViewGroups.View = System.Windows.Forms.View.Details;
             //
             // columnHeader4
             //
             this.columnHeader4.Text = "ID";
             this.columnHeader4.Width = 41;
             //
             // columnHeader5
             //
             this.columnHeader5.Text = "Name";
             this.columnHeader5.Width = 137;
             //
             // columnHeader6
             //
             this.columnHeader6.Text = "Folder ID";
             //
             // columnHeader9
             //
             this.columnHeader9.Text = "Folder";
             this.columnHeader9.Width = 152;
             //
             // columnHeader10
             //
             this.columnHeader10.Text = "Folder Permissions";
             this.columnHeader10.Width = 108;
             //
             // listViewPermissions
             //
             this.listViewPermissions.CheckBoxes = true;
             this.listViewPermissions.Location = new System.Drawing.Point(38, 383);
             this.listViewPermissions.Name = "listViewPermissions";
             this.listViewPermissions.Size = new System.Drawing.Size(431, 97);
             this.listViewPermissions.TabIndex = 13;
             this.listViewPermissions.UseCompatibleStateImageBehavior = false;
             this.listViewPermissions.View = System.Windows.Forms.View.List;
             //
             // comboVault
             //
             this.comboVault.FormattingEnabled = true;
             this.comboVault.Location = new System.Drawing.Point(108, 27);
             this.comboVault.Name = "comboVault";
             this.comboVault.Size = new System.Drawing.Size(361, 21);
             this.comboVault.TabIndex = 14;
             //
             // label4
             //
             this.label4.AutoSize = true;
             this.label4.Location = new System.Drawing.Point(38, 27);
             this.label4.Name = "label4";
             this.label4.Size = new System.Drawing.Size(66, 13);
             this.label4.TabIndex = 15;
             this.label4.Text = "Select vault:";
             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(749, 516);
             this.Controls.Add(this.label4);
             this.Controls.Add(this.comboVault);
             this.Controls.Add(this.listViewPermissions);
             this.Controls.Add(this.listViewGroups);
             this.Controls.Add(this.listViewUsers);
             this.Controls.Add(this.buttonApply);
             this.Controls.Add(this.checkboxReverseOrder);
             this.Controls.Add(this.label3);
             this.Controls.Add(this.buttonRefresh);
             this.Controls.Add(this.label2);
             this.Controls.Add(this.buttonLogIn);
             this.Name = "Form1";
             this.Text = "Folder Permissions";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         private System.Windows.Forms.Label label1;
         private System.Windows.Forms.Button buttonLogIn;
         private System.Windows.Forms.Label label2;
         private System.Windows.Forms.Button buttonRefresh;
         private System.Windows.Forms.Label label3;
         private System.Windows.Forms.CheckBox checkboxReverseOrder;
         private System.Windows.Forms.Button buttonApply;
         private System.Windows.Forms.ListView listViewUsers;
         private System.Windows.Forms.ListView listViewGroups;
         private System.Windows.Forms.ListView listViewPermissions;
         private System.Windows.Forms.ComboBox comboVault;
         public System.Windows.Forms.ColumnHeader columnHeader1;
         public System.Windows.Forms.ColumnHeader columnHeader2;
         public System.Windows.Forms.ColumnHeader columnHeader3;
         public System.Windows.Forms.ColumnHeader columnHeader7;
         public System.Windows.Forms.ColumnHeader columnHeader8;
         public System.Windows.Forms.ColumnHeader columnHeader4;
         public System.Windows.Forms.ColumnHeader columnHeader5;
         public System.Windows.Forms.ColumnHeader columnHeader6;
         public System.Windows.Forms.ColumnHeader columnHeader9;
         public System.Windows.Forms.ColumnHeader columnHeader10;
         private System.Windows.Forms.Label label4;
     }
 }
```
