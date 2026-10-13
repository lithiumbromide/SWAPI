---
title: "Log Into Vault and Display Information Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Log_Into_Vault_and_Display_Information_Example_CSharp.htm"
---

# Log Into Vault and Display Information Example (C#)

This example shows how to create an application that displays a form where a user can select a vault in which to log in and display information about that vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Start Microsoft Visual Studio.
// 2. Click File > New > Project > C#,
Windows, Desktop > Windows Forms App.

// 3. Type Exercise1CSharp in Project
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
//11. To create the form, replace the code in Form1.Designer.cs with this code.
//12. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays a dialog.
//  2. Select a vault.
//  3. Click Log in and display vault information.
//     A message box pops up containing the version of
//     SOLIDWORKS PDM Professional installed on your computer.
//  4. Click OK to close the message box.
//     Another message box pops up containing the path of the selected
//     vault view folder.
//  5. Click OK to close the message box.
//  6. Type the name of a nonexistent vault in the drop-down combo box.
//  7. Click Log in and display vault information.
//  8. A message box pops up instructing you to type or select
//     a valid database.
//  9. Click OK to close the message box.
// 10. Close the dialog box.
//----------------------------------------------------------------------------

//Form1.cs
using System;
using System.Windows.Forms;
using System.Diagnostics;
using System.Runtime.InteropServices;
using EPDM.Interop.epdm;
using EPDM.Interop.EPDMResultCode;

namespace Exercise1CSharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

        }

        void Exercise1CSharp_Load(System.Object sender, System.EventArgs e)
        {
            try
            {
                //Declare and create an instance of IEdmVault5
                IEdmVault5 vault1 = new EdmVault5();

                //Cast IEdmVault5 to IEdmVault8
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
                MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " +  ex.Message);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void LoginButton_Click(System.Object sender, System.EventArgs e)
        {
            try
            {
                //Declare and create an instance of IEdmVault5 object
                IEdmVault5 vault = new EdmVault5();

                //Log into the selected vault as the current user
                vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());

                //Display the SOLIDWORKS PDM Professional version
                int VerMajor = 0;
                int VerMinor = 0;
                vault.GetVersion(ref VerMajor, ref VerMinor);
                MessageBox.Show("SOLIDWORKS PDM Professional " + "version is " + VerMajor.ToString() + "." + VerMinor.ToString());

                //Display the path of the vault view folder
                MessageBox.Show("The path of the vault view " + "folder is \"" + vault.RootFolderPath + "\".");
            }
            catch (System.Runtime.InteropServices.COMException ex)
            {
                switch (ex.ErrorCode)
                {
                    case (int)EdmResultErrorCodes_e.E_EDM_CANT_OPEN_DATABASE:
                        MessageBox.Show("Could not open database. Select or type the name of valid database.");
                        break;
                    default:
                        MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
                        break;
                }
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

namespace Exercise1CSharp
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used
        /// </summary>
        /// <param name="disposing">True if managed resources should be disposed; otherwise false</param>
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
        /// the contents of this method with the code editor
        /// </summary>
        private void InitializeComponent()
        {
            this.VaultsLabel = new System.Windows.Forms.Label();
            this.VaultsComboBox = new System.Windows.Forms.ComboBox();
            this.LoginButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            //
            // VaultsLabel
            //
            this.VaultsLabel.AutoSize = true;
            this.VaultsLabel.Location = new System.Drawing.Point(62, 23);
            this.VaultsLabel.Name = "VaultsLabel";
            this.VaultsLabel.Size = new System.Drawing.Size(75, 13);
            this.VaultsLabel.TabIndex = 1;
            this.VaultsLabel.Text = "Select a vault:";
            //
            // VaultsComboBox
            //
            this.VaultsComboBox.FormattingEnabled = true;
            this.VaultsComboBox.Location = new System.Drawing.Point(22, 54);
            this.VaultsComboBox.Name = "VaultsComboBox";
            this.VaultsComboBox.Size = new System.Drawing.Size(184, 21);
            this.VaultsComboBox.TabIndex = 2;
            //
            // LoginButton
            //
            this.LoginButton.Location = new System.Drawing.Point(37, 100);
            this.LoginButton.Name = "LoginButton";
            this.LoginButton.Size = new System.Drawing.Size(146, 37);
            this.LoginButton.TabIndex = 4;
            this.LoginButton.Text = "Log in and display vault information";
            this.LoginButton.UseVisualStyleBackColor = true;
            this.LoginButton.Click += new System.EventHandler(this.LoginButton_Click);
            //
            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(227, 184);
            this.Controls.Add(this.LoginButton);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.VaultsLabel);
            this.Name = "Form1";
            this.Load += new System.EventHandler(this.Exercise1CSharp_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label VaultsLabel;
        private System.Windows.Forms.ComboBox VaultsComboBox;
        private System.Windows.Forms.Button LoginButton;

    }
}
```

```
Back to top
```
