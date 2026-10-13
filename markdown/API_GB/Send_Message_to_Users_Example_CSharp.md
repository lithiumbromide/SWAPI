---
title: "Send Message to Users Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Send_Message_to_Users_Example_CSharp.htm"
---

# Send Message to Users Example (C#)

This example shows how to send a message, also called a notification, to logged-in users who have permission to modify Categories.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
//  1. Start Microsoft Visual Studio 2010.
//  2. Click File > New > Project > C# > Windows Forms Application.
//  3. Type SendMessageCSharp in Name.
//  4. Click the Browse button and browse to the folder where to create the project.
//  5. Click OK.
//  6. Create a form similar to the form shown above and change:
//     a. Label to VaultsLabel.
//     b. Combo box to VaultsComboBox.
//     c. Button to TraverseUsersButton.
//  7. Replace the code in Form1.cs with this code.
//  8. Replace the code in Form1.Designer.cs with this code.
//  9. Add EPDM.Interop.epdm.dll as a reference (right-click the project
//     name in the Solution Explorer, click Add Reference, click
//     Framework in the left-side panel, browse to the top folder of your
//     SOLIDWORKS PDM Professional installation, locate and click
//     EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
// 10. Right-click EPDM.Interop.epdm in References, click Properties, and set
//     Embed Interop Types to False to handle methods that pass arrays of
//     structures.
// 11. Switch back to the Form1.cs code window.
// 12. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays a dialog.
//  2. Select a vault.
//  3. Click the Send message to users who can modify Categories button.
//  4. After several minutes, a SOLIDWORKS PDM Professional notification
//     is displayed only to logged-in users who have
//     permission to modify Categories.
//  5. To open the the message, click:
//     * either the notification while it is displayed or
//       the SOLIDWORKS PDM Professional tray icon.
//       - or -
//     * Tools > Inbox in File Explorer.
//  6. Close the dialog.
//----------------------------------------------------------------------------

//Form1.cs
using System;
using System.Windows.Forms;
using System.Diagnostics;
using System.Runtime.InteropServices;
using EPDM.Interop.epdm;

namespace SendMessageCSharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        void SendMessageCSharp_Load(System.Object sender, System.EventArgs e)
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
                MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void TraverseUsersButton_Click(System.Object sender, System.EventArgs e)
        {

            try
            {
                //Declare and create an instance of IEdmVault5 object
                IEdmVault5 vault = new EdmVault5();
                //Log into selected vault as the current user
                vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());

                //Declare an IEdmUserMgr5 object
                IEdmUserMgr5 UserMgr = default(IEdmUserMgr5);
                UserMgr = (IEdmUserMgr5)vault;

                IEdmPos5 UserPos = default(IEdmPos5);
                UserPos = UserMgr.GetFirstUserPosition();
                while (!UserPos.IsNull)
                {
                    IEdmUser5 User = default(IEdmUser5);
                    IEdmUser7 User1 = default(IEdmUser7);
                    User = UserMgr.GetNextUser(UserPos);
                    User1 = (IEdmUser7)User;
                    if (User.IsLoggedIn)
                    {
                        if (User1.HasSysRightEx(EdmSysPerm.EdmSysPerm_ModifyCategories))
                        {
                            User.SendMsg("Category request", "Please stop by my office sometime " + "this morning to discuss adding " + "a new file type to a Category.");
                        }
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
namespace SendMessageCSharp
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
            this.TraverseUsersButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            //
            // VaultsLabel
            //
            this.VaultsLabel.AutoSize = true;
            this.VaultsLabel.Location = new System.Drawing.Point(80, 27);
            this.VaultsLabel.Name = "VaultsLabel";
            this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
            this.VaultsLabel.TabIndex = 0;
            this.VaultsLabel.Text = "Select vault view:";
            //
            // VaultsComboBox
            //
            this.VaultsComboBox.FormattingEnabled = true;
            this.VaultsComboBox.Location = new System.Drawing.Point(67, 67);
            this.VaultsComboBox.Name = "VaultsComboBox";
            this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
            this.VaultsComboBox.TabIndex = 1;
            //
            // TraverseUsersButton
            //
            this.TraverseUsersButton.Location = new System.Drawing.Point(67, 110);
            this.TraverseUsersButton.Name = "TraverseUsersButton";
            this.TraverseUsersButton.Size = new System.Drawing.Size(121, 53);
            this.TraverseUsersButton.TabIndex = 2;
            this.TraverseUsersButton.Text = "Send message to users who can modify Categories";
            this.TraverseUsersButton.UseVisualStyleBackColor = true;
            this.TraverseUsersButton.Click += new System.EventHandler(this.TraverseUsersButton_Click);
            //
            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(268, 200);
            this.Controls.Add(this.TraverseUsersButton);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.VaultsLabel);
            this.Name = "Form1";
            this.Text = "Send Message to Users";
            this.Load += new System.EventHandler(this.SendMessageCSharp_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label VaultsLabel;
        private System.Windows.Forms.ComboBox VaultsComboBox;
        private System.Windows.Forms.Button TraverseUsersButton;
    }
}
```

```
Back to top
```
