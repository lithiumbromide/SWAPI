---
title: "Add Row to Bill of Materials Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Add_Row_to_Bill_of_Materials_Example_CSharp.htm"
---

# Add Row to Bill of Materials Example (C#)

This example shows how to add a row to the named Bill of Materials (BOM) of a file in the vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
   //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 //    a. Click File > New > Project > C#, Windows, Desktop > Windows Forms Application.
 //    b. Type EdmBOM_CSharp in Project name.
 //       c. For Location, click ... and navigate to the folder where to create the project.
//    d. Click Next.
//    e. Select Framework.
//    f. Click Create.
 //    g. Click Show All Files in the Solution Explorer toolbar and expand
 //       Form1.cs in the Solution Explorer.
 //    h. Replace the code in Form1.cs with this code.
 //    i. To create the form, replace the code in  Form1.Designer.cs with
 //       this code.
 // 2.     Add dependencies and safely pass arrays of structures.
 // 3. Ensure that the vault contains the BOM layout.
 //    To inspect the existing layouts:
 //    a. Open the SOLIDWORKS PDM Professional Administration tool.
 //    b. Log into vault_name.
 //    c. Expand vault_name > Bills of Materials.
 //    d. Verify that layout, BOM, exists.
  // 4. Ensure that an assembly and its parts exist in a folder of
 //    the vault.
 // 5. Check in a text file named "temp" in the assembly directory.
 // 6. Modify the path to "temp" in the code.
 // 7. Ensure that a named Bill of Materials exists for the assembly.
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
 // 1. The Bill of Materials dialog box displays.
 //    a. Select a vault_name view.
 //    b. Click Select file.
 //    c. In the Select File dialog:
 //       1. Click the assembly specified in Preconditions step 6.
 //       2. Click Open.
 //    d. Click Get BOM.
 //       Displays message boxes containing:
 //       * Version information for the named BOM.
 //       * Row and column information about a BOM view in the BOM layout
 //         for the selected assembly.
 //    e. Click OK in each message box.
 // 2. Inserts a row for "temp" after the first row in the BOM.
 // 3. Close the Bill of Materials dialog box.
 // 4. Verify the new row in the named BOM of the assembly in vault_name view.
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

 namespace EdmBOM_CSharp
 {
     public partial class Form1 : Form
     {
         private IEdmVault5 vault1 = null;
         IEdmFile7 aFile;
         IEdmBom bom;
         IEdmBomMgr bomMgr;
         IEdmBomView2 bomView;

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

                 if (aFile != null)
                 {

                     bomMgr = (IEdmBomMgr)vault2.CreateUtility(EdmUtility.EdmUtil_BomMgr);
                     EdmBomInfo[] derivedBOMs;
                     aFile.GetDerivedBOMs(out derivedBOMs);
                     int i = 0;
                     int arrSize = derivedBOMs.Length;
                     string str = "";
                     int id;
                     while (i < arrSize)
                     {
                         id = derivedBOMs[i].mlBomID;
                         bom = (IEdmBom)vault2.GetObject(EdmObjectType.EdmObject_BOM, id);
                         str = "Derived BOM: " + derivedBOMs[i].mbsBomName + " " + bom.CheckOutUserID + " " + bom.CurrentState.Name + " " + bom.CurrentVersion + " " + bom.FileID + " " + bom.IsCheckedOut;

                         MessageBox.Show(str);
                         i = i + 1;
                     }

                     bomView = (IEdmBomView2)bom.GetView(0);

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
                         str = "BOM Row " + i + ": " + "\n" + "Item ID: " + ppoRow.GetItemID() + "\n" + "Path name: " + ppoRow.GetPathName() + "\n" + "Tree level: " + ppoRow.GetTreeLevel() + "\n" + " Is locked? " + ppoRow.IsLocked();
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
                         str = "BOM Column " + i + ": " + "\n" + "Header: " + ppoColumns[i].mbsCaption + "\n" + "Column type as defined in EdmBomColumnType: " + ppoColumns[i].meType + "\n" + "ID: " + ppoColumns[i].mlColumnID + "\n" + "Flags: " + ppoColumns[i].mlFlags + "\n" + "Variable ID: " + ppoColumns[i].mlVariableID + "\n" + "Variable type as defined in EdmVariableType: " + ppoColumns[i].mlVariableType + "\n" + "Column width: " + ppoColumns[i].mlWidth;
                         MessageBox.Show(str);
                         i = i + 1;
                     }

                     EdmBomCell ppoNewRow = default(EdmBomCell);
                     string errMsg = "";
                     //object poValue = null;
                     //object poComputedValue = null;
                     //string pbsConfiguration = "";
                     //bool pbReadOnly = false;
                     int plFocusNode = 0;
                     bomView.InsertRow((EdmBomCell)ppoRows[0], EdmBomInsertRowOption.EdmBomInsertRowOption_BelowRow, out ppoNewRow);
                     ppoNewRow.SetVar(ppoColumns[0].mlVariableID, ppoColumns[0].meType, "vault_name\\temp", "", EdmBomSetVarOption.EdmBomSetVarOption_Both, out errMsg);
                     //ppoNewRow.GetVar(ppoColumns[0].mlVariableID, ppoColumns[0].meType, poValue, poComputedValue, pbsConfiguration, pbReadOnly)
                     //MessageBox.Show(poValue.ToString)
                     //MessageBox.Show(poComputedValue.ToString)
                     //MessageBox.Show(pbsConfiguration)
                     //MessageBox.Show(pbReadOnly.ToString)

                     bomView.Commit("", out errMsg, out plFocusNode);

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
 Back to top
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
             this.SelectFiles.Text = "Select file...";
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
             //GetBOM
             //
             this.GetBOM.Location = new System.Drawing.Point(40, 183);
             this.GetBOM.Name = "GetBOM";
             this.GetBOM.Size = new System.Drawing.Size(157, 23);
             this.GetBOM.TabIndex = 6;
             this.GetBOM.Text = "Get BOM";
             this.GetBOM.UseVisualStyleBackColor = true;
             this.GetBOM.Click += new System.EventHandler(this.GetBOM_Click);
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
             this.ClientSize = new System.Drawing.Size(284, 235);
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
     }
 }
Back to top
```
