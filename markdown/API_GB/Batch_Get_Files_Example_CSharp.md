---
title: "Batch Check Out Files Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Batch_Get_Files_Example_CSharp.htm"
---

# Batch Check Out Files Example (C#)

This example shows how to check out several files from the vault in one batch.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 //    a. Click File > New > Project > Visual C# > Windows Forms Application.
 //    b. Type BatchGetFiles_CSharp in Name.
 //    c. Click Browse and navigate to the folder where to create the project.
 //    d. Click OK.
 //    e. Click Show All Files in the Solution Explorer toolbar and expand
 //       Form1.cs in the Solution Explorer.
 //    f. Replace the code in Form1.cs with this code.
 //    g. To create the form, replace the code in  Form1.Designer.cs with
 //       this code.
 // 2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 //    name in the Solution Explorer, click Add Reference, click
 //    Assemblies > Framework in the left-side panel, browse to the top folder of
 //    your SOLIDWORKS PDM Professional installation, locate and click
 //    EPDM.Interop.epdm.dll, click Open, and click  Add).
  // 3. Add Microsoft.VisualBasic as a reference (click
 //    COM in the left-side panel, click
 //    Microsoft.VisualBasic, click Add, and click Close).
 // 4. Right-click EPDM.Interop.epdm in References, click Properties, and set
 //    Embed Interop Types to False to handle methods that pass arrays of
 //    structures.
 // 5. Ensure that the vault contains at least one checked-in file.
 // 6. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 //  1. The Check Out Files dialog box displays.
 //     a. Select a vault view.
 //     b. Click Select files to check out from vault.
 //     c. In the Select File dialog:
 //        1. Click a couple of files inside the vault.
 //        2. Click Open.
 //     d. Click Check out files from vault.
 //  2. Click Check Out in the Check Out dialog box.
 //  3. Close the Check Out Files dialog box.
 //  4. Observe that the selected files are checked out of the selected vault.
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
 namespace BatchGetFiles_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         private IEdmVault5 vault1 = null;
         IEdmBatchGet batchGetter;
         IEdmSelectionList6 fileList = null;
         EdmSelectionObject poSel;
         EdmSelItem[] ppoSelection = null;
         int fileCount = 0;
         IEdmFile5 aFile;
         IEdmFolder5 aFolder;
         IEdmFolder5 ppoRetParentFolder;
         IEdmPos5 aPos;
         string str;
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

                 batchGetter = (IEdmBatchGet)vault2.CreateUtility(EdmUtility.EdmUtil_BatchGet);

                 //Convert the selected files to an
                 //array of EdmSelItem structs
                 int nbrFiles = 0;
                 nbrFiles = OpenFileDialog1.Filenames.Count;
                 Array.Resize(ref ppoSelection, nbrFiles);

                 //If the user didn't click Open, no files were selected
                 if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
                 {
                     // do nothing
                 }
                 else
                 {
                     int i = 0;
                     foreach (string FileName in OpenFileDialog1.FileNames)
                     {
                         File1List.Items.Add(FileName);
                         aFile = vault1.GetFileFromPath(FileName, out ppoRetParentFolder);
                         aPos = aFile.GetFirstFolderPosition();
                         aFolder = aFile.GetNextFolder(aPos);
                         ppoSelection[i] = new EdmSelItem();
                         ppoSelection[i].mlDocID = aFile.ID;
                         ppoSelection[i].mlProjID = aFolder.ID;
                         i = i + 1;
                     }
                     // Add selections to the batch of files to check out
                     batchGetter.AddSelection((EdmVault5)vault1, ref ppoSelection);
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

         public void BatchGet_Click(System.Object sender, System.EventArgs e)
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

                 if ((batchGetter != null))
                 {
                     batchGetter.CreateTree(this.Handle.ToInt32(), (int)EdmGetCmdFlags.Egcf_Lock);

                     fileCount = batchGetter.FileCount;
                     fileList = (IEdmSelectionList6)batchGetter.GetFileList((int)EdmGetFileListFlag.Egflf_GetLocked + (int)EdmGetFileListFlag.Egflf_GetFailed + (int)EdmGetFileListFlag.Egflf_GetRetrieved + (int)EdmGetFileListFlag.Egflf_GetUnprocessed);

                     aPos = fileList.GetHeadPosition();

                     str = "Getting " + fileCount + " files: ";
                     while (!(aPos.IsNull))
                     {
                         fileList.GetNext2(aPos, out poSel);
                         str = str + Constants.vbLf + poSel.mbsPath;
                     }

                     //MsgBox(str)

                     retVal = batchGetter.ShowDlg(this.Handle.ToInt32());
                     // No dialog if checking out only one file

                     if ((retVal))
                     {
                         batchGetter.GetFiles(this.Handle.ToInt32(), null);
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
 namespace BatchGetFiles_CSharp
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
             this.BatchGet = new System.Windows.Forms.Button();
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
             //SelectFiles
             //
             this.SelectFiles.Location = new System.Drawing.Point(39, 85);
             this.SelectFiles.Name = "SelectFiles";
             this.SelectFiles.Size = new System.Drawing.Size(191, 23);
             this.SelectFiles.TabIndex = 2;
             this.SelectFiles.Text = "Select files to check out from vault...";
             this.SelectFiles.UseVisualStyleBackColor = true;
             this.SelectFiles.Click += new System.EventHandler(SelectFiles_Click);
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
             //BatchGet
             //
             this.BatchGet.Location = new System.Drawing.Point(40, 183);
             this.BatchGet.Name = "BatchGet";
             this.BatchGet.Size = new System.Drawing.Size(157, 23);
             this.BatchGet.TabIndex = 6;
             this.BatchGet.Text = "Check out files from vault";
             this.BatchGet.UseVisualStyleBackColor = true;
             this.BatchGet.Click += new System.EventHandler(this.BatchGet_Click);
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
             this.Controls.Add(this.BatchGet);
             this.Controls.Add(this.File1List);
             this.Controls.Add(this.SelectFiles);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Check Out Files";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }
         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button SelectFiles;
         internal System.Windows.Forms.ListBox File1List;
         internal System.Windows.Forms.Button BatchGet;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog1;

         #endregion
     }
 }
```

[Back to top](#top)
