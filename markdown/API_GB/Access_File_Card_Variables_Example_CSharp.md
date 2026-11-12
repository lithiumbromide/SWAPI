---
title: "Access File Card Variables Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Access_File_Card_Variables_Example_CSharp.htm"
---

# Access File Card Variables Example (C#)

This example shows how to access file card variables.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio 2010.
 //    a. Click File > New > Project > Visual C# > Windows Forms Application.
 //    b. Type CardVars_CSharp in Name.
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
 // 5. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Access file variables dialog box.
 //    a. Select a vault view.
 //    b. Click Browse.
 //       1. Locate and click a file in the vault.
 //       2. Click Open.
 //    c. Click Get variables.
 //       1. Checks out the selected file to the root folder of the vault.
 //       2. Displays a message box with all of the card variables that can be
 //          updated for the selected file in configuration, @.
 //    d. Click OK.
 //    e. Undoes the check-out of the selected file.
 // 2. Close the Access file variables dialog box.
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

 namespace CardVars_CSharp
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

         public void GetVars_Click(System.Object sender, System.EventArgs e)
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

                 IEdmFile5 aFile = default(IEdmFile5);
                 IEdmFolder5 ppoRetParentFolder = null;
                 aFile = vault2.GetFileFromPath(ListBox.Items[0].ToString(), out ppoRetParentFolder);

                 //Get card variables only from a file checked into the vault
                 if (!aFile.IsLocked)
                 {
                     aFile.LockFile(ppoRetParentFolder.ID, this.Handle.ToInt32(), (int)EdmLockFlag.EdmLock_Simple);

                     IEdmEnumeratorVariable5 varEnum = default(IEdmEnumeratorVariable5);
                     varEnum = aFile.GetEnumeratorVariable();

                     object[] valueList = null;
                     varEnum.GetUpdateVars(aFile.LockedInFolderID, out valueList);

                     int idx = 0;
                     idx = Information.LBound(valueList);
                     int upper = 0;
                     upper = Information.UBound(valueList);

                     string msg = null;
                     msg = "Card variables for " + aFile.Name + " in configuration, @:" + Constants.vbLf + Constants.vbLf;

                     IEdmVariableMgr5 varMgr = default(IEdmVariableMgr5);
                     varMgr = (IEdmVariableMgr5)aFile.Vault;

                     IEdmVariable5 var = default(IEdmVariable5);
                     IEdmVariableValue6 value = default(IEdmVariableValue6);
                     while (idx <= upper)
                     {
                         value = (IEdmVariableValue6)valueList[idx];
                         idx = idx + 1;
                         var = varMgr.GetVariable(value.VariableID);
                         msg = msg + value.VariableName + " = > " + value.GetValue("@").ToString() + Constants.vbLf;
                         msg = msg + "EdmVariableFlags: " + var.Flags + ", EdmVariableType: " + var.VariableType + Constants.vbLf + Constants.vbLf;
                         //msg = msg & "EdmVariableFlags: " & value.VariableFlags & ", EdmVariableType: " & value.VariableType & vbLf & vbLf
                     }

                     MessageBox.Show(msg);

                     aFile.UndoLockFile(this.Handle.ToInt32());
                 }
                 else
                 {
                     //User selected a checked-out file
                     MessageBox.Show("Please select a checked-in file.");
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
     }
 }
```

[Back to top](#top)

```vb
 //Form1.Designer.cs
 namespace CardVars_CSharp
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
             this.GetVars = new System.Windows.Forms.Button();
             this.OpenFileDialog = new System.Windows.Forms.OpenFileDialog();
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
             // BrowseButton
             //
             this.BrowseButton.Location = new System.Drawing.Point(16, 85);
             this.BrowseButton.Name = "BrowseButton";
             this.BrowseButton.Size = new System.Drawing.Size(98, 23);
             this.BrowseButton.TabIndex = 3;
             this.BrowseButton.Text = "Browse...";
             this.BrowseButton.UseVisualStyleBackColor = true;
             this.BrowseButton.Click += new System.EventHandler(this.BrowseButton_Click);
             //
             // ListBox
             //
             this.ListBox.FormattingEnabled = true;
             this.ListBox.HorizontalScrollbar = true;
             this.ListBox.Location = new System.Drawing.Point(16, 114);
             this.ListBox.Name = "ListBox";
             this.ListBox.Size = new System.Drawing.Size(259, 43);
             this.ListBox.TabIndex = 4;
             //
             // GetVars
             //
             this.GetVars.Location = new System.Drawing.Point(84, 178);
             this.GetVars.Name = "GetVars";
             this.GetVars.Size = new System.Drawing.Size(98, 23);
             this.GetVars.TabIndex = 5;
             this.GetVars.Text = "Get variables";
             this.GetVars.UseVisualStyleBackColor = true;
             this.GetVars.Click +=new System.EventHandler(GetVars_Click);
             //
             // OpenFileDialog
             //
             this.OpenFileDialog.Title = "Open";
             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(317, 215);
             this.Controls.Add(this.GetVars);
             this.Controls.Add(this.ListBox);
             this.Controls.Add(this.BrowseButton);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Access file variables";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button BrowseButton;
         internal System.Windows.Forms.ListBox ListBox;
         internal System.Windows.Forms.Button GetVars;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog;
     }
 }
```

[Back to top](#top)
