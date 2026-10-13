---
title: "Get Categories Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Get_Categories_Example_CSharp.htm"
---

# Get Categories Example (C#)

This example shows how to access the categories in a vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
//  1. Start Microsoft Visual Studio 2010.
//  2. Click File > New > Project > Visual C# > Windows Forms Application.
//  3. Type GetCategories_CSharp in Name.
//  4. Click Browse to navigate to the folder where to create the project.
//  5. Click OK.
//  6. Click Show All Files in the Solution Explorer toolbar and expand
//     Form1.cs in the Solution Explorer.
//  7. Replace the code in Form1.cs with this code.
//  8. To create the form, replace the code in Form1.Designer.cs with this code.
//  9. Add EPDM.Interop.epdm.dll as a reference (right-click the project
//     name in the Solution Explorer, click Add Reference, click
//     Assembly > Framework in the left-side panel, browse to the top folder of your
//     SOLIDWORKS PDM Professional installation, locate and select
//     EPDM.Interop.epdm.dll, click Open, and click Add).
// 10. Add Microsoft.VisualBasic as a reference (click COM in the left-side panel,
//     click Microsoft.VisualBasic, click Add, and click Close).
// 11. Right-click EPDM.Interop.epdm in References, click Properties, and set
//     Embed Interop Types to False to handle methods that pass arrays of
//     structures.
// 12. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays a dialog.
//  2. Select a vault.
//  3. Click Get categories.
//  4. Displays a message box with the names and descriptions of all of the categories
//     in the vault.
//  5. Click OK in the message box.
//  6. Close the dialog.
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
 using Microsoft.VisualBasic;

 namespace GetCategories_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         private IEdmVault5 vault1 = null;

         public void Form1_Load(System.Object sender, System.EventArgs e)
         {
             try
             {
                 vault1 = new EdmVault5();
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

         public void GetCategories_Click(System.Object sender, System.EventArgs e)
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

                 IEdmCategoryMgr6 Categories = default(IEdmCategoryMgr6);
                 Categories = (IEdmCategoryMgr6)vault2.CreateUtility(EdmUtility.EdmUtil_CategoryMgr);

                 IEdmPos5 Pos = default(IEdmPos5);
                 Pos = (IEdmPos5)Categories.GetFirstCategoryPosition();

                 IEdmCategory6 Category = default(IEdmCategory6);
                 string Msg = null;
                 Msg = "The categories in this vault are:";

                 while (!Pos.IsNull)
                 {
                     Category = Categories.GetNextCategory(Pos);
                     Msg = Msg + Constants.vbLf + Category.Name + " (" + Category.Description + ")";
                 }

                 Interaction.MsgBox(Msg);

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

```
Back to top
```

```
//Form1.Designer.cs
```

```vb
 namespace GetCategories_CSharp
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
             this.GetCategories = new System.Windows.Forms.Button();
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
             //GetCategories
             //
             this.GetCategories.Location = new System.Drawing.Point(39, 79);
             this.GetCategories.Name = "GetCategories";
             this.GetCategories.Size = new System.Drawing.Size(157, 23);
             this.GetCategories.TabIndex = 6;
             this.GetCategories.Text = "Get categories";
             this.GetCategories.UseVisualStyleBackColor = true;
             this.GetCategories.Click +=new System.EventHandler(GetCategories_Click);
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(284, 142);
             this.Controls.Add(this.GetCategories);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Categories";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }
         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button GetCategories;

         #endregion
     }
 }
```

```
Back to top
```
