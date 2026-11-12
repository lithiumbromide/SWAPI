---
title: "Check Out and Copy File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Check_Out_and_Copy_File_Example_CSharp.htm"
---

# Check Out and Copy File Example (C#)

This example shows how to find a vault from a file path, check out the file from the vault, and copy the file to another location.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio 2010.
 //    a. Click File > New > Project > Visual C# > Windows Forms Application.
 //    b. Type GetVaultFromFilePath_CSharp in Name.
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
 //    EPDM.Interop.epdm.dll, click Open, click Add,  and click Close).
 // 3. Right-click EPDM.Interop.epdm in References, click Properties, and set
 //    Embed Interop Types to False to handle methods that pass arrays of
 //    structures.
 // 4. Ensure that c:\temp exists.
 // 5. Ensure that at least one file is checked into a vault.
 // 6. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Check out and copy a file dialog box.
 // 2. Click Check out and copy a file.
 // 3. In the Open dialog, navigate to and click a file checked into a vault.
 // 4. Click Open.
 //    a. Gets the vault from the selected file's path.
 //    b. Logs into the vault.
 //    c. Checks out the file.
 //    d. Displays a message box confirming the check-out.
 //    e. Click OK.
 //    f. Copies the selected file to c:\temp.
 //    g. Displays a message box confirming the copy.
 //    h. Click OK.
 // 5. Close the Check out and copy a file dialog box.
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

 namespace GetVaultFromPath_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         public void Form1_Load(System.Object sender, System.EventArgs e)
         {
         }

         private void Button1_Click(System.Object sender, System.EventArgs e)
         {
             try
             {
                 EdmVault5 vault = default(EdmVault5);
                 vault = new EdmVault5();

                 IEdmStrLst5 strList = default(IEdmStrLst5);
                 strList = vault.BrowseForFile(this.Handle.ToInt32());

                 IEdmPos5 pos = default(IEdmPos5);
                 pos = strList.GetHeadPosition();
                 string filePath = strList.GetNext(pos);

                 //Get name of the vault in which the file is located
                 string VaultName = null;
                 VaultName = vault.GetVaultNameFromPath(filePath);

                 //Log into the vault
                 vault.LoginAuto(VaultName, this.Handle.ToInt32());

                 //Get the interface to the file and its parent folder
                 IEdmFile5 file = default(IEdmFile5);
                 IEdmFolder5 folder = null;
                 file = vault.GetFileFromPath(filePath, out folder);

                 if (file == null)
                 {
                     MessageBox.Show("The file is not in the vault " + VaultName + ".");
                 }
                 else
                 {
                     //Check out the file
                     file.LockFile(folder.ID, this.Handle.ToInt32());
                     MessageBox.Show("Checked out " + file.Name + " in vault " + VaultName + ".");

                     //Copy the file
                     IEdmEnumeratorVersion5 verEnum = default(IEdmEnumeratorVersion5);
                     verEnum = (IEdmEnumeratorVersion5)file;
                     int Version = 0;
                     Version = file.GetLocalVersionNo(folder.ID);
                     IEdmVersion5 ver = default(IEdmVersion5);
                     ver = verEnum.GetVersion(Version);
                     ver.GetFileCopy(this.Handle.ToInt32(), "c:\\temp\\");
                     MessageBox.Show("Copied " + file.Name + " to c:\\temp.");
                 }

             }
             catch (System.Runtime.InteropServices.COMException ex)
             {
                 if (ex.ErrorCode.ToString() == "-2147220949")
                 {
                     MessageBox.Show("The selected file is not located in a file vault.");
                 }
                 else
                 {
                     MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
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

[Back to top](#top)

```vb
 //Form1.Designer.cs
 namespace GetVaultFromPath_CSharp
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
             this.Button1 = new System.Windows.Forms.Button();
             this.SuspendLayout();
             //
             //Button1
             //
             this.Button1.Location = new System.Drawing.Point(31, 26);
             this.Button1.Name = "Button1";
             this.Button1.Size = new System.Drawing.Size(150, 23);
             this.Button1.TabIndex = 6;
             this.Button1.Text = "Check out and copy a file";
             this.Button1.UseVisualStyleBackColor = true;
             this.Button1.Click +=new System.EventHandler(Button1_Click);
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(263, 87);
             this.Controls.Add(this.Button1);
             this.Name = "Form1";
             this.Text = "Check out and copy a file";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);

         }

         #endregion

         internal System.Windows.Forms.Button Button1;
     }
 }
```

[Back to top](#top)
