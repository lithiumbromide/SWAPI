---
title: "Get Histories of Files Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Get_Histories_of_Files_Example_CSharp.htm"
---

# Get Histories of Files Example (C#)

This example shows how to update version comments and get histories of files.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
   //----------------------------------------------------------------------------
 // Preconditions:
 //  1. Start Microsoft Visual Studio.
 //     a. Click File > New > Project > Visual C# > Windows Forms Application.
 //     b. Type GetHistories_CSharp in Name.
 //     c. Click Browse and navigate to the folder where to create the project.
 //     d. Click OK.
 //     e. Click Show All Files in the Solution Explorer toolbar and expand
 //        Form1.cs in the Solution Explorer.
 //     f. Replace the code in Form1.cs with this code.
 //     g. To create the form, replace the code in Form1.Designer.cs with
 //        this code.
 //  2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 //     name in the Solution Explorer, click Add Reference, click
 //     Assemblies > Framework in the left-side panel, browse to the top folder of
 //     your SOLIDWORKS PDM Professional installation, locate and click
 //     EPDM.Interop.epdm.dll, click Open, and click Add).
  //  3. Add Microsoft.VisualBasic as a reference (click COM in the left-side
 //     panel, click Microsoft.VisualBasic, click Add, and click Close).
 //  4. Right-click EPDM.Interop.epdm in References, click Properties, and set
 //     Embed Interop Types to False to handle methods that pass arrays of
 //     structures.
 //  5. Ensure that the vault contains a checked-in file with two versions.
 //  6. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
  //  1. Displays the Get histories dialog box.
 //     a. Select a vault view.
 //     b. Click Select a file.
 //     c. In the Select File dialog:
 //        1. Select one or more checked-in vault files.
 //        2. Click Open.
 //        3. Updates all version comments for the selected files to
 //           "New comment".
 //     d. Click Get history.
 //     e. Displays a message box for each history item.
 //     f. Observe the updated version comments.
 //     g. Click OK to close each message box.
 //     h. Click Roll back to first version.
 //        Rolls back the selected file to its first version.
 //     i. Click Get history.
 //        A message box displays one history item.
 //  2. Close the Get histories dialog box.
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

 namespace GetHistories_CSharp
 {

     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         private IEdmVault5 vault1 = null;
         IEdmHistory3 history;
         IEdmHistoryUpdate historyUpdate;
         IEdmFolder5 ppoRetParentFolder;
         IEdmFile5 aFile;
          EdmHistoryItem rollbackItem;

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
                 if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
                 {
                     return;
                 }

                 historyUpdate = (IEdmHistoryUpdate)vault2.CreateUtility(EdmUtility.EdmUtil_HistoryUpdate);

                 foreach (string FileName in OpenFileDialog1.FileNames)
                 {
                     File1List.Items.Add(FileName);
                     aFile = vault1.GetFileFromPath(FileName, out ppoRetParentFolder);
                     // Update all version comments for the selected files
                     historyUpdate.UpdateVersionComment(aFile.ID, -1, "New comment");
                 }

                 historyUpdate.CommitUpdates();

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

         public void GetHistories_Click(System.Object sender, System.EventArgs e)
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

                 history = (IEdmHistory3)vault2.CreateUtility(EdmUtility.EdmUtil_History);

                 foreach (string FileName in OpenFileDialog1.FileNames)
                 {
                     aFile = vault1.GetFileFromPath(FileName, out ppoRetParentFolder);
                     // Add each file selected to the set of files for which to get histories
                     history.AddFile(aFile.ID);
                 }

                 EdmHistoryItem[] ppoRethistory = null;
                 history.GetSortedHistory(ref ppoRethistory, (int)EdmHistoryType.Edmhist_FileVersion);

                 string str = null;
                string evDesc = "";

                 foreach (EdmHistoryItem item in ppoRethistory)
                 {
                    evDesc = history.GetEventDescription(item, (int)EdmLangCode.LanEng);
                     str = "History of " + item.mbsItemName + Constants.vbLf;
                    str = str + "Event description: " + evDesc + Constants.vbLf;
                     str = str + "Type of history record as defined in EdmHistoryType: " + item.meType + Constants.vbLf;
                     str = str + "Date: " + item.moDate + Constants.vbLf;
                     str = str + "Version: " + item.mlVersion + Constants.vbLf;
                     str = str + "User ID: " + item.mlUserID + Constants.vbLf;
                     str = str + "File ID: " + item.mlFileID + Constants.vbLf;
                     str = str + "Folder ID: " + item.mlFolderID + Constants.vbLf;
                     str = str + "User name: " + item.mbsUserName + Constants.vbLf;
                     str = str + "Comment: " + item.mbsComment + Constants.vbLf;
                     str = str + Constants.vbLf;
                     MessageBox.Show(str);
                     rollbackItem = item;
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

         public void Rollback_Click(System.Object sender, System.EventArgs e)
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

                 if (history != null & aFile != null )
                 {
                     history.Rollback(rollbackItem);

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
 namespace GetHistories_CSharp
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
             this.GetHistories = new System.Windows.Forms.Button();
             this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
             this.button1 = new System.Windows.Forms.Button();
             this.SuspendLayout();
             //
             // VaultsLabel
             //
             this.VaultsLabel.AutoSize = true;
             this.VaultsLabel.Location = new System.Drawing.Point(12, 24);
             this.VaultsLabel.Name = "VaultsLabel";
             this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
             this.VaultsLabel.TabIndex = 0;
             this.VaultsLabel.Text = "Select vault view:";
             //
             // VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(15, 40);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             // SelectFiles
             //
             this.SelectFiles.Location = new System.Drawing.Point(15, 85);
             this.SelectFiles.Name = "SelectFiles";
             this.SelectFiles.Size = new System.Drawing.Size(88, 23);
             this.SelectFiles.TabIndex = 2;
             this.SelectFiles.Text = "Select a file...";
             this.SelectFiles.UseVisualStyleBackColor = true;
             this.SelectFiles.Click += new System.EventHandler(this.SelectFiles_Click);
             //
             // File1List
             //
             this.File1List.FormattingEnabled = true;
             this.File1List.HorizontalScrollbar = true;
             this.File1List.Location = new System.Drawing.Point(15, 114);
             this.File1List.Name = "File1List";
             this.File1List.Size = new System.Drawing.Size(257, 56);
             this.File1List.TabIndex = 4;
             //
             // GetHistories
             //
             this.GetHistories.Location = new System.Drawing.Point(64, 193);
             this.GetHistories.Name = "GetHistories";
             this.GetHistories.Size = new System.Drawing.Size(157, 23);
             this.GetHistories.TabIndex = 6;
             this.GetHistories.Text = "Get history";
             this.GetHistories.UseVisualStyleBackColor = true;
             this.GetHistories.Click += new System.EventHandler(this.GetHistories_Click);
             //
             // OpenFileDialog1
             //
             this.OpenFileDialog1.FileName = "OpenFileDialog1";
             this.OpenFileDialog1.Multiselect = false;
             this.OpenFileDialog1.Title = "Select File";
             //
             // button1
             //
             this.button1.Location = new System.Drawing.Point(64, 235);
             this.button1.Name = "button1";
             this.button1.Size = new System.Drawing.Size(157, 23);
             this.button1.TabIndex = 7;
             this.button1.Text = "Roll back to first version";
             this.button1.UseVisualStyleBackColor = true;
             this.button1.Click += new System.EventHandler(this.Rollback_Click);
             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(284, 280);
             this.Controls.Add(this.button1);
             this.Controls.Add(this.GetHistories);
             this.Controls.Add(this.File1List);
             this.Controls.Add(this.SelectFiles);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Get histories";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }
         #endregion
         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button SelectFiles;
         internal System.Windows.Forms.ListBox File1List;
         internal System.Windows.Forms.Button GetHistories;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog1;
         private System.Windows.Forms.Button button1;
     }
 }
```

[Back to top](#top)
