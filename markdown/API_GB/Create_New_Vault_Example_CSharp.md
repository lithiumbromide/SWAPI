---
title: "Create New Vault Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Create_New_Vault_Example_CSharp.htm"
---

# Create New Vault Example (C#)

This example shows how to:

- Create a new vault.
- Create a new vault view.
- Log into the new vault.
- Get all of the users currently logged into vault views on this machine.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio 2010.
 //    a. Click File > New > Project > Visual C# > Windows Forms Application.
 //    b. Type CreateNewVault_CSharp in Name.
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
  // 3. Add Microsoft.VisualBasic as a reference (click COM in the left-side panel,
 //    click Microsoft.VisualBasic, click Add, and click Close).
 // 4. Right-click EPDM.Interop.epdm in References, click Properties, and set
 //    Embed Interop Types to False to handle methods that pass arrays of
 //    structures.
 // 5. In the code, substitute the following parameters in IEdmVault11::CreateNewVault
 //    to create MyNewVault on your machine:
 //    * database_server
 //    * sql_sa_password
 // 6. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Create new vault dialog box.
 //    a. Click Create and log in to MyNewVault.
 //    b. After a few seconds, displays a login dialog.
 //    c. Type Admin's password in Password.
 //    d. Click Log in.
 //       1. MyNewVault is created using the Default configuration in the root
 //          folder of the archive server.
 //       2. A view of MyNewVault, accessible to all users, is created in c:\temp.
 //       3. Admin is logged into MyNewVault.
 //    e. Click Get users logged into all vaults.
 //    f. Displays a dialog with all of the users currently logged into
 //       vault views on this machine.
 //    g. Click OK.
 // 2. Close the Create new vault dialog box.
  //----------------------------------------------------------------------------

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
 using Microsoft.VisualBasic;

 namespace CreateNewVault_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }

         IEdmVault5 vault1;
         IEdmVault13 vault2;
         string vaults = "";
         public void Form1_Load(System.Object sender, System.EventArgs e)
         {
             vault1 = new EdmVault5();
             vault2 = (IEdmVault13)vault1;
         }

         public void GetLoggedIn_Click(System.Object sender, System.EventArgs e)
         {
             //Get all of the users currently logged into vault views on this machine
             try
             {
                 if (vault1 == null)
                 {
                     MessageBox.Show("Click Log in");
                     return;
                 }

                 IEdmUserMgr5 userMgr = default(IEdmUserMgr5);
                 userMgr = (IEdmUserMgr5)vault2.CreateUtility(EdmUtility.EdmUtil_UserMgr);
                 IEdmPos5 pos = default(IEdmPos5);
                 pos = userMgr.GetFirstLoggedInUserPosition(vaults);

                 string userName = "";
                 string computerName = "";
                 string vaultName = "";
                 object loginTime = null;

                 string message = null;
                 message = "The following users are logged into vault views:" + Constants.vbLf + Constants.vbLf;

                 while (!pos.IsNull)
                 {
                     userMgr.GetNextLoggedInUser(pos, out userName, out computerName, out vaultName, ref loginTime);
                     message = message + userName + " (" + computerName + ")" + " logged in to " + vaultName + " at " + loginTime + Constants.vbLf;
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

         private void Button1_Click(System.Object sender, System.EventArgs e)
         {
             // Create a new vault and vault view
             try
             {
                 vault1 = new EdmVault5();
                 vault2 = (IEdmVault13)vault1;

                 vault2.CreateNewVault("", "", "", "MyNewVault", "This is my new vault", "", "database_server", "sa", "sql_sa_password", "MyNewVault", 110, "", (int)EdmCreateVaultFlag.EdmCreateVault_UseDefaultAdminPassword, null, "Default");
                 vault2.CreateNewVaultView("", "", "", "MyNewVault", "c:\\temp", (int)EdmCreateVaultViewFlag.EdmCreateVaultView_SharedView);

                 EdmViewInfo[] Views = null;
                 vault2.GetVaultViews(out Views, false);
                 vaults = "";

                 foreach (EdmViewInfo View in Views)
                 {
                     vaults = vaults + View.mbsVaultName + Constants.vbLf;
                 }

                 //Log into the new vault view
                 vault2.LoginAuto("MyNewVault", this.Handle.ToInt32());
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

[Back to top](#top)

```vb
 //Form1.Designer.cs
 namespace CreateNewVault_CSharp
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
             this.GetLoggedIn = new System.Windows.Forms.Button();
             this.Button1 = new System.Windows.Forms.Button();
             this.SuspendLayout();
             //
             //GetLoggedIn
             //
             this.GetLoggedIn.Location = new System.Drawing.Point(31, 71);
             this.GetLoggedIn.Name = "GetLoggedIn";
             this.GetLoggedIn.Size = new System.Drawing.Size(167, 23);
             this.GetLoggedIn.TabIndex = 5;
             this.GetLoggedIn.Text = "Get users logged into all vaults";
             this.GetLoggedIn.UseVisualStyleBackColor = true;
             this.GetLoggedIn.Click +=new System.EventHandler(GetLoggedIn_Click);
             //
             //Button1
             //
             this.Button1.Location = new System.Drawing.Point(31, 26);
             this.Button1.Name = "Button1";
             this.Button1.Size = new System.Drawing.Size(178, 23);
             this.Button1.TabIndex = 6;
             this.Button1.Text = "Create and log in to MyNewVault";
             this.Button1.UseVisualStyleBackColor = true;
             this.Button1.Click +=new System.EventHandler(Button1_Click);
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(287, 136);
             this.Controls.Add(this.Button1);
             this.Controls.Add(this.GetLoggedIn);
             this.Name = "Form1";
             this.Text = "Create new vault";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Button GetLoggedIn;
         internal System.Windows.Forms.Button Button1;
     }
 }
```

[Back to top](#top)
