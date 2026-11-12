---
title: "Update References Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Update_References_Example_CSharp.htm"
---

# Update References Example (C#)

This example shows how to update the references of a file in a vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
//  1. Start Microsoft Visual Studio 2010.
//     a. Click File > New > Project > Visual C# > Windows Forms Application.
//     b. Type UpdateReferencesCSharp in Name.
//     c. Click Browse and navigate to the folder where to create the project.
//     d. Click OK.
//     e. Click Show All Files in the Solution Explorer toolbar and expand
//        Form1.cs in the Solution Explorer.
//     f. Replace the code in Form1.cs with this code.
//     g. To create the form, replace the code in Form1.Designer.cs with
//        this code.
//  2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
//     name in the Solution Explorer, click Add Reference, click
//     Assemblies > Framework in the left-side panel, browse to the top folder of
//     your SOLIDWORKS PDM Professional installation, locate and click
//     EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
//  3. Right-click EPDM.Interop.epdm in References, click Properties, and set
//     Embed Interop Types to False to handle methods that pass arrays of
//     structures.
//  4. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays your Update References dialog box.
//  2. Select a vault view.
//  3. Click Browse.
//  4. Displays the Select a file dialog box.
//     a. Click a file in the selected vault.
//     b. Click Open.
//     The selected file's path and file name appear
//     in the Select a file dialog box.
//  5. Click Update references.
//  6. Initializes and displays SOLIDWORKS PDM Professional's Update References
//     dialog box, which shows the name of the selected file whose file references
//     to update and the names of the file references, if any.
//  7. Click Close.
//  8. Close your Update References dialog box.
//----------------------------------------------------------------------------
```

```
//Form1.cs

using System;
using System.Windows.Forms;
using EPDM.Interop.epdm;

namespace UpdateReferencesCSharp
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		IEdmVault5 vault1 = null;
		IEdmFile5 aFile;
		string fileName;

		private void Form1_Load(System.Object sender, System.EventArgs e)
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

		public void UpdateReferencesButton_Click(System.Object sender, System.EventArgs e)
		{
			try
			{
				//Only create a new vault object
				//if one hasn't been created yet
				if (vault1 == null)
				{
					vault1 = new EdmVault5();
				}

				if (!vault1.IsLoggedIn)
				{
					//Log into selected vault as the current user
					vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
				}

				//Update the references for the selected document
				//and show SOLIDWORKS PDM Professional Update References dialog
				IEdmUpdateReferences updateRefs = default(IEdmUpdateReferences);
				IEdmVault7 vault2 = (IEdmVault7)vault1;
				updateRefs = (IEdmUpdateReferences)vault2.CreateUtility(EdmUtility.EdmUtil_UpdateReferences);
				updateRefs.AddFile(fileName);
				updateRefs.ShowDlg(this.Handle.ToInt32(), 0, 0);

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

		public void BrowseButton_Click(System.Object sender, System.EventArgs e)
		{
			try
			{
				//If one hasn't been created yet
				if (vault1 == null)
				{
					vault1 = new EdmVault5();
				}

				if (!vault1.IsLoggedIn)
				{
					//Log into selected vault as the current user
					vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
				}
				//Set the initial directory in the Select a file dialog
				OpenFileDialog1.InitialDirectory = vault1.RootFolderPath;
				//Show the Select a file dialog
				System.Windows.Forms.DialogResult DialogResult;
				DialogResult = OpenFileDialog1.ShowDialog();

				if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
				{
					//Do nothing
				}
				else
				{
					//Browse for a file whose next possible state
					//transitions to get
					fileName = OpenFileDialog1.FileName;
					FileListBox.Items.Add(fileName);
					IEdmFolder5 retFolder = default(IEdmFolder5);
					aFile = vault1.GetFileFromPath(fileName, out retFolder);

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

```
Back to top
```

```
//Form1.Designer.cs
```

```
namespace UpdateReferencesCSharp
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
            this.Label1 = new System.Windows.Forms.Label();
            this.VaultsComboBox = new System.Windows.Forms.ComboBox();
            this.FileListBox = new System.Windows.Forms.ListBox();
            this.BrowseButton = new System.Windows.Forms.Button();
            this.UpdateReferencesButton = new System.Windows.Forms.Button();
            this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.SuspendLayout();
            //
            // Label1
            //
            this.Label1.AutoSize = true;
            this.Label1.Location = new System.Drawing.Point(13, 9);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(91, 13);
            this.Label1.TabIndex = 0;
            this.Label1.Text = "Select vault view:";
            //
            // VaultsComboBox
            //
            this.VaultsComboBox.FormattingEnabled = true;
            this.VaultsComboBox.Location = new System.Drawing.Point(16, 26);
            this.VaultsComboBox.Name = "VaultsComboBox";
            this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
            this.VaultsComboBox.TabIndex = 1;
            //
            // FileListBox
            //
            this.FileListBox.FormattingEnabled = true;
            this.FileListBox.Location = new System.Drawing.Point(16, 66);
            this.FileListBox.Name = "FileListBox";
            this.FileListBox.Size = new System.Drawing.Size(165, 17);
            this.FileListBox.TabIndex = 2;
            //
            // BrowseButton
            //
            this.BrowseButton.Location = new System.Drawing.Point(206, 66);
            this.BrowseButton.Name = "BrowseButton";
            this.BrowseButton.Size = new System.Drawing.Size(66, 23);
            this.BrowseButton.TabIndex = 3;
            this.BrowseButton.Text = "Browse...";
            this.BrowseButton.UseVisualStyleBackColor = true;
            this.BrowseButton.Click += new System.EventHandler(this.BrowseButton_Click);
            //
            // UpdateReferencesButton
            //
            this.UpdateReferencesButton.Location = new System.Drawing.Point(16, 113);
            this.UpdateReferencesButton.Name = "UpdateReferencesButton";
            this.UpdateReferencesButton.Size = new System.Drawing.Size(121, 23);
            this.UpdateReferencesButton.TabIndex = 4;
            this.UpdateReferencesButton.Text = "Update references";
            this.UpdateReferencesButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.UpdateReferencesButton.UseVisualStyleBackColor = true;
            this.UpdateReferencesButton.Click += new System.EventHandler(this.UpdateReferencesButton_Click);
            //
            // OpenFileDialog1
            //
            this.OpenFileDialog1.FileName = "OpenFileDialog1";
            this.OpenFileDialog1.Multiselect = true;
            this.OpenFileDialog1.Title = "Select a file";
            //
            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 161);
            this.Controls.Add(this.UpdateReferencesButton);
            this.Controls.Add(this.BrowseButton);
            this.Controls.Add(this.FileListBox);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.Label1);
            this.Name = "Form1";
            this.Text = "Update References";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label Label1;
        private System.Windows.Forms.ComboBox VaultsComboBox;
        private System.Windows.Forms.ListBox FileListBox;
        private System.Windows.Forms.Button BrowseButton;
        private System.Windows.Forms.Button UpdateReferencesButton;
        private System.Windows.Forms.OpenFileDialog OpenFileDialog1;
    }
}
```

```
Back to top
```
