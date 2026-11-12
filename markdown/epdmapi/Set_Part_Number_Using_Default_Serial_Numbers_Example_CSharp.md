---
title: "Set Part Numbers Using Default Serial Numbers Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Set_Part_Number_Using_Default_Serial_Numbers_Example_CSharp.htm"
---

# Set Part Numbers Using Default Serial Numbers Example (C#)

This example shows how to set part numbers using default serial numbers.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Start Microsoft Visual Studio.
// 2. Click File > New > Project > C#,
Windows, Desktop > Windows Forms App.

// 3. Type SerialNumbersCSharp in Project
name.

// 4. For Location, click ... and navigate to the folder where to
create the project.

// 5. Click Next.

// 6. Select Framework.

// 7. Click Create.

// 8. Click Show All Files in the Solution Explorer toolbar and expand

//    Form1.cs in the Solution Explorer.

// 9. Add dependencies and
safely pass arrays of structures.
//10. Replace the code in Form1.cs with this code.
//11. To create the form, replace the code in Form1.Designer.cs with
//    this code.
//12. Ensure that you have:
//     * a vault with at least one serial number generator.
//     * a checked-out file in that vault with its Part Number variable's
//       default set to a serial number.
//13. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays the Serial Numbers dialog box.
//  2. Select a vault view.
//  3. Click Get Vault Serial Number Names.
//  4. Displays a message box containing the names of the serial number
//     generators for the selected vault.
//  5. Click OK to close the message box.
//  6. Click Browse.
//     a. Click a checked-out file in the selected vault whose
//        data card has a Part Number variable.
//     b. Click Open.
//     The selected file's path and file name appear in the Serial
//     Numbers dialog box.
//  7. Click Set New Serial Number.
//  8. Displays a message box verifying that the Part Number was
//     set and shows the value of that Part Number.
//     NOTES:
//     * The value set for the Part Number is the next number in the first
//       serial number generator shown in the message box displayed in
//       step 3.
//     * Make note of the Part Number.
//  9. Click OK to close the message box.
// 10. Check in the file whose Part Number was set in step 7, then check out the
//     file.
// 11. Examine the Part Number on the data card of the checked-out file.
// 12. Close the Serial Numbers dialog box.
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

namespace SerialNumbersCSharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private IEdmVault5 vault1 = null;
        string aSerialNbrName;
        string aFileName;
        IEdmFile5 aFile;
        string aFolder;
        IEdmSerNoGen7 serialNbrs;

    	private void Form1_Load(System.Object sender, System.EventArgs e)
	    {

		try {
			vault1 = new EdmVault5();
            		IEdmVault8 vault = (IEdmVault8)vault1;
			EdmViewInfo[] Views = null;

			vault.GetVaultViews(out Views, false);
			VaultsComboBox.Items.Clear();
			foreach (EdmViewInfo View in Views) {
				VaultsComboBox.Items.Add(View.mbsVaultName);
			}
			if (VaultsComboBox.Items.Count > 0) {
				VaultsComboBox.Text = (string) VaultsComboBox.Items[0];
			}

		} catch (System.Runtime.InteropServices.COMException ex) {
			MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " "  + ex.Message);
		} catch (Exception ex) {
			MessageBox.Show(ex.Message);
		}
	}

	public void Button1_Click(System.Object sender, System.EventArgs e)
	{
		try {
			//Only create a new vault object
			//if one hasn't been created yet
			IEdmVault11 vault2 = null;
			if (vault1 == null) {
				vault1 = new EdmVault5();
			}
			vault2 = (IEdmVault11)vault1;
			if (!vault1.IsLoggedIn) {
				//Log into selected vault as the current user
				vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
			}

			serialNbrs = (IEdmSerNoGen7)vault2.CreateUtility(EdmUtility.EdmUtil_SerNoGen);
			string[] names = {	};
			serialNbrs.GetSerialNumberNames(out names);
			string myMessage = "";
			myMessage = "Serial number names in selected vault: " + "\n ";
			int idx = 0;
			idx = (names.GetLowerBound(0));
			while (idx <= (names.GetUpperBound(0))) {
				myMessage = myMessage + names[idx] + "\n";
				idx = idx + 1;
			}

			// Use this serial number generator
			aSerialNbrName = names[0];

			MessageBox.Show(myMessage);

		} catch (System.Runtime.InteropServices.COMException ex) {
			MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
		} catch (Exception ex) {
			MessageBox.Show(ex.Message);
		}
	}

	public void BrowseButton_Click(System.Object sender, System.EventArgs e)
	{
		try {

			//Set the initial directory in the Select a file dialog
			OpenFileDialog1.InitialDirectory = vault1.RootFolderPath;
			//Show the Select a file dialog
			System.Windows.Forms.DialogResult DialogResult;
			DialogResult = OpenFileDialog1.ShowDialog();

			if (!(DialogResult == System.Windows.Forms.DialogResult.OK)) {
				// Do nothing
			} else {
				// Browse for a file whose serial number to set
				// File's data card must have a Part Number associated
				// with a serial number generator and must be checked out
				string fileName = OpenFileDialog1.FileName;
				FileListBox.Items.Add(fileName);
                			IEdmFolder5 retFolder = default(IEdmFolder5);
				aFile = vault1.GetFileFromPath(fileName, out retFolder);

			}

		} catch (System.Runtime.InteropServices.COMException ex) {
			MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
		} catch (Exception ex) {
			MessageBox.Show(ex.Message);
		}
	}

	public void NewButton_Click(System.Object sender, System.EventArgs e)
	{
		try {

			IEdmSerNoValue serialNbrValue = default(IEdmSerNoValue);
			serialNbrValue = serialNbrs.AllocSerNoValue(aSerialNbrName, this.Handle.ToInt32(), " ", 0, 0, 0, 0);
			dynamic serialNbrValueValue = serialNbrValue.Value;
			IEdmEnumeratorVariable5 enumVariable = default(IEdmEnumeratorVariable5);
			enumVariable = aFile.GetEnumeratorVariable(aFileName);
			// Set the Part Number of the selected file
			enumVariable.SetVar("Part Number", "@", serialNbrValueValue);
            		IEdmEnumeratorVariable8 enumVariable8 = (IEdmEnumeratorVariable8)enumVariable;
			enumVariable8.CloseFile(true);

			MessageBox.Show("Part Number set to " + serialNbrValueValue.ToString() + "." + " ");

		} catch (System.Runtime.InteropServices.COMException ex) {
			MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
		} catch (Exception ex) {
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
namespace SerialNumbersCSharp
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
			this.Button1 = new System.Windows.Forms.Button();
			this.FileListBox = new System.Windows.Forms.ListBox();
			this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
			this.BrowseButton = new System.Windows.Forms.Button();
			this.NewButton = new System.Windows.Forms.Button();
			this.SuspendLayout();
			//
			//VaultsLabel
			//
			this.VaultsLabel.AutoSize = true;
			this.VaultsLabel.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
			this.VaultsLabel.Location = new System.Drawing.Point(25, 28);
			this.VaultsLabel.Name = "VaultsLabel";
			this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
			this.VaultsLabel.TabIndex = 0;
			this.VaultsLabel.Text = "Select vault view:";
			//
			//VaultsComboBox
			//
			this.VaultsComboBox.FormattingEnabled = true;
			this.VaultsComboBox.Location = new System.Drawing.Point(28, 44);
			this.VaultsComboBox.Name = "VaultsComboBox";
			this.VaultsComboBox.Size = new System.Drawing.Size(190, 21);
			this.VaultsComboBox.TabIndex = 1;
			//
			//Button1
			//
			this.Button1.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
			this.Button1.Location = new System.Drawing.Point(28, 84);
			this.Button1.Name = "Button1";
			this.Button1.Size = new System.Drawing.Size(190, 23);
			this.Button1.TabIndex = 2;
			this.Button1.Text = "Get Vault Serial Number Names";
			this.Button1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			this.Button1.UseVisualStyleBackColor = true;
            		this.Button1.Click += new System.EventHandler(this.Button1_Click);
			//
			//FileListBox
			//
			this.FileListBox.FormattingEnabled = true;
			this.FileListBox.Location = new System.Drawing.Point(28, 141);
			this.FileListBox.Name = "FileListBox";
			this.FileListBox.Size = new System.Drawing.Size(190, 17);
			this.FileListBox.TabIndex = 3;
			//
			//OpenFileDialog1
			//
			this.OpenFileDialog1.FileName = "OpenFileDialog1";
			this.OpenFileDialog1.Multiselect = true;
			this.OpenFileDialog1.Title = "Select a file";
			//
			//BrowseButton
			//
			this.BrowseButton.Location = new System.Drawing.Point(239, 135);
			this.BrowseButton.Name = "BrowseButton";
			this.BrowseButton.Size = new System.Drawing.Size(56, 23);
			this.BrowseButton.TabIndex = 4;
			this.BrowseButton.Text = "Browse...";
			this.BrowseButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			this.BrowseButton.UseVisualStyleBackColor = true;
            		this.BrowseButton.Click += new System.EventHandler(this.BrowseButton_Click);
			//
			//NewButton
			//
			this.NewButton.Location = new System.Drawing.Point(28, 182);
			this.NewButton.Name = "NewButton";
			this.NewButton.Size = new System.Drawing.Size(190, 23);
			this.NewButton.TabIndex = 5;
			this.NewButton.Text = "Set New Serial Number";
			this.NewButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			this.NewButton.UseVisualStyleBackColor = true;
            		this.NewButton.Click += new System.EventHandler(this.NewButton_Click);
			//
			//Form1
			//
			this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(326, 262);
			this.Controls.Add(this.NewButton);
			this.Controls.Add(this.BrowseButton);
			this.Controls.Add(this.FileListBox);
			this.Controls.Add(this.Button1);
			this.Controls.Add(this.VaultsComboBox);
			this.Controls.Add(this.VaultsLabel);
			this.Name = "Form1";
			this.Text = "Serial Numbers";
            		this.Load += new System.EventHandler(this.Form1_Load);
			this.ResumeLayout(false);
			this.PerformLayout();

	}

	#endregion

	internal System.Windows.Forms.Label VaultsLabel;
	internal System.Windows.Forms.ComboBox VaultsComboBox;
	internal System.Windows.Forms.Button Button1;
	internal System.Windows.Forms.ListBox FileListBox;
	internal System.Windows.Forms.Button BrowseButton;
	internal System.Windows.Forms.Button NewButton;
	internal System.Windows.Forms.OpenFileDialog OpenFileDialog1;

   }

}
```

```
Back to top
```
