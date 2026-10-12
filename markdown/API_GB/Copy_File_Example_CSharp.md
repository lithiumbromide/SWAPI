---
title: "Copy File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Copy_File_Example_CSharp.htm"
---

# Copy File Example (C#)

This example shows how to copy a file in the vault to a different folder in the vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Start Microsoft Visual Studio 2010.
//    a. Click File > New > Project > Visual C# > Windows Forms Application.
//    b. Type VaultUtilities in Name.
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
// 3. Add EPDM.Interop.EPDMResultCode.dll as a reference (click Browse, locate and
//    click EPDM.Interop.EPDMResultCode.dll, click Open, click Add, and click Close).
// 4. Right-click EPDM.Interop.epdm in References, click Properties, and set
//    Embed Interop Types to False to handle methods that pass arrays of
//    structures.
// 5. Run the Administration tool, log in as admin, expand the vault,
//    right-click File Types, click Duplicate file name settings, and
//    click Do not allow duplicate files names in this file vault.
// 6. Ensure that multiple folders exists in vault.
// 7. Click Debug > Start Debugging or press F5.
//
// Postconditions:
// 1. Displays the Copy file dialog box.
//    a. Select a vault view.
//    b. Click Copy file.
//       1. In the Open dialog, click a vault file.
//       2. Click Open.
//       3. In the Select Folder dialog, click a different folder to which to
//          copy the selected file.
//       4. Click OK.
//       5. Displays a message with the file copy status.
//       6. Click OK.
// 2. Close the Copy file dialog box.
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
using Microsoft.VisualBasic;

namespace VaultUtilities_CSharp
{
    public partial class Form1 : Form
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
                MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void Button1_Click(System.Object sender, System.EventArgs e)
        {
            //Copy file

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
                    //Log into selected vault as the current user
                    vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                }

                EdmStrLst5 pathList = default(EdmStrLst5);
                pathList = vault2.BrowseForFile(this.Handle.ToInt32(), (int)EdmBrowseFlag.EdmBws_ForOpen + (int)EdmBrowseFlag.EdmBws_PermitVaultFiles);
                if (pathList == null)
                    return;

                IEdmFile5 file = default(IEdmFile5);
                IEdmFolder5 srcFolder = null;
                file = vault2.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition()), out srcFolder);

                IEdmFolder5 destFolder1 = default(IEdmFolder5);
                destFolder1 = vault2.BrowseForFolder(this.Handle.ToInt32(), "Select destination folder:");
                if (destFolder1 == null)
                    return;

                IEdmFolder8 destFolder = (IEdmFolder8)destFolder1;

                int fileID = 0;
                int copyFileStatus;
                fileID = destFolder.CopyFile2(file.ID, srcFolder.ID, this.Handle.ToInt32(), out copyFileStatus, "", (int)EdmCopyFlag.EdmCpy_Simple);
                switch (copyFileStatus)
                {
                    case (int)EdmResultSuccessCodes_e.S_EDM_FILES_NOT_UNIQUE_GLOBALLY:
                        MessageBox.Show("WARNING: File is not unique in the vault, but the file was copied to a new file with a file ID of " + fileID + ".");
                        break;
                    case 0:
                        MessageBox.Show("SUCCESS: File copied to a new file with a file ID of " + fileID + ".");
                        break;
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
//Form1.Designer.cs
```

```
namespace VaultUtilities_CSharp
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
            this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
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
            // Button1
            //
            this.Button1.Location = new System.Drawing.Point(16, 82);
            this.Button1.Name = "Button1";
            this.Button1.Size = new System.Drawing.Size(66, 23);
            this.Button1.TabIndex = 6;
            this.Button1.Text = "Copy file";
            this.Button1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.Button1.UseVisualStyleBackColor = true;
            this.Button1.Click += new System.EventHandler(this.Button1_Click);
            //
            // OpenFileDialog1
            //
            this.OpenFileDialog1.FileName = "OpenFileDialog1";
            //
            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(197, 140);
            this.Controls.Add(this.Button1);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.VaultsLabel);
            this.Name = "Form1";
            this.Text = "Copy file";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.Label VaultsLabel;
        internal System.Windows.Forms.ComboBox VaultsComboBox;
        internal System.Windows.Forms.Button Button1;
        internal System.Windows.Forms.OpenFileDialog OpenFileDialog1;
    }
}
```
