---
title: "Add File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Add_File_Example_CSharp.htm"
---

# Add File Example (C#)

This example shows how to add a file outside the vault to the vault root.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Start Microsoft Visual Studio.
//    a. Click File > New > Project > C#, Windows, Desktop > Windows Forms Application.
//    b. Type AddFiles in Project name.
//    c. For Location, click ... and navigate to the folder where to
create the project.
//    d. Click Next.
//    e. Select Framework.
//    f. Click Create.

//    g. Click Show All Files in the Solution Explorer
toolbar and expand

//       Form1.cs in the Solution Explorer.
//    h. Replace the code in Form1.cs with this code.
//    i. To create the form, replace the code in Form1.Designer.cs with this code.
// 2. Add dependencies and safely pass arrays of structures.
// 3. Run the Administration tool, log in as admin, expand the vault,
//    right-click File Types, click Duplicate file name settings, and
//    click Do not allow duplicate files names in this file vault.
// 4. Ensure that at least one file exists in a subfolder in the vault and
//    the same-named file exists outside the vault.
// 5. Click Debug > Start Debugging or press F5.
//
// Postconditions:
// 1. Displays the Add file to vault root dialog box.
//    a. Select a vault view.
//    b. Click Browse to a file outside the vault.
//       1. Locate a file outside the vault that exists in
//          a subfolder in the vault.
//       2. Click Open.
//    c. Click Add file to vault root to add the selected file to the
//       root folder of the vault.
//    d. Displays a message box warning you that the selected file is not
//       unique in the vault, but that the file will be added to the vault root.
//    e. Click OK.
// 2. Close the Add file to vault root dialog box.
// 3. Examine the vault root.
//----------------------------------------------------------------------------
```

```
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
using EPDM.Interop.EPDMResultCode;

namespace AddFiles_CSharp
{
	public partial class Form1 : Form, IEdmCallback6
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
				MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
			}
			catch (Exception ex)
			{
				MessageBox.Show(ex.Message);
			}
		}

		public void BrowseButton_Click(System.Object sender, System.EventArgs e)
		{
			try
			{
				ListBox.Items.Clear();

				if (vault1 == null)
				{
					vault1 = new EdmVault5();
				}
				if (!vault1.IsLoggedIn)
				{
					//Log into selected vault as the current user
					vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
				}

				//Set the initial directory in the Open dialog
				OpenFileDialog.InitialDirectory = vault1.RootFolderPath;
				//Show the Open dialog
				System.Windows.Forms.DialogResult DialogResult;
				DialogResult = OpenFileDialog.ShowDialog();
				//If the user didn't click Open, exit
				if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
				{
					return;
				}

				foreach (string FileName in OpenFileDialog.FileNames)
				{
					ListBox.Items.Add(FileName);
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

		public void AddFiles_Click(System.Object sender, System.EventArgs e)
	{

		try {
			IEdmVault7 vault2 = null;
			if (vault1 == null) {
				vault1 = new EdmVault5();
			}
			vault2 = (IEdmVault7)vault1;
			if (!vault1.IsLoggedIn) {
				//Log into selected vault as the current user
				vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
			}

			if (!(ListBox.Items.Count == 1)) {
				MessageBox.Show("Please browse to a file outside the vault.");
				return;
			}

			// Add selected file to the root folder of the vault
			IEdmFolder8 Folder = default(IEdmFolder8);
			Folder = (IEdmFolder8)vault2.RootFolder;

			EdmAddFileInfo[] Files = new EdmAddFileInfo[1];

			string[] FileNames = new string[1];
			int Index = 0;
			string fileStr = "";
			foreach ( Object FileName_loopVariable in ListBox.Items) {
				fileStr = FileName_loopVariable.ToString();
				FileNames[Index] = fileStr.Substring(fileStr.LastIndexOf("\\"));
				Index = Index + 1;
			}

			string Path = "";
			int addFileStatus;
			Index = 0;
			foreach (Object FileName_loopVariable in ListBox.Items) {
				Path = FileName_loopVariable.ToString();
				Files[Index].mbsPath = Path;
				Files[Index].mlEdmAddFlags = (int)EdmAddFlag.EdmAdd_Simple;
				Files[Index].mlFileID = 0;
				Files[Index].mlSrcDocumentID = 0;
				Files[Index].mlSrcProjectID = 0;
				Files[Index].mbsNewName = "";
				Folder.AddFile2(this.Handle.ToInt32(), Files[Index].mbsPath, out addFileStatus, "", Files[Index].mlEdmAddFlags);
				switch (addFileStatus)
				{
					case (int)EdmResultSuccessCodes_e.S_EDM_FILES_NOT_UNIQUE_GLOBALLY:
						MessageBox.Show("WARNING: File is not unique in the vault, but the file will be added to the vault root.");
						break;
					case 0:
						MessageBox.Show("SUCCESS: File will be added to the vault root.");
						break;
				}
				Index = Index + 1;
			}

		} catch (System.Runtime.InteropServices.COMException ex) {
			MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
		} catch (Exception ex) {
			MessageBox.Show(ex.Message);
		}
	}

		private EdmMBoxResult IEdmCallback6_MsgBox(int lParentWnd, int lMsgID, string bsMsg, EdmMBoxType eType = 0L)
		{
			MessageBox.Show(bsMsg);
			return EdmMBoxResult.EdmMbr_OK;
		}
		EdmMBoxResult IEdmCallback6.MsgBox(int lParentWnd, int lMsgID, string bsMsg, EdmMBoxType eType )
		{
			return IEdmCallback6_MsgBox(lParentWnd, lMsgID, bsMsg, eType);
		}

		private void IEdmCallback6_Resolve(int lParentWnd, ref EdmCmdData[] ppoItems)
		{
		}
		void IEdmCallback6.Resolve(int lParentWnd, ref EdmCmdData[] ppoItems)
		{
			IEdmCallback6_Resolve(lParentWnd, ref ppoItems);
		}

		private bool IEdmCallback6_SetProgress(int lBarIndex, int lPos, string bsMsg)
		{
			return true;
		}
		bool IEdmCallback6.SetProgress(int lBarIndex, int lPos, string bsMsg)
		{
			return IEdmCallback6_SetProgress(lBarIndex, lPos, bsMsg);
		}

		private void IEdmCallback6_SetProgressRange(int lBarIndex, int lMax)
		{
		}
		void IEdmCallback6.SetProgressRange(int lBarIndex, int lMax)
		{
			IEdmCallback6_SetProgressRange(lBarIndex, lMax);
		}

		private void IEdmCallback6_SetStatusMessage(int lBarIndex, string bsMessage)
		{
		}
		void IEdmCallback6.SetStatusMessage(int lBarIndex, string bsMessage)
		{
			IEdmCallback6_SetStatusMessage(lBarIndex, bsMessage);
		}
	}
}
```

```
//Form1.Designer.cs
```

```
namespace AddFiles_CSharp
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
            this.BrowseButton = new System.Windows.Forms.Button();
            this.ListBox = new System.Windows.Forms.ListBox();
            this.AddFiles = new System.Windows.Forms.Button();
            this.OpenFileDialog = new System.Windows.Forms.OpenFileDialog();
            this.SuspendLayout();
            //
            // VaultsLabel
            //
            this.VaultsLabel.AutoSize = true;
            this.VaultsLabel.Location = new System.Drawing.Point(13, 26);
            this.VaultsLabel.Name = "VaultsLabel";
            this.VaultsLabel.Size = new System.Drawing.Size(94, 13);
            this.VaultsLabel.TabIndex = 0;
            this.VaultsLabel.Text = " Select vault view:";
            //
            // VaultsComboBox
            //
            this.VaultsComboBox.FormattingEnabled = true;
            this.VaultsComboBox.Location = new System.Drawing.Point(16, 42);
            this.VaultsComboBox.Name = "VaultsComboBox";
            this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
            this.VaultsComboBox.TabIndex = 1;
            //
            // BrowseButton
            //
            this.BrowseButton.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.BrowseButton.Location = new System.Drawing.Point(16, 69);
            this.BrowseButton.Name = "BrowseButton";
            this.BrowseButton.Size = new System.Drawing.Size(259, 39);
            this.BrowseButton.TabIndex = 3;
            this.BrowseButton.Text = "Browse to a file outside the vault:";
            this.BrowseButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.BrowseButton.UseVisualStyleBackColor = true;
            this.BrowseButton.Click += new System.EventHandler(this.BrowseButton_Click);
            //
            // ListBox
            //
            this.ListBox.FormattingEnabled = true;
            this.ListBox.HorizontalScrollbar = true;
            this.ListBox.Location = new System.Drawing.Point(16, 114);
            this.ListBox.Name = "ListBox";
            this.ListBox.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended;
            this.ListBox.Size = new System.Drawing.Size(259, 43);
            this.ListBox.TabIndex = 4;
            //
            // AddFiles
            //
            this.AddFiles.Location = new System.Drawing.Point(16, 163);
            this.AddFiles.Name = "AddFiles";
            this.AddFiles.Size = new System.Drawing.Size(121, 23);
            this.AddFiles.TabIndex = 5;
            this.AddFiles.Text = "Add file to vault root";
            this.AddFiles.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.AddFiles.UseVisualStyleBackColor = true;
            this.AddFiles.Click += new System.EventHandler(this.AddFiles_Click);
            //
            // OpenFileDialog
            //
            this.OpenFileDialog.Multiselect = true;
            this.OpenFileDialog.Title = "Open";
            //
            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(317, 215);
            this.Controls.Add(this.AddFiles);
            this.Controls.Add(this.ListBox);
            this.Controls.Add(this.BrowseButton);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.VaultsLabel);
            this.Name = "Form1";
            this.Text = "Add file to vault root";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.Label VaultsLabel;
        internal System.Windows.Forms.ComboBox VaultsComboBox;
        internal System.Windows.Forms.Button BrowseButton;
        internal System.Windows.Forms.ListBox ListBox;
        internal System.Windows.Forms.Button AddFiles;
        internal System.Windows.Forms.OpenFileDialog OpenFileDialog;
    }
}
```
