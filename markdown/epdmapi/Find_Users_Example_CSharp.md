---
title: "Find Users Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Find_Users_Example_CSharp.htm"
---

# Find Users Example (C#)

This example shows how to find users in the vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 //  1. Start Microsoft Visual Studio.
 //  2. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
 //  3. Type FindUser_CSharp in Project name.
 //  4. For Location, click ... and navigate to the folder where to create the project.
 //  5. Click Next.
 //  6. Select Framework.
 //  7. Click Create.
 //  8. Click Show All Files in the Solution Explorer toolbar and expand
 //     Form1.cs in the Solution Explorer.
 //  9. Replace the code in Form1.cs with this code.
 // 10. To create the form, replace the code in Form1.Designer.cs with
 //     this code.
 // 11. Add dependencies and safely pass arrays of structures.
 // 12 Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 //  1. Displays the Find Users dialog box.
  //     a. Select a vault view.
  //     b. In Full name contains, type a substring of the full name of a
  //        user that exists in the vault.
  //     c. Click Find Users.
  //        A message box confirms the substring typed in Postconditions
  //        step 1b.
  //     d. Click OK.
  //        Displays a Search for users dialog.
  //     e. Click Find.
  //        Displays a Search for users dialog with results.
  //     f. Click the first row.
  //     g. Click Select.
  //        * Displays a message box with the updated user information.
  //        * The selected user's phone and website information are updated.
  //     h. Click OK.
  //  2. Updates the Find Users dialog box with the full name and picture,
 //     if it exists, of the last user found whose full name contains the substring
  //     typed in Postconditions step 1b.
  //  3. Close the Find Users dialog box.
 //----------------------------------------------------------------------------
```

```
//Form1.cs
```

```vb
 using System;
 using System.Collections.Generic;
 using System.ComponentModel;
 using System.Data;
 using System.Drawing;
 using System.Linq;
 using System.Text;
 using System.Windows.Forms;
 using EPDM.Interop.epdm;

 namespace FindUser_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         IEdmVault5 vault1;
         IEdmVault8 vault;
         EdmViewInfo[] Views = null;

         public void Form1_Load(System.Object sender, System.EventArgs e)
         {
             try
             {
                 vault1 = new EdmVault5();
                 vault = (IEdmVault8)vault1;
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

         private void FindUsers_Click(System.Object sender, System.EventArgs e)
         {
           try {
                IEdmVault7 vault2 = null;
                if (vault1 == null) {
                   vault1 = new EdmVault5();
                }
                vault2 = (IEdmVault7)vault1;

                if (!vault1.IsLoggedIn) {
                   vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                }

                //Get the user search interface
                IEdmFindUser poFind = default(IEdmFindUser);
                poFind = (IEdmFindUser)vault2.CreateUtility(EdmUtility.EdmUtil_FindUser);

                 //Search for a user with specified text in the full user name
                poFind.SetPropt(EdmFindUserProp.Edmfup_FullName, this.TextBox1.Text);
                string val = null;
                val = (string)poFind.GetPropt(EdmFindUserProp.Edmfup_FullName);
                MessageBox.Show("Find users whose full names contain " + "\"" + val + "\"");

                poFind.ShowFindUI(this.Handle.ToInt32(), true, "Search for users");

                IEdmEnum poResult = default(IEdmEnum);
                poResult = poFind.Result;
                string str = "Found " + poResult.Count.ToString() + " users with full names containing, " +
                                          "\"" + this.TextBox1.Text + "\"" + ":";

                System.Drawing.Image oImg = default(System.Drawing.Image);
                IEdmUser10 poUser = default(IEdmUser10);
                EdmUserDataEx UserInfo = new EdmUserDataEx();

                //Specify which user data fields are valid
                UserInfo.mlEdmUserDataExFlags = (int)EdmUserDataExFlag.Edmudex_All;

                foreach ( object foundUser in poResult) {
                        poUser = (IEdmUser10)foundUser;

                        //Get user's information
                        poUser.GetUserDataEx(ref UserInfo);

                        //Update user's information
                        UserInfo.mbsPhone = "123456789";
                        UserInfo.mbsWebSite1 = "http://www.solidworks.com";
                        UserInfo.mbsWebSite2 = "https://www.facebook.com/solidworks";
                        poUser.SetUserDataEx(ref UserInfo);
                        str = str + "\n" + "Full name: " + UserInfo.mbsCompleteName + ", Phone: " + UserInfo.mbsPhone +
                                            ", WebSite1: " + UserInfo.mbsWebSite1 + ", Website2: " + UserInfo.mbsWebSite2;
                }

                MessageBox.Show(str);

                //Display the picture, if available, of the last user found
                if ((UserInfo.mbsPicturePath != null)) {
                  this.TextBox2.Text = UserInfo.mbsCompleteName;
                  oImg = System.Drawing.Bitmap.FromFile(UserInfo.mbsPicturePath);
                  this.CreateGraphics().DrawImage(oImg, 40, 220);
                 }

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

```vb
 namespace FindUser_CSharp
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
             this.FindUsers = new System.Windows.Forms.Button();
             this.VaultsComboBox = new System.Windows.Forms.ComboBox();
             this.Label1 = new System.Windows.Forms.Label();
             this.Label2 = new System.Windows.Forms.Label();
             this.TextBox1 = new System.Windows.Forms.TextBox();
             this.Label3 = new System.Windows.Forms.Label();
             this.TextBox2 = new System.Windows.Forms.TextBox();
             this.SuspendLayout();
             //
             // FindUsers
             //
             this.FindUsers.Location = new System.Drawing.Point(72, 136);
             this.FindUsers.Name = "FindUsers";
             this.FindUsers.Size = new System.Drawing.Size(66, 23);
             this.FindUsers.TabIndex = 0;
             this.FindUsers.Text = "Find Users";
             this.FindUsers.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
             this.FindUsers.UseVisualStyleBackColor = true;
             this.FindUsers.Click += new System.EventHandler(this.FindUsers_Click);
             //
             // VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(30, 39);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(169, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             // Label1
             //
             this.Label1.AutoSize = true;
             this.Label1.Location = new System.Drawing.Point(27, 23);
             this.Label1.Name = "Label1";
             this.Label1.Size = new System.Drawing.Size(91, 13);
             this.Label1.TabIndex = 2;
             this.Label1.Text = "Select vault view:";
             //
             // Label2
             //
             this.Label2.AutoSize = true;
             this.Label2.Location = new System.Drawing.Point(27, 77);
             this.Label2.Name = "Label2";
             this.Label2.Size = new System.Drawing.Size(98, 13);
             this.Label2.TabIndex = 3;
             this.Label2.Text = "Full name contains:";
             //
             // TextBox1
             //
             this.TextBox1.Location = new System.Drawing.Point(32, 93);
             this.TextBox1.Name = "TextBox1";
             this.TextBox1.Size = new System.Drawing.Size(167, 20);
             this.TextBox1.TabIndex = 4;
             //
             // Label3
             //
             this.Label3.AutoSize = true;
             this.Label3.Location = new System.Drawing.Point(29, 172);
             this.Label3.Name = "Label3";
             this.Label3.Size = new System.Drawing.Size(83, 13);
             this.Label3.TabIndex = 6;
             this.Label3.Text = "Last user found:";
             //
             // TextBox2
             //
             this.TextBox2.Location = new System.Drawing.Point(30, 188);
             this.TextBox2.Name = "TextBox2";
             this.TextBox2.Size = new System.Drawing.Size(169, 20);
             this.TextBox2.TabIndex = 7;
             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(406, 447);
             this.Controls.Add(this.TextBox2);
             this.Controls.Add(this.Label3);
             this.Controls.Add(this.TextBox1);
             this.Controls.Add(this.Label2);
             this.Controls.Add(this.Label1);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.FindUsers);
             this.Name = "Form1";
             this.Text = "Find Users";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }
         internal System.Windows.Forms.Button FindUsers;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Label Label1;
         internal System.Windows.Forms.Label Label2;
         internal System.Windows.Forms.TextBox TextBox1;
         internal System.Windows.Forms.Label Label3;
         internal System.Windows.Forms.TextBox TextBox2;

         #endregion
     }
 }
```

```
Back to top
```
