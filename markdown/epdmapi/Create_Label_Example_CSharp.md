---
title: "Create Labels on Folders Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Create_Label_Example_CSharp.htm"
---

# Create Labels on Folders Example (C#)

This example shows how to create a label on a folder and all of its subfolders and files.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 //    a. Click File > New > Project > Visual C# > Windows Forms Application.
 //    b. Type CreateLabel_CSharp in Name.
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
 // 3. Right-click EPDM.Interop.epdm in References, click Properties, and set
 //    Embed Interop Types to False to handle methods that pass arrays of
 //    structures.
 // 4. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Create label dialog box.
  //    a. Select a vault view.
  //    b. Click Browse for parent folder.
  //       1. Locate and click a folder in the vault.
   //       2. Click OK.
   //    c. Click Create label.
   //       1. Creates label, MyCompany, on the selected folder and all of its
   //          subfolders and files.
   //       2. Displays a message box with information about all of the labels
   //          on the selected folder.
   //       3. Click OK.
  // 2. Close the Create label dialog box.
 // 3. To verify label creation on a folder or file, open a view on the
 //    selected vault, click either a folder or a file, and click
 //    Display > History.
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

 namespace CreateLabel_CSharp
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

         public void CreateLabel_Click(System.Object sender, System.EventArgs e)
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

                 int labelID = 0;
                 string labelName = "MyCompany";
                 labelID = parentFolder.CreateLabel(labelName, "Label set by test program", true);

                 IEdmPos5 pos = default(IEdmPos5);
                 IEdmLabel5 label = default(IEdmLabel5);
                 string message = null;
                 message = "The following labels have been set on folder " + parentFolder.Name + ":" + "\n";
                 pos = parentFolder.GetFirstLabelPosition();
                 while (!pos.IsNull)
                 {
                     label = (IEdmLabel5)parentFolder.GetNextLabel(pos);
                     message = message + label.Name + " (" + label.Comment + ")" + " created by " + label.User.Name + "(ID = " + label.UserID + ")" + " at " + label.Time + "\n";
                 }

                 MessageBox.Show(message);

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
 namespace CreateLabel_CSharp
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
             this.CreateLabel = new System.Windows.Forms.Button();
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
             //CreateLabel
             //
             this.CreateLabel.Location = new System.Drawing.Point(84, 178);
             this.CreateLabel.Name = "CreateLabel";
             this.CreateLabel.Size = new System.Drawing.Size(98, 23);
             this.CreateLabel.TabIndex = 5;
             this.CreateLabel.Text = "Create label";
             this.CreateLabel.UseVisualStyleBackColor = true;
             this.CreateLabel.Click +=new System.EventHandler(CreateLabel_Click);
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(317, 215);
             this.Controls.Add(this.CreateLabel);
             this.Controls.Add(this.ListBox);
             this.Controls.Add(this.BrowseButton);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Create label";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button BrowseButton;
         internal System.Windows.Forms.ListBox ListBox;
         internal System.Windows.Forms.Button CreateLabel;
         internal System.Windows.Forms.FolderBrowserDialog FolderBrowserDialog1;
     }
 }
```

[Back to top](#top)
