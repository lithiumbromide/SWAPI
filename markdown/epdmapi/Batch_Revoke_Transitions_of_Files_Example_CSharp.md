---
title: "Batch Revoke State Transitions of Files Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Batch_Revoke_Transitions_of_Files_Example_CSharp.htm"
---

# Batch Revoke State Transitions of Files Example (C#)

This example shows how to revoke the state transitions of several files in one batch.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 //  1. Start Microsoft Visual Studio.
 //     a. Click File > New > Project > C#, Windows, Desktop > Windows Forms Application.
 //     b. Type BatchChangeFileStates_CSharp in Project name.
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
 //  3. Ensure that:
 //     a. A workflow exists with a No Approval Required transition.
 //     b. One or more vault files are transitioned to the Approved state using the
 //        No Approval Required transition.
 //  4. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 //  1. The Revoke state transitions dialog box displays.
 //     a. Select a vault view.
 //     b. Click Select files for which to revoke transitions.
 //     c. In the Select File dialog:
 //        1. Select a file that transitioned to the Approved state using the
 //           No Approval Required transition.
 //        2. Click Open.
 //  2. Click Revoke transitions.
 //  3. Click OK in the Revoke Transition dialog box.
 //     The selected file's No Approval Required transition is revoked.
 //  4. Close the Revoke state transitions dialog box.
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

 namespace BatchRevokeTransitions_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         private IEdmVault5 vault1 = null;
         IEdmBatchChangeState3 batchChanger;
         IEdmFile5 aFile;
         IEdmFolder5 aFolder;
         IEdmPos5 aPos;
         bool retVal;

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

         public void SelectFiles_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 File1List.Items.Clear();

                 IEdmVault11 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault11)vault1;

                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 //Set the initial directory in the Select File dialog
                 OpenFileDialog1.InitialDirectory = vault1.RootFolderPath;
                 //Show the Select File dialog
                 System.Windows.Forms.DialogResult DialogResult;
                 DialogResult = OpenFileDialog1.ShowDialog();
                 //If the user didn't click Open, exit this subroutine
                 if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
                 {
                     return;
                 }

                 batchChanger = (IEdmBatchChangeState3)vault2.CreateUtility(EdmUtility.EdmUtil_BatchChangeState);
                 IEdmFolder5 ppoRetParentFolder = null;
                 foreach (string FileName in OpenFileDialog1.FileNames)
                 {
                     File1List.Items.Add(FileName);
                     aFile = vault1.GetFileFromPath(FileName, out ppoRetParentFolder);
                     aPos = aFile.GetFirstFolderPosition();
                     aFolder = aFile.GetNextFolder(aPos);
                     // Add each file selected to the batch
                     batchChanger.AddFile(aFile.ID, aFolder.ID);
                 }

                 batchChanger.Comment = "Revoke transitions.";
                 batchChanger.AllowAdminToRevoke(true);
                 //batchChanger.SetRevokeUserID(vault2.GetLoggedInWindowsUserID(vault2.Name))

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

         public void RevokeTransitions_Click(System.Object sender, System.EventArgs e)
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

                 // Get list of files affected by the transition revocation
                 IEdmSelectionList6 selList = default(IEdmSelectionList6);
                 selList = (IEdmSelectionList6)batchChanger.GetFileList((int)EdmChangeStateFileListFlag.Ecsflf_GetChanged);

                 EdmSelectionObject selObject = new EdmSelectionObject();

                 string str = null;
                 int i = 0;
                 aPos = selList.GetHeadPosition();
                 str = "Files affected by this transition revocation: ";
                 i = 0;
                 while (i < selList.Count)
                 {
                     selList.GetNext2(aPos, out selObject);
                     str = str + selObject.mbsPath;
                     i = i + 1;
                 }

                 //MessageBox.Show(str)

                 // Create the file reference tree and verify transition revocation
                 retVal = batchChanger.CreateTreeForRevoke("No Approval Required");

                 bool retVal2 = false;
                 if ((retVal))
                 {
                     // Show all of the items in the batch
                     retVal2 = batchChanger.ShowDlg(this.Handle.ToInt32());

                     if ((retVal2))
                     {
                         // Commit all of the items in the batch to the vault
                         batchChanger.ChangeState(this.Handle.ToInt32());
                     }
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
 namespace BatchRevokeTransitions_CSharp
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
             this.SelectFiles = new System.Windows.Forms.Button();
             this.File1List = new System.Windows.Forms.ListBox();
             this.RevokeTransitions = new System.Windows.Forms.Button();
             this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
             this.SuspendLayout();
             //
             //VaultsLabel
             //
             this.VaultsLabel.AutoSize = true;
             this.VaultsLabel.Location = new System.Drawing.Point(12, 24);
             this.VaultsLabel.Name = "VaultsLabel";
             this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
             this.VaultsLabel.TabIndex = 0;
             this.VaultsLabel.Text = "Select vault view:";
             //
             //VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(15, 40);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             //SelectFiles
             //
             this.SelectFiles.Location = new System.Drawing.Point(15, 85);
             this.SelectFiles.Name = "SelectFiles";
             this.SelectFiles.Size = new System.Drawing.Size(233, 23);
             this.SelectFiles.TabIndex = 2;
             this.SelectFiles.Text = "Select files for which to revoke transitions...";
             this.SelectFiles.UseVisualStyleBackColor = true;
             this.SelectFiles.Click +=new System.EventHandler(SelectFiles_Click);
             //
             //File1List
             //
             this.File1List.FormattingEnabled = true;
             this.File1List.HorizontalScrollbar = true;
             this.File1List.Location = new System.Drawing.Point(15, 114);
             this.File1List.Name = "File1List";
             this.File1List.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended;
             this.File1List.Size = new System.Drawing.Size(257, 43);
             this.File1List.TabIndex = 4;
             //
             //RevokeTransitions
             //
             this.RevokeTransitions.Location = new System.Drawing.Point(40, 183);
             this.RevokeTransitions.Name = "RevokeTransitions";
             this.RevokeTransitions.Size = new System.Drawing.Size(157, 23);
             this.RevokeTransitions.TabIndex = 6;
             this.RevokeTransitions.Text = "Revoke transitions";
             this.RevokeTransitions.UseVisualStyleBackColor = true;
             this.RevokeTransitions.Click +=new System.EventHandler(RevokeTransitions_Click);
             //
             //OpenFileDialog1
             //
             this.OpenFileDialog1.FileName = "OpenFileDialog1";
             this.OpenFileDialog1.Multiselect = false;
             this.OpenFileDialog1.Title = "Select File";
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(284, 235);
             this.Controls.Add(this.RevokeTransitions);
             this.Controls.Add(this.File1List);
             this.Controls.Add(this.SelectFiles);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Revoke state transitions";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }
         #endregion
         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button SelectFiles;
         internal System.Windows.Forms.ListBox File1List;
         internal System.Windows.Forms.Button RevokeTransitions;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog1;
     }
 }
```

[Back to top](#top)
