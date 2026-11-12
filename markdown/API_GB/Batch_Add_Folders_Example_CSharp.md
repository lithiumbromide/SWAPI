---
title: "Batch Add Folders Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Batch_Add_Folders_Example_CSharp.htm"
---

# Batch Add Folders Example (C#)

This example shows how to create several folders in the vault at once.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio 2010.
 //    a. Click File > New > Project > Visual C# > Windows Forms Application.
 //    b. Type BatchAddFolders_CSharp in Name.
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
 // 1. Displays the Add folders dialog box.
  //    a. Select a vault view.
  //    b. Type the name of a new folder to create in the root folder
 //       of the vault.
   //    c. Click Add folder to the batch.
   //       1. Displays a message that the folder is added to the batch.
   //       2. Click OK.
  // 2. Repeat steps 1b-c repeatedly to add more folders to the batch.
 // 3. Click Create folders.
 //    a. Displays a message that the folder is created.
 //    b. Click OK in each message box.
 // 4. Close the Add folders dialog box.
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
 using Microsoft.VisualBasic;
 using EPDM.Interop.epdm;

 namespace BatchAddFolders_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         private IEdmVault5 vault1 = null;
         IEdmBatchAddFolders batchAddFolders;
         EdmFolderInfo[] ppoRetFolders = null;

         int i;

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

         private void AddFolders_Click(System.Object sender, System.EventArgs e)
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

                 if (batchAddFolders == null)
                 {
                     batchAddFolders = (IEdmBatchAddFolders)vault2.CreateUtility(EdmUtility.EdmUtil_BatchAddFolders);
                 }

                 batchAddFolders.AddFolder(vault2.RootFolderID, TextBox1.Text, i, (int)EdmBatchAddFolderFlag.Ebaff_GetInterface, null, 0);
                 i = i + 1;

                 Interaction.MsgBox(TextBox1.Text + " added to the batch.");
                 TextBox1.Clear();

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

         public void CreateFolders_Click(System.Object sender, System.EventArgs e)
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

                 batchAddFolders.Create(this.Handle.ToInt32(), ref ppoRetFolders, (int)EdmBatchCreateFolderFlag.Ebcf_Nothing);

                 foreach (EdmFolderInfo FoldName in ppoRetFolders)
                 {
                     Interaction.MsgBox("Created " + FoldName.mbsPath + " successfully" + " in " + vault2.RootFolder.Name);
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
 namespace BatchAddFolders_CSharp
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
             this.AddFolders = new System.Windows.Forms.Button();
             this.CreateFolders = new System.Windows.Forms.Button();
             this.TextBox1 = new System.Windows.Forms.TextBox();
             this.Label1 = new System.Windows.Forms.Label();
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
             //AddFolders
             //
             this.AddFolders.Location = new System.Drawing.Point(16, 112);
             this.AddFolders.Name = "AddFolders";
             this.AddFolders.Size = new System.Drawing.Size(145, 23);
             this.AddFolders.TabIndex = 3;
             this.AddFolders.Text = "Add folder to the batch...";
             this.AddFolders.UseVisualStyleBackColor = true;
             this.AddFolders.Click +=new System.EventHandler(AddFolders_Click);
             //
             //CreateFolders
             //
             this.CreateFolders.Location = new System.Drawing.Point(111, 156);
             this.CreateFolders.Name = "CreateFolders";
             this.CreateFolders.Size = new System.Drawing.Size(98, 23);
             this.CreateFolders.TabIndex = 5;
             this.CreateFolders.Text = "Create folders";
             this.CreateFolders.UseVisualStyleBackColor = true;
             this.CreateFolders.Click +=new System.EventHandler(CreateFolders_Click);
             //
             //TextBox1
             //
             this.TextBox1.Location = new System.Drawing.Point(16, 88);
             this.TextBox1.Name = "TextBox1";
             this.TextBox1.Size = new System.Drawing.Size(289, 20);
             this.TextBox1.TabIndex = 6;
             //
             //Label1
             //
             this.Label1.AutoSize = true;
             this.Label1.Location = new System.Drawing.Point(13, 72);
             this.Label1.Name = "Label1";
             this.Label1.Size = new System.Drawing.Size(237, 13);
             this.Label1.TabIndex = 7;
             this.Label1.Text = "Type name of new folder to add to the vault root:";
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(317, 208);
             this.Controls.Add(this.Label1);
             this.Controls.Add(this.TextBox1);
             this.Controls.Add(this.CreateFolders);
             this.Controls.Add(this.AddFolders);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Add folders";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button AddFolders;
         internal System.Windows.Forms.Button CreateFolders;
         internal System.Windows.Forms.TextBox TextBox1;
         internal System.Windows.Forms.Label Label1;
     }
 }
```

[Back to top](#top)
