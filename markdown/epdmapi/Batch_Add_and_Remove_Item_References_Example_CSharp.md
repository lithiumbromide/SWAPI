---
title: "Batch Add Item References Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Batch_Add_and_Remove_Item_References_Example_CSharp.htm"
---

# Batch Add Item References Example (C#)

This example shows how to add item references in one batch.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 //    a. Click File > New > Project > C#, Windows, Desktop > Windows Forms Application.
 //    b. Type BatchAddItemRefs_CSharp in Project name.
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
 // 3. Open Start > All Programs > SOLIDWORKS PDM Professional >
 //    Item Explorer.
 //    a. Click the vault to which to add new items.
 //    b. Click New Item on the toolbar to add   00000004 and 00000005.
 //    c. Keep the Item Explorer open.
 // 4. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 //  1. The Add Item Reference dialog box displays.
 //     a. Select a vault view.
 //     b. Click Add item reference.
 //  2. Click  OK in the BatchAddItemRefs dialog box.
 //  3. In the Item Explorer:
 //     a. Click 00000004 under New Item Folder.
 //     b. Observe that item 00000005 is linked to item 00000004.
 //  4. Close the Add Item Reference dialog box and the Item Explorer.
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

 namespace BatchAddItemRefs_CSharp
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

         public void AddItemRefs_Click(System.Object sender, System.EventArgs e)
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

                 AddItemReference((IEdmVault11)vault1);

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

         private void AddItemReference(IEdmVault11 vault)
         {
             //Set up the search interface to find items
             IEdmSearchResult5 res = default(IEdmSearchResult5);
             IEdmSearch7 search = default(IEdmSearch7);
             search = (IEdmSearch7)vault.CreateUtility(EdmUtility.EdmUtil_Search);
             search.StartFolderID = vault.ItemRootFolderID;
             search.SetToken(EdmSearchToken.Edmstok_FindFolders, false);
             search.SetToken(EdmSearchToken.Edmstok_FindFiles, true);
             search.SetToken(EdmSearchToken.Edmstok_FindItems, true);
             search.SetToken(EdmSearchToken.Edmstok_Recursive, true);

             //Get the database ID of item number 00000004
             search.FileName = "00000004.<item>";
             res = search.GetFirstResult();
             if (res == null)
                 return;
             int item4ID = 0;
             item4ID = res.ID;

             //Get the database ID of item number 00000005
             search.FileName = "00000005.<item>";
             res = search.GetFirstResult();
             if (res == null)
                 return;
             int item5ID = 0;
             item5ID = res.ID;

             //Add item number 00000005 as a reference to item number 00000004
             EdmItemRef[] addRefs = new EdmItemRef[1];
             addRefs[0].moParentNamePathOrItemID = item4ID;
             addRefs[0].moNamePathOrID = item5ID;
             addRefs[0].mlEdmRefFlags = (int)EdmRefFlags.EdmRef_Item;

             //No item references to remove
             EdmItemRef[] removeRefs = null;
             removeRefs = null;

             IEdmBatchItemReferenceUpdate batch = default(IEdmBatchItemReferenceUpdate);
             batch = (IEdmBatchItemReferenceUpdate)vault.CreateUtility(EdmUtility.EdmUtil_BatchItemReferenceUpdate);
             batch.UpdateReferences(addRefs, removeRefs);
             MessageBox.Show("Result of operation: " + "\n" + vault.GetErrorMessage(addRefs[0].mhResult));

         }
     }
 }
```

[Back to top](#top)

```vb
 //Form1.Designer.cs
 namespace BatchAddItemRefs_CSharp
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
             this.AddItemRefs = new System.Windows.Forms.Button();
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
             //AddItemRefs
             //
             this.AddItemRefs.Location = new System.Drawing.Point(39, 84);
             this.AddItemRefs.Name = "AddItemRefs";
             this.AddItemRefs.Size = new System.Drawing.Size(157, 23);
             this.AddItemRefs.TabIndex = 6;
             this.AddItemRefs.Text = "Add item reference";
             this.AddItemRefs.UseVisualStyleBackColor = true;
             this.AddItemRefs.Click += new System.EventHandler(AddItemRefs_Click);
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(284, 147);
             this.Controls.Add(this.AddItemRefs);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Add Item Reference";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }
         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button AddItemRefs;

         #endregion
     }
 }
```

[Back to top](#top)
