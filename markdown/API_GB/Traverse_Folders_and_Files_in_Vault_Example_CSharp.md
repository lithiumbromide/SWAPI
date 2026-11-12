---
title: "Traverse Folders and Files in Vault Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Traverse_Folders_and_Files_in_Vault_Example_CSharp.htm"
---

# Traverse Folders and Files in Vault Example (C#)

This example shows how to recursively traverse all of the folders and files in a vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 //  1. Start Microsoft Visual Studio 2010 or later.
 //  2. Click File > New > Project > Visual C# > Windows Forms Application.
 //  3. Type TraverseFilesFoldersCSharp in Name.
 //  4. Click Browse and navigate to the folder where to create the project.
 //  5. Click OK.
 //  6. Replace the code in Form1.cs with this code.
 //  7. Replace the code in Form1.Designer.cs with this code.
 //  8. If using Microsoft Visual Studio 2012 and .NET Framework 4.5, ensure
 //     that the Prefer 32-bit check box is cleared (right-click the project
 //     name in the Solution Explorer and click Properties. On the Build tab,
 //     if Platform target is set to Any CPU, ensure that Prefer 32-bit is cleared.)
 //  9. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 //     name in the Solution Explorer, click Add Reference, click Browse,
 //     navigate to the top folder of your SOLIDWORKS PDM Professional installation,
 //     locate and select EPDM.Interop.epdm.dll).
 // 10. Right-click EPDM.Interop.epdm in References, click Properties, and set
 //     Embed Interop Types to False to handle methods that pass arrays of
 //     structures.
 // 11. Ensure that the vault contains one or more checked-out files.
 // 12. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays a Traverse Folders and Files dialog.
 // 2. Select a vault.
 // 3. Click Log in, get client log, get checked-out files in vault.
 // 4. Displays a message box with the vault type.
 // 5. Click OK.
 // 6. Populates Client log and Checked-out files.
 // 7. Close the dialog.
 //----------------------------------------------------------------------------

//Form1.cs

 using System;
 using System.Diagnostics;
 using System.Windows.Forms;
 using System.Runtime.InteropServices;
 using EPDM.Interop.epdm;

 namespace TraverseFilesAndFoldersCSharp
 {
     public partial class Form1 : Form
     {
         IEdmVault20 vault;
         public Form1()
         {
             InitializeComponent();
         }

         void TraverseFilesAndFolders_Load(System.Object sender, System.EventArgs e)
         {
             try
             {
                 //Declare and create an instance of IEdmVault5
                 IEdmVault5 vault1 = new EdmVault5();

                 vault = (IEdmVault20)vault1;

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

         private void TraverseFoldersButton_Click(System.Object sender, System.EventArgs e)
         {
             try
             {

                 //Log into selected vault as the current user
                 vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());

                 MessageBox.Show(vault.GetVaultType().ToString(), "Vault type");

                 String log;
                 vault.GetClientLog(out log);
                 textBox1.Text = log;

                 TraverseFolder(vault.RootFolder);

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

         private void TraverseFolder(IEdmFolder5 CurFolder)
         {
             try
             {
                 //Enumerate the files in the folder
                 IEdmPos5 FilePos = default(IEdmPos5);
                 FilePos = CurFolder.GetFirstFilePosition();
                 IEdmFile5 file = default(IEdmFile5);
                 while (!FilePos.IsNull)
                 {
                     file = CurFolder.GetNextFile(FilePos);
                     //Get its checked out status
                     if (file.IsLocked)
                     {
                         listBox1.Items.Add(file.LockPath);
                     }
                 }

                 //Enumerate the sub-folders in the folder
                 IEdmPos5 FolderPos = default(IEdmPos5);
                 FolderPos = CurFolder.GetFirstSubFolderPosition();
                 while (!FolderPos.IsNull)
                 {
                     IEdmFolder5 SubFolder = default(IEdmFolder5);
                     SubFolder = CurFolder.GetNextSubFolder(FolderPos);
                     TraverseFolder(SubFolder);
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
     }
 }
```

```vb
Back to top
```

```vb
//Form1.Designer.cs
 namespace TraverseFilesAndFoldersCSharp
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
             this.TraverseFoldersButton = new System.Windows.Forms.Button();
             this.label1 = new System.Windows.Forms.Label();
             this.label2 = new System.Windows.Forms.Label();
             this.listBox1 = new System.Windows.Forms.ListBox();
             this.textBox1 = new System.Windows.Forms.TextBox();
             this.SuspendLayout();
             //
             // VaultsLabel
             //
             this.VaultsLabel.AutoSize = true;
             this.VaultsLabel.Location = new System.Drawing.Point(25, 30);
             this.VaultsLabel.Name = "VaultsLabel";
             this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
             this.VaultsLabel.TabIndex = 0;
             this.VaultsLabel.Text = "Select vault view:";
             //
             // VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(28, 46);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             // TraverseFoldersButton
             //
             this.TraverseFoldersButton.Location = new System.Drawing.Point(28, 84);
             this.TraverseFoldersButton.Name = "TraverseFoldersButton";
             this.TraverseFoldersButton.Size = new System.Drawing.Size(238, 44);
             this.TraverseFoldersButton.TabIndex = 2;
             this.TraverseFoldersButton.Text = "Log in, get client log, get checked-out files in vault";
             this.TraverseFoldersButton.UseVisualStyleBackColor = true;
             this.TraverseFoldersButton.Click += new System.EventHandler(this.TraverseFoldersButton_Click);
             //
             // label1
             //
             this.label1.AutoSize = true;
             this.label1.Location = new System.Drawing.Point(25, 158);
             this.label1.Name = "label1";
             this.label1.Size = new System.Drawing.Size(53, 13);
             this.label1.TabIndex = 3;
             this.label1.Text = "Client log:";
             //
             // label2
             //
             this.label2.AutoSize = true;
             this.label2.Location = new System.Drawing.Point(29, 349);
             this.label2.Name = "label2";
             this.label2.Size = new System.Drawing.Size(92, 13);
             this.label2.TabIndex = 4;
             this.label2.Text = "Checked-out files:";
             //
             // listBox1
             //
             this.listBox1.FormattingEnabled = true;
             this.listBox1.HorizontalScrollbar = true;
             this.listBox1.Location = new System.Drawing.Point(32, 365);
             this.listBox1.Name = "listBox1";
             this.listBox1.ScrollAlwaysVisible = true;
             this.listBox1.Size = new System.Drawing.Size(234, 147);
             this.listBox1.TabIndex = 5;
             //
             // textBox1
             //
             this.textBox1.Location = new System.Drawing.Point(28, 174);
             this.textBox1.Multiline = true;
             this.textBox1.Name = "textBox1";
             this.textBox1.ScrollBars = System.Windows.Forms.ScrollBars.Both;
             this.textBox1.Size = new System.Drawing.Size(238, 153);
             this.textBox1.TabIndex = 6;
             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(293, 531);
             this.Controls.Add(this.textBox1);
             this.Controls.Add(this.listBox1);
             this.Controls.Add(this.label2);
             this.Controls.Add(this.label1);
             this.Controls.Add(this.TraverseFoldersButton);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Traverse Folders and Files";
             this.Load += new System.EventHandler(this.TraverseFilesAndFolders_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         private System.Windows.Forms.Label VaultsLabel;
         private System.Windows.Forms.ComboBox VaultsComboBox;
         private System.Windows.Forms.Button TraverseFoldersButton;
         private System.Windows.Forms.Label label1;
         private System.Windows.Forms.Label label2;
         private System.Windows.Forms.ListBox listBox1;
         private System.Windows.Forms.TextBox textBox1;
     }
 }
```

```
Back to top
```
