---
title: "Vault Utilities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Vault_Utilities_Example_CSharp.htm"
---

# Vault Utilities Example (C#)

This example shows how to:

- Verify installed SOLIDWORKS PDM Professional version is at least 5.3.
- Get installed SOLIDWORKS PDM Professional licenses.
- Add a group.
- Remove a group.
- Add a user.
- Remove a user.
- Copy a file.
- Delete a file.
- Get check-out permission for a file.
- Delete a folder.
- Restore deleted items to the vault view.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 // 2. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
 // 3. Type VaultUtilities_CSharp in Project name.
  // 4. For Location, click ... and navigate to the folder where to create the project.
 // 5. Click Next.
 // 6. Select Framework.
 // 7. Click Create.
 // 8. Click Show All Files in the Solution Explorer toolbar and expand
 //    Form1.cs in the Solution Explorer.
 // 9.  Add dependencies and safely pass arrays of structures.
 //10. Replace the code in Form1.cs with this code.
 //11. To create the form, replace the code in Form1.Designer.cs with this code.
 //12. Ensure that an empty folder exists in the vault.
 //13. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Vault utilities dialog box.
 //    a. Select a vault view.
 //    b. Click Verify SOLIDWORKS PDM Professional 5.3.
 //       1. Displays message about the installed version.
 //       2. Click OK.
 //    c. Click Get SOLIDWORKS PDM Professional licenses.
 //       1. Displays a message with the installed licenses.
 //       2. Click OK.
 //    d. Click Add group.
 //       1. Displays a message that group, My Group, is created.
 //       2. Click OK.
 //    e. Click Add user.
 //       1. Displays a message that user, Temp, is created.
 //       2. Click OK.
 //    f. Click Remove group.
 //       1. Displays a message with the removal status.
 //       2. Click OK.
 //    g. Click Remove user.
 //       1. Displays a message with the removal status.
 //       2. Click OK.
 //    h. Click Copy file.
 //       1. In the Open dialog, click a vault file.
 //       2. Click Open.
 //       3. In the Select Folder dialog, click a folder to which to copy
 //          the selected file.
 //       4. Click OK.
 //       5. Displays a message with the file copy status.
 //       6. Click OK.
 //    i. Click Delete file.
 //       1. In the Select Files to Delete dialog box, click a vault file
 //          to delete.
 //       2. Click Open.
 //       3. Displays a message with the file deletion status.
 //       4. Click OK.
 //    j. Click Check-out permission.
 //       1. In the Open dialog, click a file for which to get the check-out
 //          permission.
 //       2. Click Open.
 //       3. Displays a message with the user's permission.
 //       4. Click OK.
 //    k. Click Delete folder.
 //       1. In the Select Folder dialog, click an empty vault folder to delete.
 //       2. Click OK.
 //       3. Displays a message with the status of the folder deletion.
 //       4. Click OK.
 //    l. Click Restore deleted items.
 //       1. In the Select Folder dialog, click the folder from which you deleted
 //          a file in step 1i.
 //       2. Click OK.
 //       3. Displays a message with the status of the folder restoration.
 //       4. Click OK.
 // 2. Close the Vault utilities dialog box.
  //----------------------------------------------------------------------------

 //Form1.cs

 using System;
 using System.Collections.Generic;
 using System.ComponentModel;
 using System.Data;
 using System.Drawing;
 using System.Linq;
 using System.Text;
 using System.Windows.Forms;
 using EPDM.Interop.epdm;

 namespace VaultUtilities_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         private IEdmVault5 vault1 = null;

         public void Form1_Load(System.Object sender, System.EventArgs e)
         {
             try
             {
                 IEdmVault5 vault1 = new EdmVault5();
                 IEdmVault8 vault = (IEdmVault8)vault1;
                 EdmViewInfo[] Views = null;

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
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

         private void Button5_Click(System.Object sender, System.EventArgs e)
         {
             //Verify SOLIDWORKS PDM Professional version is 5.3 or higher
             try
             {
                 IEdmVault7 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault7)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 vault2.VerifyVersion(5, 3);

                 MessageBox.Show("SOLIDWORKS PDM Professional version is at least 5.3");

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

         private void Button6_Click(System.Object sender, System.EventArgs e)
         {
             //Get licenses
             try
             {
                 IEdmVault11 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault11)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 string msg = null;
                 msg = "Installed licenses:" + "\n";
                 EdmLicense[] lics = null;
                 lics = null;
                 vault2.GetLicense(out lics);
                 int idx = 0;
                 idx = Information.LBound(lics);
                 while ((idx <= Information.UBound(lics)))
                 {
                     msg = msg + "Type=";
                     switch (lics[idx].meType)
                     {
                         case EdmLicenseType.EdmLic_Editor:
                             msg = msg + "Editor";
                             break;
                         case EdmLicenseType.EdmLic_Contributor:
                             msg = msg + "Contributor";
                             break;
                         case EdmLicenseType.EdmLic_Viewer:
                             msg = msg + "Viewer";
                             break;
                         case EdmLicenseType.EdmLic_Processor:
                             msg = msg + "Processor";
                             break;
                         default:
                             msg = msg + Convert.ToString(lics[idx].meType);
                             break;
                     }

                     msg = msg + " Users=" + Convert.ToString(lics[idx].mlUserCount) + "\n";
                     idx = idx + 1;
                 }

                 vault2.MsgBox(this.Handle.ToInt32(), msg);

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

         private void Button7_Click(System.Object sender, System.EventArgs e)
         {
             //Add group, My Group
             try
             {
                 IEdmVault11 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault11)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 IEdmUserMgr7 userMgr = default(IEdmUserMgr7);
                 userMgr = (IEdmUserMgr7)vault2.CreateUtility(EdmUtility.EdmUtil_UserMgr);

                 IEdmUser7 admin = default(IEdmUser7);
                 admin = (IEdmUser7)userMgr.GetUser("Admin");

                 EdmGroupData2[] groups = new EdmGroupData2[1];
                 groups[0].mbAutoAdd = 0;
                 groups[0].mbsDescription = "A group created by the API";
                 groups[0].mbsName = "My Group";
                 groups[0].mlFlags = (int)EdmGroupDataFlags.Edmgdf_GetInterface;
                 int[] members = new int[1];
                 members[0] = admin.ID;
                 groups[0].moMembers = members;
                 EdmSysPerm[] perms = new EdmSysPerm[1];
                 perms[0] = EdmSysPerm.EdmSysPerm_ModifyToolbox;
                 groups[0].moSysPerms = perms;

                 userMgr.AddGroups2(ref groups);

                 string msg = null;
                 msg = "";
                 int idx = 0;
                 idx = Information.LBound(groups);
                 while ((idx <= Information.UBound(groups)))
                 {
                     if (groups[idx].mhStatus != 0)
                     {
                         msg = msg + "Error creating group, '" + groups[idx].mbsName + "' - " + vault2.GetErrorMessage(groups[idx].mhStatus) + "\n";
                     }
                     else
                     {
                         msg = msg + "Created group, '" + groups[idx].mbsName + "', successfully with ID, " + groups[idx].mlGroupID.ToString() + "\n";
                     }
                     idx = idx + 1;
                 }

                 vault2.MsgBox(this.Handle.ToInt32(), msg);

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

         private void Button8_Click(System.Object sender, System.EventArgs e)
         {
             //Remove group, My Group
             try
             {
                 IEdmVault7 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault7)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 IEdmUserMgr7 userMgr = default(IEdmUserMgr7);
                 userMgr = (IEdmUserMgr7)vault2.CreateUtility(EdmUtility.EdmUtil_UserMgr);
                 IEdmUserGroup6 @group = default(IEdmUserGroup6);
                 @group = (IEdmUserGroup6)userMgr.GetUserGroup("My Group");
                 if (@group == null)
                     return;

                 int[] groups = new int[1];
                 groups[0] = @group.ID;
                 userMgr.RemoveGroups(groups);

                 MessageBox.Show("Group, My Group, removed");

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

         private void Button9_Click(System.Object sender, System.EventArgs e)
         {
             //Add user, Temp
             try
             {
                 IEdmVault11 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault11)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 IEdmUserMgr7 UsrMgr = (IEdmUserMgr7)vault2;
                 EdmUserData2[] UserData = new EdmUserData2[1];

                 UserData[0].mbsCompleteName = "Temp";
                 UserData[0].mbsEmail = "Temp";
                 UserData[0].mbsInitials = "TJ";
                 UserData[0].mbsUserName = "Temp";
                 UserData[0].mlFlags = (int)EdmUserDataFlags.Edmudf_GetInterface;
                 UserData[0].mlFlags += (int)EdmUserDataFlags.Edmudf_ForceAdd;

                 EdmSysPerm[] perms = new EdmSysPerm[3];
                 perms[0] = EdmSysPerm.EdmSysPerm_EditUserMgr;
                 perms[1] = EdmSysPerm.EdmSysPerm_EditReportQuery;
                 perms[2] = EdmSysPerm.EdmSysPerm_MandatoryVersionComments;
                 UserData[0].moSysPerms = perms;

                 UsrMgr.AddUsers2(UserData);

                 string msg = "";
                 foreach (EdmUserData2 usr in UserData)
                 {
                     if (usr.mhStatus == 0)
                     {
                         msg += "Created user, \"" + usr.mbsUserName + "\", successfully with ID, " + usr.mlUserID.ToString() + "\n";
                     }
                     else
                     {
                         msg += "Error creating user, \"" + usr.mbsUserName + "\" - " + vault2.GetErrorMessage(usr.mhStatus) + "\n";
                     }
                 }
                 MessageBox.Show(msg);

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

         private void Button10_Click(System.Object sender, System.EventArgs e)
         {
             //Remove user, Temp
             try
             {
                 IEdmVault7 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault7)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 IEdmUserMgr7 userMgr = default(IEdmUserMgr7);
                 userMgr = (IEdmUserMgr7)vault2.CreateUtility(EdmUtility.EdmUtil_UserMgr);
                 IEdmUser7 user = default(IEdmUser7);
                 user = (IEdmUser7)userMgr.GetUser("Temp");
                 if (user == null)
                     return;

                 int[] users = new int[1];
                 users[0] = user.ID;
                 userMgr.RemoveUsers(users);

                 MessageBox.Show("User, Temp, removed");

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

         private void Button4_Click(System.Object sender, System.EventArgs e)
         {
             //Get user's check-out permission for a file
             try
             {
                 IEdmVault7 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault7)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 EdmStrLst5 pathList = default(EdmStrLst5);
                 pathList = vault2.BrowseForFile(this.Handle.ToInt32(), (int)EdmBrowseFlag.EdmBws_ForOpen + (int)EdmBrowseFlag.EdmBws_PermitVaultFiles);
                 if (pathList == null)
                     return;

                 IEdmFile5 file = default(IEdmFile5);
                 IEdmFolder5 srcFolder = null;
                 file = vault2.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition()), out srcFolder);

                 if (srcFolder.HasRightsEx((int)EdmRightFlags.EdmRight_Lock, file.ID))
                 {
                     MessageBox.Show("User can check out this file");
                 }
                 else
                 {
                     MessageBox.Show("User does not have check-out permission");
                 }

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

         private void Button1_Click(System.Object sender, System.EventArgs e)
         {
             //Copy file
             try
             {
                 IEdmVault7 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault7)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 EdmStrLst5 pathList = default(EdmStrLst5);
                 pathList = vault2.BrowseForFile(this.Handle.ToInt32(), (int)EdmBrowseFlag.EdmBws_ForOpen + (int)EdmBrowseFlag.EdmBws_PermitVaultFiles);
                 if (pathList == null)
                     return;

                 IEdmFile5 file = default(IEdmFile5);
                 IEdmFolder5 srcFolder = null;
                 file = vault2.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition()), out srcFolder);

                 IEdmFolder5 destFolder = default(IEdmFolder5);
                 destFolder = vault2.BrowseForFolder(this.Handle.ToInt32(), "Select destination folder:");
                 if (destFolder == null)
                     return;

                 int fileID = 0;
                 fileID = destFolder.CopyFile(file.ID, srcFolder.ID, this.Handle.ToInt32(), "", (int)EdmCopyFlag.EdmCpy_Simple);
                 MessageBox.Show("Copied file successfully to new file with ID, " + fileID);

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

         private void Button2_Click(System.Object sender, System.EventArgs e)
         {
             //Delete file
             try
             {
                 IEdmVault7 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault7)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 EdmStrLst5 pathList = default(EdmStrLst5);
                 pathList = vault2.BrowseForFile(this.Handle.ToInt32(), (int)EdmBrowseFlag.EdmBws_ForOpen + (int)EdmBrowseFlag.EdmBws_PermitVaultFiles + (int)EdmBrowseFlag.EdmBws_PermitMultipleSel, "", "", "", "", "Select Files to Delete");
                 if (pathList == null)
                     return;

                 IEdmPos5 pos = default(IEdmPos5);
                 pos = pathList.GetHeadPosition();
                 while (!pos.IsNull)
                 {
                     IEdmFile5 file = default(IEdmFile5);
                     IEdmFolder5 folder = null;
                     file = vault2.GetFileFromPath(pathList.GetNext(pos), out folder);
                     folder.DeleteFile(this.Handle.ToInt32(), file.ID);
                 }

                 string strCount = null;
                 strCount = pathList.Count.ToString();
                 MessageBox.Show("Deleted " + strCount + " file");

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

         private void Button3_Click(System.Object sender, System.EventArgs e)
         {
             //Delete folder
             try
             {
                 IEdmVault7 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault7)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 IEdmFolder5 folder = default(IEdmFolder5);
                 folder = vault2.BrowseForFolder(this.Handle.ToInt32(), "Select folder to delete:");
                 if (folder == null)
                     return;

                 IEdmFolder5 parentFolder = default(IEdmFolder5);
                 parentFolder = folder.ParentFolder;

                 if (parentFolder == null)
                 {
                     MessageBox.Show("You cannot delete the vault root folder");
                     return;
                 }

                 parentFolder.DeleteFolder(this.Handle.ToInt32(), folder.ID);

                 MessageBox.Show(folder.Name + " deleted");

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }
     private void Button11_Click(System.Object sender, System.EventArgs e)
         {
             //Restore folder
             try
             {
                 IEdmVault7 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault7)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 IEdmFolder11 folder = default(IEdmFolder11);
                 folder = vault2.BrowseForFolder(this.Handle.ToInt32(), "Select folder to delete:");
                 if (folder == null)
                     return;

                 EdmDeletedItems[] arrayEdmDeletedItems;

                 folder.GetDeletedItems(out arrayEdmDeletedItems, true);
                 folder.RecoverDeletedItems(arrayEdmDeletedItems);

                 MessageBox.Show(folder.Name + " restored");

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }
     }
 }
```

[Back to top](#top)

```vb
 //Form1.Designer.cs
 namespace VaultUtilities_CSharp
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
             this.VaultsLabel = new System.Windows.Forms.Label();
             this.VaultsComboBox = new System.Windows.Forms.ComboBox();
             this.Button1 = new System.Windows.Forms.Button();
             this.Button2 = new System.Windows.Forms.Button();
             this.Button3 = new System.Windows.Forms.Button();
             this.Button4 = new System.Windows.Forms.Button();
             this.Button5 = new System.Windows.Forms.Button();
             this.Button6 = new System.Windows.Forms.Button();
             this.Button7 = new System.Windows.Forms.Button();
             this.Button8 = new System.Windows.Forms.Button();
             this.Button9 = new System.Windows.Forms.Button();
             this.Button10 = new System.Windows.Forms.Button();
             this.Button11 = new System.Windows.Forms.Button();
             this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
             this.SuspendLayout();
             //
             //VaultsLabel
             //
             this.VaultsLabel.AutoSize = true;
             this.VaultsLabel.Location = new System.Drawing.Point(13, 26);
             this.VaultsLabel.Name = "VaultsLabel";
             this.VaultsLabel.Size = new System.Drawing.Size(94, 13);
             this.VaultsLabel.TabIndex = 0;
             this.VaultsLabel.Text = " Select vault view:";
             //
             //VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(16, 42);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             //Button1
             //
             this.Button1.Location = new System.Drawing.Point(16, 223);
             this.Button1.Name = "Button1";
             this.Button1.Size = new System.Drawing.Size(91, 23);
             this.Button1.TabIndex = 6;
             this.Button1.Text = "Copy file...";
             this.Button1.UseVisualStyleBackColor = true;
             this.Button1.Click +=new System.EventHandler(Button1_Click);
             //
             //Button2
             //
             this.Button2.Location = new System.Drawing.Point(113, 223);
             this.Button2.Name = "Button2";
             this.Button2.Size = new System.Drawing.Size(96, 23);
             this.Button2.TabIndex = 7;
             this.Button2.Text = "Delete file...";
             this.Button2.UseVisualStyleBackColor = true;
             this.Button2.Click +=new System.EventHandler(Button2_Click);
             //
             //Button3
             //
             this.Button3.Location = new System.Drawing.Point(69, 281);
             this.Button3.Name = "Button3";
             this.Button3.Size = new System.Drawing.Size(96, 23);
             this.Button3.TabIndex = 8;
             this.Button3.Text = "Delete folder...";
             this.Button3.UseVisualStyleBackColor = true;
             this.Button3.Click +=new System.EventHandler(Button3_Click);
             //
             //Button4
             //
             this.Button4.Location = new System.Drawing.Point(43, 252);
             this.Button4.Name = "Button4";
             this.Button4.Size = new System.Drawing.Size(156, 23);
             this.Button4.TabIndex = 9;
             this.Button4.Text = "Check-out permission...";
             this.Button4.UseVisualStyleBackColor = true;
             this.Button4.Click +=new System.EventHandler(Button4_Click);
             //
             //Button5
             //
             this.Button5.Location = new System.Drawing.Point(16, 83);
             this.Button5.Name = "Button5";
             this.Button5.Size = new System.Drawing.Size(233, 23);
             this.Button5.TabIndex = 10;
             this.Button5.Text = "Verify SOLIDWORKS PDM Professional 5.3";
             this.Button5.UseVisualStyleBackColor = true;
             this.Button5.Click +=new System.EventHandler(Button5_Click);
             //
             //Button6
             //
             this.Button6.Location = new System.Drawing.Point(16, 121);
             this.Button6.Name = "Button6";
             this.Button6.Size = new System.Drawing.Size(233, 23);
             this.Button6.TabIndex = 11;
             this.Button6.Text = "Get SOLIDWORKS PDM Professional licenses";
             this.Button6.UseVisualStyleBackColor = true;
             this.Button6.Click +=new System.EventHandler(Button6_Click);
             //
             //Button7
             //
             this.Button7.Location = new System.Drawing.Point(16, 165);
             this.Button7.Name = "Button7";
             this.Button7.Size = new System.Drawing.Size(91, 23);
             this.Button7.TabIndex = 12;
             this.Button7.Text = "Add group";
             this.Button7.UseVisualStyleBackColor = true;
             this.Button7.Click +=new System.EventHandler(Button7_Click);
             //
             //Button8
             //
             this.Button8.Location = new System.Drawing.Point(16, 194);
             this.Button8.Name = "Button8";
             this.Button8.Size = new System.Drawing.Size(91, 23);
             this.Button8.TabIndex = 13;
             this.Button8.Text = "Remove group";
             this.Button8.UseVisualStyleBackColor = true;
             this.Button8.Click +=new System.EventHandler(Button8_Click);
             //
             //Button9
             //
             this.Button9.Location = new System.Drawing.Point(113, 165);
             this.Button9.Name = "Button9";
             this.Button9.Size = new System.Drawing.Size(96, 23);
             this.Button9.TabIndex = 14;
             this.Button9.Text = "Add user";
             this.Button9.UseVisualStyleBackColor = true;
             this.Button9.Click +=new System.EventHandler(Button9_Click);
             //
             //Button10
             //
             this.Button10.Location = new System.Drawing.Point(113, 194);
             this.Button10.Name = "Button10";
             this.Button10.Size = new System.Drawing.Size(96, 23);
             this.Button10.TabIndex = 15;
             this.Button10.Text = "Remove user";
             this.Button10.UseVisualStyleBackColor = true;
             this.Button10.Click +=new System.EventHandler(Button10_Click);
             //
             //Button11
             //
             this.Button11.Location = new System.Drawing.Point(43, 310);
             this.Button11.Name = "Button11";
             this.Button11.Size = new System.Drawing.Size(156, 29);
             this.Button11.TabIndex = 16;
             this.Button11.Text = "Restore deleted items";
             this.Button11.UseVisualStyleBackColor = true;
             this.Button11.Click +=new System.EventHandler(Button11_Click);
             //
             //OpenFileDialog1
             //
             this.OpenFileDialog1.FileName = "OpenFileDialog1";
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(276, 330);
             this.Controls.Add(this.Button11);
             this.Controls.Add(this.Button10);
             this.Controls.Add(this.Button9);
             this.Controls.Add(this.Button8);
             this.Controls.Add(this.Button7);
             this.Controls.Add(this.Button6);
             this.Controls.Add(this.Button5);
             this.Controls.Add(this.Button4);
             this.Controls.Add(this.Button3);
             this.Controls.Add(this.Button2);
             this.Controls.Add(this.Button1);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Vault utilities";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button Button1;
         internal System.Windows.Forms.Button Button2;
         internal System.Windows.Forms.Button Button3;
         internal System.Windows.Forms.Button Button4;
         internal System.Windows.Forms.Button Button5;
         internal System.Windows.Forms.Button Button6;
         internal System.Windows.Forms.Button Button7;
         internal System.Windows.Forms.Button Button8;
         internal System.Windows.Forms.Button Button9;
         internal System.Windows.Forms.Button Button10;
         internal System.Windows.Forms.Button Button11;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog1;
     }
 }
```

[Back to top](#top)
