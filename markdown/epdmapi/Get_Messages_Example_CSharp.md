---
title: "Get Messages Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_Messages_Example_CSharp.htm"
---

# Get Messages Example (C#)

This example shows how to get and encapsulate text messages in the Admin's inbox in a vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Start Microsoft Visual Studio.
// 2. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
// 3. Type MessageCSharp in Project name.
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
//12. Ensure that one or more text messages exist in the inbox of
//     Admin in a vault.
//     a. Log into a vault as Admin.
//     b. Open a File Explorer window for that vault.
//     c. Click Tools > Inbox.
//     d. Click Text Messages.
//     e. If no text messages are listed, send a text message to Admin.
//        1. Click New mail message.
//        2. Type Admin in To.
//        3. Type Test Get messages in Subject.
//        4. Type Testing Get messages in the body of the message.
//        5. Click Send.
//        6. Wait until you receive the SOLIDWORKS PDM Professional
//           message notification before executing the next step.
//13. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays the Get Messages dialog.
//  2. Select the vault that you examined or where you sent Admin
//     a text message in Preconditions step 4.
//  3. Click Get messages.
//  4. Displays a message box for each text message in Admin's inbox
//     in the selected vault. The message box contains encapsulated
//     information about the text message.
//  5. Click OK to close each message box.
//  6. Close the Get Messages dialog box.
//----------------------------------------------------------------------------
```

```
//Form1.cs
using System;
using System.Windows.Forms;
using EPDM.Interop.epdm;

namespace MessageCSharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        IEdmVault5 vault1 = null;

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

        private void GetMessagesButton_Click(System.Object sender, System.EventArgs e)
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

                //Declare an IEdmUserMgr5 object
                IEdmUserMgr5 userMgr = default(IEdmUserMgr5);

                //The IEdmUserMgr5 interface is implemented by the
                //same class as the IEdmVault5 interface,
                //so you can assign the value of
                //the IEdmVault5 object
                userMgr = (IEdmUserMgr5)vault1;

                IEdmUser5 user = default(IEdmUser5);
                user = userMgr.GetLoggedInUser();
                IEdmInbox5 inbox = (IEdmInbox5)user;

                //Get first text message in Admin's inbox
                IEdmMessage5 message = default(IEdmMessage5);
                IEdmPos5 pos = default(IEdmPos5);
                pos = inbox.GetFirstMessagePosition((int)EdmGetMsgFlag.EdmGetMsg_UserMessages);

                //If no text messages in Admin's inbox, exit application
                if (pos.IsNull)
                {
                    MessageBox.Show("No messages in Admin's inbox.");
                    return;
                }

                //Otherwise, iterate through Admin's inbox and
                //display a message box with each encapsulated text message
                while (!pos.IsNull)
                {
                    message = inbox.GetNextMessage(pos);
                    bool readStatus = false;
                    readStatus = message.IsRead;
                    System.DateTime messageDate;
                    messageDate = message.Date;

                    MessageBox.Show("Sender name = " + message.SenderName + "\n" +
                        "Send ID = " + message.SenderID.ToString() + "\n" +
                        "Is read = " + readStatus + "\n" +
                        "Type = " + message.MessageType.ToString() + "\n" +
                        "Date = " + messageDate.ToString() + "\n" +
                        "Subject = " + message.Subject + "\n" +
                        "Body = " + message.Body + "\n");

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
namespace MessageCSharp
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
            this.GetMessagesButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            //
            // VaultsLabel
            //
            this.VaultsLabel.AutoSize = true;
            this.VaultsLabel.Location = new System.Drawing.Point(13, 26);
            this.VaultsLabel.Name = "VaultsLabel";
            this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
            this.VaultsLabel.TabIndex = 0;
            this.VaultsLabel.Text = "Select vault view:";
            //
            // VaultsComboBox
            //
            this.VaultsComboBox.FormattingEnabled = true;
            this.VaultsComboBox.Location = new System.Drawing.Point(16, 54);
            this.VaultsComboBox.Name = "VaultsComboBox";
            this.VaultsComboBox.Size = new System.Drawing.Size(189, 21);
            this.VaultsComboBox.TabIndex = 1;
            //
            // GetMessagesButton
            //
            this.GetMessagesButton.Location = new System.Drawing.Point(16, 93);
            this.GetMessagesButton.Name = "GetMessagesButton";
            this.GetMessagesButton.Size = new System.Drawing.Size(130, 23);
            this.GetMessagesButton.TabIndex = 2;
            this.GetMessagesButton.Text = "Get messages";
            this.GetMessagesButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.GetMessagesButton.UseVisualStyleBackColor = true;
            this.GetMessagesButton.Click += new System.EventHandler(this.GetMessagesButton_Click);
            //
            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(241, 142);
            this.Controls.Add(this.GetMessagesButton);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.VaultsLabel);
            this.Name = "Form1";
            this.Text = "Get Messages";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label VaultsLabel;
        private System.Windows.Forms.ComboBox VaultsComboBox;
        private System.Windows.Forms.Button GetMessagesButton;
    }
}
```

```
Back to top
```
