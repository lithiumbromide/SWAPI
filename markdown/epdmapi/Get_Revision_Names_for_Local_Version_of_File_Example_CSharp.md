---
title: "Get Revision Names for Local Version of File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_Revision_Names_for_Local_Version_of_File_Example_CSharp.htm"
---

# Get Revision Names for Local Version of File Example (C#)

This example shows how to the revision names for the local version of a file.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Start Microsoft Visual Studio.
// 2. Click File > New > Project > C#, Windows, Desktop > Windows Forms Application.
// 3. Type RevisionCSharp in Project name.
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
//12. To find a file with a revision scheme:
//     a. Open a vault view in File Explorer.
//     b. Click a file.
//     c. Click Display > History.
//     d. Examine the Event column. If Revision is:
//        * listed in the Event column, then the file
//          has a revision scheme.
//        * not listed in the Event column, then
//          repeat steps 4b - 4d until you find a file with
//          a revision scheme.
//13. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays the Get revision names dialog box.
//  2. Select a vault view.
//  3. Click Browse.
//  4. Displays the Select a file dialog box.
//     a. Click the file identified in Preconditions step 4 in the
//        selected vault.
//     b. Click Open.
//        The selected file's path and file name appear
//        in the Get revision names dialog box.
//  5. Click Get revisions.
//  6. Displays a message box:
//     * telling you that a local copy of the selected file does not exist.
//       - or -
//     * telling you that the selected file does not have a revision scheme.
//       - or -
//     * showing you a list of the names of the revisions for the selected file.
//  7. Click OK to close the message box.
//  8. Close the Get revision names dialog box.
//----------------------------------------------------------------------------
//Form1.cs

using EPDM.Interop.epdm;
using System.Windows.Forms;
using System;

namespace RevisionCSharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        IEdmVault5 vault1 = null;
        IEdmVault8 vault = null;
        IEdmFile5 aFile;
        IEdmFolder5 folder;

        private void Form1_Load(System.Object sender, System.EventArgs e)
        {
            try
            {
                vault1 = new EdmVault5();
                vault = (IEdmVault8)vault1;
                EdmViewInfo[] Views = { };

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

        public void RevisionButton_Click(System.Object sender, System.EventArgs e)
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

                //Get the local version number
                int version = 0;
                version = aFile.GetLocalVersionNo(folder.ID);
                if (version < 1)
                {
                    MessageBox.Show("A local copy of " + aFile.Name + " does not exist.");
                    return;
                }

                //Get the version interface
                IEdmEnumeratorVersion5 verEnum = default(IEdmEnumeratorVersion5);
                verEnum = (IEdmEnumeratorVersion5)aFile;
                IEdmVersion5 ver = default(IEdmVersion5);
                ver = (IEdmVersion5)verEnum.GetVersion(version);

                //Enumerate the revisions
                string message = null;
                IEdmPos5 pos = default(IEdmPos5);
                pos = ver.GetFirstRevisionPosition();

                if (!pos.IsNull)
                {
                    message = "The following revisions are set on " + aFile.Name + ": " + "\n";
                    IEdmRevision5 rev = default(IEdmRevision5);
                    while (!pos.IsNull)
                    {
                        rev = ver.GetNextRevision(pos);
                        message = message + "    " + rev.Name + "\n";
                    }
                }
                else
                {
                    message = "A revision scheme is not defined for " + aFile.Name + "." + "\n";
                    MessageBox.Show(message);
                    return;
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
                    //Browse for a local file whose revisions you want to see
                    string fileName = OpenFileDialog1.FileName;
                    FileListBox.Items.Add(fileName);
                    aFile = vault1.GetFileFromPath(fileName, out folder);

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
namespace RevisionCSharp
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
            this.FileListBox = new System.Windows.Forms.ListBox();
            this.BrowseButton = new System.Windows.Forms.Button();
            this.RevisionButton = new System.Windows.Forms.Button();
            this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.SuspendLayout();
            //
            // VaultsLabel
            //
            this.VaultsLabel.AutoSize = true;
            this.VaultsLabel.Location = new System.Drawing.Point(23, 13);
            this.VaultsLabel.Name = "VaultsLabel";
            this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
            this.VaultsLabel.TabIndex = 0;
            this.VaultsLabel.Text = "Select vault view:";
            //
            // VaultsComboBox
            //
            this.VaultsComboBox.FormattingEnabled = true;
            this.VaultsComboBox.Location = new System.Drawing.Point(26, 30);
            this.VaultsComboBox.Name = "VaultsComboBox";
            this.VaultsComboBox.Size = new System.Drawing.Size(220, 21);
            this.VaultsComboBox.TabIndex = 1;
            //
            // FileListBox
            //
            this.FileListBox.FormattingEnabled = true;
            this.FileListBox.Location = new System.Drawing.Point(26, 90);
            this.FileListBox.Name = "FileListBox";
            this.FileListBox.Size = new System.Drawing.Size(167, 17);
            this.FileListBox.TabIndex = 2;
            //
            // BrowseButton
            //
            this.BrowseButton.Location = new System.Drawing.Point(199, 84);
            this.BrowseButton.Name = "BrowseButton";
            this.BrowseButton.Size = new System.Drawing.Size(75, 23);
            this.BrowseButton.TabIndex = 3;
            this.BrowseButton.Text = "Browse...";
            this.BrowseButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.BrowseButton.UseVisualStyleBackColor = true;
            this.BrowseButton.Click += new System.EventHandler(BrowseButton_Click);
            //
            // OpenFileDialog1
            //
            this.OpenFileDialog1.FileName = "OpenFileDialog1";
            this.OpenFileDialog1.Multiselect = true;
            this.OpenFileDialog1.Title = "Select a file";

            //
            // RevisionButton
            //
            this.RevisionButton.Location = new System.Drawing.Point(26, 137);
            this.RevisionButton.Name = "RevisionButton";
            this.RevisionButton.Size = new System.Drawing.Size(88, 23);
            this.RevisionButton.TabIndex = 4;
            this.RevisionButton.Text = "Get revisions";
            this.RevisionButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.RevisionButton.UseVisualStyleBackColor = true;
            this.RevisionButton.Click += new System.EventHandler(RevisionButton_Click);
            //
            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 187);
            this.Controls.Add(this.RevisionButton);
            this.Controls.Add(this.BrowseButton);
            this.Controls.Add(this.FileListBox);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.VaultsLabel);
            this.Name = "Form1";
            this.Text = "Get revision names";
            this.Load += new System.EventHandler(Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label VaultsLabel;
        private System.Windows.Forms.ComboBox VaultsComboBox;
        private System.Windows.Forms.ListBox FileListBox;
        private System.Windows.Forms.Button BrowseButton;
        private System.Windows.Forms.Button RevisionButton;
        private System.Windows.Forms.OpenFileDialog OpenFileDialog1;
    }
}
```

```
Back to top
```
