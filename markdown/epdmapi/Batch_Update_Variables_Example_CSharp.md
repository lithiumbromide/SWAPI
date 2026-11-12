---
title: "Batch Update Card Variables Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Batch_Update_Variables_Example_CSharp.htm"
---

# Batch Update Card Variables Example (C#)

This example shows how to update file and folder card variables in one batch.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 //    a. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
 //    b. Type BatchUpdateCardVarsCSharp in Project name.
 //       c. For Location, click ... and navigate to the folder where to create the project.
//    d. Click Next.
//    e. Select Framework.
//    f. Click Create.
 //    g. Click Show All Files in the Solution Explorer toolbar and expand
 //        Form1.cs in the Solution Explorer.
 //    h. Replace the code in Form1.cs with this code.
 //    i. To create the form, replace the code in  Form1.Designer.cs with
 //       this code.
 // 2.     Add dependencies and safely pass arrays of structures.
  // 3. Add Microsoft.CSharp as reference (click
 //    Assemblies > Framework in the left-side panel, select
 //    Microsoft.CSharp, and click OK).
 // 4.  Ensure that at least one text file is checked out, and at least one folder
 //    with the word Folder in the name exists in the vault.
 // 5. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 //  1. Displays the Batch Update dialog box.
 //     a. Select a vault.
 //     b. Click Batch Update Variables.
 //        * Updates the Title and Comment variables in the data cards
 //          only of checked-out text files.
 //        * Updates the Description variable of the data cards of all folders
 //          with the word  Folder in their names.
 //        * Displays a message box saying  Card variables updated.
 //     c. Click OK to close the message box.
 //  2. Close the Batch Update dialog box.
 //  3. Inspect the data cards of any checked-out text files and folders with
 //     the word Folder in their names in the selected vault.
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

 namespace BatchUpdateCardVarsCSharp
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

         private void BatchUpdateButton_Click(System.Object sender, System.EventArgs e)
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

                 //Create a batch update utility
                 IEdmBatchUpdate2 Update = default(IEdmBatchUpdate2);
                 Update = (IEdmBatchUpdate2)vault2.CreateUtility(EdmUtility.EdmUtil_BatchUpdate);

                 //Get the IDs of the file and folder card variables to update
                 int TitleID = 0;
                 int CommentID = 0;
                 int DescriptionID = 0;
                 IEdmVariableMgr5 VariableMgr = default(IEdmVariableMgr5);

                 VariableMgr = (IEdmVariableMgr5)vault1;
                 TitleID = VariableMgr.GetVariable("Title").ID;
                 DescriptionID = VariableMgr.GetVariable("Description").ID;
                 CommentID = VariableMgr.GetVariable("Comment").ID;

                 //Search for all text files in the vault
                 IEdmSearch5 Search = default(IEdmSearch5);
                 Search = (IEdmSearch5)vault2.CreateUtility(EdmUtility.EdmUtil_Search);

                 Search.FileName = "%.txt";

                 IEdmSearchResult5 Result = default(IEdmSearchResult5);
                 Result = Search.GetFirstResult();

                 while ((Result != null))
                 {
                     Update.SetVar(Result.ID, TitleID, "My Title", "", (int)EdmBatchFlags.EdmBatch_Nothing);
                     Update.SetVar(Result.ID, CommentID, "My Comment", "", (int)EdmBatchFlags.EdmBatch_Nothing);
                     Result = Search.GetNextResult();
                 }

                 //Search for all folders whose names contain "Folder" in the vault
                 Search.FileName = "%Folder%";

                 Result = Search.GetFirstResult();

                 while ((Result != null))
                 {
                     Update.SetFolderVar(Result.ID, DescriptionID, "My Description", (int)EdmBatchFlags.EdmBatch_Nothing);
                     Result = Search.GetNextResult();
                 }

                 //Write all the card variable values to the database
                 EdmBatchError2[] Errors = null;
                 int errorSize = 0;
                 errorSize = Update.CommitUpdate(out Errors, null);

                 //Display any errors
                 string Msg = null;
                 Msg = "Card variables updated.";

                 string ErrName = null;
                 string ErrDesc = null;
                 string FileName = null;

                 int Lo = 0;
                 Lo = Errors.GetLowerBound(0);

                 int Hi = 0;
                 Hi = Errors.GetUpperBound(0);
```

```
               IEdmVault9 vault9;
                vault9 = (IEdmVault9)vault1;
                EdmObjectInfo[] ppoObjects = null;

                while (Lo < Hi - 1)
                {
                    ppoObjects[Lo].meType = EdmObjectType.EdmObject_File;
                    Lo = Lo + 1;
                }

                vault9.GetObjects(ref ppoObjects);

                while (Lo < Hi - 1)
                {
                    if ((Errors[Lo].mlFileID > 0))
                    {
                        IEdmFile6 File = default(IEdmFile6);
                        int ID;
                        ID = (int)ppoObjects[Lo].moObjectID;
                        if (ppoObjects[Lo].meType == EdmObjectType.EdmObject_File)
                        {
                            if (ID == Errors[Lo].mlFileID)
                            {
                                File = (IEdmFile6)ppoObjects[Lo].mpoObject;
                                FileName = File.Name;
                            }
                        }
                    }

                    vault1.GetErrorString(Errors[Lo].mlErrorCode, out ErrName, out ErrDesc);

                    Msg = Msg + "\n" + ErrName + " " + FileName;

                    Lo = Lo + 1;

                }

                MessageBox.Show(Msg);

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
 namespace BatchUpdateCardVarsCSharp
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
             this.BatchUpdateButton = new System.Windows.Forms.Button();
             this.VaultsComboBox = new System.Windows.Forms.ComboBox();
             this.Label1 = new System.Windows.Forms.Label();
             this.SuspendLayout();
             //
             //BatchUpdateButton
             //
             this.BatchUpdateButton.Location = new System.Drawing.Point(30, 100);
             this.BatchUpdateButton.Name = "BatchUpdateButton";
             this.BatchUpdateButton.Size = new System.Drawing.Size(215, 23);
             this.BatchUpdateButton.TabIndex = 0;
             this.BatchUpdateButton.Text = "Batch Update Variables";
             this.BatchUpdateButton.UseVisualStyleBackColor = true;
             this.BatchUpdateButton.Click += new System.EventHandler(this.BatchUpdateButton_Click);
             //
             //VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(30, 56);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             //Label1
             //
             this.Label1.AutoSize = true;
             this.Label1.Location = new System.Drawing.Point(27, 23);
             this.Label1.Name = "Label1";
             this.Label1.Size = new System.Drawing.Size(91, 13);
             this.Label1.TabIndex = 2;
             this.Label1.Text = "Select vault view:";
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(284, 153);
             this.Controls.Add(this.Label1);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.BatchUpdateButton);
             this.Name = "Form1";
             this.Text = "Batch Update";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }
         internal System.Windows.Forms.Button BatchUpdateButton;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Label Label1;
         #endregion
     }
 }
```

[Back to top](#top)
