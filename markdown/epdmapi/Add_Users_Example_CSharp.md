---
title: "Add Users Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Add_Users_Example_CSharp.htm"
---

# Add Users Example (C#)

This example shows how to add users to a vault by deserializing an XML file containing user data.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//---------------------------------------------------------------------------
// Preconditions:
//  1. Create an XML file for this example.
//     a. Open a text editor like Notepad and copy and paste this code
//        into the editor.
//     b. Save the file as User.xml and remember where you save the file.
//  2. Start Microsoft Visual Studio.
//     a. Click File > New > Project > C#, Windows, Desktop > Windows Forms Application.
//     b. Type AddUsersCSharp in Project name.
//     c. For Location, click ... and navigate to the folder where to
create the project.
//     d. Click Next.
//     e. Select Framework.
//     f. Click Create.

//     g. Click Show All Files in the Solution Explorer
toolbar and expand

//       Form1.cs in the Solution Explorer.
//     h. Replace the code in Form1.cs with this code.
//     i. Replace the code in Form1.Designer.cs with this code.
//     j. Right-click the AddUsersCSharp project name in the Solution Explorer.
//        1. Click Add > Class > Class.
//        2. Type EdmVaultSingleton.cs in Name.
//        3. Click Add.
//        4. Replace the code in EdmVaultSingleton.cs with this code.
//     k. Right-click the AddUsersCSharp project name in the Solution Explorer.
//        1. Click Add > Class > Class.
//        2. Type User.cs in Name.
//        3. Click Add.
//        4. Replace the code in User.cs with this code.
//  3. Add dependencies and safely pass arrays of structures.
//  4. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays a dialog.
//  2. Select a vault.
//  3. Click Browse, locate and select User.xml, and click Open.
//  4. Click Add users.
//     A message box is displayed showing the names of the new users added
//     to the vault.
//  5. Click OK to close the message box.
//  6. Close the dialog.
//  7. Start and log into the SOLIDWORKS PDM Professional Administration
//     tool as Admin.
//  8. Expand the vault where the new users were added.
//  9. Expand Users to see the names of the new users.
// 10. Double-click jdoe.
//     a. Examine the properties.
//     b. Click Administrative Permissions and examine the permissions.
//     c. Click OK.
// 11. Double-click jsmith and repeat steps 10a - 10c.
//----------------------------------------------------------------------------
```

```
<?xml version="1.0" encoding="utf-8"?>
<ArrayOfAnyType xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <anyType xsi:type="User">
      <sn>Doe</sn>
      <givenName>John</givenName>
      <title>Designer</title>
      <cn>John Doe</cn>
      <username>jdoe@yourcompany.com</username>
  </anyType>
  <anyType xsi:type="User">
      <sn>Smith</sn>
      <givenName>Jane</givenName>
      <title>Manager</title>
      <cn>Jane Smith</cn>
      <username>jsmith@yourcompany.com</username>
  </anyType>
</ArrayOfAnyType>
```

```
Back to top
```

```
//Form1.cs
using System;
using System.Collections;
using System.Data;
using System.Diagnostics;
using System.IO;
using System.Xml.Serialization;
using System.Windows.Forms;
using EPDM.Interop.epdm;
using System.Xml;
using System.Runtime.InteropServices;

namespace AddUsersCSharp
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		public void BrowseButton_Click(System.Object sender, System.EventArgs e)
		{
			try
			{
				DialogResult dlgResult = XmlOpenFileDialog.ShowDialog();
				if (dlgResult == DialogResult.Cancel)
				{
					return;
				}
				XmlTextBox.Text = XmlOpenFileDialog.FileName;
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

		public void AddUsersButton_Click(System.Object sender, System.EventArgs e)
		{
			StreamReader StrReader = null;

			try
			{
				//Deserialize users from an XML file
				Type[] ExtraTypes = { Type.GetType("AddUsersCSharp.User") };
				XmlSerializer XmlSer = new XmlSerializer(Type.GetType("System.Collections.ArrayList"), ExtraTypes);
				StrReader = new StreamReader(XmlTextBox.Text);
				ArrayList NewUsers = (ArrayList)XmlSer.Deserialize(StrReader);

				//Obtain the only instance of the IEdmVaultObject
				IEdmVault5 vault = EdmVaultSingleton.Instance;

				if (!vault.IsLoggedIn)
				{
					//Log into selected vault as the current user
					vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
				}

				//Assign IEdmVault object to the IEdmUserMgr7 object
				IEdmUserMgr7 UsrMgr = (IEdmUserMgr7)vault;

				//Declare EdmUserData array to hold new user data
				EdmUserData2[] UserData = new EdmUserData2[NewUsers.Count];

				//Set the EdmUserData members for each new user
				for (int i = 0; i <= NewUsers.Count - 1; i++)
				{
					if (NewUsers[i] != null)
					{
						UserData[i].mbsCompleteName = (NewUsers[i] as User).cn;
						UserData[i].mbsEmail = (NewUsers[i] as User).username;
						UserData[i].mbsInitials = (NewUsers[i] as User).givenName.Substring(0, 1) + (NewUsers[i] as User).sn.Substring(0, 1);
						UserData[i].mbsUserName = (NewUsers[i] as User).username.Split('@')[0];
						//Return user's IEdmUser6 interface in mpoUser
						UserData[i].mlFlags = (int)EdmUserDataFlags.Edmudf_GetInterface;
						//Add this user even if others cannot be added
						UserData[i].mlFlags += (int)EdmUserDataFlags.Edmudf_ForceAdd;

						//Set permissions
						EdmSysPerm[] perms = new EdmSysPerm[3];
						perms[0] = EdmSysPerm.EdmSysPerm_EditUserMgr;
						perms[1] = EdmSysPerm.EdmSysPerm_EditReportQuery;
						perms[2] = EdmSysPerm.EdmSysPerm_MandatoryVersionComments;
						UserData[i].moSysPerms = perms;
					}
				}

				//Add the users to the vault
				UsrMgr.AddUsers2(ref UserData);

				string msg = "";
				foreach (EdmUserData2 usr in UserData)
				{
					if (usr.mhStatus == 0)

					{
						msg += "Created user \"" + usr.mpoUser.Name + "\" successfully. ID = " + usr.mpoUser.ID.ToString() + "\n";

					}
					else
					{
						IEdmVault11 vault2 = (IEdmVault11)vault;
						msg += "Error creating user \"" + usr.mbsUserName + "\" - " + vault2.GetErrorMessage(usr.mhStatus) + "\n";
					}
				}
				MessageBox.Show(msg);

			}
			catch (System.Runtime.InteropServices.COMException ex)
			{
				MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
			}
			catch (Exception ex)
			{
				MessageBox.Show(ex.Message);
			}
			finally
			{
				if ((StrReader != null))
				{
					StrReader.Close();
				}
			}
		}

		public void AddUsers_Load(System.Object sender, System.EventArgs e)
		{

			try
			{
			  //Obtain the only instance of the IEdmVault object
			  IEdmVault8 vault = (IEdmVault8)EdmVaultSingleton.Instance;

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
namespace AddUsersCSharp
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
            this.XmlLabel = new System.Windows.Forms.Label();
            this.XmlTextBox = new System.Windows.Forms.TextBox();
            this.BrowseButton = new System.Windows.Forms.Button();
            this.AddUsersButton = new System.Windows.Forms.Button();
            this.XmlOpenFileDialog = new System.Windows.Forms.OpenFileDialog();
            this.SuspendLayout();

            //
            //XmlOpenFileDialog
            //
            this.XmlOpenFileDialog.Filter = "XML files|*.XML";
            //

            //
            // VaultsLabel
            //
            this.VaultsLabel.AutoSize = true;
            this.VaultsLabel.Location = new System.Drawing.Point(23, 34);
            this.VaultsLabel.Name = "VaultsLabel";
            this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
            this.VaultsLabel.TabIndex = 0;
            this.VaultsLabel.Text = "Select vault view:";
            //
            // VaultsComboBox
            //
            this.VaultsComboBox.FormattingEnabled = true;
            this.VaultsComboBox.Location = new System.Drawing.Point(26, 62);
            this.VaultsComboBox.Name = "VaultsComboBox";
            this.VaultsComboBox.Size = new System.Drawing.Size(171, 21);
            this.VaultsComboBox.TabIndex = 1;
            //
            // XmlLabel
            //
            this.XmlLabel.AutoSize = true;
            this.XmlLabel.Location = new System.Drawing.Point(26, 111);
            this.XmlLabel.Name = "XmlLabel";
            this.XmlLabel.Size = new System.Drawing.Size(173, 13);
            this.XmlLabel.TabIndex = 2;
            this.XmlLabel.Text = "XML file from which to import users:";
            //
            // XmlTextBox
            //
            this.XmlTextBox.Location = new System.Drawing.Point(26, 139);
            this.XmlTextBox.Name = "XmlTextBox";
            this.XmlTextBox.Size = new System.Drawing.Size(171, 20);
            this.XmlTextBox.TabIndex = 3;
            //
            // BrowseButton
            //
            this.BrowseButton.Location = new System.Drawing.Point(203, 135);
            this.BrowseButton.Name = "BrowseButton";
            this.BrowseButton.Size = new System.Drawing.Size(75, 23);
            this.BrowseButton.TabIndex = 4;
            this.BrowseButton.Text = "Browse...";
            this.BrowseButton.UseVisualStyleBackColor = true;
            this.BrowseButton.Click += new System.EventHandler(BrowseButton_Click);
            //
            // AddUsersButton
            //
            this.AddUsersButton.Location = new System.Drawing.Point(29, 189);
            this.AddUsersButton.Name = "AddUsersButton";
            this.AddUsersButton.Size = new System.Drawing.Size(75, 23);
            this.AddUsersButton.TabIndex = 5;
            this.AddUsersButton.Text = "Add users";
            this.AddUsersButton.UseVisualStyleBackColor = true;
            this.AddUsersButton.Click += new System.EventHandler(this.AddUsersButton_Click);
            //
            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 262);
            this.Controls.Add(this.AddUsersButton);
            this.Controls.Add(this.BrowseButton);
            this.Controls.Add(this.XmlTextBox);
            this.Controls.Add(this.XmlLabel);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.VaultsLabel);
            this.Name = "Form1";
            this.Text = "Add new users";
            this.Load += new System.EventHandler(this.AddUsers_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label VaultsLabel;
        private System.Windows.Forms.ComboBox VaultsComboBox;
        private System.Windows.Forms.Label XmlLabel;
        private System.Windows.Forms.TextBox XmlTextBox;
        private System.Windows.Forms.Button BrowseButton;
        private System.Windows.Forms.Button AddUsersButton;
        private System.Windows.Forms.OpenFileDialog XmlOpenFileDialog;
    }
}
```

```
Back to top
```

```
//EdmVaultSingleton.cs
using System;
using System.Collections;
using System.Diagnostics;
using System.Threading;
using EPDM.Interop.epdm;

namespace AddUsersCSharp
{
    public class EdmVaultSingleton
    {
        private static EdmVault5 mInstance = null;
        private static object mLockObj = new object();

        private EdmVaultSingleton()
        {

        }

        public static EdmVault5 Instance
        {
            get
            {
                try
                {
                    if (mInstance == null)
                    {
                        Monitor.Enter(mLockObj);
                        if (mInstance == null)
                        {
                            mInstance = new EdmVault5();
                        }
                        Monitor.Exit(mLockObj);
                    }
                }
                catch (Exception ex)
                {
                    Monitor.Exit(mLockObj);
                }

                return mInstance;

            }
        }

    }
}
```

```
Back to top
```

```
//User.cs
using System;
using System.Collections;
using System.Diagnostics;

namespace AddUsersCSharp
{
    public class User
    {
        //First name
        private string mSn;
        //Last name
        private string mGivenName;
        //Title
        private string mTitle;
        //Complete name
        private string mCn;
        //Email address
        private string mUsername;

        public User()
        {

        }

        public string sn
        {
            get { return mSn; }
            set { mSn = value; }
        }

        public string givenName
        {
            get { return mGivenName; }
            set { mGivenName = value; }
        }

        public string title
        {
            get { return mTitle; }
            set { mTitle = value; }
        }

        public string cn
        {
            get { return mCn; }
            set { mCn = value; }
        }

        public string username
        {
            get { return mUsername; }
            set { mUsername = value; }
        }
    }
}
```

```
Back to top
```
