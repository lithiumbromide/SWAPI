---
title: "Destroy Deleted Files in Vault Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Destroy_Deleted_Files_in_Vault_Example_CSharp.htm"
---

# Destroy Deleted Files in Vault Example (C#)

This example shows how to create an application that displays a form in which a user can select the vault in whose root folder and subfolders all deleted files will be permanently destroyed. The user must have permission to delete files.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

**IMPORTANT:** Do not recreate and run this example if you do not want to destroy all deleted files in the root folder and subfolders in the selected vault. Instead, SOLIDWORKS PDM Professional suggests that you review the code to understand how you can programmatically destroy deleted files in the root folder and subfolders of a vault.

```vb
 //--------------------------------------------------------------------------------------
 // Preconditions:
 //  1. Start Microsoft Visual Studio.
 //  2. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
 //  3. Type DestroyDeletedItems in Project name.
 //  4.     For Location, click ... and navigate to the folder where to create the project.
//  5. Click Next.
 //  6. Select Framework.
//  7. Click  Create.
//  8. Click Show All Files in the Solution Explorer toolbar and expand
//     Form1.cs in the Solution Explorer.
 //  9. Replace the code in Form1.cs with this code.
 // 10. Replace the code in Form1.Designer.cs with this code.
 // 11.     Add dependencies and safely pass arrays of structures.
 // 12. Ensure that the namespaces specified in all of the *.cs files match
 //     the project name.
// 13. Delete one or more checked-in files from the root folder of your vault.
 // 14. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 //  1. Displays the Destroy Deleted Files dialog.
 //  2. Select a vault.
 //  3. Optionally select the Include all subfolders check box.
 //  4. Click the Destroy deleted files button.
 //     A message box pops up informing you that:
 //     * No deleted files were found to destroy.
 //       - or -
 //     * The deleted files were destroyed.
 //  5. Click OK in the message box.
 //  6. Close the Destroy Deleted Files dialog.
 //--------------------------------------------------------------------------------------
//Form1.cs
using System;
 using System.Windows.Forms;
 using EPDM.Interop.epdm;

 namespace DestroyDeletedItems
 {

       public  partial  class   Form1 : Form
      {
            void DestroyDeletedItems_Load(object sender, EventArgs e)
           {
               try
              {
                    //Declare and create an instance of IEdmVault5
                  IEdmVault5 vault1 =   new EdmVault5();

                  //Cast IEdmVault5 to IEdmVault8
                  IEdmVault8 vault = (IEdmVault8)vault1;

                  EdmViewInfo[] Views =   null;

                    //Populate the form with the names of
                    //the vaults on the computer
                  vault.GetVaultViews(out Views,   false);
                  VaultsComboBox.Items.Clear();
                   foreach (EdmViewInfo View  in Views)
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
                  MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + ex.Message);
              }
               catch (Exception ex)
              {
                  MessageBox.Show(ex.Message);
              }
           }

            void DestroyDeletedItemsButton_Click(object sender, EventArgs e)
           {
               try
              {
                    //Declare and create an instance of IEdmVault5
                  IEdmVault5 vault =   new EdmVault5();

                    //Log into selected vault as the current user
                  vault.LoginAuto(VaultsComboBox.Text,  this.Handle.ToInt32());

                    //Check to see if deleted files should be
                    //destroyed in all the subfolders
                   bool aRecursive =   false;
                  if (CheckBox_Recursive.Checked)
                  {
                      aRecursive =   true;
                  }

                  EdmDeletedItems[] poDeletedItems =  null;
                  EdmFileInfo[] ppoDestroyedItems =   null;
                  EdmBatchDelErrInfo[] poErrors =   null;
                  IEdmFolder5 DeletedFolder1 =   default(IEdmFolder5);

                    //Get the root folder of the vault
                  DeletedFolder1 = vault.RootFolder;
                  IEdmFolder13 DeletedFolder = (IEdmFolder13)DeletedFolder1;
                  DeletedFolder.GetDeletedItems(out poDeletedItems,   true);

                    //Destroy all deleted files in the root folder and
                    //subfolders, if the check box is selected on the form
                  DeletedFolder.DestroyDeletedItems2(poDeletedItems,   out ppoDestroyedItems,  out poErrors);

                    //If any deleted files found, display their names in a message box
                   string msg =   null;
                   int idx = 0;
                   foreach (EdmFileInfo ppoDestroyedItem  in ppoDestroyedItems)
                  {
                        string row =   null;
                      row =   "\nDocumentID: " + Convert.ToString(ppoDestroyedItem.mlFileID) +  ", FolderID: " + Convert.ToString(ppoDestroyedItem.mlFolderID) +  ", File path: " + ppoDestroyedItem.mbsPath;

                       if (ppoDestroyedItem.mhResult == 0)
                      {
                          row = row +   "\nStatus: OK\n";
                      }
                        else
                      {
                          EdmBatchDelErrInfo[] poError =  null;
                          row = row +   " status: Failed=" +   "HRESULT = 0x" + Convert.ToString(poError[idx].mlErrorCode);
                          idx += 1;
                      }

                      msg = msg + row;
                  }

                   if (msg ==   null)
                  {
                      MessageBox.Show("No deleted files were found in the selected vault's root folder or \n subfolders.");
                  }
                   else
                  {
                      MessageBox.Show("The status for each destroyed file is:\n" + msg);
                  }
              }

               catch (System.Runtime.InteropServices.COMException ex)
              {
                  MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + ex.Message);
              }
               catch (Exception ex)
              {
                  MessageBox.Show(ex.Message);
              }
           }

            void CheckBox_Recursive_CheckedChanged(object sender, EventArgs e)
           {

          }

            private  void label1_Click(object sender, EventArgs e)
           {

           }

     }

 }
Back to top
 //Form1.Designer.cs
namespace DestroyDeletedItems
 {

 partial   class   Form1
      {
            ///  <summary>
            ///  Required designer variable.
            ///  </summary>
            private System.ComponentModel.IContainer components =  null;

            ///  <summary>
            ///  Clean up any resources being used.
            ///  </summary>
            ///  <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
            protected  override   void Dispose(bool disposing)
           {
               if (disposing && (components !=   null))
              {
                  components.Dispose();
              }
               base.Dispose(disposing);
           }

            #region Windows Form Designer generated code

            ///  <summary>
            ///  Required method for Designer support - do not modify
            ///  the contents of this method with the code editor.
            ///  </summary>
            private  void InitializeComponent()
           {
               this.components =   new System.ComponentModel.Container();
               this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
               this.ClientSize =   new System.Drawing.Size(800, 450);
               this.Text =  "Form1";
               this.label1 =  new System.Windows.Forms.Label();
               this.VaultsLabel =   new System.Windows.Forms.Label();
               this.VaultsComboBox =   new System.Windows.Forms.ComboBox();
               this.DestroyDeletedItemsButton =   new System.Windows.Forms.Button();
               this.CheckBox_Recursive =   new System.Windows.Forms.CheckBox();
              this.SuspendLayout();
             //
             // label1
             //
             this.label1.Location =   new System.Drawing.Point(32, 19);
               this.label1.Name =   "label1";
               this.label1.Size =   new System.Drawing.Size(187, 79);
               this.label1.TabIndex = 0;
               this.label1.Text =   "This application destroys all deleted files in the root folder of the selected va" +
                "ult and also allows you to destroy all deleted files in all of the selected vaul" +
               "t\'s subfolders.";
               this.label1.Click +=   new System.EventHandler(this.label1_Click);
             //
             // VaultsLabel
             //
             this.VaultsLabel.AutoSize =   true;
               this.VaultsLabel.Location =   new System.Drawing.Point(35, 113);
               this.VaultsLabel.Name =   "VaultsLabel";
               this.VaultsLabel.Size =   new System.Drawing.Size(75, 13);
               this.VaultsLabel.TabIndex = 1;
               this.VaultsLabel.Text =   "Select a vault:";
             //
             // VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled =   true;
               this.VaultsComboBox.Location =   new System.Drawing.Point(35, 130);
               this.VaultsComboBox.Name =   "VaultsComboBox";
              this.VaultsComboBox.Size =   new System.Drawing.Size(184, 21);
               this.VaultsComboBox.TabIndex = 2;
             //
             // DestroyDeletedItemsButton
             //
             this.DestroyDeletedItemsButton.Location =   new System.Drawing.Point(35, 229);
               this.DestroyDeletedItemsButton.Name =   "DestroyDeletedItemsButton";
               this.DestroyDeletedItemsButton.Size =   new System.Drawing.Size(184, 23);
               this.DestroyDeletedItemsButton.TabIndex = 4;
              this.DestroyDeletedItemsButton.Text =   "Destroy deleted files";
               this.DestroyDeletedItemsButton.UseVisualStyleBackColor =   true;
               this.DestroyDeletedItemsButton.Click +=   new System.EventHandler(this.DestroyDeletedItemsButton_Click);
             //
             // CheckBox_Recursive
             //
             this.CheckBox_Recursive.AutoSize =   true;
               this.CheckBox_Recursive.Location =   new System.Drawing.Point(38, 174);
               this.CheckBox_Recursive.Name =   "CheckBox_Recursive";
               this.CheckBox_Recursive.Size =   new System.Drawing.Size(125, 17);
               this.CheckBox_Recursive.TabIndex = 5;
               this.CheckBox_Recursive.Text =   "Include all subfolders";
               this.CheckBox_Recursive.UseVisualStyleBackColor =   true;
               this.CheckBox_Recursive.CheckedChanged +=   new System.EventHandler(this.CheckBox_Recursive_CheckedChanged);
             //
             // Form1
             //
             this.AutoScaleDimensions =   new System.Drawing.SizeF(6F, 13F);
               this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
               this.ClientSize =   new System.Drawing.Size(254, 274);
               this.Controls.Add(this.CheckBox_Recursive);
              this.Controls.Add(this.DestroyDeletedItemsButton);
               this.Controls.Add(this.VaultsComboBox);
               this.Controls.Add(this.VaultsLabel);
               this.Controls.Add(this.label1);
               this.Name =  "Form1";
               this.Text =   "Destroy Deleted Files";
               this.Load +=  new System.EventHandler(this.DestroyDeletedItems_Load);
               this.ResumeLayout(false);
               this.PerformLayout();
           }

            #endregion
            private System.Windows.Forms.Label label1;
            private System.Windows.Forms.Label VaultsLabel;
            private System.Windows.Forms.ComboBox VaultsComboBox;
            private System.Windows.Forms.Button DestroyDeletedItemsButton;
            private System.Windows.Forms.CheckBox CheckBox_Recursive;
     }

 }
```

```vb
 Back to top
```
