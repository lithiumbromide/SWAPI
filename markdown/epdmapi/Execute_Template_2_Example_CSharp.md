---
title: "Execute Template and Return Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Execute_Template_2_Example_CSharp.htm"
---

# Execute Template and Return Data Example (C#)

This example shows how to execute a template to create a folder structure in a vault and return information.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
//  1. Start Microsoft Visual Studio.
//     a. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
//     b. Type TemplateCSharp in Project name.
//     c. For Location, click ... and navigate to the folder where to
create the project.
//     d. Click Next.
//     e. Select Framework.
//     f. Click Create.
//     g. Click Show All Files in the Solution Explorer toolbar and expand
//        Form1.cs in the Solution Explorer.
//     h. Replace the code in Form1.cs with this code.
//     i. To create the form, replace the code in Form1.Designer.cs with
//        this code.
//  2. Add dependencies and safely pass arrays of structures.
//  3. Ensure that a template exists in the vault that you plan to
//     select and that a template card is assigned to that template.
//     NOTE: This example assumes that the template in your selected vault
//     creates a folder structure and that folder structure does not already
//     exist in the selected vault.
//  4. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays the Execute Template dialog box.
//     a. Select a vault view.
//     b. Click Execute Template.
//     c. Displays a message box showing the name of the template to execute.
//     d. Click OK to close the message box.
//     e. A template card dialog may appear to prompt for values.
//        1. Type values.
//        2. Click OK.
//  2. Displays a message box informing you that a new folder structure
//     is, or is not, created in the selected vault.
//  3. Click OK.
//  4. If a folder structure is created, displays a message box with
//     information about the folder structure.
//  5. Click OK.
//  6. Close the Execute Template dialog box.
//  7. Examine the selected vault to verify that a new folder
//     structure based on the template is, or is not, created.
//----------------------------------------------------------------------------
```

```
//Form1.cs
```

```vb
 using System;
 using System.Collections.Generic;
 using System.ComponentModel;
 using System.Data;
 using System.Drawing;
 using System.Linq;
 using System.Text;
 using System.Windows.Forms;
 using EPDM.Interop.epdm;

 namespace TemplateCSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }

         IEdmVault5 vault1 = new EdmVault5();

         public void Form1_Load(System.Object sender, System.EventArgs e)
         {
             try {

                 IEdmVault8 vault = (IEdmVault8)vault1;
                 EdmViewInfo[] Views = null;

                 vault.GetVaultViews(out Views, false);
                 VaultsComboBox.Items.Clear();
                 foreach (EdmViewInfo View in Views) {
                     VaultsComboBox.Items.Add(View.mbsVaultName);
                 }
                 if (VaultsComboBox.Items.Count > 0) {
                     VaultsComboBox.Text = (string)VaultsComboBox.Items[0];
                 }
             } catch (System.Runtime.InteropServices.COMException ex) {
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             } catch (Exception ex) {
                 MessageBox.Show(ex.Message);
             }

         }

         private void ExecuteTemplateButton_Click(System.Object sender, System.EventArgs e)
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

                 //Access template in the selected vault
                 IEdmTemplateMgr5 templateMgr = default(IEdmTemplateMgr5);
                 templateMgr = (IEdmTemplateMgr5)vault2.CreateUtility(EdmUtility.EdmUtil_TemplateMgr);
                 IEdmPos5 pos = default(IEdmPos5);
                 pos = templateMgr.GetFirstTemplatePosition();
                 IEdmTemplate53 template = null;

                 string message = "";
                 message = "Installed template in vault, " + vault2.Name + ", to use:" + "\n" + "\n";

                 while (!pos.IsNull)
                 {

                     template = (IEdmTemplate53)templateMgr.GetNextTemplate(pos);

                     message = message + template.GetMenuString() + "\n";
                     //Display message box with name of template
                     MessageBox.Show(message);

                     //Create template folders in the selected vault
                     //using this template
                     EdmRefreshFlag refreshFlag = default(EdmRefreshFlag);
                     object[] retData = null;
                     refreshFlag = (EdmRefreshFlag)template.RunEx(this.Handle.ToInt32(), vault1.RootFolderID, out retData);

                     if (retData.Length <= 0)
                     {
                         MessageBox.Show("No folder structure created.");
                     }
                     else
                     {
                         MessageBox.Show("The new folder structure based on the template is created in the selected vault.");
                         if (refreshFlag == EdmRefreshFlag.EdmRefresh_FileList)
                         {
                             vault1.RefreshFolder(vault1.RootFolderPath);
                         }

                         //Show a message box with information about the folder structure created by the template
                         long idx = 0;
                         idx = retData.GetLowerBound(0);
                         long upper = 0;
                         upper = retData.GetUpperBound(0);

                         EdmData data = default(EdmData);
                         message = "Template generated:" + "\n";
                         string row = null;

                         while (idx <= upper)
                         {
                             data = (EdmData)retData[idx];
                             switch (data.Type)
                             {
                                 case EdmDataType.EdmData_File:
                                     row = "Type=File, Path=" + data.Get(EdmDataPropertyType.EdmProp_Path);
                                     break;
                                 case EdmDataType.EdmData_Folder:
                                     row = "Type=Folder, path=" + data.Get(EdmDataPropertyType.EdmProp_Path);
                                     break;
                                 case EdmDataType.EdmData_Variable:
                                     row = "Type=Variable, Name=" + data.Get(EdmDataPropertyType.EdmProp_Name) + ", Value=" + data.Get(EdmDataPropertyType.EdmProp_Value);
                                     break;
                                 case EdmDataType.EdmData_Link:
                                     row = "Type=Link, Name=" + data.Get(EdmDataPropertyType.EdmProp_LinkPath);
                                     break;
                                 default:
                                     row = "No data";
                                     break;
                             }

                             idx = idx + 1;
                             message = message + row + "\n";
                         }

                         MessageBox.Show(message);
                     }

                 }

 } catch (System.Runtime.InteropServices.COMException ex) {
 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
 } catch (Exception ex) {
 MessageBox.Show(ex.Message);
 }

   }
    }
 }
```

```
Back to top
```

```
//Form1.Designer.cs
```

```
namespace TemplateCSharp
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
            this.label1 = new System.Windows.Forms.Label();
            this.VaultsComboBox = new System.Windows.Forms.ComboBox();
            this.ExecuteTemplateButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            //
            // label1
            //
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(24, 24);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(91, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Select vault view:";
            //
            // VaultsComboBox
            //
            this.VaultsComboBox.FormattingEnabled = true;
            this.VaultsComboBox.Location = new System.Drawing.Point(27, 41);
            this.VaultsComboBox.Name = "VaultsComboBox";
            this.VaultsComboBox.Size = new System.Drawing.Size(242, 21);
            this.VaultsComboBox.TabIndex = 1;
            //
            // ExecuteTemplateButton
            //
            this.ExecuteTemplateButton.Location = new System.Drawing.Point(27, 81);
            this.ExecuteTemplateButton.Name = "ExecuteTemplateButton";
            this.ExecuteTemplateButton.Size = new System.Drawing.Size(113, 23);
            this.ExecuteTemplateButton.TabIndex = 2;
            this.ExecuteTemplateButton.Text = "Execute Template";
            this.ExecuteTemplateButton.Click += new System.EventHandler(ExecuteTemplateButton_Click);
            this.ExecuteTemplateButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.ExecuteTemplateButton.UseVisualStyleBackColor = true;
            //
            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(290, 125);
            this.Controls.Add(this.ExecuteTemplateButton);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Execute Template";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox VaultsComboBox;
        private System.Windows.Forms.Button ExecuteTemplateButton;

    #endregion
    }
}
```

```
Back to top
```
