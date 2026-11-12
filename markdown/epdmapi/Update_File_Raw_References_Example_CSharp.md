---
title: "Update File Raw References Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Update_File_Raw_References_Example_CSharp.htm"
---

# Update File Raw References Example (C#)

This example shows how to get file references directly from a file and update file references directly in that file.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Start Microsoft Visual Studio.
// 2. Click File > New > Project > C#,
Windows, Desktop > Windows Forms App.

// 3. Type RawReferencesCSharp in Project
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
//12. Check out a SOLIDWORKS assembly or drawing document whose file
//    references you want to update and check out all of the document's
//    referenced files.
//13. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays the Update Raw References in File dialog box.
//  2. Select the vault view where the SOLIDWORKS assembly or
//     drawing document that you checked out in
//     Preconditions step 4 resides.
//  3. Click Open file.
//  4. Displays the Open a file dialog box.
//     a. Click the assembly or drawing document you checked out
//        in Preconditions step 4.
//     b. Click Open.
//     The opened file's path and file name appear
//     in the Update Raw References in File dialog box.
//  5. Click Get references.
//     a. Displays a message box for each referenced file.
//        The referenced file's ID, path and file name, file name,
//        type, and number of times referenced appear in the
//        message box.
//     b. Click OK to close each message box.
//  6. Rename one of the referenced files in the selected vault
//     in File Explorer.
//  7. Click Update references.
//     a. Displays a message box confirming that references were updated.
//     b. Click OK to close the message box.
//  8. Click Get references.
//     a. Displays a message box for each referenced file.
//        The referenced file's ID, path and file name, file name,
//        type, and number of times referenced appear in the
//        message box. Note that the renamed file is now a referenced
//        file of the open document.
//     b. Click OK to close each message box.
//  9. Click Close file.
// 10. Click OK to close the message box confirming that the open
//     document was closed.
// 11. Close the Update Raw References in File dialog box.
// 12. Check in the SOLIDWORKS assembly or drawing document and
//     its file references.
//----------------------------------------------------------------------------

//Form1.cs
using System;
using System.Windows.Forms;
using EPDM.Interop.epdm;

namespace RawReferencesCSharp
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
        IEdmRawReferenceMgr rawRefs;
        EdmRawReference[] refs = null;

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

        public void UpdateButton_Click(System.Object sender, System.EventArgs e)
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

                //Update the file references directly in the file
                rawRefs.UpdateReferences(refs);
                MessageBox.Show("File references updated.");

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

        public void OpenButton_Click(System.Object sender, System.EventArgs e)
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
                //Set the initial directory in the Open a file dialog
                OpenFileDialog1.InitialDirectory = vault1.RootFolderPath;
                //Show the Open a file dialog
                System.Windows.Forms.DialogResult DialogResult;
                DialogResult = OpenFileDialog1.ShowDialog();

                if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
                {
                    //Do nothing
                }
                else
                {
                    //Click a file
                    IEdmFolder5 retPath = default(IEdmFolder5);
                    fileName = OpenFileDialog1.FileName;
                    FileListBox.Items.Add(fileName);
                    aFile = vault1.GetFileFromPath(fileName, out retPath);

                }

                //Get IEdmRawReferences interface
                IEdmVault7 vault2 = null;
                vault2 = (IEdmVault7)vault1;
                rawRefs = (IEdmRawReferenceMgr)vault2.CreateUtility(EdmUtility.EdmUtil_RawReferenceMgr);
                bool fileRefsSupported = false;
                fileRefsSupported = rawRefs.Open(fileName);
                if (!fileRefsSupported)
                {
                    MessageBox.Show("File's format does not support file references.");
                    return;
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

        private void GetButton_Click(System.Object sender, System.EventArgs e)
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

                int arrSize = 0;
                int i = 0;
                string message = null;
                //Get the file references directly from the file
                rawRefs.GetReferences(ref refs);
                arrSize = refs.Length;
                if (arrSize == 0)
                {
                    MessageBox.Show("No file references for opened file.");
                    return;
                }
                while (i < arrSize)
                {
                    message = "File reference information: " + "\n" + "\n";
                    message = message + "  Internal ID: " + refs[i].mbsRefID + "\n";
                    message = message + "  Referenced how: " + refs[i].mbsIncludePath + "\n";
                    message = message + "  Reference name: " + refs[i].mbsRefName + "\n";
                    message = message + "  Number of times file referenced = " + refs[i].mlCount.ToString() + "\n";
                    switch (refs[i].mlFlags)
                    {
                        case (int)EdmRawRefFlags.Edmrrf_Ghost:
                            message = message + "  Type = DWG files can store grandchildren as references" + "\n";
                            break;
                        case (int)EdmRawRefFlags.Edmrrf_InternalComponent:
                            message = message + "  Type = Not used" + "\n";
                            break;
                        case (int)EdmRawRefFlags.Edmrrf_Nothing:
                            message = message + "  Type = Normal file reference" + "\n";
                            break;
                    }
                    i = i + 1;
                    MessageBox.Show(message);
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

        private void CloseButton_Click(System.Object sender, System.EventArgs e)
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

                //Close the file
                rawRefs.Close();
                MessageBox.Show("File closed.");

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
namespace RawReferencesCSharp
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
            this.label1 = new System.Windows.Forms.Label();
            this.VaultsComboBox = new System.Windows.Forms.ComboBox();
            this.OpenButton = new System.Windows.Forms.Button();
            this.FileListBox = new System.Windows.Forms.ListBox();
            this.UpdateButton = new System.Windows.Forms.Button();
            this.GetButton = new System.Windows.Forms.Button();
            this.CloseButton = new System.Windows.Forms.Button();
            this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.SuspendLayout();
            //
            // label1
            //
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(82, 24);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(91, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Select vault view:";
            //
            // VaultsComboBox
            //
            this.VaultsComboBox.FormattingEnabled = true;
            this.VaultsComboBox.Location = new System.Drawing.Point(41, 40);
            this.VaultsComboBox.Name = "VaultsComboBox";
            this.VaultsComboBox.Size = new System.Drawing.Size(196, 21);
            this.VaultsComboBox.TabIndex = 1;
            //
            // OpenButton
            //
            this.OpenButton.Location = new System.Drawing.Point(74, 67);
            this.OpenButton.Name = "OpenButton";
            this.OpenButton.Size = new System.Drawing.Size(108, 23);
            this.OpenButton.TabIndex = 2;
            this.OpenButton.Text = "Open file";
            this.OpenButton.UseVisualStyleBackColor = true;
            this.OpenButton.Click += new System.EventHandler(OpenButton_Click);
            //
            // FileListBox
            //
            this.FileListBox.FormattingEnabled = true;
            this.FileListBox.Location = new System.Drawing.Point(12, 96);
            this.FileListBox.Name = "FileListBox";
            this.FileListBox.Size = new System.Drawing.Size(235, 30);
            this.FileListBox.TabIndex = 3;
            //
            // OpenFileDialog1
            //
            this.OpenFileDialog1.FileName = "OpenFileDialog1";
            this.OpenFileDialog1.Multiselect = true;
            this.OpenFileDialog1.Title = "Open a file";
            //
            // UpdateButton
            //
            this.UpdateButton.Location = new System.Drawing.Point(139, 144);
            this.UpdateButton.Name = "UpdateButton";
            this.UpdateButton.Size = new System.Drawing.Size(108, 23);
            this.UpdateButton.TabIndex = 4;
            this.UpdateButton.Text = "Update references";
            this.UpdateButton.UseVisualStyleBackColor = true;
            this.UpdateButton.Click += new System.EventHandler(UpdateButton_Click);
            //
            // GetButton
            //
            this.GetButton.Location = new System.Drawing.Point(12, 144);
            this.GetButton.Name = "GetButton";
            this.GetButton.Size = new System.Drawing.Size(108, 23);
            this.GetButton.TabIndex = 5;
            this.GetButton.Text = "Get references";
            this.GetButton.UseVisualStyleBackColor = true;
            this.GetButton.Click += new System.EventHandler(GetButton_Click);
            //
            // CloseButton
            //
            this.CloseButton.Location = new System.Drawing.Point(74, 192);
            this.CloseButton.Name = "CloseButton";
            this.CloseButton.Size = new System.Drawing.Size(99, 23);
            this.CloseButton.TabIndex = 6;
            this.CloseButton.Text = "Close file";
            this.CloseButton.UseVisualStyleBackColor = true;
            this.CloseButton.Click += new System.EventHandler(CloseButton_Click);
            //
            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(266, 233);
            this.Controls.Add(this.CloseButton);
            this.Controls.Add(this.GetButton);
            this.Controls.Add(this.UpdateButton);
            this.Controls.Add(this.FileListBox);
            this.Controls.Add(this.OpenButton);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Update Raw References in File";
            this.Load += new System.EventHandler(Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox VaultsComboBox;
        private System.Windows.Forms.Button OpenButton;
        private System.Windows.Forms.ListBox FileListBox;
        private System.Windows.Forms.Button UpdateButton;
        private System.Windows.Forms.Button GetButton;
        private System.Windows.Forms.Button CloseButton;
        private System.Windows.Forms.OpenFileDialog OpenFileDialog1;

    }
}
```

```
Back to top
```
