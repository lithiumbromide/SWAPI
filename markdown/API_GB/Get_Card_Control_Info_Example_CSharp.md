---
title: "Get Card Control Information Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Get_Card_Control_Info_Example_CSharp.htm"
---

# Get Card Control Information Example (C#)

This example shows how to get information about the list and edit box controls in a selected file's data card.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 //  1. Start Microsoft Visual Studio 2010.
 //  2. Click File > New > Project > Visual C# > Windows Forms Application.
 //  3. Type CardControlInfo_CSharp in Name.
 //  4. Click Browse to navigate to the folder where to create the project.
 //  5. Click OK.
 //  6. Click Show All Files in the Solution Explorer toolbar and expand
 //     Form1.cs in the Solution Explorer.
 //  7. Replace the code in Form1.cs with this code.
 //  8. To create the form, replace the code in Form1.Designer.cs with this code.
 //  9. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 //     name in the Solution Explorer, click Add Reference, click
 //     Framework in the left-side panel, browse to the top folder of your
 //     SOLIDWORKS PDM Professional installation, locate and select
 //     EPDM.Interop.epdm.dll, click Open, and click Add).
 // 10. Add Microsoft.VisualBasic as a reference (click COM in the left-side panel,
 //     click Microsoft.VisualBasic, click Add, and click Close).
 // 11. Right-click EPDM.Interop.epdm in References, click Properties, and set
 //     Embed Interop Types to False to handle methods that pass arrays of
 //     structures.
 // 12. Ensure that there is a file in the vault whose extension has a
 //     file data card in the vault.
 // 13. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 //  1. Displays a dialog.
//  2. Select a vault.
//  3. Click Select file.
//  4. In the Select File dialog:
//     a. Click a file whose extension has a file data card in the vault.
//     b. Click Open.
//  5. Click Get card information.
 //  6. A message box displays information about the selected file's data card.
 //  7. Click OK in the message box.
 //  8. A message box displays the list items of any drop list controls.
 //  9. Click OK in the message box.
 // 10. A message box displays information about each edit box control in the
 //     data card.
 // 11. Click OK in the message box.
 // 12. Close the dialog.
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

 namespace CardControlInfo_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         private IEdmVault5 vault1 = null;
         IEdmFile5 aFile;
         IEdmFolder5 aFolder;
         IEdmFolder5 ppoRetParentFolder;
         IEdmCard6 aCard;
         IEdmCardControl7 aControl;
         IEdmPos5 aPos;
         int plWidth;
         int plHeight;
         int plX;
         int plY;
         int plParentCtrlID;
         int plPageNo;
         object poMin = null;
         object poMax = null;
         int varType;
         int contType;
         string fileExt;
         int cardID;
         string str;

         int k;

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

         public void SelectFiles_Click(System.Object sender, System.EventArgs e)
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
                         aFile = vault1.GetFileFromPath(FileName, out ppoRetParentFolder);
                         k = FileName.LastIndexOf(".");
                         fileExt = FileName.Substring(k + 1, (FileName.Length) - k - 1);
                         aPos = aFile.GetFirstFolderPosition();
                         aFolder = aFile.GetNextFolder(aPos);
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

         public void GetCardControls_Click(System.Object sender, System.EventArgs e)
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

                 if ((aFile != null))
                 {
                     // Get the selected file's data card
                     aCard = (IEdmCard6)aFolder.GetCard(fileExt);
                     cardID = aFolder.GetCardID(fileExt);

                     aCard.GetSize(out plWidth, out plHeight);
                     str = "File: " + aFile.Name + Constants.vbLf + "Card ID: " + cardID + ", EdmCardType: " + aCard.CardType + ", Width: " + plWidth + ", Height: " + plHeight;
                     MessageBox.Show(str);

                     aPos = aCard.GetFirstControlPosition();
                     while (!(aPos.IsNull))
                     {
                         aControl = (IEdmCardControl6)aCard.GetNextControl(aPos);
                         contType = (int)aControl.ControlType;

                         bool ret = false;
                         string[] variableItemsList = null;
                         if (((contType == 7) | (contType == 8) | (contType == 9) | (contType == 10)))
                         {
                             str = "List values associated with drop-down card control: " + aControl.VariableID.ToString();
                             ret = aControl.GetControlVariableList(aFile.ID, out variableItemsList);

                             foreach (string listValue in variableItemsList)
                             {
                                 str = str + Constants.vbLf + listValue;
                             }
                             MessageBox.Show(str);
                         }

                         // Get the edit box controls in the card
                         if (contType == 4)
                         {
                             str = "";
                             aControl.GetParentInfo(out plParentCtrlID, out plPageNo);
                             aControl.GetPosition(out plX, out plY, out plWidth, out plHeight);
                             varType = (int)aControl.GetValidation(out poMin, out poMax);

                             str = "Card control: " + aControl.Name;
                             str = str + Constants.vbLf + "Variable ID: " + aControl.VariableID + Constants.vbLf + "EdmCardControlType: " + contType + Constants.vbLf + "Is multi-line? " + aControl.IsMultiLine + Constants.vbLf + "Is read-only? " + aControl.IsReadOnly + Constants.vbLf + "Show in preview? " + aControl.ShowInPreview;
                             str = str + Constants.vbLf + "Location on card: [" + plX + ", " + plY + "], Width: " + plWidth + ", Height: " + plHeight;
                             str = str + Constants.vbLf + "Parent control ID (0, if none): " + plParentCtrlID;
                             str = str + Constants.vbLf + "Tab index: " + plPageNo;
                             str = str + Constants.vbLf + "EdmVariableType: " + varType;
                            str = str + Constants.vbLf + "Updates all configurations? " + aControl.UpdatesAllConfigurations.ToString();

                             MessageBox.Show(str);
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

```vb
Back to top
```

```vb
//Form1.Designer.cs
```

```vb
 namespace CardControlInfo_CSharp
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
             this.SelectFiles = new System.Windows.Forms.Button();
             this.File1List = new System.Windows.Forms.ListBox();
             this.GetCardControls = new System.Windows.Forms.Button();
             this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
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
             //SelectFiles
             //
             this.SelectFiles.Location = new System.Drawing.Point(39, 85);
             this.SelectFiles.Name = "SelectFiles";
             this.SelectFiles.Size = new System.Drawing.Size(191, 23);
             this.SelectFiles.TabIndex = 2;
             this.SelectFiles.Text = "Select file...";
             this.SelectFiles.UseVisualStyleBackColor = true;
             this.SelectFiles.Click +=new System.EventHandler(SelectFiles_Click);
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
             //GetCardControls
             //
             this.GetCardControls.Location = new System.Drawing.Point(40, 183);
             this.GetCardControls.Name = "GetCardControls";
             this.GetCardControls.Size = new System.Drawing.Size(157, 23);
             this.GetCardControls.TabIndex = 6;
             this.GetCardControls.Text = "Get card  information";
             this.GetCardControls.UseVisualStyleBackColor = true;
             this.GetCardControls.Click += new System.EventHandler(GetCardControls_Click);
             //
             //OpenFileDialog1
             //
             this.OpenFileDialog1.FileName = "OpenFileDialog1";
             this.OpenFileDialog1.Title = "Select File";
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(284, 235);
             this.Controls.Add(this.GetCardControls);
             this.Controls.Add(this.File1List);
             this.Controls.Add(this.SelectFiles);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Card controls";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }
         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button SelectFiles;
         internal System.Windows.Forms.ListBox File1List;
         internal System.Windows.Forms.Button GetCardControls;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog1;

         #endregion
     }
 }
```

```vb
Back to top
```
