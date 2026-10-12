---
title: "Add Files to Vault Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Add_Files_to_Vault_Example_CSharp.htm"
---

# Add Files to Vault Example (C#)

This example shows how to add files to a vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 //    a. Click File > New > Project > C#, Windows, Desktop > Windows Forms Application.
 //    b. Type AddFiles_CSharp in Project name.
 //    c. For Location, click ... and navigate to the folder where to create the project.
//    d. Click Next.
//    e. Select Framework.
//    f. Click Create.
 //    g. Click Show All Files in the Solution Explorer toolbar and expand
 //       Form1.cs in the Solution Explorer.
 //    h. Replace the code in Form1.cs with this code.
 //    i. To create the form, replace the code in Form1.Designer.cs with this code.
  // 2.     Add dependencies and safely pass arrays of structures.
 // 3. Ensure that the vault workflow contains the Waiting for Approval state.
 // 4. Ensure that the vault workflow contains the Submit for Approval transition
 //    to the Waiting for Approval state.
 // 5. Ensure that the logged-in PDM user has permission to move files.
 // 6. Modify password in IEdmFile13::ChangeState3 to
 //    match the password of your logged-in PDM user.
 // 7. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Add files to vault dialog box.
  //    a. Select a vault view.
  //    b. Click Browse.
  //       1. Locate and click three files outside the vault.
   //       2. Click Open.
   //    c. Click Add files.
   //       1. Adds the selected files to the root folder of the vault.
   //       2. Checks in the files.
   //       3. Creates path \temp\files in the root folder.
   //       4. Moves one of the files to subfolder \temp\files.
   //       5. Copies one of the files to subfolder \temp.
   //       6. Changes the state of one of the files in the root folder to
   //          Waiting for Approval.
 // 2. Click OK to close each message box.
 // 3. Examine the vault.
  // 4. Close the Add files to vault dialog box.
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

 namespace AddFiles_CSharp
 {
     public partial class Form1 : Form, IEdmCallback6
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
                 IEdmVault16 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault16)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     //Log into selected vault as the current user
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 if (!(ListBox.Items.Count == 3))
                 {
                     MessageBox.Show("Please click three files that are not in the vault.");
                     return;
                 }

                 //MessageBox.Show("Vault type as defined in EdmVaultType: " + vault2.GetVaultType().ToString());

                 IEdmFile13 aFile = default(IEdmFile13);

                 // Add selected files to the root folder of the vault
                 IEdmFolder9 Folder = default(IEdmFolder9);
                 Folder = (IEdmFolder9)vault2.RootFolder;

                 EdmAddFileInfo[] Files = new EdmAddFileInfo[3];

                 string[] FileNames = new string[3];
                 int Index = 0;
                 string fileStr = "";
                 foreach (Object FileName_loopVariable in ListBox.Items)
                 {
                     fileStr = FileName_loopVariable.ToString();
                     FileNames[Index] = fileStr.Substring(fileStr.LastIndexOf("\\"));
                     Index = Index + 1;
                 }

                 string Path = "";
                 Index = 0;
                 foreach (Object FileName_loopVariable in ListBox.Items)
                 {
                     Path = FileName_loopVariable.ToString();
                     Files[Index].mbsPath = Path;
                     Files[Index].mlEdmAddFlags = (int)EdmAddFlag.EdmAdd_Simple;
                     Files[Index].mlFileID = 0;
                     Files[Index].mlSrcDocumentID = 0;
                     Files[Index].mlSrcProjectID = 0;
                     Files[Index].mbsNewName = "";
                     Index = Index + 1;
                 }

                 Folder.AddFiles(this.Handle.ToInt32(), ref Files, this);

                 // Check in the files
                 IEdmFile13[] arrFiles = new IEdmFile13[3];
                 Index = 0;
                 fileStr = "";
                 IEdmFolder5 ppoRetParentFolder;
                 foreach (Object FileName_loopVariable in FileNames)
                 {
                     fileStr = FileName_loopVariable.ToString();
                     aFile = (IEdmFile13)vault2.GetFileFromPath(Folder.LocalPath + "\\" + fileStr, out ppoRetParentFolder);
                     //MessageBox.Show("User can rename " + aFile.Name + " in this folder? " + Folder.HasRenameRights(this.Handle.ToInt32(), aFile.ID, fileStr, "new", true).ToString());
                     //MessageBox.Show(aFile.Name + " is in a private state? " + aFile.PrivateStateFile.ToString());
                     int ID;
                     string fName;
                     string vaultName;
                     IEdmVault5 vaultObject;
                     ID = aFile.ID;
                     fName = aFile.Name;
                     vaultObject = aFile.Vault;
                     vaultName = vaultObject.Name;
                     MessageBox.Show("Database ID: " + ID.ToString() + "; Vault name: " + vaultName + "; Folder name: " + fName);

                     aFile.UnlockFile(this.Handle.ToInt32(), "");
                     arrFiles[Index] = aFile;
                     Index = Index + 1;
                 }

                 // Create \temp\files subfolder under the root folder
                 Folder.CreateFolderPath("\\temp\\files", this.Handle.ToInt32());

                 // Move one of the files to the \temp\files subfolder
                 IEdmFolder5 dest = default(IEdmFolder5);
                 dest = vault2.GetFolderFromPath(Folder.LocalPath + "\\temp\\files");
                 aFile = arrFiles[0];
                 aFile.Move(this.Handle.ToInt32(), Folder.ID, dest.ID, 0);

                 // Copy one of the files to the \temp subfolder
                 aFile = arrFiles[1];
                 aFile.GetFileCopy(this.Handle.ToInt32(), "", Folder.LocalPath + "\\temp\\");

                 // Change the state of one of the files to Waiting for Approval
                 aFile = arrFiles[2];
                 aFile.ChangeState3("Waiting for Approval", "Submit for Approval", Folder.ID, "The file is waiting for approval.", this.Handle.ToInt32(), (int)EdmStateFlags.EdmState_Simple, "password");

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

        private EdmMBoxResult IEdmCallback6_MsgBox(int lParentWnd, int lMsgID, string bsMsg, EdmMBoxType eType = 0L)
        {
            MessageBox.Show(bsMsg);
            return EdmMBoxResult.EdmMbr_OK;
        }
        EdmMBoxResult IEdmCallback6.MsgBox(int lParentWnd, int lMsgID, string bsMsg, EdmMBoxType eType )
        {
            return IEdmCallback6_MsgBox(lParentWnd, lMsgID, bsMsg, eType);
        }

        private void IEdmCallback6_Resolve(int lParentWnd, ref EdmCmdData[] ppoItems)
        {
        }
        void IEdmCallback6.Resolve(int lParentWnd, ref EdmCmdData[] ppoItems)
        {
            IEdmCallback6_Resolve(lParentWnd, ref ppoItems);
        }

        private bool IEdmCallback6_SetProgress(int lBarIndex, int lPos, string bsMsg)
        {
            return true;
        }
        bool IEdmCallback6.SetProgress(int lBarIndex, int lPos, string bsMsg)
        {
            return IEdmCallback6_SetProgress(lBarIndex, lPos, bsMsg);
        }

        private void IEdmCallback6_SetProgressRange(int lBarIndex, int lMax)
        {
        }
        void IEdmCallback6.SetProgressRange(int lBarIndex, int lMax)
        {
            IEdmCallback6_SetProgressRange(lBarIndex, lMax);
        }

        private void IEdmCallback6_SetStatusMessage(int lBarIndex, string bsMessage)
        {
        }
        void IEdmCallback6.SetStatusMessage(int lBarIndex, string bsMessage)
        {
            IEdmCallback6_SetStatusMessage(lBarIndex, bsMessage);
        }
    }
}
```

[Back to top](#top)

```vb
 //Form1.Designer.cs
 namespace AddFiles_CSharp
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
             this.AddFiles = new System.Windows.Forms.Button();
             this.OpenFileDialog = new System.Windows.Forms.OpenFileDialog();
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
             this.BrowseButton.Size = new System.Drawing.Size(98, 23);
             this.BrowseButton.TabIndex = 3;
             this.BrowseButton.Text = "Browse...";
             this.BrowseButton.UseVisualStyleBackColor = true;
             this.BrowseButton.Click +=new System.EventHandler(BrowseButton_Click);
             //
             //ListBox
             //
             this.ListBox.FormattingEnabled = true;
             this.ListBox.HorizontalScrollbar = true;
             this.ListBox.Location = new System.Drawing.Point(16, 114);
             this.ListBox.Name = "ListBox";
             this.ListBox.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended;
             this.ListBox.Size = new System.Drawing.Size(259, 43);
             this.ListBox.TabIndex = 4;
             //
             //AddFiles
             //
             this.AddFiles.Location = new System.Drawing.Point(84, 178);
             this.AddFiles.Name = "AddFiles";
             this.AddFiles.Size = new System.Drawing.Size(98, 23);
             this.AddFiles.TabIndex = 5;
             this.AddFiles.Text = "Add files";
             this.AddFiles.UseVisualStyleBackColor = true;
             this.AddFiles.Click +=new System.EventHandler(AddFiles_Click);
             //
             //OpenFileDialog
             //
             this.OpenFileDialog.Multiselect = true;
             this.OpenFileDialog.Title = "Open";
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(317, 215);
             this.Controls.Add(this.AddFiles);
             this.Controls.Add(this.ListBox);
             this.Controls.Add(this.BrowseButton);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Add files to vault";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button BrowseButton;
         internal System.Windows.Forms.ListBox ListBox;
         internal System.Windows.Forms.Button AddFiles;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog;
     }
 }
```

[Back to top](#top)
