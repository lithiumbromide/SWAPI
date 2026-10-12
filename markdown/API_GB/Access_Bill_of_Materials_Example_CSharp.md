---
title: "Access Bill of Materials Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Access_Bill_of_Materials_Example_CSharp.htm"
---

# Access Bill of Materials Example (C#)

This example shows how to access the Bill of Materials (BOM) of a file in the vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 //    a. Click File > New > Project > Visual C# > Windows Forms Application.
 //    b. Type EdmBOM_CSharp in Name.
 //    c. Click Browse and navigate to the folder where to create the project.
 //    d. Click OK.
 //    e. Click Show All Files in the Solution Explorer toolbar and expand
 //       Form1.cs in the Solution Explorer.
 //    f. Replace the code in Form1.cs with this code.
 //    g. To create the form, replace the code in  Form1.Designer.cs with
 //       this code.
 // 2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 //    name in the Solution Explorer, click Add Reference, click
 //    Assemblies > Framework in the left-side panel, browse to the top folder
 //    of your SOLIDWORKS PDM Professional installation, locate and click
 //    EPDM.Interop.epdm.dll, click Open, and click  Add).
  // 3. Add Microsoft.VisualBasic as a reference (click COM in the left-side panel,
 //    click Microsoft.VisualBasic, click Add, and click Close).
 // 4. Right-click EPDM.Interop.epdm in References, click Properties, and set
 //    Embed Interop Types to False to handle methods that pass arrays of
 //    structures.
 // 5. Ensure that the vault contains the BOM layout.
 //    To inspect the existing layouts:
 //    a. Open the SOLIDWORKS PDM Professional Administration tool.
 //    b. Log into vault_name.
 //    c. Expand vault_name > Bills of Materials.
 //    d. Verify that layout, BOM, exists.
 // 6. Ensure that an assembly and its parts exist in the root folder of the
 //    vault in default configuration, @.
 // 7. Ensure that one or more named Bills of Materials exist for the assembly.
 //    a. Open File Explorer on a vault_name view.
 //    b. Click the assembly.
 //    c. Click the Bill of Materials tab.
 //    d. Click BOM.
 //    e. If a named Bill of Materials does not exist in the BOM list:
 //       1. Click Save > Save As in the tab toolbar.
 //       2. In the Save As dialog, click  Save.
 // 8. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Opens the Bill of Materials dialog box.
 //    a. Select a vault_name view.
 //    b. Click Select file.
 //    c. In the Select File dialog:
 //       1. Click the assembly specified in Preconditions step 6.
 //       2. Click Open.
 //    d. Click Get BOM Info.
 //       Displays message boxes containing:
 //       * Information about all named BOMs of the assembly.
 //       * Version information for the named BOMs.
 //       * Information about all BOM layouts in the vault.
 //       * Row and column information about a BOM view in the BOM layout
 //         for the selected assembly in its @ configuration.
 //    e. Click OK in each message box.
 //    f. Click Save BOM to CSV.
 //       Saves the BOM to c:\temp\SavedBOM.csv.
 // 2. Close the Bill of Materials dialog box.
 // 3. Verify that c:\temp\SavedBOM.csv is created.
 //----------------------------------------------------------------------------

 //Form1.cs
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using System.IO;
 using System.Xml.Serialization;
 using System.Windows.Forms;
 using System.ComponentModel;
 using EPDM.Interop.epdm;
 using Microsoft.VisualBasic;

 namespace EdmBOM_CSharp
 {
     public partial class Form1 : Form
     {
         private IEdmVault5 vault1 = null;
         IEdmFile7 aFile;
         IEdmBom bom;
         IEdmBomMgr2 bomMgr;
         IEdmBomView3 bomView;

         public Form1()
         {
             InitializeComponent();
         }
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
                     // do nothing
                 }
                 else
                 {
                     IEdmFolder5 ppoRetParentFolder;
                     foreach (string FileName in OpenFileDialog1.FileNames)
                     {
                         File1List.Items.Add(FileName);
                         aFile = (IEdmFile7)vault1.GetFileFromPath(FileName, out ppoRetParentFolder);
                     }
                 }

                GetBOM.Enabled = true;
               SaveBOM.Enabled = false;

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

         public void GetBOM_Click(System.Object sender, System.EventArgs e)
         {

             try
             {
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

               if (aFile != null)
               {
                 // Get named BOMs and their versions for the selected file
                 EdmBomInfo[] derivedBOMs = null;
                 aFile.GetDerivedBOMs(out derivedBOMs);

                 int arrSize = 0;
                 EdmBomVersion[] ppoVersions = null;
                 int i = 0;
                 int j = 0;
                 int id = 0;
                 string str = "";
                 string verstr = "";
                 int verArrSize = 0;
                 arrSize = derivedBOMs.Length;
                int userID = 0;
                bool canSeeLayout = false;
                userID = vault2.GetLoggedInWindowsUserID(vault2.Name);

                 while (i < arrSize)
                 {
                     id = derivedBOMs[i].mlBomID;
                     bom = (IEdmBom)vault2.GetObject(EdmObjectType.EdmObject_BOM, id);
                     str = "Named BOM: " + derivedBOMs[i].mbsBomName + Constants.vbLf + "Type of BOM as defined in EdmBomType: " + derivedBOMs[i].meType + Constants.vbLf + "Check-out user: " + bom.CheckOutUserID + Constants.vbLf + "Current state: " + bom.CurrentState.Name + Constants.vbLf + "Current version: " + bom.CurrentVersion + Constants.vbLf + "ID: " + bom.FileID + Constants.vbLf + "Is checked out: " + bom.IsCheckedOut;
                     MessageBox.Show(str);
                     bom.GetVersions(out ppoVersions);
                     verArrSize = ppoVersions.Length;
                     while (j < verArrSize)
                     {
                         verstr = "BOM version: " + Constants.vbLf + "Type as defined in EdmBomVersionType: " + ppoVersions[j].meType + Constants.vbLf + "Version number: " + ppoVersions[j].mlVersion + Constants.vbLf + "Date: " + ppoVersions[j].moDate + Constants.vbLf + "Label: " + ppoVersions[j].mbsTag + Constants.vbLf + "Comment: " + ppoVersions[j].mbsComment;
                         MessageBox.Show(verstr);
                         j = j + 1;
                     }
                     i = i + 1;
                 }

                 // Get a BOM view with the specified layout
                 bomMgr = (IEdmBomMgr2)vault2.CreateUtility(EdmUtility.EdmUtil_BomMgr);
                 EdmBomLayout2[] ppoRetLayouts = null;
                 EdmBomLayout2 ppoRetLayout = default(EdmBomLayout2);
                 bomMgr.GetBomLayouts2(out ppoRetLayouts);
                 i = 0;
                 arrSize = ppoRetLayouts.Length;
                 str = "";
                 while (i < arrSize)
                 {
                     ppoRetLayout = ppoRetLayouts[i];

                    canSeeLayout = bomMgr.CanSeeBomLayout(userID, ppoRetLayout.mlLayoutID);
                     str = "BOM Layout " + i + ": " + ppoRetLayout.mbsLayoutName + Constants.vbLf + "ID: " + ppoRetLayout.mlLayoutID;
                    str = str + "  Logged-in user can see this layout? " + canSeeLayout;
                     if (ppoRetLayout.mbsLayoutName == "BOM")
                     {
                         bomView = (IEdmBomView3)aFile.GetComputedBOM(ppoRetLayout.mbsLayoutName, 0, "@", (int)EdmBomFlag.EdmBf_AsBuilt + (int)EdmBomFlag.EdmBf_ShowSelected);
                     }
                     MessageBox.Show(str);
                     i = i + 1;
                 }

                 // Display BOM view row and column information
                 object[] ppoRows = null;
                 IEdmBomCell ppoRow = default(IEdmBomCell);
                 bomView.GetRows(out ppoRows);
                 i = 0;
                 arrSize = ppoRows.Length;
                 str = "";
                 while (i < arrSize)
                 {
                     ppoRow = (IEdmBomCell)ppoRows[i];
                     str = "BOM Row " + i + ": " + Constants.vbLf + "Item ID: " + ppoRow.GetItemID() + Constants.vbLf + "Path name: " + ppoRow.GetPathName() + Constants.vbLf + "Tree level: " + ppoRow.GetTreeLevel() + Constants.vbLf + " Is locked? " + ppoRow.IsLocked();
                     MessageBox.Show(str);
                     i = i + 1;
                 }

                 EdmBomColumn[] ppoColumns = null;
                 bomView.GetColumns(out ppoColumns);
                 i = 0;
                 arrSize = ppoColumns.Length;
                 str = "";
                 while (i < arrSize)
                 {
                     str = "BOM Column " + i + ": " + Constants.vbLf + "Header: " + ppoColumns[i].mbsCaption + Constants.vbLf + "Column type as defined in EdmBomColumnType: " + ppoColumns[i].meType + Constants.vbLf + "ID: " + ppoColumns[i].mlColumnID + Constants.vbLf + "Flags: " + ppoColumns[i].mlFlags + Constants.vbLf + "Variable ID: " + ppoColumns[i].mlVariableID + Constants.vbLf + "Variable type as defined in EdmVariableType: " + ppoColumns[i].mlVariableType + Constants.vbLf + "Column width: " + ppoColumns[i].mlWidth;
                     MessageBox.Show(str);
                     i = i + 1;
                 }

                SaveBOM.Enabled = true;

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
         public void SaveBOM_Click(System.Object sender, System.EventArgs e)
         {

             try
             {
                 IEdmVault7 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault9)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 if ((aFile != null) & (bomView != null))
                 {
                     bomView.SaveToCSV("c:\\temp\\SavedBOM.csv", false);

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
 namespace EdmBOM_CSharp
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
             this.GetBOM = new System.Windows.Forms.Button();
             this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
             this.SaveBOM = new System.Windows.Forms.Button();
             this.SuspendLayout();
             //
             // VaultsLabel
             //
             this.VaultsLabel.AutoSize = true;
             this.VaultsLabel.Location = new System.Drawing.Point(36, 24);
             this.VaultsLabel.Name = "VaultsLabel";
             this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
             this.VaultsLabel.TabIndex = 0;
             this.VaultsLabel.Text = "Select vault view:";
             //
             // VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(39, 40);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             // SelectFiles
             //
             this.SelectFiles.Location = new System.Drawing.Point(39, 85);
             this.SelectFiles.Name = "SelectFiles";
             this.SelectFiles.Size = new System.Drawing.Size(191, 23);
             this.SelectFiles.TabIndex = 2;
             this.SelectFiles.Text = "Select file...";
             this.SelectFiles.UseVisualStyleBackColor = true;
             this.SelectFiles.Click += new System.EventHandler(this.SelectFiles_Click);
             //
             // File1List
             //
             this.File1List.FormattingEnabled = true;
             this.File1List.HorizontalScrollbar = true;
             this.File1List.Location = new System.Drawing.Point(40, 114);
             this.File1List.Name = "File1List";
             this.File1List.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended;
             this.File1List.Size = new System.Drawing.Size(220, 43);
             this.File1List.TabIndex = 4;
             //
             // GetBOM
             //
             this.GetBOM.Location = new System.Drawing.Point(40, 183);
             this.GetBOM.Name = "GetBOM";
             this.GetBOM.Size = new System.Drawing.Size(157, 23);
             this.GetBOM.TabIndex = 6;
             this.GetBOM.Text = "Get BOM";
             this.GetBOM.UseVisualStyleBackColor = true;
             this.GetBOM.Enabled = false;
             this.GetBOM.Click += new System.EventHandler(this.GetBOM_Click);
             //
             // OpenFileDialog1
             //
             this.OpenFileDialog1.FileName = "OpenFileDialog1";
             this.OpenFileDialog1.Title = "Select File";
             //
             // SaveBOM
             //
             this.SaveBOM.Location = new System.Drawing.Point(40, 252);
             this.SaveBOM.Name = "SaveBOM";
             this.SaveBOM.Size = new System.Drawing.Size(157, 23);
             this.SaveBOM.TabIndex = 7;
             this.SaveBOM.Text = "Save BOM to CSV";
             this.SaveBOM.UseVisualStyleBackColor = true;
             this.SaveBOM.Enabled = false;
             this.SaveBOM.Click += new System.EventHandler(this.SaveBOM_Click);
             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(284, 363);
             this.Controls.Add(this.SaveBOM);
             this.Controls.Add(this.GetBOM);
             this.Controls.Add(this.File1List);
             this.Controls.Add(this.SelectFiles);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Bill of Materials";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }
         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button SelectFiles;
         internal System.Windows.Forms.ListBox File1List;
         internal System.Windows.Forms.Button GetBOM;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog1;

         #endregion

         private System.Windows.Forms.Button SaveBOM;
     }
 }
```

[Back to top](#top)
