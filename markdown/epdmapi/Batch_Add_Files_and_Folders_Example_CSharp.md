---
title: "Batch Add Files and Folders to Vault Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Batch_Add_Files_and_Folders_Example_CSharp.htm"
---

# Batch Add Files and Folders to Vault Example (C#)

This example shows how to add several files and folders to the vault in one batch.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 //  1. Start Microsoft Visual Studio.
 //     a. Click File > New > Project > C#, Windows, Desktop > Windows Forms Application.
 //     b. Type BatchAddFiles_CSharp in Project name.
 //     c. For Location, click ... and navigate to the folder where to create the project.
//     d. Click Next.
//     e. Select Framework.
//     f. Click Create.
 //     g. Click Show All Files in the Solution Explorer toolbar and expand
 //        Form1.cs in the Solution Explorer.
 //     h. Replace the code in Form1.cs with this code.
 //     i. To create the form, replace the code in Form1.Designer.cs with
 //        this code.
 //  2. Add dependencies and safely pass arrays of structures.
 //  3. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 //  1. The Batch add files to vault dialog box displays.
 //     a. Select a vault view.
 //     b. Click Select file outside vault to copy to vault.
 //     c. In the Select File dialog:
 //        1. Click a file outside the vault.
 //        2. Click Open.
 //     d. Click Select file inside vault to copy to vault.
 //     e. In the Select File dialog:
 //        1. Click a file in the vault.
 //        2. Click Open.
 //     f. Click Commit all files to vault.
 //  2. Click Add in the Batch Items dialog box.
 //  3. Click OK to close the message box.
 //     Two new folders, Folder1 and Folder2, are created in the vault's
 //     root directory. The first selected file is copied to Folder1.
 //     The second selected file is copied to Folder2.
 //  4. Close the Batch add files to vault dialog box.
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

 namespace BatchAddFiles_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         private IEdmVault5 vault1 = null;
         IEdmBatchAdd2 batchAdder;

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

         public void CopyToVault_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 FileList1.Items.Clear();

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

                 //Set the initial directory in the Select File dialog
                 SelectFileDialog.InitialDirectory = vault1.RootFolderPath;
                 //Show the Select File dialog
                 System.Windows.Forms.DialogResult DialogResult;
                 DialogResult = SelectFileDialog.ShowDialog();
                 //If the user did not click Open, exit this subroutine
                 if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
                 {
                     return;
                 }

                 batchAdder = (IEdmBatchAdd2)vault2.CreateUtility(EdmUtility.EdmUtil_BatchAdd);

                 // Add Folder1 to the batch
                 string newFolder = vault1.RootFolderPath + "\\Folder1";
                 batchAdder.AddFolderPath(newFolder, 0, (int)EdmBatchAddFolderFlag.Ebaff_Nothing);

                 foreach (string FileName in SelectFileDialog.FileNames)
                 {
                     FileList1.Items.Add(FileName);

                     // Add each selected file to the batch
                     batchAdder.AddFileFromPathToPath(FileName, newFolder, 0);
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
         public void CopyFromVault_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 FileList2.Items.Clear();

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

                 //Set the initial directory in the Select File dialog
                 SelectFileDialog.InitialDirectory = vault1.RootFolderPath;
                 //Show the Select File dialog
                 System.Windows.Forms.DialogResult DialogResult;
                 DialogResult = SelectFileDialog.ShowDialog();
                 //If the user didn't click Open, exit this subroutine
                 if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
                 {
                     return;
                 }

                 // Add Folder2 to the batch
                 batchAdder.AddFolder(vault1.RootFolderID, "Folder2", 0, (int)EdmBatchAddFolderFlag.Ebaff_Nothing);

                 IEdmFile5 aFile = default(IEdmFile5);
                 IEdmFolder5 aFolder = default(IEdmFolder5);
                 IEdmPos5 aPos = default(IEdmPos5);
                 IEdmFolder5 ppoRetParentFolder = default(IEdmFolder5);
                 foreach (string FileName in SelectFileDialog.FileNames)
                 {
                     FileList2.Items.Add(FileName);

                     aFile = vault1.GetFileFromPath(FileName, out ppoRetParentFolder);
                     aPos = aFile.GetFirstFolderPosition();
                     aFolder = aFile.GetNextFolder(aPos);

                     // Add each selected file to the batch
                     batchAdder.AddFileFromVaultToPath(aFile.ID, aFolder.ID, vault1.RootFolderPath + "\\Folder2");
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

         public void BatchAdd_Click(System.Object sender, System.EventArgs e)
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
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 // Show all of the items in the batch
                 batchAdder.ShowDlg(this.Handle.ToInt32(), (int)EdmAddFileDlgFlag.Eafdf_Nothing, "Files and folders in the batch:", "Batch Items");

                 EdmFileInfo[] ppoAddedFiles = new EdmFileInfo[10];

                 // Commit all of the items in the batch to the vault
                 batchAdder.CommitAdd(this.Handle.ToInt32(), ref ppoAddedFiles);

                 //Display the returned information in a message box

                 int idx;
                 idx = ppoAddedFiles.GetLowerBound(0);
                 string msg = "";

                 while (idx <= ppoAddedFiles.GetUpperBound(0))
                 {
                     string row = null;
                     row = "(" + ppoAddedFiles[idx].mbsPath + ") arg = " + (ppoAddedFiles[idx].mlArg).ToString();

                     if (ppoAddedFiles[idx].mhResult == 0)
                     {
                         row = row + " status = OK ";
                     }
                     else
                     {
                         string oErrName = "";
                         string oErrDesc = "";

                         vault1.GetErrorString(ppoAddedFiles[idx].mhResult, out oErrName, out oErrDesc);
                         row = row + " status = " + oErrName;
                     }

                     idx = idx + 1;
                     msg = msg + "\n" + row;

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
     }
 }
```

[Back to top](#top)

```vb
 //Form1.Designer.cs
 namespace BatchAddFiles_CSharp
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
             this.BatchAdd = new System.Windows.Forms.Button();
             this.CopyToVault = new System.Windows.Forms.Button();
             this.FileList1 = new System.Windows.Forms.ListBox();
             this.CopyFromVault = new System.Windows.Forms.Button();
             this.FileList2 = new System.Windows.Forms.ListBox();
             this.SelectFileDialog = new System.Windows.Forms.OpenFileDialog();
             this.SuspendLayout();
             //
             //VaultsLabel
             //
             this.VaultsLabel.AutoSize = true;
             this.VaultsLabel.Location = new System.Drawing.Point(12, 27);
             this.VaultsLabel.Name = "VaultsLabel";
             this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
             this.VaultsLabel.TabIndex = 0;
             this.VaultsLabel.Text = "Select vault view:";
             //
             //VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(12, 43);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             //BatchAdd
             //
             this.BatchAdd.Location = new System.Drawing.Point(67, 236);
             this.BatchAdd.Name = "BatchAdd";
             this.BatchAdd.Size = new System.Drawing.Size(123, 23);
             this.BatchAdd.TabIndex = 2;
             this.BatchAdd.Text = "Commit all files to vault";
             this.BatchAdd.UseVisualStyleBackColor = true;
             this.BatchAdd.Click += new System.EventHandler(this.BatchAdd_Click);
             //
             //CopyToVault
             //
             this.CopyToVault.Location = new System.Drawing.Point(12, 80);
             this.CopyToVault.Name = "CopyToVault";
             this.CopyToVault.Size = new System.Drawing.Size(239, 23);
             this.CopyToVault.TabIndex = 3;
             this.CopyToVault.Text = "Select file outside vault to copy to vault...";
             this.CopyToVault.UseVisualStyleBackColor = true;
             this.CopyToVault.Click += new System.EventHandler(this.CopyToVault_Click);
             //
             //FileList1
             //
             this.FileList1.FormattingEnabled = true;
             this.FileList1.Location = new System.Drawing.Point(12, 109);
             this.FileList1.Name = "FileList1";
             this.FileList1.Size = new System.Drawing.Size(239, 30);
             this.FileList1.TabIndex = 4;
             //
             //CopyFromVault
             //
             this.CopyFromVault.Location = new System.Drawing.Point(12, 160);
             this.CopyFromVault.Name = "CopyFromVault";
             this.CopyFromVault.Size = new System.Drawing.Size(239, 23);
             this.CopyFromVault.TabIndex = 5;
             this.CopyFromVault.Text = "Select file inside vault to copy to vault...";
             this.CopyFromVault.UseVisualStyleBackColor = true;
             this.CopyFromVault.Click += new System.EventHandler(this.CopyFromVault_Click);
             //
             //FileList2
             //
             this.FileList2.FormattingEnabled = true;
             this.FileList2.Location = new System.Drawing.Point(12, 189);
             this.FileList2.Name = "FileList2";
             this.FileList2.Size = new System.Drawing.Size(239, 30);
             this.FileList2.TabIndex = 6;
             //
             //SelectFileDialog
             //
             this.SelectFileDialog.Title = "Select File";
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(284, 291);
             this.Controls.Add(this.FileList2);
             this.Controls.Add(this.CopyFromVault);
             this.Controls.Add(this.FileList1);
             this.Controls.Add(this.CopyToVault);
             this.Controls.Add(this.BatchAdd);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Batch add files to vault";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         private System.Windows.Forms.Label VaultsLabel;
         private System.Windows.Forms.ComboBox VaultsComboBox;
         private System.Windows.Forms.Button BatchAdd;
         private System.Windows.Forms.Button CopyToVault;
         private System.Windows.Forms.ListBox FileList1;
         private System.Windows.Forms.Button CopyFromVault;
         private System.Windows.Forms.ListBox FileList2;
         private System.Windows.Forms.OpenFileDialog SelectFileDialog;
     }
 }
```

[Back to top](#top)
