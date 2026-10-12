---
title: "Get File's State Transitions Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_Files_State_Transitions_Example_CSharp.htm"
---

# Get File's State Transitions Example (C#)

This example shows how to get a file's current and next possible state transitions.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 // 2. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
 // 3. Type StatesCSharp in Project name.
  // 4. For Location, click ... and navigate to the folder where to create the project.
 // 5. Click Next.
 // 6. Select Framework.
 // 7. Click Create.
 // 8. Click Show All Files in the Solution Explorer toolbar and expand
 //    Form1.cs in the Solution Explorer.
 // 9.  Add dependencies and safely pass arrays of structures.
 //10. Replace the code in Form1.cs with this code.
 //11. To create the form, replace the code in Form1.Designer.cs with
 //    this code.
 //12. Ensure that the vault contains a file in a workflow state.
 //13. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the State Transitions dialog box.
 // 2. Select a vault view.
 // 3. Click Browse.
 // 4. Displays the Select a file dialog box.
 //    a. Select a file in the selected vault.
 //    b. Click Open.
 //    The selected file's path and file name appear
 //    in the Select a file dialog box.
 // 5. Click Get state transitions.
 // 6. Displays a message box showing the name of the selected
 //    file and its current and next possible state transitions.
 // 7. Click OK to close the message box.
 // 8.  Displays a message box showing whether the logged-in user must
 //    add comment when transitioning the selected file to one of its next
 //    possible states.
 // 9. Click OK to close the message box.
 //10. Displays a message box with the archive server log.
 //11. Click OK to close the message box.
 //12. Close the State Transitions dialog box.
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

 namespace StatesCSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }

         IEdmVault5 vault1 = null;
         IEdmFile5 aFile;

         void Form1_Load(System.Object sender, System.EventArgs e)
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

         public void GetTransitionButton_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 //Only create a new vault object
                 //if one hasn't been created yet
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }

                 if (!vault1.IsLoggedIn)
                 {
                     //Log into selected vault as the current user
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 IEdmVault20 vault2;
                 vault2 = (IEdmVault20)vault1;

                 //Get the file's current workflow state
                 IEdmState5 workflowState = default(IEdmState5);
                 workflowState = aFile.CurrentState;

                 //Start an enumeration of the transitions to
                 //and from the file's current workflow state
                 IEdmPos5 pos = default(IEdmPos5);
                 pos = workflowState.GetFirstTransitionPosition();

                 //Make sure current workflow state
                 //has a next transition state
                 //If not, exit application
                 if (pos.IsNull)
                 {
                     MessageBox.Show("No next possible transition states.");
                     return;
                 }

                IEdmTransition10 transition = default(IEdmTransition10);

                 //Get the file's next possible transition to or from
                 //the file's current workflow state
                 transition = (IEdmTransition10)workflowState.GetNextTransition(pos);

                 string message = "Current state for " + aFile.Name + ": " + "\n";
                 message = message + " * " + workflowState.Name + "\n" + "\n";
                 message = message + "Next possible state transitions for " + aFile.Name + ":" + "\n";
                 message = message + "  * " + transition.Name + "\n";
                 //message = message + "    Requires authentication? " + transition.Authentication.ToString() + "\n";

                 //Iterate through the file's remaining next possible state
                 //transitions to or from the file's current workflow state
                 while ((!pos.IsNull))
                 {
                     transition = (IEdmTransition10)workflowState.GetNextTransition(pos);
                     message = message + "  * " + transition.Name + "\n";
                     //message = message + "    Requires authentication? " + transition.Authentication.ToString() + "\n";
                 }

                 //Display a message box showing the file's name and its
                 //next possible state transitions
                 MessageBox.Show(message);

                 IEdmUserMgr10 userMgr;
                 userMgr = (IEdmUserMgr10)vault2.CreateUtility(EdmUtility.EdmUtil_UserMgr);

                 IEdmUser5 user;
                 user = userMgr.GetLoggedInUser();

                 int[] files = new int[1];
                 files[0] = aFile.ID;

                 string[] transitions = new string[1];
                 transitions[0] = transition.Name;  //a possible transition

                 bool[] permBool = new bool[1];
                 permBool = vault2.GetTransitionCommentPermissions(user.ID, files, transitions);

                 message = "Logged-in user, " + user.Name + ", must add a state change comment on " + transition.Name + " for " + aFile.Name + "? " + permBool[0];

                 //Display a message box showing whether the logged-in user must add a comment
                 //when transitioning the file to one of the next possible states
                 MessageBox.Show(message);
                 //Display a message box with the archive server's log
                 string asLog = "";
                 vault2.GetArchiveServerLog(out asLog);
                 message = "Archive server log: " + asLog;
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

         public void BrowseButton_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 //If one hasn't been created yet
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }

                 if (!vault1.IsLoggedIn)
                 {
                     //Log into selected vault as the current user
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }
                 //Set the initial directory in the Select a file dialog
                 OpenFileDialog1.InitialDirectory = vault1.RootFolderPath;
                 //Show the Select a file dialog
                 System.Windows.Forms.DialogResult DialogResult;
                 DialogResult = OpenFileDialog1.ShowDialog();

                 if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
                 {
                     //Do nothing
                 }
                 else
                 {
                     //Browse for a file whose next possible state
                     //transitions to get
                     string fileName = OpenFileDialog1.FileName;
                     FileListBox.Items.Add(fileName);
                     IEdmFolder5 retFolder = default(IEdmFolder5);
                     aFile = vault1.GetFileFromPath(fileName, out retFolder);

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

```vb
Back to top
```

```vb
//Form1.Designer.cs
namespace StatesCSharp
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
             this.FileListBox = new System.Windows.Forms.ListBox();
             this.BrowseButton = new System.Windows.Forms.Button();
             this.GetTransitionButton = new System.Windows.Forms.Button();
             this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
             this.SuspendLayout();
             //
             // VaultsLabel
             //
             this.VaultsLabel.AutoSize = true;
             this.VaultsLabel.Location = new System.Drawing.Point(13, 22);
             this.VaultsLabel.Name = "VaultsLabel";
             this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
             this.VaultsLabel.TabIndex = 0;
             this.VaultsLabel.Text = "Select vault view:";
             //
             // VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(16, 39);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(221, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             // FileListBox
             //
             this.FileListBox.FormattingEnabled = true;
             this.FileListBox.Location = new System.Drawing.Point(16, 96);
             this.FileListBox.Name = "FileListBox";
             this.FileListBox.Size = new System.Drawing.Size(179, 30);
             this.FileListBox.TabIndex = 2;
             //
             // BrowseButton
             //
             this.BrowseButton.Location = new System.Drawing.Point(209, 96);
             this.BrowseButton.Name = "BrowseButton";
             this.BrowseButton.Size = new System.Drawing.Size(75, 23);
             this.BrowseButton.TabIndex = 3;
             this.BrowseButton.Text = "Browse...";
             this.BrowseButton.UseVisualStyleBackColor = true;
             this.BrowseButton.Click += new System.EventHandler(BrowseButton_Click);
             //
             // GetTransitionButton
             //
             this.GetTransitionButton.Location = new System.Drawing.Point(16, 150);
             this.GetTransitionButton.Name = "GetTransitionButton";
             this.GetTransitionButton.Size = new System.Drawing.Size(188, 23);
             this.GetTransitionButton.TabIndex = 4;
             this.GetTransitionButton.Text = "Get next possible state transitions";
             this.GetTransitionButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
             this.GetTransitionButton.UseVisualStyleBackColor = true;
             this.GetTransitionButton.Click += new System.EventHandler(GetTransitionButton_Click);
             //
             //OpenFileDialog1
             //
             this.OpenFileDialog1.FileName = "OpenFileDialog1";
             this.OpenFileDialog1.Multiselect = true;
             this.OpenFileDialog1.Title = "Select a file";
             //

             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(284, 200);
             this.Controls.Add(this.GetTransitionButton);
             this.Controls.Add(this.BrowseButton);
             this.Controls.Add(this.FileListBox);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Workflow State Transitions";
             this.ResumeLayout(false);
             this.PerformLayout();
             this.Load += new System.EventHandler(Form1_Load);

         }

         #endregion

         private System.Windows.Forms.Label VaultsLabel;
         private System.Windows.Forms.ComboBox VaultsComboBox;
         private System.Windows.Forms.ListBox FileListBox;
         private System.Windows.Forms.Button BrowseButton;
         private System.Windows.Forms.Button GetTransitionButton;
         private System.Windows.Forms.OpenFileDialog OpenFileDialog1;
     }
 }
```

```vb
Back to top
```
