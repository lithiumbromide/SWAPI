---
title: "Batch Get and Set Reference Variables Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Batch_Get_and_Set_Reference_Variables_Example_CSharp.htm"
---

# Batch Get and Set Reference Variables Example (C#)

This example shows how to get and set reference variables in one batch.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 //  1. Start Microsoft Visual Studio.
 //     a. Click File > New > Project > C#, Windows, Desktop > Windows Forms Application.
 //     b. Type BatchGetSetRefVariables_CSharp in  Project name.
 //        c. For Location, click ... and navigate to the folder where to create the project.
//     d. Click Next.
//     e. Select Framework.
//     f. Click Create.
 //     g. Click Show All Files in the Solution Explorer toolbar and expand
 //        Form1.cs in the Solution Explorer.
 //     h. Replace the code in Form1.cs with this code.
 //     i. To create the form, replace the code in  Form1.Designer.cs with
 //        this code.
 //  2.     Add dependencies and safely pass arrays of structures.
 //  3. Open the Administration tool.
 //     a. Log into a vault.
 //     b. Double-click Bill of Materials > BOM.
 //     c. Click Description in the Columns list.
 //     d. Select Look for variable in reference specific values.
 //     e. Click OK.
 //  4. Open File Explorer on a vault view.
 //  5. Ensure that an assembly and its referenced parts reside in the vault.
 //  6. Check out the assembly.
 //  7. Click the Bill of Materials tab in the vault view.
 //  8. Select Latest in the Reference Version dropdown.
 //  9. Select @ in the Configuration dropdown.
 // 10. Type a description in Description for each part in the assembly.
 // 11. Click Save on the Bill of Materials toolbar and close the vault view.
 // 12. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 //  1. The Batch Reference Variables dialog box displays.
 //     a. Select a vault view.
 //     b. Click Show all reference variables.
 //        1. In the Select Parent File dialog, select the assembly file identified
 //           in Preconditions step 8 and click Open.
 //        2. In the Select Child File dialog, select a part file referenced by the
 //           assembly file and click Open.
 //            Displays all of the reference variables for all configurations.
 //        3. Click OK in the dialog box.
 //     c. Click Get Description reference variable.
 //        1. In the Select Parent File dialog, select the assembly file identified
 //           in Preconditions step 8 and click Open.
 //        2.  In the Select Child File dialog, select a part file referenced by the
 //           assembly file and click Open.
 //            Displays the current value of reference variable, Description.
 //        3. Click OK in the dialog box.
 //     d. Click Update Description reference variable.
 //        1. In the Select Parent File dialog, select the assembly file identified
 //           in Preconditions step 8 and click Open.
 //        2.  In the Select Child File dialog, select a part file referenced by the
 //           assembly file and click Open.
 //
 //  2. Close the Batch Reference Variables dialog box.
 //  3. Open the vault view and click the assembly.
 //  4. Click the Bill of Materials tab.
 //  5. Select @ in the  Configuration dropdown.
 //  6. Observe the text in the Description column for the updated part.
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

 namespace BatchGetSetRefVariables_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }

         private IEdmVault5 vault = null;
         IEdmFolder5 ppoRetParentFolder;

         public void Form1_Load(System.Object sender, System.EventArgs e)
         {
             try
             {
                 vault = new EdmVault5();
                 IEdmVault8 vault1 = (IEdmVault8)vault;
                 EdmViewInfo[] Views = null;

                 vault1.GetVaultViews(out Views, false);
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

         public void Button1_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 ShowRefVars((IEdmVault11)vault);
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

         public void Button2_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 ShowRefDescription((IEdmVault11)vault);
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

         public void Button3_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 UpdateRefDescription((IEdmVault11)vault);
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

         private void ShowRefVars(IEdmVault11 vault)
         {
             if (vault == null)
             {
                 vault = (IEdmVault11)new EdmVault5();
             }

             if (!vault.IsLoggedIn)
             {
                 vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
             }

             //Let the user select the parent file
             IEdmStrLst5 pathList = default(IEdmStrLst5);
             pathList = (IEdmStrLst5)vault.BrowseForFile(this.Handle.ToInt32(), (int)EdmBrowseFlag.EdmBws_ForOpen + (int)EdmBrowseFlag.EdmBws_PermitVaultFiles, "All Files (*.*)|*.*||", "", "", "", "Select Parent File:");
             if (pathList == null)
                 return;

             IEdmFile8 parent = default(IEdmFile8);

             parent = (IEdmFile8)vault.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition()), out ppoRetParentFolder);

             //Let the user select the child file
             pathList = vault.BrowseForFile(this.Handle.ToInt32(), (int)EdmBrowseFlag.EdmBws_ForOpen + (int)EdmBrowseFlag.EdmBws_PermitVaultFiles, "All Files (*.*)|*.*||", "", "", "", "Select Child File:");
             if (pathList == null)
                 return;

             IEdmFile8 child = default(IEdmFile8);
             child = (IEdmFile8)vault.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition()), out ppoRetParentFolder);

             //Get reference variables in the latest version
             IEdmBatchRefVars batch = default(IEdmBatchRefVars);
             batch = (IEdmBatchRefVars)vault.CreateUtility(EdmUtility.EdmUtil_BatchRefVars);
             EdmRefVar[] vars = null;
             batch.GetAllRefVars(out vars, parent.ID, 0, child.ID);

             //Show the result
             string msg = null;
             msg = "Reference variables:" + "\n" + "\n";
             int idx = 0;
             idx = vars.GetLowerBound(0);
             while (idx <= vars.GetUpperBound(0))
             {
                 msg = msg + "Parent ID: " + (vars[idx].mlParentFileID).ToString() + "\n";
                 msg = msg + "Parent cfg: " + vars[idx].mbsParentCfgName + "\n";
                 msg = msg + "Child ID: " + (vars[idx].mlChildFileID).ToString() + "\n";
                 msg = msg + "Child cfg: " + vars[idx].mbsChildCfgName + "\n";
                 msg = msg + "Status: " + vault.GetErrorMessage(vars[idx].mhResult) + "\n";
                 msg = msg + "Variable ID: " + (vars[idx].mlVarID).ToString() + "\n";
                 msg = msg + "Value: " + (vars[idx].moValue).ToString() + "\n";
                 msg = msg + "\n";
                 idx = idx + 1;
             }

             MessageBox.Show(msg);
         }

         private void ShowRefDescription(IEdmVault11 vault)
         {
             if (vault == null)
             {
                 vault = (IEdmVault11)new EdmVault5();
             }

             if (!vault.IsLoggedIn)
             {
                 vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
             }

             //Let the user select the parent file
             IEdmStrLst5 pathList = default(IEdmStrLst5);
             pathList = vault.BrowseForFile(this.Handle.ToInt32(), (int)EdmBrowseFlag.EdmBws_ForOpen + (int)EdmBrowseFlag.EdmBws_PermitVaultFiles, "All Files (*.*)|*.*||", "", "", "", "Select Parent File:");
             if (pathList == null)
                 return;

             IEdmFile8 parent = default(IEdmFile8);
             parent = (IEdmFile8)vault.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition()), out ppoRetParentFolder);

             //Let the user select the child file
             pathList = vault.BrowseForFile(this.Handle.ToInt32(), (int)EdmBrowseFlag.EdmBws_ForOpen + (int)EdmBrowseFlag.EdmBws_PermitVaultFiles, "All Files (*.*)|*.*||", "", "", "", "Select Child File:");
             if (pathList == null)
                 return;

             IEdmFile8 child = default(IEdmFile8);
             child = (IEdmFile8)vault.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition()), out ppoRetParentFolder);

             //Get the Description variable
             IEdmVariableMgr6 varMgr = default(IEdmVariableMgr6);
             varMgr = (IEdmVariableMgr6)vault.CreateUtility(EdmUtility.EdmUtil_VariableMgr);
             IEdmVariable5 desc = default(IEdmVariable5);
             desc = varMgr.GetVariable("Description");
             if (desc == null)
                 return;

             //Get reference variables in the latest version
             IEdmBatchRefVars batch = default(IEdmBatchRefVars);
             batch = (IEdmBatchRefVars)vault.CreateUtility(EdmUtility.EdmUtil_BatchRefVars);

             EdmRefVar[] vars = new EdmRefVar[1];
             vars[0].mlParentFileID = parent.ID;
             vars[0].mlChildFileID = child.ID;
             vars[0].mbsChildCfgName = "@";
             vars[0].mbsParentCfgName = "@";
             vars[0].mlParentVersion = 0;
             vars[0].mlVarID = desc.ID;

             batch.GetRefVars(ref vars);

             //Show the result to the caller
             string msg = null;
             msg = "Reference variable: " + "Description" + "\n" + "\n";
             msg = msg + "Status: " + vault.GetErrorMessage(vars[0].mhResult) + "\n";
             msg = msg + "Value: " + (vars[0].moValue).ToString();

             MessageBox.Show(msg);

         }

         private void UpdateRefDescription(IEdmVault11 vault)
         {
             if (vault == null)
             {
                 vault = (IEdmVault11)new EdmVault5();
             }

             if (!vault.IsLoggedIn)
             {
                 vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
             }

             //Let the user select the parent file
             IEdmStrLst5 pathList = default(IEdmStrLst5);
             pathList = vault.BrowseForFile(this.Handle.ToInt32(), (int)EdmBrowseFlag.EdmBws_ForOpen + (int)EdmBrowseFlag.EdmBws_PermitVaultFiles, "All Files (*.*)|*.*||", "", "", "", "Select Parent File:");
             if (pathList == null)
                 return;

             IEdmFile8 parent = default(IEdmFile8);
             parent = (IEdmFile8)vault.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition()), out ppoRetParentFolder);

             //Let the user select the child file
             pathList = vault.BrowseForFile(this.Handle.ToInt32(), (int)EdmBrowseFlag.EdmBws_ForOpen + (int)EdmBrowseFlag.EdmBws_PermitVaultFiles, "All Files (*.*)|*.*||", "", "", "", "Select Child File:");
             if (pathList == null)
                 return;

             IEdmFile8 child = default(IEdmFile8);
             child = (IEdmFile8)vault.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition()), out ppoRetParentFolder);

             //Get the Description variable
             IEdmVariableMgr6 varMgr = default(IEdmVariableMgr6);
             varMgr = (IEdmVariableMgr6)vault.CreateUtility(EdmUtility.EdmUtil_VariableMgr);
             IEdmVariable5 desc = default(IEdmVariable5);
             desc = varMgr.GetVariable("Description");
             if (desc == null)
                 return;

             //Get reference variables in the latest version
             IEdmBatchRefVars batch = default(IEdmBatchRefVars);
             batch = (IEdmBatchRefVars)vault.CreateUtility(EdmUtility.EdmUtil_BatchRefVars);

             EdmRefVar[] vars = new EdmRefVar[1];
             vars[0].mlParentFileID = parent.ID;
             vars[0].mlChildFileID = child.ID;
             vars[0].mbsChildCfgName = "@";
             vars[0].mbsParentCfgName = "@";
             vars[0].mlParentVersion = 0;
             vars[0].mlVarID = desc.ID;

             batch.GetRefVars(ref vars);

             //Change the Description variable
             vars[0].moValue = "New description";

             //Store the value back in the reference
             batch.SetRefVars(ref vars);

             MessageBox.Show(vault.GetErrorMessage(vars[0].mhResult));
         }
     }
 }
```

[Back to top](#top)

```vb
 //Form1.Designer.cs
 namespace BatchGetSetRefVariables_CSharp
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
             this.VaultsComboBox = new System.Windows.Forms.ComboBox();
             this.VaultsLabel = new System.Windows.Forms.Label();
             this.Button1 = new System.Windows.Forms.Button();
             this.Button2 = new System.Windows.Forms.Button();
             this.Button3 = new System.Windows.Forms.Button();
             this.SuspendLayout();
             //
             //VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(33, 43);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
             this.VaultsComboBox.TabIndex = 0;
             //
             //VaultsLabel
             //
             this.VaultsLabel.AutoSize = true;
             this.VaultsLabel.Location = new System.Drawing.Point(30, 18);
             this.VaultsLabel.Name = "VaultsLabel";
             this.VaultsLabel.Size = new System.Drawing.Size(100, 13);
             this.VaultsLabel.TabIndex = 1;
             this.VaultsLabel.Text = "Select a vault view:";
             //
             //Button1
             //
             this.Button1.Location = new System.Drawing.Point(33, 84);
             this.Button1.Name = "Button1";
             this.Button1.Size = new System.Drawing.Size(187, 23);
             this.Button1.TabIndex = 2;
             this.Button1.Text = "Show all reference variables...";
             this.Button1.UseVisualStyleBackColor = true;
             this.Button1.Click += new System.EventHandler(Button1_Click);
             //
             //Button2
             //
             this.Button2.Location = new System.Drawing.Point(33, 138);
             this.Button2.Name = "Button2";
             this.Button2.Size = new System.Drawing.Size(187, 24);
             this.Button2.TabIndex = 3;
             this.Button2.Text = "Get Description reference variable...";
             this.Button2.UseVisualStyleBackColor = true;
             this.Button2.Click += new System.EventHandler(Button2_Click);
             //
             //Button3
             //
             this.Button3.Location = new System.Drawing.Point(33, 190);
             this.Button3.Name = "Button3";
             this.Button3.Size = new System.Drawing.Size(208, 23);
             this.Button3.TabIndex = 4;
             this.Button3.Text = "Update Description reference variable...";
             this.Button3.UseVisualStyleBackColor = true;
             this.Button3.Click += new System.EventHandler(Button3_Click);
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(284, 262);
             this.Controls.Add(this.Button3);
             this.Controls.Add(this.Button2);
             this.Controls.Add(this.Button1);
             this.Controls.Add(this.VaultsLabel);
             this.Controls.Add(this.VaultsComboBox);
             this.Name = "Form1";
             this.Text = "Batch Reference Variables";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.Button Button1;
         internal System.Windows.Forms.Button Button2;
         internal System.Windows.Forms.Button Button3;

         #endregion
     }
 }
```

[Back to top](#top)
