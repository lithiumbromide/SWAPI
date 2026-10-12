---
title: "Get a File's Thumbnail Handle by File Version (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_File_Thumbnail_Handle_by_File_Version_Example_CSharp.htm"
---

# Get a File's Thumbnail Handle by File Version (C#)

This example shows how to get a file's thumbnail by version.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 // 2. Click File > New > Project > C#, Windows, Desktop > Windows Forms App.
 // 3. Type CallingCSharp in Project name.
 // 4. For Location, click ... and navigate to the folder where to create the project.
 // 5. Click Next.
 // 6. Select Framework.
 // 7. Click Create.
 // 8. Click Show All Files in the Solution Explorer toolbar and expand
 //    Form1.cs in the Solution Explorer.
 // 9. Replace the code in Form1.cs with this code.
 //10. To create the form, replace the code in Form1.Designer.cs with
 //    this code.
 //11.     Add dependencies and safely pass arrays of structures.
//12. Modify the vault admin password in the code: (vault5.Login("admin", "", vaultName)).
 //13. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. In the Get Thumbnail dialog, click Browse.
 // 2. Navigate to a vault that contains a model with a thumbnail. Click Open.
 // 3. In the Get Thumbnail dialog, click Get thumbnail.
 // 4. c:\temp\123456.bmp is the thumbnail of the model.
 //----------------------------------------------------------------------------
  //Form1.cs
using System;
 using System.Collections.Generic;
 using System.Windows.Forms;
 using EPDM.Interop.epdm;

 namespace CallingCSharp
 {
     public partial class Form1 : Form
     {
         //Create form
         public Form1()
         {
             InitializeComponent();
         }

         //Load form
         private void Form1_Load(System.Object sender, System.EventArgs e)
         {
             textBox1.Text = "Image will be saved as 123456.bmp in C:\\Temp. \nChange code to update the location and name if needed.";
             textBox1.Enabled = false;
         }

         //Event handler: browse button click
         private void btnBrowse_Click(object sender, EventArgs e)
         {
             var openDlg = new OpenFileDialog();
             openDlg.Multiselect = false;
             var result = openDlg.ShowDialog();
             if(result == DialogResult.OK)
             {
                 var path = openDlg.FileName;
                 filePath.Text = path;
             }
         }

         //Event handler: get button click
         private void btnGet_Click(object sender, EventArgs e)
         {
             if (string.IsNullOrEmpty(filePath.Text))
             {
                 MessageBox.Show("Invalid file path");
                 return;
             }

             if(!System.IO.File.Exists(filePath.Text))
             {
                 MessageBox.Show("Invalid file path");
                 return;
             }

             IEdmVault5 vault5 = new EdmVault5();
             var vaultName = vault5.GetVaultNameFromPath(filePath.Text);
             vault5.Login("admin", "", vaultName);
             IEdmVault20 vault20 = (IEdmVault20)vault5;
             IEdmFolder5 folder5 = null;
             IEdmFile5 file5 = null;
             file5 = vault20.GetFileFromPath(filePath.Text, out folder5);
             if (file5 == null || folder5 == null)
             {
                 MessageBox.Show("Invalid vault file or folder");
             }
             var fileId = file5.ID;
             var version = file5.CurrentVersion;
             IEdmFile18 file18 = file5 as IEdmFile18;
            var obj = (IntPtr)file18.GetThumbnail3(version);
            var imgPreview = System.Drawing.Image.FromHbitmap(obj);
            imgPreview.Save(@"C:\temp\123456.bmp", System.Drawing.Imaging.ImageFormat.Png);
             imgPreview.Dispose();
         }
     }

 Back to top

  //Form1.Designer
 namespace CallingCSharp
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
             this.btnBrowse = new System.Windows.Forms.Button();
             this.filePath = new System.Windows.Forms.TextBox();
             this.btnTest = new System.Windows.Forms.Button();
             this.textBox1 = new System.Windows.Forms.TextBox();
             this.SuspendLayout();
             //
             // btnBrowse
             //
             this.btnBrowse.Location = new System.Drawing.Point(352, 12);
             this.btnBrowse.Name = "btnBrowse";
             this.btnBrowse.Size = new System.Drawing.Size(75, 23);
             this.btnBrowse.TabIndex = 0;
             this.btnBrowse.Text = "Browse";
             this.btnBrowse.UseVisualStyleBackColor = true;
             this.btnBrowse.Click += new System.EventHandler(this.btnBrowse_Click);
             //
             // filePath
             //
             this.filePath.Enabled = false;
             this.filePath.Location = new System.Drawing.Point(12, 14);
             this.filePath.Name = "filePath";
             this.filePath.Size = new System.Drawing.Size(334, 20);
             this.filePath.TabIndex = 1;
             //
             // btnTest
             //
             this.btnTest.Location = new System.Drawing.Point(352, 59);
             this.btnTest.Name = "btnTest";
             this.btnTest.Size = new System.Drawing.Size(73, 22);
             this.btnTest.TabIndex = 2;
             this.btnTest.Text = "Get thumbnail";
             this.btnTest.UseVisualStyleBackColor = true;
             this.btnTest.Click += new System.EventHandler(this.btnGet_Click);
             //
             // textBox1
             //
             this.textBox1.Enabled = false;
             this.textBox1.Location = new System.Drawing.Point(12, 49);
             this.textBox1.Multiline = true;
             this.textBox1.Name = "textBox1";
             this.textBox1.Size = new System.Drawing.Size(334, 42);
             this.textBox1.TabIndex = 3;
             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(439, 103);
             this.Controls.Add(this.textBox1);
             this.Controls.Add(this.btnTest);
             this.Controls.Add(this.filePath);
             this.Controls.Add(this.btnBrowse);
             this.Name = "Form1";
             this.Text = "Get Thumbnail";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         private System.Windows.Forms.Label label1;
         private System.Windows.Forms.Button btnBrowse;
         private System.Windows.Forms.TextBox filePath;
         private System.Windows.Forms.Button btnTest;
         private System.Windows.Forms.TextBox textBox1;
     }
 }

 Back to top
```
