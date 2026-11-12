---
title: "Get Files in Workflow State Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Get_Files_in_State_Example_CSharp.htm"
---

# Get Files in Workflow State Example (C#)

This example shows how to get all of the files in a particular workflow state.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio 2010.
 //    a. Click File > New > Project > Visual C# > Windows Forms Application.
 //    b. Type GetFilesInState_CSharp in Name.
 //    c. Click Browse and navigate to the folder where to create
 //       the project.
 //    d. Click OK.
 //    e. Click Show All Files in the Solution Explorer toolbar and expand
 //       Form1.cs in the Solution Explorer.
 //    f. Replace the code in Form1.cs with this code.
 //    g. To create the form, replace the code in Form1.Designer.cs with this code.
 // 2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 //    name in the Solution Explorer, click Add Reference, click
 //    Assemblies > Framework in the left-side panel, browse to the top folder of
 //    your SOLIDWORKS PDM Professional installation, locate and click
 //    EPDM.Interop.epdm.dll, click Open, and click Add).
  // 3. Add Microsoft.VisualBasic as a reference (click COM in the left-side panel,
 //    click Microsoft.VisualBasic, click Add, and click Close).
 // 4. Right-click EPDM.Interop.epdm in References, click Properties, and set
 //    Embed Interop Types to False to handle methods that pass arrays of
 //    structures.
 // 5. Ensure that you have at least one approved file in the vault.
 // 6. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Get files in state dialog box.
 // 2. Select a vault view.
 // 3. Click Get approved files.
 // 4. Displays a message box with all of the files in the Approved state
 //    for each workflow in the vault.
 // 5. Click OK in each message box.
 // 6. Close the Get files in state dialog box.
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

 namespace GetFilesInState_CSharp
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

         public void GetApprovedFiles_Click(System.Object sender, System.EventArgs e)
         {
             //Get approved files
             try
             {

                 IEdmVault7 vault2 = default(IEdmVault7);
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }

                 vault2 = (IEdmVault7)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 IEdmWorkflowMgr6 wfmgr = (IEdmWorkflowMgr6)vault2.CreateUtility(EdmUtility.EdmUtil_WorkflowMgr);

                 IEdmPos5 pos = default(IEdmPos5);
                 pos = wfmgr.GetFirstWorkflowPosition();
                 while (!pos.IsNull)
                 {
                     IEdmWorkflow6 wf = wfmgr.GetNextWorkflow(pos);

                     IEdmState6 state = default(IEdmState6);
                     state = wf.GetState("Approved");
                     if ((state != null))
                     {

                         string message = null;
                         IEdmFile5 file = default(IEdmFile5);
                         IEdmPos5 pos2 = default(IEdmPos5);
                         pos2 = state.GetFirstFilePosition();

                         if (!pos2.IsNull)
                         {
                             message = "These files are approved in workflow, " + wf.Name + ":" + Constants.vbLf;

                             while (!pos2.IsNull)
                             {
                                 file = state.GetNextFile(pos2);
                                 message = message + file.Name + Constants.vbLf;
                             }

                             MessageBox.Show(message);
                         }
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
 namespace GetFilesInState_CSharp
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
             this.GetApprovedFiles = new System.Windows.Forms.Button();
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
             //GetApprovedFiles
             //
             this.GetApprovedFiles.Location = new System.Drawing.Point(16, 86);
             this.GetApprovedFiles.Name = "GetApprovedFiles";
             this.GetApprovedFiles.Size = new System.Drawing.Size(139, 23);
             this.GetApprovedFiles.TabIndex = 5;
             this.GetApprovedFiles.Text = "Get approved files";
             this.GetApprovedFiles.UseVisualStyleBackColor = true;
             this.GetApprovedFiles.Click +=new System.EventHandler(GetApprovedFiles_Click);
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(216, 137);
             this.Controls.Add(this.GetApprovedFiles);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Get files in state";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button GetApprovedFiles;
     }
 }
```

[Back to top](#top)
