---
title: "Install Add-in Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Load_Addin_Example_CSharp.htm"
---

# Install Add-in Example (C#)

This example shows how to install an add-in, obtain information about it, and uninstall it.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 // 2. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
 // 3. Type AddinMgr_CSharp in Project name.
  // 4. For Location, click ... and navigate to the folder where to create the project.
 // 5. Click Next.
 // 6. Select Framework.
 // 7. Click Create.
 // 8. Click Show All Files in the Solution Explorer toolbar and expand
 //    Form1.cs in the Solution Explorer.
 // 9.  Add dependencies and safely pass arrays of structures.
 //10. Replace the code in Form1.cs with this code.
 //11. Replace the code in Form1.Designer.cs with this code.
 //12. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 //  1. The Install add-in dialog box displays.
 //     a. Select a vault view.
 //     b. Click Browse for add-in.
 //     c. In the Browse for add-ins dialog:
 //        1. Navigate to your add-in directory and click addin_name.dll
 //           and EPDM.Interop.epdm.dll.
 //        2. Click Open.
 //     d. Click Install add-in.
 //        A message box containing information about each add-in installed in
 //        the selected vault displays.
 //     e. Click OK to close each message box.
 //     f. Click Remove add-in.
 //  2. Close the Install add-in dialog box.
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

 namespace AddinMgr_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }

         private IEdmVault5 vault1 = null;
         string addinName = "";

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
                 AddinListBox.Items.Clear();

                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 //Set the initial directory in the Browse for add-ins dialog
                 AddinOpenFileDialog.InitialDirectory = vault1.RootFolderPath;

                 //Show the Browse for add-ins dialog
                 System.Windows.Forms.DialogResult DialogResult;
                 DialogResult = AddinOpenFileDialog.ShowDialog();

                 //If the user did not click Open, exit the subroutine
                 if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
                 {
                     return;
                 }

                 foreach (string FileName in AddinOpenFileDialog.FileNames)
                 {
                     AddinListBox.Items.Add(FileName);
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

         public void LoadAddin_Click(System.Object sender, System.EventArgs e)
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

                 IEdmAddInMgr8 AddinMgr = default(IEdmAddInMgr8);
                 AddinMgr = (IEdmAddInMgr8)vault1;

                 string fileList = "";
                 int fileidx = 1;

                 // Save the path and name of the add-in just installed
                 string justInstalledPathName = "";

                 foreach (string FileName in AddinListBox.Items)
                 {
                     if (!(FileName.Contains("Interop")))
                     {
                         justInstalledPathName = FileName;
                     }

                     if (fileidx == 1)
                     {
                         fileList = FileName;
                     }
                     else
                     {
                         fileList = fileList + "\n" + FileName;
                     }

                     fileidx = fileidx + 1;
                 }

                 AddinMgr.AddAddIns(fileList, (int)EdmAddAddInFlags.EdmAddin_AddAllFilesToOneAddIn, null);

                 // Get information about each of the installed add-ins
                 EdmAddInInfo2[] addIns = null;
                 AddinMgr.GetInstalledAddIns(out addIns);

                 string s = "";
                 int idx = 0;
                 idx = addIns.GetLowerBound(0);

                 while (idx <= addIns.GetUpperBound(0))
                 {
                     s = "Add-in: " + addIns[idx].mbsAddInName + "\n" + "Class: " + addIns[idx].mbsClassID + "\n";
                     s = s + "Company: " + addIns[idx].mbsCompany + "\n" + "Description: " + addIns[idx].mbsDescription + "\n";
                     s = s + "Path: " + addIns[idx].mbsModulePath + "\n" + "Version: " + Convert.ToString(addIns[idx].mlAddInVersion) + "\n";
                     s = s + "Req ver: " + Convert.ToString(addIns[idx].mlRequiredVersionMajor) + "." + Convert.ToString(addIns[idx].mlRequiredVersionMinor);

                     MessageBox.Show(s);
                     // Save the name of the add-in just installed
                     addinName = addIns[idx].mbsAddInName;

                     idx = idx + 1;
                 }

                 // Get information about each of the add-ins installed for debugging
                 EdmAddInInfo2[] debugAddIns = new EdmAddInInfo2[10];
                 AddinMgr.GetDebugAddIns(ref debugAddIns);

                 idx = debugAddIns.GetLowerBound(0);

                 while (idx <= debugAddIns.GetUpperBound(0))
                 {
                     s = "Debug add-in: " + debugAddIns[idx].mbsAddInName + "\n" + "Class: " + debugAddIns[idx].mbsClassID + "\n";
                     s = s + "Company: " + debugAddIns[idx].mbsCompany + "\n" + "Description: " + debugAddIns[idx].mbsDescription + "\n";
                     s = s + "Path: " + debugAddIns[idx].mbsModulePath + "\n" + "Version: " + Convert.ToString(debugAddIns[idx].mlAddInVersion) + "\n";
                     s = s + "Req ver: " + Convert.ToString(debugAddIns[idx].mlRequiredVersionMajor) + "." + Convert.ToString(debugAddIns[idx].mlRequiredVersionMinor);

                     MessageBox.Show(s);
                     idx = idx + 1;
                 }

                 // Get information about the add-in just installed
                 EdmAddInInfo2 poInfo = new EdmAddInInfo2();
                 AddinMgr.GetAddInInfo2(justInstalledPathName, null, ref poInfo);

                 s = "Getting info for add-in: " + poInfo.mbsAddInName + "\n" + "Class: " + poInfo.mbsClassID + "\n";
                 s = s + "Company: " + poInfo.mbsCompany + "\n" + "Description: " + poInfo.mbsDescription + "\n";
                 s = s + "Path: " + poInfo.mbsModulePath + "\n" + "Version: " + Convert.ToString(poInfo.mlAddInVersion) + "\n";
                 s = s + "Req ver: " + Convert.ToString(poInfo.mlRequiredVersionMajor) + "." + Convert.ToString(poInfo.mlRequiredVersionMinor);

                 MessageBox.Show(s);

                 // Extract information about the add-in just installed
                 EdmAddInFileInfo[] ppoFiles = null;
                 EdmAddInMenuInfo[] ppoCmds = null;
                 AddinMgr.GetInstalledAddIn(addinName, "c:\\temp", out poInfo, out ppoFiles, out ppoCmds);

                 string msg = null;
                 msg = "Extracting info for add-in: " + poInfo.mbsAddInName + "\n";
                 msg = msg + "CLSID=" + poInfo.mbsClassID + "\n";
                 msg = msg + "Company=" + poInfo.mbsCompany + "\n";
                 msg = msg + "Module=" + poInfo.mbsModulePath + "\n";
                 msg = msg + "Version=" + Convert.ToString(poInfo.mlAddInVersion) + "\n";
                 msg = msg + "Requires version=" + Convert.ToString(poInfo.mlRequiredVersionMajor) + "." + Convert.ToString(poInfo.mlRequiredVersionMinor);
                 msg = msg + "\n" + "Files:" + "\n";

                 idx = ppoFiles.GetLowerBound(0);
                 while (idx <= ppoFiles.GetUpperBound(0))
                 {
                     msg = msg + ppoFiles[idx].mbsFileName + " Flags=" + Convert.ToString(ppoFiles[idx].mlEdmAddInFileInfoFlags) + "\n";
                     idx = idx + 1;
                 }

                 msg = msg + "\n" + "Commands:" + "\n";

                 idx = ppoCmds.GetLowerBound(0);
                 while (idx <= ppoCmds.GetUpperBound(0))
                 {
                     msg = msg + "'" + ppoCmds[idx].mbsMenuStr + "' Flags=" + Convert.ToString(ppoCmds[idx].mlEdmMenuFlags) + "\n";
                     idx = idx + 1;
                 }

                 vault1.MsgBox(this.Handle.ToInt32(), msg);

                 // Get CAF information about the add-in just installed
                 AddinMgr.GetCAFInfo(poInfo.mbsModulePath, "c:\\temp", out poInfo, out ppoFiles, out ppoCmds);
                 msg = "Getting CAF info for add-in: " + poInfo.mbsAddInName + "\n";
                 msg = msg + "CLSID=" + poInfo.mbsClassID + "\n";
                 msg = msg + "Company=" + poInfo.mbsCompany + "\n";
                 msg = msg + "Module=" + poInfo.mbsModulePath + "\n";
                 msg = msg + "Version=" + Convert.ToString(poInfo.mlAddInVersion) + "\n";
                 msg = msg + "Requires version=" + Convert.ToString(poInfo.mlRequiredVersionMajor) + "." + Convert.ToString(poInfo.mlRequiredVersionMinor);
                 msg = msg + "\n" + "Files:" + "\n";

                 idx = ppoFiles.GetLowerBound(0);
                 while (idx <= ppoFiles.GetUpperBound(0))
                 {
                     msg = msg + ppoFiles[idx].mbsFileName + " Flags=" + Convert.ToString(ppoFiles[idx].mlEdmAddInFileInfoFlags) + "\n";
                     idx = idx + 1;
                 }

                 msg = msg + "\n" + "Commands:" + "\n";

                 idx = ppoCmds.GetLowerBound(0);
                 while (idx <= ppoCmds.GetUpperBound(0))
                 {
                     msg = msg + "'" + ppoCmds[idx].mbsMenuStr + "' flags=" + Convert.ToString(ppoCmds[idx].mlEdmMenuFlags) + "\n";
                     idx = idx + 1;
                 }

                 vault1.MsgBox(this.Handle.ToInt32(), msg);

                 return;

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

         private void button1_Click(object sender, EventArgs e)
         {
             try
             {
                 IEdmAddInMgr9 AddinMgr = default(IEdmAddInMgr9);
                 AddinMgr = (IEdmAddInMgr9)vault1;

                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 AddinMgr.RemoveAddIn(addinName);
                 this.button1.Enabled = false;
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
 namespace AddinMgr_CSharp
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
             this.AddinListBox = new System.Windows.Forms.ListBox();
             this.LoadAddin = new System.Windows.Forms.Button();
             this.AddinOpenFileDialog = new System.Windows.Forms.OpenFileDialog();
             this.button1 = new System.Windows.Forms.Button();
             this.SuspendLayout();
             //
             // VaultsLabel
             //
             this.VaultsLabel.AutoSize = true;
             this.VaultsLabel.Location = new System.Drawing.Point(13, 26);
             this.VaultsLabel.Name = "VaultsLabel";
             this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
             this.VaultsLabel.TabIndex = 0;
             this.VaultsLabel.Text = "Select vault view:";
             //
             // VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(16, 59);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             // BrowseButton
             //
             this.BrowseButton.Location = new System.Drawing.Point(16, 98);
             this.BrowseButton.Name = "BrowseButton";
             this.BrowseButton.Size = new System.Drawing.Size(271, 23);
             this.BrowseButton.TabIndex = 3;
             this.BrowseButton.Text = "Browse for add-in...";
             this.BrowseButton.UseVisualStyleBackColor = true;
             this.BrowseButton.Click += new System.EventHandler(this.BrowseButton_Click);
             //
             // AddinListBox
             //
             this.AddinListBox.FormattingEnabled = true;
             this.AddinListBox.HorizontalScrollbar = true;
             this.AddinListBox.Location = new System.Drawing.Point(16, 151);
             this.AddinListBox.Name = "AddinListBox";
             this.AddinListBox.SelectionMode = System.Windows.Forms.SelectionMode.MultiSimple;
             this.AddinListBox.Size = new System.Drawing.Size(259, 56);
             this.AddinListBox.TabIndex = 4;
             //
             // LoadAddin
             //
             this.LoadAddin.Location = new System.Drawing.Point(16, 230);
             this.LoadAddin.Name = "LoadAddin";
             this.LoadAddin.Size = new System.Drawing.Size(259, 23);
             this.LoadAddin.TabIndex = 5;
             this.LoadAddin.Text = "Install add-in";
             this.LoadAddin.UseVisualStyleBackColor = true;
             this.LoadAddin.Click += new System.EventHandler(this.LoadAddin_Click);
             //
             // AddinOpenFileDialog
             //
             this.AddinOpenFileDialog.Multiselect = true;
             this.AddinOpenFileDialog.Title = "Browse for add-ins";
             //
             // button1
             //
             this.button1.Location = new System.Drawing.Point(16, 260);
             this.button1.Name = "button1";
             this.button1.Size = new System.Drawing.Size(259, 23);
             this.button1.TabIndex = 6;
             this.button1.Text = "Remove add-in";
             this.button1.UseVisualStyleBackColor = true;
             this.button1.Enabled = false;
             this.button1.Click += new System.EventHandler(this.button1_Click);
             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(317, 308);
             this.Controls.Add(this.button1);
             this.Controls.Add(this.LoadAddin);
             this.Controls.Add(this.AddinListBox);
             this.Controls.Add(this.BrowseButton);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Install add-in";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

     }

     #endregion

     private System.Windows.Forms.OpenFileDialog AddinOpenFileDialog;
     private System.Windows.Forms.Label VaultsLabel;
     private System.Windows.Forms.ComboBox VaultsComboBox;
     private System.Windows.Forms.Button BrowseButton;
     private System.Windows.Forms.ListBox AddinListBox;
     private System.Windows.Forms.Button LoadAddin;
     private System.Windows.Forms.Button button1;
     }
 }
```

[Back to top](#top)
