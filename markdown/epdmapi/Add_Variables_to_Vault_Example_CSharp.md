---
title: "Add Card Variables to Vault Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Add_Variables_to_Vault_Example_CSharp.htm"
---

# Add Card Variables to Vault Example (C#)

This example shows how to add card variables to a vault and edit them.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 //    a. Click File > New > Project > C#, Desktop, Windows > Windows Forms Application.
 //    b. Type AddEditVars_CSharp in Project name.
 //    c. For Location, click ... and navigate to the folder where to create the project.
//    d. Click Next.
//    e. Select Framework.
//    f. Click Create.
 //    g. Click Show All Files in the Solution Explorer toolbar and expand
 //       Form1.cs in the Solution Explorer.
 //    h. Replace the code in Form1.cs with this code.
 //    i. To create the form, replace the code in Form1.Designer.cs with this code.
 // 2. Add dependencies and safely pass arrays of structures.
 // 3. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Add variables to vault dialog box.
 // 2. Select a vault view.
 // 3. Click Add card variables.
 //    a. Adds two card variables, MyNewVar and MySecondVar, to the vault.
 //    b. Displays a message box with the IDs of the new variables.
 //    c. Click OK.
 // 4. Click Edit card variables.
 //    a. Displays the Edit Variables dialog box.
 //    b. Click OK.
 //    c. Displays a message box.
 //    d. Click OK.
 // 5. Close the Add variables to vault dialog box.
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

 namespace AddEditVars_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         private IEdmVault5 vault1 = null;
         IEdmItem item;

         IEdmFile8 fileInt;

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

                 Button1.Enabled = false;

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

         public void AddVaultVars_Click(System.Object sender, System.EventArgs e)
         {
             //Add card variables to vault
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
                     //Log into selected vault as the current user
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 IEdmVariableMgr6 poVarMgr = default(IEdmVariableMgr6);
                 poVarMgr = (IEdmVariableMgr6)vault2.CreateUtility(EdmUtility.EdmUtil_VariableMgr);

                 EdmVariableData[] aoNewVars = new EdmVariableData[2];

                 //Set some properties for the first variable
                 aoNewVars[0].mbsVariableName = "MyNewVar";
                 aoNewVars[0].meType = EdmVariableType.EdmVarType_Text;
                 aoNewVars[0].mlEdmVariableFlags = (int)EdmVariableFlags.EdmVar_Mandatory;
                 EdmAttributeData[] aoAttributes = new EdmAttributeData[1];
                 aoAttributes[0].mbsBlockName = "DrawingBorder";
                 aoAttributes[0].mbsAttribName = "PartNumber";
                 aoAttributes[0].mbsExtensions = "DWG,DXF";
                 aoNewVars[0].mpoAttributes = aoAttributes;

                 //Set some properties for the second variable
                 aoNewVars[1].mbsVariableName = "MySecondVar";
                 aoNewVars[1].meType = EdmVariableType.EdmVarType_Date;

                 //Add the variables
                 poVarMgr.AddVariables(ref aoNewVars);

                 //Show the IDs of the new variables
                 string sMsg = null;
                 sMsg = "";

                 int iIdx = 0;
                 iIdx = aoNewVars.GetLowerBound(0);

                 while (iIdx <= aoNewVars.GetUpperBound(0))
                 {
                     sMsg = sMsg + aoNewVars[iIdx].mbsVariableName + " has ID " + (aoNewVars[iIdx].mlVariableID).ToString() + "\n";
                     iIdx = iIdx + 1;
                 }

                 MessageBox.Show(sMsg);

                 Button1.Enabled = true;

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

         private void Button1_Click(System.Object sender, System.EventArgs e)
         {
             //Edit card variables
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

                 IEdmVariableMgr5 varMgr = default(IEdmVariableMgr5);
                 varMgr = (IEdmVariableMgr5)vault2;
                 if (varMgr.EditVariables(this.Handle.ToInt32()))
                 {
                     MessageBox.Show("An update was made!");
                 }
                 else
                 {
                     MessageBox.Show("No changes were made.");
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
 namespace AddEditVars_CSharp
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
             this.AddVaultVars = new System.Windows.Forms.Button();
             this.OpenFileDialog = new System.Windows.Forms.OpenFileDialog();
             this.Button1 = new System.Windows.Forms.Button();
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
             //AddVaultVars
             //
             this.AddVaultVars.Location = new System.Drawing.Point(16, 86);
             this.AddVaultVars.Name = "AddVaultVars";
             this.AddVaultVars.Size = new System.Drawing.Size(139, 23);
             this.AddVaultVars.TabIndex = 5;
             this.AddVaultVars.Text = "Add card variables";
             this.AddVaultVars.UseVisualStyleBackColor = true;
             this.AddVaultVars.Click +=new System.EventHandler(AddVaultVars_Click);
             //
             //OpenFileDialog
             //
             this.OpenFileDialog.Title = "Open";
             //
             //Button1
             //
             this.Button1.Location = new System.Drawing.Point(16, 127);
             this.Button1.Name = "Button1";
             this.Button1.Size = new System.Drawing.Size(139, 23);
             this.Button1.TabIndex = 6;
             this.Button1.Text = "Edit card variables";
             this.Button1.UseVisualStyleBackColor = true;
             this.Button1.Click +=new System.EventHandler(Button1_Click);
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(243, 185);
             this.Controls.Add(this.Button1);
             this.Controls.Add(this.AddVaultVars);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Add variables to vault";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button AddVaultVars;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog;
         internal System.Windows.Forms.Button Button1;
     }
 }
```

[Back to top](#top)
