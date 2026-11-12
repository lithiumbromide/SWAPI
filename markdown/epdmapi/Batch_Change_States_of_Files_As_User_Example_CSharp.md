---
title: "Batch Change States of Files As User Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Batch_Change_States_of_Files_As_User_Example_CSharp.htm"
---

# Batch Change States of Files As User Example (C#)

This example shows how to change the states of several files in one batch using other credentials.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 //    a. Click File > New > Project > C#, Windows, Desktop > Windows Forms Application.
 //    b. Type BatchChangeFileStates_CSharp in Project name.
 //    c. For Location, click ... and navigate to the folder where to create the project.
//    d. Click Next.
//    e. Select Framework.
//    f. Click Create.
 //    g. Click Show All Files in the Solution Explorer toolbar and expand
 //       Form1.cs in the Solution Explorer.
 //    h. Replace the code in Form1.cs with this code.
 //    i. To create the form, replace the code in Form1.Designer.cs with
 //       this code.
 // 2. Add dependencies and safely pass arrays of structures.
 // 3. In the Admin Tool ensure that a workflow exists with:
 //    a. A Waiting for Approval state.
 //    b. An Approved state.
  //    c. A Passed Approval transition from the Waiting for Approval state to
 //       the Approved state.
  //    d. One or more vault files in the Waiting for Approval state.
 // 4.  If you want to change states as another user, modify the RunAsUser credentials to match a user in your vault.
 // 5. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. The Approve Files dialog box displays.
 //    a. Select a vault view.
 //    b. Click Select files to approve.
 //    c. In the Select File dialog:
  //       1. Select vault files in the Waiting for Approval state.
 //       2. Click Open.
 //    d. Click Approve all files.
 // 2. Click OK in the Do Transition dialog box.
  //    The selected files change to the Approved state using the Passed Approval
 //    transition.
 // 3. Close the Approve Files dialog box.
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

 namespace BatchChangeFileStates_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }

         private IEdmVault5 vault1 = null;
         IEdmBatchChangeState6 batchChanger;
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

         public void Transition_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 //File1List.Items.Clear()

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
                 OpenFileDialog1.InitialDirectory = vault1.RootFolderPath;
                 //Show the Select File dialog
                 System.Windows.Forms.DialogResult DialogResult;
                 DialogResult = OpenFileDialog1.ShowDialog();
                 //If the user didn't click Open, exit this subroutine
                 if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
                 {
                     return;
                 }

                 batchChanger = (IEdmBatchChangeState4)vault2.CreateUtility(EdmUtility.EdmUtil_BatchChangeState);
                 IEdmFolder5 ppoRetParentFolder;
                 foreach (string FileName in OpenFileDialog1.FileNames)
                 {
                     File1List.Items.Add(FileName);
                     aFile = vault1.GetFileFromPath(FileName, out ppoRetParentFolder);
                     aPos = aFile.GetFirstFolderPosition();
                     aFolder = aFile.GetNextFolder(aPos);
                     // Add each file selected to the batch
                     batchChanger.AddFile(aFile.ID, aFolder.ID);
                 }

                 batchChanger.Comment = "Transition to Approved state.";

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

         public void BatchChange_Click(System.Object sender, System.EventArgs e)
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

                 // Get the available transitions
                 EdmChangeStateTransitionInfo[] ppoTransitions = null;
                 batchChanger.GetAvailableTransitionList(out ppoTransitions);

                 int i = 0;
                 string str = "";
                 while (i <= ppoTransitions.GetUpperBound(0))
                 {
                     if (i == 0)
                     {
                         str = ppoTransitions[i].moName;
                     }
                     else
                     {
                         str = str + ", " + ppoTransitions[i].moName;
                     }
                     i = i + 1;
                 }

                 //MsgBox("Transitions available: " & str)

                 // Get list of files affected by the state transition
                 IEdmSelectionList6 selList = default(IEdmSelectionList6);
                 selList = (IEdmSelectionList6)batchChanger.GetFileList((int)EdmChangeStateFileListFlag.Ecsflf_GetActionUpdated + (int)EdmChangeStateFileListFlag.Ecsflf_GetChanged + (int)EdmChangeStateFileListFlag.Ecsflf_GetUnprocessed);

                 EdmSelectionObject selObject = new EdmSelectionObject();

                 aPos = selList.GetHeadPosition();
                 str = "Files affected by this state transition: ";
                 i = 0;
                 while (i < selList.Count)
                 {
                     selList.GetNext2(aPos, out selObject);
                     str = str + selObject.mbsPath;
                     i = i + 1;
                 }

                 //MsgBox(str)

                 // Create the file reference tree and verify allowed transitions
```

//'''''''''''''''''''''''''''''''''''''RunAsUser API''''''''''''''''''''''''''''''''''''''''''''
// Admin is the logged in user here, but if you uncomment the next line (batchChanger.RunAsUser),
// you will do a state change using the admin_jeda user.
// Change the username and password to match a user that exists in your vault.
// CreateTree, ShowDlg, and ChangeState2 should all be called after RunAsUser.

```vb
                //batchChanger.RunAsUser(Me.Handle.ToInt32(), "Admin_jeda", "abc")
```

retVal = batchChanger.**CreateTree**("Passed Approval");

bool retVal2 = false;
if ((retVal))
{
// Show all of the items in the batch
retVal2 = batchChanger.**ShowDlg**(this.Handle.ToInt32());

if ((retVal2))
{
// User clicked OK; commit all of the items in the batch to the vault
batchChanger.**ChangeState2**(this.Handle.ToInt32(), "");
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

```vb
 Back to top
 //Form1.Designer.cs
 namespace BatchChangeFileStates_CSharp
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
             this.Transition = new System.Windows.Forms.Button();
             this.File1List = new System.Windows.Forms.ListBox();
             this.BatchChange = new System.Windows.Forms.Button();
             this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
             this.SuspendLayout();
             //
             //VaultsLabel
             //
             this.VaultsLabel.AutoSize = true;
             this.VaultsLabel.Location = new System.Drawing.Point(36, 24);
             this.VaultsLabel.Name = "VaultsLabel";
             this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
             this.VaultsLabel.TabIndex = 0;
             this.VaultsLabel.Text = "Select vault view:";
             //
             //VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(39, 40);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             //Transition
             //
             this.Transition.Location = new System.Drawing.Point(39, 85);
             this.Transition.Name = "Transition";
             this.Transition.Size = new System.Drawing.Size(158, 23);
             this.Transition.TabIndex = 2;
             this.Transition.Text = "Select files to approve...";
             this.Transition.UseVisualStyleBackColor = true;
             this.Transition.Click += new System.EventHandler(this.Transition_Click);
             //
             //File1List
             //
             this.File1List.FormattingEnabled = true;
             this.File1List.HorizontalScrollbar = true;
             this.File1List.Location = new System.Drawing.Point(40, 114);
             this.File1List.Name = "File1List";
             this.File1List.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended;
             this.File1List.Size = new System.Drawing.Size(220, 43);
             this.File1List.TabIndex = 4;
             //
             //BatchChange
             //
             this.BatchChange.Location = new System.Drawing.Point(40, 183);
             this.BatchChange.Name = "BatchChange";
             this.BatchChange.Size = new System.Drawing.Size(157, 23);
             this.BatchChange.TabIndex = 6;
             this.BatchChange.Text = "Approve all files";
             this.BatchChange.UseVisualStyleBackColor = true;
             this.BatchChange.Click += new System.EventHandler(this.BatchChange_Click);
             //
             //OpenFileDialog1
             //
             this.OpenFileDialog1.FileName = "OpenFileDialog1";
             this.OpenFileDialog1.Multiselect = true;
             this.OpenFileDialog1.Title = "Select File";
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(284, 235);
             this.Controls.Add(this.BatchChange);
             this.Controls.Add(this.File1List);
             this.Controls.Add(this.Transition);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Approve Files";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button Transition;
         internal System.Windows.Forms.ListBox File1List;
         internal System.Windows.Forms.Button BatchChange;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog1;
     }
 }
 Back to top
```
