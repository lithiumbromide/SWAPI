---
title: "Add Folder Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Add_Folder_Example_CSharp.htm"
---

# Add Folder Example (C#)

This example shows how to create a folder and set its data card and permissions.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio 2010.
 //    a. Click File > New > Project > Visual C# > Windows Forms Application.
 //    b. Type AddFolder_CSharp in Name.
 //    c. Click Browse and navigate to the folder where to create
 //       the project.
 //    d. Click OK.
 //    e. Click Show All Files in the Solution Explorer toolbar and expand
 //       Form1.cs in the Solution Explorer.
 //    f. Replace the code in Form1.cs with this code.
 //    g. To create the form, replace the code in Form1.Designer.cs with this code.
 // 2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 //    name in the Solution Explorer, click Add Reference, click
 //    Assemblies > Framework in the left-side panel, browse to the top folder of
 //    your SOLIDWORKS PDM Professional installation, locate and click
 //    EPDM.Interop.epdm.dll, click Open, and click Add).
  // 3. Add Microsoft.VisualBasic as a reference (click COM in the left-side panel,
 //    click Microsoft.VisualBasic, click Add, and click Close).
 // 4. Right-click EPDM.Interop.epdm in References, click Properties, and set
 //    Embed Interop Types to False to handle methods that pass arrays of
 //    structures.
 // 5. Ensure that the vault has user, Engineer1, and group,
 //    Administrators.
 // 6. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Add folder dialog box.
  //    a. Select a vault view.
  //    b. Click Browse for parent folder.
  //       1. Locate and click a folder in the vault.
   //       2. Click OK.
   //    c. Click Add folder.
   //       1.  Creates an IEdmFolderData5 object with:
   //           * Folder user permissions for user, Engineer1.
   //           * Folder group permissions for group, Administrators.
   //           * File data card for .doc files.
   //       2. Displays a message that folder, Temp, is added as a subfolder to
   //          the folder clicked in Postconditions 1b1.
   //       3. Click OK.
  // 2. Close the Add folder dialog box.
   // 3. Open File Explorer on a vault view and observe the new sub-folder,
   //    Temp.
 // 4. Open the Administration tool.
 //    a. Log in to the vault selected in step 1a.
 //    b. Expand Groups and double-click Administrators.
 //    c. Click Folder Permissions.
 //    d. Inspect the folder permissions for Temp and click OK.
 //    e. Expand Users and double-click Engineer1.
 //    f. Repeat steps 4c and 4d.
 // 5. Exit the Administration tool.
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
 using Microsoft.VisualBasic;

 namespace AddFolder_CSharp
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

         public void BrowseButton_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 ListBox.Items.Clear();

                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 if (!vault1.IsLoggedIn)
                 {
                     //Log into selected vault as the current user
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 //Show the Browse For Folder dialog
                 System.Windows.Forms.DialogResult DialogResult;
                 DialogResult = FolderBrowserDialog1.ShowDialog();
                 //If the user didn't click OK, exit
                 if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
                 {
                     return;
                 }

                 ListBox.Items.Add(FolderBrowserDialog1.SelectedPath);

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

         public void AddFolder_Click(System.Object sender, System.EventArgs e)
         {

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
                     //Log into selected vault as the current user
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 IEdmFolder5 parentFolder = default(IEdmFolder5);
                 parentFolder = vault2.GetFolderFromPath(ListBox.Items[0].ToString());

                 dynamic folderName = "Temp";
                 IEdmUserMgr5 usrMgr = default(IEdmUserMgr5);
                 usrMgr = (IEdmUserMgr5)parentFolder.Vault;

                 EdmFolderData data = default(EdmFolderData);
                 data = new EdmFolderData();

                 data.SetUserRights(usrMgr.GetUser("Engineer1").ID, (int)EdmRightFlags.EdmRight_Read | (int)EdmRightFlags.EdmRight_Lock);
                 data.SetGroupRights(usrMgr.GetUserGroup("Administrators").ID, (int)EdmRightFlags.EdmRight_All);

                 IEdmCard5 card = default(IEdmCard5);
                 card = parentFolder.Vault.RootFolder.GetCard("doc");
                 data.SetCardSource(card.ID, "doc");

                 IEdmFolder5 folder = default(IEdmFolder5);
                 folder = parentFolder.AddFolder(this.Handle.ToInt32(), folderName, data);
                 Interaction.MsgBox("Created " + folderName + " successfully with ID, " + Conversion.Str(folder.ID) + ", in " + parentFolder.Name);

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
 namespace AddFolder_CSharp
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
             this.BrowseButton = new System.Windows.Forms.Button();
             this.ListBox = new System.Windows.Forms.ListBox();
             this.AddFolder = new System.Windows.Forms.Button();
             this.FolderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
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
             //BrowseButton
             //
             this.BrowseButton.Location = new System.Drawing.Point(16, 85);
             this.BrowseButton.Name = "BrowseButton";
             this.BrowseButton.Size = new System.Drawing.Size(186, 23);
             this.BrowseButton.TabIndex = 3;
             this.BrowseButton.Text = "Browse for parent folder...";
             this.BrowseButton.UseVisualStyleBackColor = true;
             this.BrowseButton.Click +=new System.EventHandler(BrowseButton_Click);
             //
             //ListBox
             //
             this.ListBox.FormattingEnabled = true;
             this.ListBox.HorizontalScrollbar = true;
             this.ListBox.Location = new System.Drawing.Point(16, 114);
             this.ListBox.Name = "ListBox";
             this.ListBox.Size = new System.Drawing.Size(259, 43);
             this.ListBox.TabIndex = 4;
             //
             //AddFolder
             //
             this.AddFolder.Location = new System.Drawing.Point(84, 178);
             this.AddFolder.Name = "AddFolder";
             this.AddFolder.Size = new System.Drawing.Size(98, 23);
             this.AddFolder.TabIndex = 5;
             this.AddFolder.Text = "Add folder";
             this.AddFolder.UseVisualStyleBackColor = true;
             this.AddFolder.Click +=new System.EventHandler(AddFolder_Click);
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(317, 215);
             this.Controls.Add(this.AddFolder);
             this.Controls.Add(this.ListBox);
             this.Controls.Add(this.BrowseButton);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Add folder";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button BrowseButton;
         internal System.Windows.Forms.ListBox ListBox;
         internal System.Windows.Forms.Button AddFolder;
         internal System.Windows.Forms.FolderBrowserDialog FolderBrowserDialog1;
     }
 }
```

[Back to top](#top)
