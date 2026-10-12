---
title: "Get File Version Information Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_File_Version_Information_Example_CSharp.htm"
---

# Get File Version Information Example (C#)

This example shows how to get the version information of a file.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Start Microsoft Visual Studio.
// 2. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
// 3. Type GetFileVersionsCSharp in Project name.
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
//12. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays the Version Information dialog box.
//     a. Select a vault view.
//     b. Click Browse.
//     c. In the Select a file dialog:
//        1. Click a file in the vault.
//        2. Click Open.
//  2. Click Get file's version information.
//  3. Displays a message box containing the file name, number of versions, and
//     each version number, date, user, file size, and comments, if any.
//  4. Click OK to close the message box.
//  5. Close the Version Information dialog box.
//----------------------------------------------------------------------------
```

```
//Form1.cs

using EPDM.Interop.epdm;
using System;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace GetFileVersionsCSharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private IEdmVault5 vault1 = null;
        IEdmFile5 aFile;

        public void GetFileVersionsCSharp_Load(System.Object sender, System.EventArgs e)
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

        public void BrowseButton_Click(System.Object sender, System.EventArgs e)
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

                //Set the initial directory in the Select a file dialog
                OpenFileDialog1.InitialDirectory = vault1.RootFolderPath;
                //Show the Select a file dialog
                System.Windows.Forms.DialogResult DialogResult;
                DialogResult = OpenFileDialog1.ShowDialog();

                if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
                {
                    // Do nothing
                }
                else
                {
                    // Browse for file whose versions to get
                    string FileName = OpenFileDialog1.FileName;
                    FileListBox.Items.Add(FileName);
                    IEdmFolder5 retFolder = default(IEdmFolder5);
                    aFile = vault1.GetFileFromPath(FileName, out retFolder);
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

        public void Button1_Click(System.Object sender, System.EventArgs e)
        {
            try
            {
                IEdmFile5 file = null;
                file = aFile;
                IEdmEnumeratorVersion5 enumVersion;
                enumVersion = (IEdmEnumeratorVersion5)file;
                IEdmPos5 pos = default(IEdmPos5);
                pos = enumVersion.GetFirstVersionPosition();
                IEdmVersion7 version = default(IEdmVersion7);
                string message = null;
                message = "History of " + file.Name + ": " + "\n";
                message = message + "Number of versions: " + enumVersion.VersionCount.ToString() + "\n";
                message = message + "\n";
                string str = null;
                while (!pos.IsNull)
                {
                    version = (IEdmVersion7)enumVersion.GetNextVersion(pos);
                    str = "Version: " + version.VersionNo.ToString();
                    message = message + str;
                    str = version.VersionDate.ToString();
                    message = message + ", file date = " + str + ", user = " + version.User.Name;
                    str = version.FileSize2.ToString();
                    message = message + ", file size = " + str + " bytes, comment = " + version.Comment + "\n";
                }

                MessageBox.Show(message);

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
namespace GetFileVersionsCSharp
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
		    this.VaultsComboBox = new System.Windows.Forms.ComboBox();
		    this.Button1 = new System.Windows.Forms.Button();
		    this.BrowseButton = new System.Windows.Forms.Button();
		    this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
		    this.Label1 = new System.Windows.Forms.Label();
		    this.FileListBox = new System.Windows.Forms.ListBox();
		    this.SuspendLayout();
		    //
		    //VaultsComboBox
		    //
		    this.VaultsComboBox.Location = new System.Drawing.Point(12, 37);
		    this.VaultsComboBox.Name = "VaultsComboBox";
		    this.VaultsComboBox.Size = new System.Drawing.Size(161, 21);
		    this.VaultsComboBox.TabIndex = 7;
		    //
		    //Button1
		    //
		    this.Button1.Location = new System.Drawing.Point(12, 135);
		    this.Button1.Name = "Button1";
		    this.Button1.Size = new System.Drawing.Size(158, 23);
		    this.Button1.TabIndex = 4;
		    this.Button1.Text = "Get file's version information";
		    this.Button1.UseVisualStyleBackColor = true;
            this.Button1.Click += new System.EventHandler(Button1_Click);
		    //
		    //BrowseButton
		    //
		    this.BrowseButton.ImageAlign = System.Drawing.ContentAlignment.TopLeft;
		    this.BrowseButton.Location = new System.Drawing.Point(179, 83);
		    this.BrowseButton.Name = "BrowseButton";
		    this.BrowseButton.Size = new System.Drawing.Size(60, 28);
		    this.BrowseButton.TabIndex = 5;
		    this.BrowseButton.Text = "Browse...";
		    this.BrowseButton.UseVisualStyleBackColor = true;
            this.BrowseButton.Click += new System.EventHandler(BrowseButton_Click);
		    //
		    //OpenFileDialog1
		    //
		    this.OpenFileDialog1.FileName = "OpenFileDialog1";
		    this.OpenFileDialog1.Multiselect = true;
		    this.OpenFileDialog1.Title = "Select a file";
		    //
		    //Label1
		    //
		    this.Label1.AutoSize = true;
		    this.Label1.Location = new System.Drawing.Point(12, 21);
		    this.Label1.Name = "Label1";
		    this.Label1.Size = new System.Drawing.Size(91, 13);
		    this.Label1.TabIndex = 6;
		    this.Label1.Text = "Select vault view:";
		    //
		    //FileListBox
		    //
		    this.FileListBox.FormattingEnabled = true;
		    this.FileListBox.Location = new System.Drawing.Point(12, 81);
		    this.FileListBox.Name = "FileListBox";
		    this.FileListBox.Size = new System.Drawing.Size(161, 30);
		    this.FileListBox.TabIndex = 8;
		    //
		    //Form1
		    //
		    this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
		    this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
		    this.ClientSize = new System.Drawing.Size(252, 175);
		    this.Controls.Add(this.FileListBox);
		    this.Controls.Add(this.Label1);
		    this.Controls.Add(this.BrowseButton);
		    this.Controls.Add(this.Button1);
		    this.Controls.Add(this.VaultsComboBox);
		    this.Name = "Form1";
		    this.Text = "Version Information";
            this.Load += new System.EventHandler(this.GetFileVersionsCSharp_Load);

		    this.ResumeLayout(false);
		    this.PerformLayout();

	}

    #endregion

	private System.Windows.Forms.ComboBox VaultsComboBox;
	private System.Windows.Forms.Button BrowseButton;
	private System.Windows.Forms.Button Button1;
	private System.Windows.Forms.OpenFileDialog OpenFileDialog1;
	private System.Windows.Forms.Label Label1;
	private System.Windows.Forms.ListBox FileListBox;

    }
}
```

```
Back to top
```
