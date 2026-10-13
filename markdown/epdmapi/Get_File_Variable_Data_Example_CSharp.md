---
title: "Get File Variable Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_File_Variable_Data_Example_CSharp.htm"
---

# Get File Variable Data Example (C#)

This example shows how to get the card variable data for the latest version of a selected file.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 // 2. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
 // 3. Type FileVariableData_CSharp in Project name.
 // 4. For Location, click ... and navigate to the folder where to create the project.
 // 5. Click Next.
 // 6. Select Framework.
 // 7. Click Create.
 // 8. Click Show All Files in the Solution Explorer toolbar and expand
 //    Form1.cs in the Solution Explorer.
 // 9.  Add dependencies and safely pass arrays of structures.
 //10. Replace the code in Form1.cs with this code.
 //11. To create the form, replace the code in  Form1.Designer.cs with
 //       this code.
 //12. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the File variable data dialog box.
 // 2. Select a vault view.
 // 3. Click Select file.
 //    a. In the Select File dialog:
 //       1. Click a vault file.
 //       2. Click Open.
 // 4. Click Get variable data.
 // 5. Click OK in the message box.
 // 6. Close the File variable data dialog box.
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

 namespace FileVariableData_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         private IEdmVault5 vault1;
         IEdmFile7 aFile;
         IEdmFolder5 aFolder;

         IEdmEnumeratorVariable7 enumVar;
         public void Form1_Load(System.Object sender, System.EventArgs e)
         {
             try
             {
                 vault1 = new EdmVault5();
                 IEdmVault10 vault = (IEdmVault10)vault1;
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

         public void SelectFile_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 File1List.Items.Clear();

                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }

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
                     // do nothing
                 }
                 else
                 {
                     foreach (string FileName in OpenFileDialog1.FileNames)
                     {
                         File1List.Items.Add(FileName);
                         aFile = (IEdmFile7)vault1.GetFileFromPath(FileName, out aFolder);
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

         public void GetVarData_Click(System.Object sender, System.EventArgs e)
         {

             try
             {
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }

                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 object[] ppoRetVars = null;
                 string[] ppoRetConfs = null;
                 EdmGetVarData poRetDat = new EdmGetVarData();

                 enumVar = (IEdmEnumeratorVariable7)aFile.GetEnumeratorVariable();
                 enumVar.GetVersionVars(0, aFolder.ID, out ppoRetVars, out ppoRetConfs, ref poRetDat);

                 string str = null;
                 str = "File variable data for " + aFile.Name + "\r\n";
                 str = str + "Version: " + poRetDat.mlVersion + "\r\n";
                 str = str + "Latest version: " + poRetDat.mlLatestVersion + "\r\n";
                 str = str + "Revision: " + poRetDat.mbsRevision + "\r\n";
                 str = str + "State: " + poRetDat.mbsState + "\r\n";
                 str = str + "Workflow: " + poRetDat.mbsWorkflow + "r\\n";
                 str = str + "Category: " + poRetDat.mbsCategory + "\r\n";
                 str = str + "SQL Server date format code: " + poRetDat.mlDateFmt + "\r\n";
                 str = str + "EdmGetVarDataFlags: " + poRetDat.mlEdmGetVarDataFlags;

                 MessageBox.Show(str);

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
 namespace FileVariableData_CSharp
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
             this.SelectFile = new System.Windows.Forms.Button();
             this.File1List = new System.Windows.Forms.ListBox();
             this.GetVarData = new System.Windows.Forms.Button();
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
             //SelectFile
             //
             this.SelectFile.Location = new System.Drawing.Point(39, 85);
             this.SelectFile.Name = "SelectFile";
             this.SelectFile.Size = new System.Drawing.Size(157, 23);
             this.SelectFile.TabIndex = 2;
             this.SelectFile.Text = "Select file...";
             this.SelectFile.UseVisualStyleBackColor = true;
             this.SelectFile.Click +=new System.EventHandler(SelectFile_Click);
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
             //GetVarData
             //
             this.GetVarData.Location = new System.Drawing.Point(40, 176);
             this.GetVarData.Name = "GetVarData";
             this.GetVarData.Size = new System.Drawing.Size(107, 23);
             this.GetVarData.TabIndex = 6;
             this.GetVarData.Text = "Get variable data";
             this.GetVarData.UseVisualStyleBackColor = true;
             this.GetVarData.Click +=new System.EventHandler(GetVarData_Click);
             //
             //OpenFileDialog1
             //
             this.OpenFileDialog1.FileName = "OpenFileDialog1";
             this.OpenFileDialog1.Title = "Select File";
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(284, 227);
             this.Controls.Add(this.GetVarData);
             this.Controls.Add(this.File1List);
             this.Controls.Add(this.SelectFile);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "File variable data";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }
         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button SelectFile;
         internal System.Windows.Forms.ListBox File1List;
         internal System.Windows.Forms.Button GetVarData;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog1;

         #endregion
     }
 }
```

[Back to top](#top)
