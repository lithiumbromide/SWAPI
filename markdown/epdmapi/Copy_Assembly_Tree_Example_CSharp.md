---
title: "Copy Assembly Tree of Files Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Copy_Assembly_Tree_Example_CSharp.htm"
---

# Copy Assembly Tree of Files Example (C#)

This example shows how to copy an assembly and its tree of reference files to a destination folder in the vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 //    a. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
 //    b. Type CopyTree_CSharp in Project name.
 //    c. For Location, click ... and navigate to the folder where to create the project.
//    d. Click Next.
//    e. Select Framework.
//    f. Click Create.
 //    g. Click Show All Files in the Solution Explorer toolbar and expand
 //        Form1.cs in the Solution Explorer.
 //    h. Replace the code in Form1.cs with this code.
 //    i. To create the form, replace the code in Form1.Designer.cs with this code.
  // 2.     Add dependencies and safely pass arrays of structures.
 // 3. Ensure that the vault root folder contains an assembly that
 //    is checked in with its referenced parts and drawings.
 // 4. Create a destination folder called New Folder in the vault.
 // 5. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Copy Assembly dialog box.
 //    a. Select a vault view.
 //    b. Click Select assembly.
 //       Locate and double-click an assembly.
 //    c. Click Select a destination folder.
 //       1. Locate and select New Folder.
 //       2. Click OK.
 //    d. Click Copy tree.
 //       The Copy Tree dialog shows the files to copy.
 //    e. Click Copy.
 //       The Copying tree progress bar appears.
 //    f. Inspect the destination folder.
 // 2. Close the Copy Assembly dialog box.
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

 namespace CopyTree_CSharp
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
         public void AddFiles_Click(System.Object sender, System.EventArgs e)
         {

             try
             {

                 IEdmVault19 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault19)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     //Log into selected vault as the current user
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 if (!(ListBox.Items.Count == 1))
                 {
                     MessageBox.Show("Please select an assembly.");
                     return;
                 }

                 if (!(listBox1.Items.Count == 1))
                 {
                     MessageBox.Show("Please select a destination folder.");
                     return;
                 }

                 IEdmFile12 aFile = default(IEdmFile12);
                 string destFolder = null;
                 IEdmFolder9 Folder = default(IEdmFolder9);

                 Folder = (IEdmFolder9)vault2.RootFolder;

                 string[] FileNames = new string[3];
                 int Index = 0;
                 dynamic fileStr = "";
                 foreach (Object FileName_loopVariable in ListBox.Items)
                 {
                     fileStr = FileName_loopVariable.ToString();

                     FileNames[Index] = fileStr.Substring(fileStr.LastIndexOf("\\"));
                     Index = Index + 1;
                 }

                 // Copy the assembly's tree of files to the specified destination folder
                 EdmCopyTreeOptions copyTreeOptions;
                 copyTreeOptions.mbsPrefix = "Copy_";
                 copyTreeOptions.mbsSuffix = "";
                 copyTreeOptions.mbIncludeDrawings = -1;
                 copyTreeOptions.mbUseLatestVersion = -1;

                 IEdmFolder5 ppoParentFolder;

                 aFile = (IEdmFile12)vault2.GetFileFromPath(Folder.LocalPath + "\\" + FileNames[0], out ppoParentFolder);
                 destFolder = listBox1.Items[0].ToString();
                 vault2.CopyTree(aFile.ID, Folder.ID, destFolder, true, true, copyTreeOptions, this.Handle.ToInt32());

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

         private void BrowseDestFolder_Click(object sender, EventArgs e)
         {
             try
             {
                 listBox1.Items.Clear();

                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 if (!vault1.IsLoggedIn)
                 {
                     //Log into selected vault as the current user
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 IEdmFolder10 rootFolder = default(IEdmFolder10);
                 rootFolder = (IEdmFolder10)vault1.RootFolder;

                 IEdmFolder10 aFolder = default(IEdmFolder10);
                 aFolder = (IEdmFolder10)vault1.BrowseForFolder(this.Handle.ToInt32(), "Select a destination folder");

                 listBox1.Items.Add(rootFolder.LocalPath + "\\" + aFolder.Name);

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
 namespace CopyTree_CSharp
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
             this.BrowseAssembly = new System.Windows.Forms.Button();
             this.ListBox = new System.Windows.Forms.ListBox();
             this.CopyTree = new System.Windows.Forms.Button();
             this.OpenFileDialog = new System.Windows.Forms.OpenFileDialog();
             this.BrowseDestFolder = new System.Windows.Forms.Button();
             this.listBox1 = new System.Windows.Forms.ListBox();
             this.SuspendLayout();
             //
             // VaultsLabel
             //
             this.VaultsLabel.AutoSize = true;
             this.VaultsLabel.Location = new System.Drawing.Point(13, 26);
             this.VaultsLabel.Name = "VaultsLabel";
             this.VaultsLabel.Size = new System.Drawing.Size(94, 13);
             this.VaultsLabel.TabIndex = 0;
             this.VaultsLabel.Text = " Select vault view:";
             //
             // VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(16, 42);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             // BrowseAssembly
             //
             this.BrowseAssembly.Location = new System.Drawing.Point(16, 85);
             this.BrowseAssembly.Name = "BrowseAssembly";
             this.BrowseAssembly.Size = new System.Drawing.Size(121, 23);
             this.BrowseAssembly.TabIndex = 3;
             this.BrowseAssembly.Text = "Select assembly...";
             this.BrowseAssembly.UseVisualStyleBackColor = true;
             this.BrowseAssembly.Click += new System.EventHandler(this.BrowseButton_Click);
             //
             // ListBox
             //
             this.ListBox.FormattingEnabled = true;
             this.ListBox.HorizontalScrollbar = true;
             this.ListBox.Location = new System.Drawing.Point(16, 114);
             this.ListBox.Name = "ListBox";
             this.ListBox.SelectionMode = System.Windows.Forms.SelectionMode.None;
             this.ListBox.Size = new System.Drawing.Size(259, 30);
             this.ListBox.TabIndex = 4;
             //
             // CopyTree
             //
             this.CopyTree.Location = new System.Drawing.Point(77, 293);
             this.CopyTree.Name = "CopyTree";
             this.CopyTree.Size = new System.Drawing.Size(98, 23);
             this.CopyTree.TabIndex = 5;
             this.CopyTree.Text = "Copy tree";
             this.CopyTree.UseVisualStyleBackColor = true;
             this.CopyTree.Click += new System.EventHandler(this.AddFiles_Click);
             //
             // OpenFileDialog
             //
             this.OpenFileDialog.Title = "Open";
             //
             // BrowseDestFolder
             //
             this.BrowseDestFolder.Location = new System.Drawing.Point(16, 181);
             this.BrowseDestFolder.Name = "BrowseDestFolder";
             this.BrowseDestFolder.Size = new System.Drawing.Size(142, 23);
             this.BrowseDestFolder.TabIndex = 6;
             this.BrowseDestFolder.Text = "Select destination folder...";
             this.BrowseDestFolder.UseVisualStyleBackColor = true;
             this.BrowseDestFolder.Click += new System.EventHandler(this.BrowseDestFolder_Click);
             //
             // listBox1
             //
             this.listBox1.FormattingEnabled = true;
             this.listBox1.Location = new System.Drawing.Point(16, 211);
             this.listBox1.Name = "listBox1";
             this.listBox1.SelectionMode = System.Windows.Forms.SelectionMode.None;
             this.listBox1.Size = new System.Drawing.Size(259, 30);
             this.listBox1.TabIndex = 7;
             //
             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(317, 363);
             this.Controls.Add(this.listBox1);
             this.Controls.Add(this.BrowseDestFolder);
             this.Controls.Add(this.CopyTree);
             this.Controls.Add(this.ListBox);
             this.Controls.Add(this.BrowseAssembly);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Copy Assembly";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button BrowseAssembly;
         internal System.Windows.Forms.ListBox ListBox;
         internal System.Windows.Forms.Button CopyTree;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog;
         internal System.Windows.Forms.Button BrowseDestFolder;
         internal System.Windows.Forms.ListBox listBox1;
     }
 }
```

[Back to top](#top)
