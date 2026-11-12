---
title: "Create Custom Card View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Create_Custom_Card_View_Example_CSharp.htm"
---

# Create Custom Card View Example (C#)

This example shows how to create a custom file card view.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
   //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 //    a. Click File > New > Project > Visual C# > Windows Forms Application.
 //    b. Type CustomCardView_CSharp in Name.
 //    c. Click Browse and navigate to the folder where to create the project.
 //    d. Click OK.
 //    e. Click Show All Files in the Solution Explorer toolbar and expand
 //       Form1.cs in the Solution Explorer.
 //    f. Replace the code in Form1.cs with this code.
 //    g. To create the form, replace the code in  Form1.Designer.cs with
 //       this code.
 // 2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 //    name in the Solution Explorer, click Add Reference, click
 //    Assemblies > Framework in the left-side panel, browse to the top folder of
 //    your SOLIDWORKS PDM Professional installation, locate and click
 //    EPDM.Interop.epdm.dll, click Open, and click  Add).
  // 3. Add Microsoft.VisualBasic as a reference (click Framework in the left-side panel,
 //    click Microsoft.VisualBasic, click Add, and click Close).
 // 4. Right-click EPDM.Interop.epdm in References, click Properties, and set
 //    Embed Interop Types to False to handle methods that pass arrays of
 //    structures.
 // 5. Check out a file that has a data card with a Comment tab and a
 //    Comment variable.
 // 6. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Custom Card View dialog box.
 // 2. Select a vault view.
 // 3. Click Select file.
 //    a. In the Select File dialog:
 //       1. Click the text file checked out in Preconditions step 5.
 //       2. Click Open.
 //    b. In the file data card, click the Comment tab.
 //    c. Type something in Comments.
 // 4. Click Save data card.
 // 5. Click OK in the message box.
 // 6. Close the Custom Card View dialog box.
 // 7. Check in the file and inspect the comment in the file data card.
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

 namespace CustomCardView_CSharp
 {
     public partial class Form1 : Form, IEdmCardViewCallback6
     {
         public Form1()
         {
             InitializeComponent();
         }
         private IEdmVault5 vault1;
         IEdmCardView63 view;
         IEdmFile7 aFile;
         IEdmFolder5 aFolder;

         public void Form1_Load(System.Object sender, System.EventArgs e)
         {
             try
             {
                 vault1 = new EdmVault5();
                 IEdmVault10 vault = (IEdmVault10)vault1;
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

                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }

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

         public void SaveCard_Click(System.Object sender, System.EventArgs e)
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

         //Display the card of the selected file
         private void ShowCard(IEdmFolder5 folder, int fileID)
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
                 IEdmVault10 vault = (IEdmVault10)vault1;

                 EdmCardViewParams @params = default(EdmCardViewParams);
                 @params.mlFileID = fileID;
                 @params.mlFolderID = folder.ID;
                 @params.mlCardID = 0;
                 @params.mlX = 40;
                 @params.mlY = 300;
                 @params.mhParentWindow = this.Handle.ToInt32();
                 @params.mlEdmCardViewFlags = (int)EdmCardViewFlag.EdmCvf_Normal;

                 //Create the card view interface
                 view = vault.CreateCardViewEx2(@params, this);

                 if (view == null)
                 {
                     Interaction.MsgBox("The file does not have a card.");
                     return;
                 }

                 //Set input focus to the first control in the card
                 view.SetFocus(0);

                 //Enable all controls in the card
                 view.Update(EdmCardViewUpdateType.EdmCvut_EnableCtrl);

                 //Get the size needed to display the card
                 int width = 0;
                 int height = 0;
                 view.GetCardSize(out width, out height);

                 //Resize the form window to make room for the card
                 this.Width = (width + 100);
                 this.Height = (height + 400);
                 view.ShowWindow(true);

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

         private void EdmCardViewCallback6_SetModifiedFlag()
         {
             SaveCard.Enabled = true;
         }
         void IEdmCardViewCallback6.SetModifiedFlag()
         {
             EdmCardViewCallback6_SetModifiedFlag();
         }

         private void EdmCardViewCallback6_OnAddInInput(int lFlags)
         {
         }
         void IEdmCardViewCallback6.OnAddInInput(int lFlags)
         {
             EdmCardViewCallback6_OnAddInInput(lFlags);
         }

         private void EdmCardViewCallback6_SetCtrlData(int lCardWnd, int lCardID, int lControlID, int lVariableID, string bsVariableName, IEdmCardView5 poView, ref object poValue)
         {
             try
             {
                 if (bsVariableName == "Comment")
                 {
                     Interaction.MsgBox(lCardWnd + " " + lCardID + " " + lControlID + " " + lVariableID + " " + bsVariableName + " " + poValue.ToString());

                     IEdmEnumeratorVariable8 enumvar = default(IEdmEnumeratorVariable8);
                     enumvar = (IEdmEnumeratorVariable8)aFile.GetEnumeratorVariable();

                     enumvar.SetVar(bsVariableName, "", poValue, true);
                     enumvar.CloseFile(true);
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
         void IEdmCardViewCallback6.SetCtrlData(int lCardWnd, int lCardID, int lControlID, int lVariableID, string bsVariableName, IEdmCardView5 poView, ref object poValue)
         {
             EdmCardViewCallback6_SetCtrlData(lCardWnd, lCardID, lControlID, lVariableID, bsVariableName, poView, ref poValue);
         }

         private object EdmCardViewCallback6_GetCtrlData(int lCardWnd, int lCardID, int lControlID, int lVariableID, string bsVariableName, IEdmCardView5 poView)
         {
             object poValue = null;
             try
             {
                  IEdmEnumeratorVariable8 enumVar = (IEdmEnumeratorVariable8)aFile.GetEnumeratorVariable();
                 enumVar.GetVar(bsVariableName, "", out poValue);
             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                   MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
             }
             catch (Exception ex)
             {
                   MessageBox.Show(ex.Message);
             }

             return  poValue;
         }
         object IEdmCardViewCallback6.GetCtrlData(int lCardWnd, int lCardID, int lControlID, int lVariableID, string bsVariableName, IEdmCardView5 poView)
         {
             return EdmCardViewCallback6_GetCtrlData(lCardWnd, lCardID, lControlID, lVariableID, bsVariableName, poView);
         }

         private object EdmCardViewCallback6_GetDefaultValueComponent(EdmDefValComp eValue)
         {
             return null;
         }
         object IEdmCardViewCallback6.GetDefaultValueComponent(EdmDefValComp eValue)
         {
             return EdmCardViewCallback6_GetDefaultValueComponent(eValue);
         }
     }
 }
```

[Back to top](#top)

```vb
 //Form1.Designer.cs
 namespace CustomCardView_CSharp
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
             this.SelectFile.Click +=new System.EventHandler(SelectFile_Click);
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
             this.SaveCard.Location = new System.Drawing.Point(40, 176);
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
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(284, 227);
             this.Controls.Add(this.SaveCard);
             this.Controls.Add(this.File1List);
             this.Controls.Add(this.SelectFile);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Custom Card View";
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

         #endregion
     }
 }
```

[Back to top](#top)
