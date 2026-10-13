---
title: "Access Custom File References Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Access_Custom_File_References_Example_CSharp.htm"
---

# Access Custom File References Example (C#)

This example shows how to access custom file references.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 //    a. Click File > New > Project > C#, Desktop, Windows > Windows Forms Application.
 //    b. Type AccessCustRef_CSharp in Project name.
 //    c. For Location, click ... and navigate to the folder where to create the project.
//    d. Click Next.
//    e. Select Framework.
//    f. Click Create.
 //    g. Click Show All Files in the Solution Explorer toolbar and expand
 //       Form1.cs in the Solution Explorer.
 //    f. Replace the code in Form1.cs with this code.
 //    g. To create the form, replace the code in Form1.Designer.cs with
 //       this code.
 // 2.     Add dependencies and safely pass arrays of structures.
 // 3. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Add custom file reference dialog box.
  //    a. Select a vault view.
  //    b. Click Browse for two files.
  //       1. Locate and click two files in the root folder of the vault.
   //       2. Click Open.
 //       3. Checks out the first file.
 //    c. Click Add custom file reference.
 //    d. Click OK to close each message box.
  // 2. Close the Add custom file reference dialog.
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

 namespace AccessCustRefs_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         private IEdmVault5 vault1 = null;
         IEdmEnumeratorCustomReference7 addCustRefs;
         IEdmFile5 file1 = null;
         IEdmFile5 file2 = null;

         IEdmFolder5 parentFolder = null;

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
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
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
                 CustRefListBox.Items.Clear();

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
                 CustRefOpenFileDialog.InitialDirectory = vault1.RootFolderPath;
                 //Show the Open dialog
                 System.Windows.Forms.DialogResult DialogResult;
                 DialogResult = CustRefOpenFileDialog.ShowDialog();
                 //If the user didn't click Open, exit
                 if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
                 {
                     return;
                 }

                 foreach (string FileName in CustRefOpenFileDialog.FileNames)
                 {
                     CustRefListBox.Items.Add(FileName);
                 }
             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

         public void AddCustomFileReference_Click(System.Object sender, System.EventArgs e)
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

                 //Get the two selected files
                 file1 = vault2.GetFileFromPath(CustRefListBox.Items[0].ToString(), out parentFolder);
                 file2 = vault2.GetFileFromPath(CustRefListBox.Items[1].ToString(), out parentFolder);

                 //Check out the first file
                 if (!file1.IsLocked)
                 {
                     file1.LockFile(parentFolder.ID, this.Handle.ToInt32(), Convert.ToInt32(EdmLockFlag.EdmLock_Simple));
                 }

                 //Add the second file as a custom reference to the first file
                 addCustRefs = (IEdmEnumeratorCustomReference7)file1;
                 addCustRefs.AddReference3(file2.ID, parentFolder.ID, 1, true);
                 MessageBox.Show(file2.Name + " added as reference to " + file1.Name);
                 bool shownInBOM;
                 shownInBOM = addCustRefs.GetShowInBOM(file2.ID, parentFolder.ID);
                 MessageBox.Show(file2.Name + " shown in BOM? " + shownInBOM);

                 //Check in the first file
                 file1.UnlockFile(this.Handle.ToInt32(), "Custom reference added");

                 //Display all of the custom references of the first file
                 ShowFileRefs();

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
             }
             catch (Exception ex)
             {
                 MessageBox.Show(ex.Message);
             }
         }

         private void ShowFileRefs()
         {
             try
             {
                 IEdmEnumeratorCustomReference6 enumRef = default(IEdmEnumeratorCustomReference6);
                 enumRef = (IEdmEnumeratorCustomReference6)file1;
                 IEdmPos5 pos = default(IEdmPos5);
                 pos = enumRef.GetFirstRefPosition();
                 int fileID = 0;
                 int folderID = 0;
                 string message = null;
                 int quant = 1;
                 string pbsRetPath = "";
                 message = "Custom references of " + file1.Name + ":" + "\r\n";
                 while (!pos.IsNull)
                 {
                     enumRef.GetNextRef2(pos, out fileID, out folderID, out pbsRetPath, out quant);
                     message = message + pbsRetPath + " (fileID=" + fileID.ToString() + ", folderID=" + folderID.ToString() + ", quantity=" + quant.ToString() + ")" + "\r\n";
                 }
                 MessageBox.Show(message);
             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\r\n" + ex.Message);
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
 namespace AccessCustRefs_CSharp
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
             this.CustRefListBox = new System.Windows.Forms.ListBox();
             this.AddCustomFileReference = new System.Windows.Forms.Button();
             this.CustRefOpenFileDialog = new System.Windows.Forms.OpenFileDialog();
             this.SuspendLayout();
             //
             //VaultsLabel
             //
             this.VaultsLabel.AutoSize = true;
             this.VaultsLabel.Location = new System.Drawing.Point(13, 26);
             this.VaultsLabel.Name = "VaultsLabel";
             this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
             this.VaultsLabel.TabIndex = 0;
             this.VaultsLabel.Text = "Select vault view:";
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
             this.BrowseButton.Location = new System.Drawing.Point(16, 78);
             this.BrowseButton.Name = "BrowseButton";
             this.BrowseButton.Size = new System.Drawing.Size(146, 23);
             this.BrowseButton.TabIndex = 3;
             this.BrowseButton.Text = "Browse for two files...";
             this.BrowseButton.UseVisualStyleBackColor = true;
             this.BrowseButton.Click +=new System.EventHandler(BrowseButton_Click);
             //
             //CustRefListBox
             //
             this.CustRefListBox.FormattingEnabled = true;
             this.CustRefListBox.HorizontalScrollbar = true;
             this.CustRefListBox.Location = new System.Drawing.Point(16, 107);
             this.CustRefListBox.Name = "CustRefListBox";
             this.CustRefListBox.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended;
             this.CustRefListBox.Size = new System.Drawing.Size(259, 56);
             this.CustRefListBox.TabIndex = 4;
             //
             //AddCustomFileReference
             //
             this.AddCustomFileReference.Location = new System.Drawing.Point(68, 175);
             this.AddCustomFileReference.Name = "AddCustomFileReference";
             this.AddCustomFileReference.Size = new System.Drawing.Size(150, 23);
             this.AddCustomFileReference.TabIndex = 5;
             this.AddCustomFileReference.Text = "Add custom file reference";
             this.AddCustomFileReference.UseVisualStyleBackColor = true;
             this.AddCustomFileReference.Click +=new System.EventHandler(AddCustomFileReference_Click);
             //
             //CustRefOpenFileDialog
             //
             this.CustRefOpenFileDialog.Multiselect = true;
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(287, 222);
             this.Controls.Add(this.AddCustomFileReference);
             this.Controls.Add(this.CustRefListBox);
             this.Controls.Add(this.BrowseButton);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Add custom file reference";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button BrowseButton;
         internal System.Windows.Forms.ListBox CustRefListBox;
         internal System.Windows.Forms.Button AddCustomFileReference;
         internal System.Windows.Forms.OpenFileDialog CustRefOpenFileDialog;
     }
 }
```

[Back to top](#top)
