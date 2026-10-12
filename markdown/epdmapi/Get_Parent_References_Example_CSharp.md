---
title: "Get Parent References of File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_Parent_References_Example_CSharp.htm"
---

# Get Parent References of File Example (C#)

This example shows how to find the parent references of a file.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 // 2. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
 // 3. Type GetParentReferences_CSharp in Project name.
  // 4. For Location, click ... and navigate to the folder where to create the project.
 // 5. Click Next.
 // 6. Select Framework.
 // 7. Click Create.
 // 8. Click Show All Files in the Solution Explorer toolbar and expand
 //    Form1.cs in the Solution Explorer.
 // 9.  Add dependencies and safely pass arrays of structures.
 //10. Replace the code in Form1.cs with this code.
 //11. To create the form, replace the code in Form1.Designer.cs with this code.
 //12. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. The Get parent references dialog displays.
 // 2. Select a vault view.
 // 3. Click Browse for file.
 // 4. Locate and click one of the parts mentioned in Preconditions step 4.
 // 5. Click Open.
 // 6. Click Get parent references.
 // 7. Displays the references of the selected part.
 // 8. Click OK.
 // 9. Close the Get parent references dialog.
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

 namespace GetParentReferences_CSharp
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
                 Listbox.Items.Clear();

                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 if (!vault1.IsLoggedIn)
                 {
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
                     Listbox.Items.Add(FileName);
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

         public void GetParentReferences_Click(System.Object sender, System.EventArgs e)
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

                 IEdmFile5 file = null;
                 IEdmFolder5 parentFolder = null;
                 int i = 0;
                 foreach (string FileName in Listbox.Items)
                 {
                     file = vault2.GetFileFromPath(FileName, out parentFolder);
                     i += 1;
                 }

                 //Get an interface to the reference tree
                 IEdmReference7 @ref = default(IEdmReference7);
                 @ref = (IEdmReference7)file.GetReferenceTree(parentFolder.ID);

                 //Enumerate parent references
                 string msg = null;
                 msg = "Parent references of file '" + file.Name + "':" + "\n";
                 IEdmPos5 pos = default(IEdmPos5);
                 pos = @ref.GetFirstParentPosition2(0, false, (int)EdmRefFlags.EdmRef_File + (int)EdmRefFlags.EdmRef_Item + (int)EdmRefFlags.EdmRef_Dynamic + (int)EdmRefFlags.EdmRef_Static);
                 while (!pos.IsNull)
                 {
                     IEdmReference7 parent = default(IEdmReference7);
                     parent = (IEdmReference7)@ref.GetNextParent(pos);
                     msg = msg + parent.FoundPath + "\n";
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
 namespace GetParentReferences_CSharp
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
             this.Listbox = new System.Windows.Forms.ListBox();
             this.GetParentReferences = new System.Windows.Forms.Button();
             this.OpenFileDialog = new System.Windows.Forms.OpenFileDialog();
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
             this.BrowseButton.Location = new System.Drawing.Point(16, 81);
             this.BrowseButton.Name = "BrowseButton";
             this.BrowseButton.Size = new System.Drawing.Size(121, 23);
             this.BrowseButton.TabIndex = 3;
             this.BrowseButton.Text = "Browse for file...";
             this.BrowseButton.UseVisualStyleBackColor = true;
             this.BrowseButton.Click +=new System.EventHandler(BrowseButton_Click);
             //
             //Listbox
             //
             this.Listbox.FormattingEnabled = true;
             this.Listbox.HorizontalScrollbar = true;
             this.Listbox.Location = new System.Drawing.Point(16, 110);
             this.Listbox.Name = "Listbox";
             this.Listbox.Size = new System.Drawing.Size(259, 43);
             this.Listbox.TabIndex = 4;
             //
             //GetParentReferences
             //
             this.GetParentReferences.Location = new System.Drawing.Point(16, 173);
             this.GetParentReferences.Name = "GetParentReferences";
             this.GetParentReferences.Size = new System.Drawing.Size(121, 23);
             this.GetParentReferences.TabIndex = 5;
             this.GetParentReferences.Text = "Get parent references";
             this.GetParentReferences.UseVisualStyleBackColor = true;
             this.GetParentReferences.Click +=new System.EventHandler(GetParentReferences_Click);
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(289, 215);
             this.Controls.Add(this.GetParentReferences);
             this.Controls.Add(this.Listbox);
             this.Controls.Add(this.BrowseButton);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Get parent references";
             this.Load +=new System.EventHandler(Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button BrowseButton;
         internal System.Windows.Forms.ListBox Listbox;
         internal System.Windows.Forms.Button GetParentReferences;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog;
     }
 }
```

[Back to top](#top)
