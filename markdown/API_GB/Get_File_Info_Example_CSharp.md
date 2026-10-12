---
title: "Get File Information Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Get_File_Info_Example_CSharp.htm"
---

# Get File Information Example (C#)

This example shows how to access a file and get information about it.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio 2010.
 //    a. Click File > New > Project > Visual C# > Windows Forms Application.
 //    b. Type Files_CSharp in Name.
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
  // 3. Add Microsoft.VisualBasic as a reference (click Framework in the left-side panel,
 //    click Microsoft.VisualBasic, click Add, and click Close).
 // 4. Right-click EPDM.Interop.epdm in References, click Properties, and set
 //    Embed Interop Types to False to handle methods that pass arrays of
 //    structures.
 // 5. Check out a file in the vault.
 // 6. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Get file information dialog box.
 //    a. Select a vault view.
 //    b. Click Browse.
 //       1. Locate and select the file checked out in Preconditions step 5.
 //       2. Click Open.
 //    c. Click Get information.
 //    d. Displays a message box with information about the selected file.
 //    e. Click OK.
 // 2. Close the Get file information dialog box.
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

 namespace Files_CSharp
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

                 //Set the initial directory in the Open dialog
                 OpenFileDialog.InitialDirectory = vault1.RootFolderPath;
                 //Show the Open dialog
                 System.Windows.Forms.DialogResult DialogResult;
                 DialogResult = OpenFileDialog.ShowDialog();
                 //If the user didn't click Open, exit
                 if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
                 {
                     return;
                 }

                 foreach (string FileName in OpenFileDialog.FileNames)
                 {
                     ListBox.Items.Add(FileName);
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

         public void GetInfo_Click(System.Object sender, System.EventArgs e)
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

                 IEdmFile17 aFile = default(IEdmFile17);
                 IEdmFolder5 ppoRetParentFolder;
                 aFile = (IEdmFile17)vault2.GetFileFromPath(ListBox.Items[0].ToString(), out ppoRetParentFolder);

                 //Get configurations
                 string msg = "Configurations: " + Constants.vbLf;
                 IEdmFolder5 folder = default(IEdmFolder5);
                 folder = vault2.RootFolder;

                 EdmStrLst5 cfgList = default(EdmStrLst5);
                 cfgList = aFile.GetConfigurations();

                 IEdmPos5 pos = default(IEdmPos5);
                 pos = cfgList.GetHeadPosition();
                 string cfgName = null;
                 while (!pos.IsNull)
                 {
                     cfgName = cfgList.GetNext(pos);
                     msg = msg + cfgName + Constants.vbLf;
                 }

                 msg = msg + Constants.vbLf;

                 //Get type of file
                 int typ = 0;
                 typ = (int)aFile.FileType;
                 msg = msg + "EdmFileType: " + typ + Constants.vbLf;

                 msg = msg + Constants.vbLf;

                 //Get category of file
                 IEdmCategory6 cat = default(IEdmCategory6);
                 cat = aFile.Category;
                 if ((cat != null))
                 {
                     msg = msg + "Category: " + cat.Name + ", Category ID: " + aFile.CategoryID + Constants.vbLf;
                     msg = msg + Constants.vbLf;
                 }

                 //Get local file timestamp
                 string filePath = aFile.Name;
                 object fileDate = null;
                 fileDate = aFile.GetLocalFileDate(filePath);

                 if ((fileDate != null))
                 {
                     string text = null;
                     text = fileDate.ToString();
                     msg = msg + aFile.GetLocalPath(folder.ID) + " was modified " + text + Constants.vbLf;
                 }
                 else
                 {
                     msg = msg + "There is no local copy of the file" + Constants.vbLf;
                 }

                 msg = msg + Constants.vbLf;

                 //Get local version number
                 int versionNo = 0;
                 versionNo = aFile.GetLocalVersionNo(aFile.GetLocalPath(folder.ID));

                 if (versionNo == -1)
                 {
                     msg = msg + "The local copy of " + aFile.Name + " does not match any existing versions" + Constants.vbLf;
                 }
                 else
                 {
                     string versionStr = null;
                     versionStr = versionNo.ToString();
                     msg = msg + "The local copy of " + aFile.Name + " has version " + versionStr + Constants.vbLf;
                 }

                 msg = msg + Constants.vbLf;

                 //Get current version
                 int ver = 0;
                 ver = aFile.CurrentVersion;
                 msg = msg + "Current version: " + ver + Constants.vbLf;

                 msg = msg + Constants.vbLf;

                 //Get local revision name
                 string revName = null;
                 revName = aFile.GetLocalRevisionName(aFile.GetLocalPath(folder.ID));

                 if (string.IsNullOrEmpty(revName))
                 {
                     msg = msg + "The local copy of " + aFile.Name + " does not match any existing revisions" + Constants.vbLf;
                 }
                 else
                 {
                     msg = msg + "The local copy of " + aFile.Name + " has revision name " + revName + Constants.vbLf;
                 }

                 msg = msg + Constants.vbLf;

                 //Get current revision
                 revName = aFile.CurrentRevision;
                 msg = msg + "Current revision: " + revName + Constants.vbLf;

                 msg = msg + Constants.vbLf;

                 //Get local file size
                 int fileSize = 0;
                 fileSize = (int)aFile.GetLocalFileSize2(aFile.GetLocalPath(folder.ID));

                 if (fileSize == -1)
                 {
                     msg = msg + "The local copy of " + aFile.Name + " is missing" + Constants.vbLf;
                 }
                 else
                 {
                     msg = msg + "The local copy of " + aFile.Name + " has size " + fileSize + " bytes" + Constants.vbLf;
                 }

                 msg = msg + Constants.vbLf;

                 //Get current workflow state
                 IEdmState5 state = default(IEdmState5);
                 state = aFile.CurrentState;
                 msg = msg + "Current workflow state: " + state.Name + Constants.vbLf;

                 msg = msg + Constants.vbLf;

                 //Get whether the file is checked out
                 bool checkedOut = false;
                 checkedOut = aFile.IsLocked;
                 msg = msg + "File is checked out? " + checkedOut + Constants.vbLf;
                 if (checkedOut)
                 {
                     msg = msg + "Lock path: " + aFile.LockPath + Constants.vbLf;
                     msg = msg + "Locked by: " + aFile.LockedByUser.Name + ", User ID: " + aFile.LockedByUserID + Constants.vbLf;
                     msg = msg + "Locked in: " + aFile.LockedInFolder.Name + ", Folder ID: " + aFile.LockedInFolderID + Constants.vbLf;
                     msg = msg + "Locked on: " + aFile.LockedOnComputer  + ", Vault View ID: " + aFile.LockedOnViewID;
                 }
```

```
                 msg = msg + Constants.vbLf;
```

```
                 //Get whether the file has cut list items
                bool hasCutListItems = false;
                hasCutListItems = aFile.HasCutListItems;
                msg = msg + "File has cut list items? " + hasCutListItems + Constants.vbLf;
```

```vb
                 msg = msg + Constants.vbLf;
                   //Create a label
                   int labelID;
                labelID = aFile.CreateLabel("File label", "Label description shows in the history dialog box");
                  msg = msg + "File label ID: " + Constants.vbLf;
```

```vb
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
     }
 }
```

[Back to top](#top)

```vb
 //Form1.Designer.cs
 namespace Files_CSharp
 {
     partial class Form1
     {
         /// <summary>
         /// Required designer variable.
         /// </summary>
         private System.ComponentModel.IContainer components = null;

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
             this.GetInfo = new System.Windows.Forms.Button();
             this.OpenFileDialog = new System.Windows.Forms.OpenFileDialog();
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
             this.BrowseButton.Size = new System.Drawing.Size(98, 23);
             this.BrowseButton.TabIndex = 3;
             this.BrowseButton.Text = "Browse...";
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
             //GetInfo
             //
             this.GetInfo.Location = new System.Drawing.Point(84, 178);
             this.GetInfo.Name = "GetInfo";
             this.GetInfo.Size = new System.Drawing.Size(98, 23);
             this.GetInfo.TabIndex = 5;
             this.GetInfo.Text = "Get information";
             this.GetInfo.UseVisualStyleBackColor = true;
             this.GetInfo.Click +=new System.EventHandler(GetInfo_Click);
             //
             //OpenFileDialog
             //
             this.OpenFileDialog.Title = "Open";
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(317, 215);
             this.Controls.Add(this.GetInfo);
             this.Controls.Add(this.ListBox);
             this.Controls.Add(this.BrowseButton);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Get file information";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button BrowseButton;
         internal System.Windows.Forms.ListBox ListBox;
         internal System.Windows.Forms.Button GetInfo;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog;
     }
 }
```

[Back to top](#top)
