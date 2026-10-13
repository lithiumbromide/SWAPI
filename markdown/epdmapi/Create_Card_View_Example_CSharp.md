---
title: "Create Card View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Create_Card_View_Example_CSharp.htm"
---

# Create Card View Example (C#)

This example shows how to create a file or folder card view.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 //    a. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
 //    b. Type CreateCardView_CSharp in Project name.
 //    c.    For Location, click ... and navigate to the folder where to create the project.
//    d. Click Next.
//    e. Select Framework.
//    f. Click Create.
 //    g. Click Show All Files in the Solution Explorer toolbar and expand
 //       Form1.cs in the Solution Explorer.
 //    h. Replace the code in Form1.cs with this code.
 //    i. To create the form, replace the code in  Form1.Designer.cs with
 //       this code.
 // 2.      Add dependencies and safely pass arrays of structures.
 // 3. Create a folder in a vault.
 // 4. Check out a file from the vault in which you created the folder.
 // 5. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Create Card View dialog box.
 // 2. Select the vault view in which you created a folder and
 //    checked out a file.
 // 3. Click either:
 //    a. Select file.
 //    b. In the Select File dialog:
 //       1. Click the file checked out in Preconditions step 5.
 //       2. Click Open.
 //       3. Inspect the message box, then click OK.
 //    c. In the file data card, modify a field.
 //    d. Click Save data card.
 //    e. Check in the file and inspect its data card.
 //       - or -
 //    a. Select folder.
 //    b. In the Select Folder dialog, select the vault folder created
 //       in Preconditions step 4 and click OK.
 //    c. Inspect the message box, then click OK.
 //    d. In the folder data card, click the Edit Values tab.
 //    e. Modify a field.
 //    f. Click Save data card.
 //    g. Inspect the folder card in the vault.
 // 4. Close the Create Card View dialog box.
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

 namespace CreateCardView_CSharp
 {
     public partial class Form1 : Form, EdmCallback
     {

         private IEdmVault5 vault1 = null;
         IEdmCardView64 view;
         IEdmFile7 aFile;
         IEdmFolder5 aFolder;

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

         public void SelectFile_Click(System.Object sender, System.EventArgs e)
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

                 SelectFolder.Enabled = false;

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
                     foreach (string FileName in OpenFileDialog1.FileNames)
                     {
                         File1List.Items.Add(FileName);
                         aFile = (IEdmFile7)vault1.GetFileFromPath(FileName, out aFolder);
                         ShowCard(aFolder, aFile.ID);
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

         public void SelectFolder_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 Folder1List.Items.Clear();

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

                 SelectFile.Enabled = false;
                 aFolder = vault1.BrowseForFolder(this.Handle.ToInt32(), "Select folder:");
                 if (Folder1List == null)
                     return;
                 Folder1List.Items.Add(aFolder.Name);
                 ShowCard(aFolder, 0);

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

         public void SaveCard_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 Folder1List.Items.Clear();

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

                 view.SaveData();
                 SaveCard.Enabled = false;

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

         //Display the card of the selected file or folder
         public void ShowCard(IEdmFolder5 folder, int fileID)
         {
             // Create the card view interface
             IEdmFolder10 folder10;
             folder10 = (IEdmFolder10)folder;
             view = (IEdmCardView64)folder10.CreateCardView2(fileID, this.Handle.ToInt32(), 40, 300, (EdmCallback)this,  (int)EdmCardViewFlag.EdmCvf_Normal);
             if (view == null)
             {
                 MessageBox.Show("The file does not have a card.");
                 return;
             }
              view.SetFlagIsFocusOnDataCard(true);

             // Set input focus to the first control in the card
             view.SetFocus(0);

             // Enable all controls in the card
             view.Update(EdmCardViewUpdateType.EdmCvut_EnableCtrl);

             // Get the size needed to display the card
             int width = 0;
             int height = 0;
             view.GetCardSize(out width, out height);

             // Resize the form window to make room for the card
             this.Width = (width + 100);
             this.Height = (height + 400);
             view.ShowWindow(true);
             int ID;
             string folderName;
             string vaultName;
             IEdmVault5 vaultObject;

             // Get some folder information
             ID = folder10.ID;
             folderName = folder10.Name;
             vaultObject = folder10.Vault;
             vaultName = vaultObject.Name;

             MessageBox.Show("Database ID: " + ID.ToString() + "; Vault name: " + vaultName + "; Folder name: " + folderName);

             folder10.Refresh();

             SaveCard.Enabled = false;
         }

         public void CancelButton_Click(System.Object sender, System.EventArgs e)
         {
             view.OnCancel();
             SaveCard.Enabled = false;
             SelectFile.Enabled = true;
             SelectFolder.Enabled = true;
             view.ShowWindow(false);
         }

         public void SetModifiedFlag()
         {
             SaveCard.Enabled = true;
         }

         public void SetProgressPos(int lPos)
         {
         }

         public void SetProgressRange(int lMin, int lMax)
         {
         }

         public void SetStatusMessage(string bsMessage)
         {
         }
     }

 }
```

[Back to top](#top)

```vb
 //Form1.Designer.cs
 namespace CreateCardView_CSharp
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
             this.SelectFile = new System.Windows.Forms.Button();
             this.File1List = new System.Windows.Forms.ListBox();
             this.SaveCard = new System.Windows.Forms.Button();
             this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
             this.SelectFolder = new System.Windows.Forms.Button();
             this.Folder1List = new System.Windows.Forms.ListBox();
             this.Cancel = new System.Windows.Forms.Button();
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
             //SelectFile
             //
             this.SelectFile.Location = new System.Drawing.Point(39, 85);
             this.SelectFile.Name = "SelectFile";
             this.SelectFile.Size = new System.Drawing.Size(157, 23);
             this.SelectFile.TabIndex = 2;
             this.SelectFile.Text = "Select file...";
             this.SelectFile.UseVisualStyleBackColor = true;
             this.SelectFile.Click += new System.EventHandler(SelectFile_Click);
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
             //SaveCard
             //
             this.SaveCard.Location = new System.Drawing.Point(40, 255);
             this.SaveCard.Name = "SaveCard";
             this.SaveCard.Size = new System.Drawing.Size(107, 23);
             this.SaveCard.TabIndex = 6;
             this.SaveCard.Text = "Save data card";
             this.SaveCard.UseVisualStyleBackColor = true;
             this.SaveCard.Click +=new System.EventHandler(SaveCard_Click);
             //
             //OpenFileDialog1
             //
             this.OpenFileDialog1.FileName = "OpenFileDialog1";
             this.OpenFileDialog1.Title = "Select File";
             //
             //SelectFolder
             //
             this.SelectFolder.Location = new System.Drawing.Point(40, 163);
             this.SelectFolder.Name = "SelectFolder";
             this.SelectFolder.Size = new System.Drawing.Size(157, 23);
             this.SelectFolder.TabIndex = 7;
             this.SelectFolder.Text = "Select folder...";
             this.SelectFolder.UseVisualStyleBackColor = true;
             this.SelectFolder.Click += new System.EventHandler(this.SelectFolder_Click);
             //
             //Folder1List
             //
             this.Folder1List.FormattingEnabled = true;
             this.Folder1List.Location = new System.Drawing.Point(39, 192);
             this.Folder1List.Name = "Folder1List";
             this.Folder1List.Size = new System.Drawing.Size(220, 43);
             this.Folder1List.TabIndex = 8;
             //
             //Cancel
             //
             this.Cancel.Location = new System.Drawing.Point(163, 255);
             this.Cancel.Name = "Cancel";
             this.Cancel.Size = new System.Drawing.Size(96, 23);
             this.Cancel.TabIndex = 9;
             this.Cancel.Text = "Cancel";
             this.Cancel.UseVisualStyleBackColor = true;
             this.Cancel.Click += new System.EventHandler(this.Form1_Load);
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(284, 327);
             this.Controls.Add(this.Cancel);
             this.Controls.Add(this.Folder1List);
             this.Controls.Add(this.SelectFolder);
             this.Controls.Add(this.SaveCard);
             this.Controls.Add(this.File1List);
             this.Controls.Add(this.SelectFile);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Create Card View";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }
         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button SelectFile;
         internal System.Windows.Forms.ListBox File1List;
         internal System.Windows.Forms.Button SaveCard;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog1;
         internal System.Windows.Forms.Button SelectFolder;
         internal System.Windows.Forms.ListBox Folder1List;
         internal System.Windows.Forms.Button Cancel;

         #endregion
     }
 }
```

[Back to top](#top)
