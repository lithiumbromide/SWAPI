---
title: "Generate Configuration Values Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Generate_Config_Values_Example_CSharp.htm"
---

# Generate Configuration Values Example (C#)

This example shows how to copy card control variable values from one configuration to another.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio 2010.
 //    a. Click File > New > Project > Visual C# > Windows Forms Application.
 //    b. Type Files_CSharp in Name.
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
  // 3. Add Microsoft.VisualBasic as a reference (click Framework in the left-side panel,
 //    click Microsoft.VisualBasic, click Add, and click Close).
 // 4. Right-click EPDM.Interop.epdm in References, click Properties, and set
 //    Embed Interop Types to False to handle methods that pass arrays of
 //    structures.
 // 5. Check out a file that has a data card with two or more configurations.
 // 6. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Copy Control Values to Configurations dialog box.
 //    a. Select a vault view.
 //       Folder is set to the root folder.
 //    b. Select a file that has a data card with two or more configurations.
 //    c. Displays the data card.
 //    d. Click Copy Control Values.
 //       Copies the value set in Preconditions step 5 to all configurations.
 // 2. Close the dialog box.
 // 3. Inspect the control values in all of the configurations of the data card.
  //----------------------------------------------------------------------------

 //Form1.cs

 using System;
 using System.Collections.Generic;
 using System.ComponentModel;
 using System.Data;
 using System.Drawing;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Windows.Forms;
 using EPDM.Interop.epdm;

 namespace Files_CSharp
 {
     public partial class MainForm : Form
     {
         Dictionary<int,IEdmFolder5> oFoldersArray = new Dictionary<int, IEdmFolder5>();
         Dictionary<int, IEdmFile5> oFileArray = new Dictionary<int, IEdmFile5>();
         IEdmCardView63 edmCardView;

         public MainForm()
         {
             InitializeComponent();
         }

         private void MainForm_Load(object sender, EventArgs e)
         {
             try
             {
                 //Declare and create an instance of IEdmVault5
                 IEdmVault5 vault1 = new EdmVault5();

                 //Cast IEdmVault5 to IEdmVault8
                 IEdmVault8 vault = (IEdmVault8)vault1;

                 EdmViewInfo[] Views = null;

                 //Populate the form with the names of
                 //the vaults on the computer
                 vault.GetVaultViews(out Views, false);
                 VaultsComboBox.Items.Clear();
                 foreach (EdmViewInfo View in Views)
                 {
                     VaultsComboBox.Items.Add(View.mbsVaultName);
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

         private void VaultsComboBox_SelectedIndexChanged(object sender, EventArgs e)
         {
             try
             {
                 //Declare and create an instance of IEdmVault5
                 IEdmVault5 vault = new EdmVault5();

                 //Log into selected vault as the current user
                 vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());

                 IEdmPos5 folderPos = vault.RootFolder.GetFirstSubFolderPosition();

                 FoldersComboBox.Items.Clear();
                 oFoldersArray.Clear();

                 int i = FoldersComboBox.Items.Add("\\");
                 oFoldersArray[i] = vault.RootFolder;

                 while (!folderPos.IsNull)
                 {
                     IEdmFolder5 edmFolder = vault.RootFolder.GetNextSubFolder(folderPos);

                     i = FoldersComboBox.Items.Add(edmFolder.Name);
                     oFoldersArray[i] = edmFolder;
                 }

                 FoldersComboBox.Text = (string)FoldersComboBox.Items[0];
             }catch(Exception)
             {
                 FoldersComboBox.Items.Clear();
                 oFoldersArray.Clear();
                 FoldersComboBox.Text = "Error";
             }
         }

         private void FoldersComboBox_SelectedIndexChanged(object sender, EventArgs e)
         {
             try
             {
                 int i = FoldersComboBox.SelectedIndex;
                 IEdmFolder5 edmFolder = oFoldersArray[i];

                 IEdmPos5 filePos = edmFolder.GetFirstFilePosition();

                 FilesComboBox.Items.Clear();
                 oFileArray.Clear();

                 while (!filePos.IsNull)
                 {
                     IEdmFile5 edmFile = edmFolder.GetNextFile(filePos);

                     i = FilesComboBox.Items.Add(edmFile.Name);
                     oFileArray[i] = edmFile;
                 }

                 FilesComboBox.Text = (string)FilesComboBox.Items[0];
             }
             catch (Exception ex)
             {
                 FilesComboBox.Items.Clear();
                 oFileArray.Clear();
                 FilesComboBox.Text = "Error";
             }

         }

         private void ShowDataCard()
         {
             if (edmCardView != null)
                 edmCardView.ShowWindow(false);

             int i = FoldersComboBox.SelectedIndex;
             IEdmFolder5 edmFolder = oFoldersArray[i];

             i = FilesComboBox.SelectedIndex;
             IEdmFile5 edmFile = oFileArray[i];

             IEdmVault10 vault1 = (IEdmVault10)edmFolder.Vault;

             EdmCardViewParams @params = default(EdmCardViewParams);
             @params.mlFileID = edmFile.ID;
             @params.mlFolderID = edmFolder.ID;
             @params.mlCardID = 0;
             @params.mlX = 10;
             @params.mlY = 15;
             @params.mhParentWindow = CardPanel.Handle.ToInt32();
             @params.mlEdmCardViewFlags = (int)EdmCardViewFlag.EdmCvf_Normal;

             edmCardView = vault1.CreateCardViewEx2(@params, this);
             if (edmCardView == null)
             {
                 MessageBox.Show("The file does not have a card.");
                 return;
             }

             edmCardView.SetFocus(0);

             int width = 0;
             int height = 0;
             edmCardView.GetCardSize(out width, out height);
             CardPanel.Width = width+20;
             CardPanel.Height = height+20;
             edmCardView.ShowWindow(true);
         }

         private void FilesComboBox_SelectedIndexChanged(object sender, EventArgs e)
         {
             ShowDataCard();
         }

         private void DoBtn_Click(object sender, EventArgs e)
         {
             int i = FoldersComboBox.SelectedIndex;
             IEdmFolder5 edmFolder = oFoldersArray[i];

             i = FilesComboBox.SelectedIndex;
             IEdmFile14 edmFile = (IEdmFile14)oFileArray[i];

             List<string> cfgList = new List<string>();
             EdmStrLst5 configLst =  edmFile.GetConfigurations();
             IEdmPos5 cfgPos = configLst.GetHeadPosition();
             while(!cfgPos.IsNull)
             {
                 string configName = configLst.GetNext(cfgPos);
                 cfgList.Add(configName);
             }

             foreach (string configName in cfgList)
                 // Move variable values from "@" to configName
                 edmFile.GenerateDefaultConfigValues(edmFile.ID, "@", configName, "", false);

             ShowDataCard();
         }
     }
 }
```

[Back to top](#top)

```vb
 //Form1.Designer.cs
 namespace Files_CSharp
 {
     partial class MainForm
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
             this.DoBtn = new System.Windows.Forms.Button();
             this.CardPanel = new System.Windows.Forms.Panel();
             this.VaultsComboBox = new System.Windows.Forms.ComboBox();
             this.FoldersComboBox = new System.Windows.Forms.ComboBox();
             this.FilesComboBox = new System.Windows.Forms.ComboBox();
             this.label1 = new System.Windows.Forms.Label();
             this.label2 = new System.Windows.Forms.Label();
             this.label3 = new System.Windows.Forms.Label();
             this.label4 = new System.Windows.Forms.Label();
             this.SuspendLayout();
             //
             // DoBtn
             //
             this.DoBtn.Location = new System.Drawing.Point(223, 108);
             this.DoBtn.Name = "DoBtn";
             this.DoBtn.Size = new System.Drawing.Size(271, 23);
             this.DoBtn.TabIndex = 0;
             this.DoBtn.Text = "Copy Control Values";
             this.DoBtn.UseVisualStyleBackColor = true;
             this.DoBtn.Click += new System.EventHandler(this.DoBtn_Click);
             //
             // CardPanel
             //
             this.CardPanel.AutoScroll = true;
             this.CardPanel.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
             this.CardPanel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
             this.CardPanel.Location = new System.Drawing.Point(12, 162);
             this.CardPanel.Name = "CardPanel";
             this.CardPanel.Size = new System.Drawing.Size(841, 479);
             this.CardPanel.TabIndex = 1;
             //
             // VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(108, 25);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(273, 21);
             this.VaultsComboBox.TabIndex = 2;
             this.VaultsComboBox.SelectedIndexChanged += new System.EventHandler(this.VaultsComboBox_SelectedIndexChanged);
             //
             // FoldersComboBox
             //
             this.FoldersComboBox.FormattingEnabled = true;
             this.FoldersComboBox.Location = new System.Drawing.Point(108, 52);
             this.FoldersComboBox.Name = "FoldersComboBox";
             this.FoldersComboBox.Size = new System.Drawing.Size(434, 21);
             this.FoldersComboBox.TabIndex = 3;
             this.FoldersComboBox.SelectedIndexChanged += new System.EventHandler(this.FoldersComboBox_SelectedIndexChanged);
             //
             // FilesComboBox
             //
             this.FilesComboBox.FormattingEnabled = true;
             this.FilesComboBox.Location = new System.Drawing.Point(108, 79);
             this.FilesComboBox.Name = "FilesComboBox";
             this.FilesComboBox.Size = new System.Drawing.Size(434, 21);
             this.FilesComboBox.TabIndex = 4;
             this.FilesComboBox.SelectedIndexChanged += new System.EventHandler(this.FilesComboBox_SelectedIndexChanged);
             //
             // label1
             //
             this.label1.AutoSize = true;
             this.label1.Location = new System.Drawing.Point(9, 25);
             this.label1.Name = "label1";
             this.label1.Size = new System.Drawing.Size(31, 13);
             this.label1.TabIndex = 5;
             this.label1.Text = "Vault";
             //
             // label2
             //
             this.label2.AutoSize = true;
             this.label2.Location = new System.Drawing.Point(9, 52);
             this.label2.Name = "label2";
             this.label2.Size = new System.Drawing.Size(36, 13);
             this.label2.TabIndex = 6;
             this.label2.Text = "Folder";
             //
             // label3
             //
             this.label3.AutoSize = true;
             this.label3.Location = new System.Drawing.Point(9, 79);
             this.label3.Name = "label3";
             this.label3.Size = new System.Drawing.Size(23, 13);
             this.label3.TabIndex = 7;
             this.label3.Text = "File";
             //
             // label4
             //
             this.label4.AutoSize = true;
             this.label4.Location = new System.Drawing.Point(12, 143);
             this.label4.Name = "label4";
             this.label4.Size = new System.Drawing.Size(57, 13);
             this.label4.TabIndex = 8;
             this.label4.Text = "Data card:";
             //
             // MainForm
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(913, 670);
             this.Controls.Add(this.label4);
             this.Controls.Add(this.label3);
             this.Controls.Add(this.label2);
             this.Controls.Add(this.label1);
             this.Controls.Add(this.FilesComboBox);
             this.Controls.Add(this.FoldersComboBox);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.CardPanel);
             this.Controls.Add(this.DoBtn);
             this.Name = "MainForm";
             this.Text = "Copy Control Values to Configurations";
             this.Load += new System.EventHandler(this.MainForm_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         private System.Windows.Forms.Button DoBtn;
         private System.Windows.Forms.Panel CardPanel;
         private System.Windows.Forms.ComboBox VaultsComboBox;
         private System.Windows.Forms.ComboBox FoldersComboBox;
         private System.Windows.Forms.ComboBox FilesComboBox;
         private System.Windows.Forms.Label label1;
         private System.Windows.Forms.Label label2;
         private System.Windows.Forms.Label label3;
         private System.Windows.Forms.Label label4;
     }
 }
```

[Back to top](#top)
