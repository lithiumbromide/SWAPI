---
title: "Read and Write to Third-party Storage Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_and_Set_3rd_Party_Storage_Example_CSharp.htm"
---

# Read and Write to Third-party Storage Example (C#)

This example shows how to read and write to third-party storage in a document.

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 //  1. Read the SOLIDWORKS Document Manager API Getting Started
 //     topic and ensure that the required DLLs are registered.
 //  2. Start Microsoft Visual Studio 2010.
 //  3. Click File > New > Project > Visual C# > Windows Forms Application.
 //     a. Type  SwDocMgrStorageApp in Name.
 //     b. Click Browse and navigate to the folder where to create
 //        the project.
 //     c. Click OK.
 //  4. Add references to the project:
 //     a. Right-click the solution in Solution Explorer.
 //     b. Click Add Reference.
 //     c. Click Browse.
 //     d. Click:
 //        install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll
 //     e. Click Open.
 //     f. Click Add.
 //     g. Click Browse.
 //     h. Click:
 //        C:\Program Files\Microsoft Visual Studio 11.0\Common7\IDE\Remote Debugger\x64\Microsoft.VisualStudio.OLE.Interop.dll
 //     i. Click Open.
 //     j. Click  Add.
 //     k. Click Close.
 //  5. Click Show All Files in the Solution Explorer toolbar and expand
 //     Form1.cs in the Solution Explorer.
 //  6. Replace the code in Form1.cs with this code.
 //  7. Replace the code in Form1.Designer.cs with this code.
 //  8. Substitute your_license_key with your SOLIDWORKS Document
 //     Manager license key.
 //
 // Postconditions:
 //  1. Displays a dialog.
 //  2. Click Browse.
 //     a. Locate and click a SOLIDWORKS document.
 //     b. Click Open.
 //  3. Type temp in StoreName and in both StorageName fields.
 //  4. Type Some third-party text in both text boxes.
 //  5. Click Write.
 //  6. Click Exit.
 //  7. Press F5.
 //  8. In the dialog, click Browse.
 //     a. Locate and click the document you clicked in step 2a.
 //     b. Click Open.
 //  9. Type temp in StoreName and in both  StorageName fields.
 // 10. Click Read.
 // 11. Displays Some third-party text in both text boxes.
 // 12. Click Exit.
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
 using SwDocumentMgr;
 using Microsoft.VisualStudio.OLE.Interop;
 using System.IO;
 using System.Diagnostics;
 using System.Runtime.InteropServices;

 namespace SwDocMgrStorageApp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        SwDMDocument19 swDoc19;
        SwDMApplication swDocMgr;

        SwDMClassFactory swClassFact;

        string  sLicenseKey = "your_license_key";
        private void btnFile_Click(System.Object sender, System.EventArgs e)
        {
            OpenFileDialog1.Filter = "SOLIDWORKS Files (*.sldprt;*sldasm;*slddrw)|*.sldprt;*sldasm;*slddrw|SOLIDWORKS Part (*.sldprt)|*.sldprt|SOLIDWORKS Assembly (*.sldasm)|*.sldasm|SOLIDWORKS Drawing (*.slddrw)|*.slddrw";
            if (OpenFileDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK) {
            txtFileName.Text = OpenFileDialog1.FileName;
        }
    }

    private void btnOpen_Click(System.Object sender, System.EventArgs e)
    {
        OpenFile();
        if ((swDoc19 != null)) {
                if (txtStorageName.Text != string.Empty)
                    Read3rdPartyStorageData();
                if (txtStoreName.Text != string.Empty && txtStreamName.Text != string.Empty)
                    Read3rdPartyStorageStoreData();
        }
         CloseFile();
        this.Refresh();
    }

    private void btnSave_Click(System.Object sender, System.EventArgs e)
    {
        OpenFile();
        if ((swDoc19 != null)) {
                if (txtStorageName.Text != string.Empty)
                    Write3rdPartyStorageData();
                if (txtStoreName.Text != string.Empty && txtStreamName.Text != string.Empty)
                    Write3rdPartyStorageStoreData();
        }
            rtbStorage.Text = string.Empty;
            rtbStore.Text = string.Empty;
            CloseFile();
            this.Refresh();
    }

    private void btnExit_Click(System.Object sender, System.EventArgs e)
    {
            this.Close();
    }
    private void OpenFile()
    {
        if ((swDoc19 != null)) {
            swDoc19.CloseDoc();
            swDoc19 = null;
        }

            string sDocFileName = null;
            SwDmDocumentType nDocType = 0;
            SwDmDocumentOpenError nRetVal = 0;

            sDocFileName = txtFileName.Text;
            if (sDocFileName.ToLower().EndsWith("sldprt"))
            {
                nDocType = SwDmDocumentType.swDmDocumentPart;
            }
            else if (sDocFileName.ToLower().EndsWith("sldasm"))
            {
                nDocType = SwDmDocumentType.swDmDocumentAssembly;
            }
            else if (sDocFileName.ToLower().EndsWith("slddrw"))
            {
                nDocType = SwDmDocumentType.swDmDocumentDrawing;
            }
            else
            {

                // Not a SOLIDWORKS file
                nDocType = SwDmDocumentType.swDmDocumentUnknown;

                return;
            }

            swClassFact = new SwDMClassFactory();
            swDocMgr = swClassFact.GetApplication(sLicenseKey) as SwDMApplication ;
            swDoc19 = swDocMgr.GetDocument(sDocFileName, nDocType, false, out nRetVal) as SwDMDocument19;
            Debug.Assert(SwDmDocumentOpenError.swDmDocumentOpenErrorNone == nRetVal);
    }
        private void CloseFile()
        {
            if ((swDoc19 != null))
            {
                swDoc19.CloseDoc();
                System.Runtime.InteropServices.Marshal.ReleaseComObject(swDoc19);
                GC.Collect();
                GC.WaitForPendingFinalizers();
                GC.Collect();
                GC.WaitForPendingFinalizers();
                swDoc19 = null;
            }

        }
    private void Read3rdPartyStorageData()
    {
            try
            {
                IStream pIStream = default(IStream);
                pIStream = swDoc19.Get3rdPartyStorage(txtStorageName.Text, false);
                if (pIStream == null)
                {
                    rtbStorage.Text = "Error: " + "Storage " + txtStorageName.Text + " not found";
                    return;
                }
                string strStream = null;
                byte[] byteArray = new byte[1000];
                uint outlength = 0;
                pIStream.Read(byteArray, (uint)byteArray.Length, out outlength);
                strStream = Encoding.UTF8.GetString(byteArray);
                rtbStorage.Text = strStream.Substring(0, (int)outlength);
                swDoc19.Release3rdPartyStorage(txtStorageName.Text);
                System.Runtime.InteropServices.Marshal.ReleaseComObject(pIStream);
                GC.Collect();
                GC.WaitForPendingFinalizers();
                GC.Collect();
                GC.WaitForPendingFinalizers();
            }
            catch (Exception ex)
            {
                rtbStorage.Text = "Error: " + ex.Message;
            }
    }
    private void Read3rdPartyStorageStoreData()
    {
            try
            {
                IStorage storage = default(IStorage);
                storage = swDoc19.Get3rdPartyStorageStore(txtStoreName.Text, false);
                if (storage == null)
                {
                    rtbStore.Text = "Error: " + "Store " + txtStoreName.Text + " not found";
                    return;
                }
                IStream pIStream = default(IStream);
                int grfmode = 0;
                grfmode |= (int)STGM.SHARE_EXCLUSIVE;
                storage.OpenStream(txtStreamName.Text, IntPtr.Zero, (uint)grfmode, 0, out pIStream);
                if (pIStream == null)
                {
                    rtbStore.Text = "Error: " + "Stream " + txtStreamName.Text + " not found";
                    return;
                }
                string strStream = null;
                byte[] byteArray = new byte[1000];
                uint outlength = 0;
                pIStream.Read(byteArray, (uint)byteArray.Length, out outlength);
                strStream = Encoding.UTF8.GetString(byteArray);
                rtbStore.Text = strStream;
                System.Runtime.InteropServices.Marshal.ReleaseComObject(pIStream);
                GC.Collect();
                GC.WaitForPendingFinalizers();
                GC.Collect();
                GC.WaitForPendingFinalizers();
                swDoc19.Release3rdPartyStorageStore(txtStoreName.Text);
            }
            catch (Exception ex)
            {
                rtbStore.Text = "Error: " + ex.Message;
            }
    }
    private void Write3rdPartyStorageData()
    {
            try
            {
                IStream pIStream = default(IStream);
                pIStream = swDoc19.Get3rdPartyStorage(txtStorageName.Text, true);
                if (pIStream == null)
                {
                    rtbStorage.Text = "Error: " + "Storage " + txtStorageName.Text + " not found";
                    return;
                }
                byte[] strStream = null;
                strStream = Encoding.UTF8.GetBytes(rtbStorage.Text);
                uint outlength = 0;
                pIStream.Write(strStream, (uint)strStream.Length, out outlength);
                System.Runtime.InteropServices.Marshal.ReleaseComObject(pIStream);
                GC.Collect();
                GC.WaitForPendingFinalizers();
                GC.Collect();
                GC.WaitForPendingFinalizers();
                swDoc19.Release3rdPartyStorage(txtStorageName.Text);
                swDoc19.Save();
            }
            catch(Exception ex)
            {
                rtbStorage.Text = "Error: " + ex.Message;
            }
    }
    private void Write3rdPartyStorageStoreData()
    {
            try
            {
                IStorage storage = default(IStorage);
                storage = swDoc19.Get3rdPartyStorageStore(txtStoreName.Text, true);
                if (storage == null)
                {
                    rtbStore.Text = "Error: " + "Store " + txtStoreName.Text + " not found";
                    return;
                }
                IStream pIStream = default(IStream);
                int grfmode = 0;
                grfmode |= (int)STGM.SHARE_EXCLUSIVE;
                grfmode |= (int)STGM.READWRITE;
                grfmode |= (int)STGM.CREATE;
                storage.CreateStream(txtStreamName.Text, (uint)grfmode, 0, 0, out pIStream);
                if (pIStream == null)
                {
                    rtbStore.Text = "Error: " + "Stream " + txtStreamName.Text + " not found";
                    return;
                }
                byte[] strStream = null;
                strStream = Encoding.UTF8.GetBytes(rtbStore.Text);
                uint outlength = 0;
                pIStream.Write(strStream, (uint)strStream.Length, out outlength);
                System.Runtime.InteropServices.Marshal.ReleaseComObject(storage);
                System.Runtime.InteropServices.Marshal.ReleaseComObject(pIStream);
                GC.Collect();
                GC.WaitForPendingFinalizers();
                GC.Collect();
                GC.WaitForPendingFinalizers();
                swDoc19.Release3rdPartyStorageStore(txtStoreName.Text);
                swDoc19.Save();
            }
            catch(Exception ex)
            {
                rtbStore.Text = "Error: " + ex.Message;
            }
    }
    [Flags]
    public enum STGM : uint
    {
            DIRECT = 0x00000000,
            TRANSACTED = 0x00010000,
            SIMPLE = 0x08000000,
            READ = 0x00000000,
            WRITE = 0x00000001,
            READWRITE = 0x00000002,
            SHARE_DENY_NONE = 0x00000040,
            SHARE_DENY_READ = 0x00000030,
            SHARE_DENY_WRITE = 0x00000020,
            SHARE_EXCLUSIVE = 0x00000010,
            PRIORITY = 0x00040000,
            DELETEONRELEASE = 0x04000000,
            NOSCRATCH = 0x00100000,
            CREATE = 0x00001000,
            CONVERT = 0x00020000,
            FAILIFTHERE = 0x00000000,
            NOSNAPSHOT = 0x00200000,
            DIRECT_SWMR = 0x00400000,
    }

    }
}

 //Form1.Designer.cs
 namespace SwDocMgrStorageApp
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
             this.rtbStorage = new System.Windows.Forms.RichTextBox();
             this.rtbStore = new System.Windows.Forms.RichTextBox();
             this.btnExit = new System.Windows.Forms.Button();
             this.btnSave = new System.Windows.Forms.Button();
             this.btnOpen = new System.Windows.Forms.Button();
             this.btnFile = new System.Windows.Forms.Button();
             this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
             this.txtFileName = new System.Windows.Forms.TextBox();
             this.groupBox1 = new System.Windows.Forms.GroupBox();
             this.txtStoreName = new System.Windows.Forms.TextBox();
             this.label1 = new System.Windows.Forms.Label();
             this.label3 = new System.Windows.Forms.Label();
             this.txtStreamName = new System.Windows.Forms.TextBox();
             this.groupBox2 = new System.Windows.Forms.GroupBox();
             this.label5 = new System.Windows.Forms.Label();
             this.txtStorageName = new System.Windows.Forms.TextBox();
             this.groupBox1.SuspendLayout();
             this.groupBox2.SuspendLayout();
             this.SuspendLayout();
             //
             // rtbStorage
             //
             this.rtbStorage.Location = new System.Drawing.Point(6, 83);
             this.rtbStorage.Name = "rtbStorage";
             this.rtbStorage.Size = new System.Drawing.Size(198, 91);
             this.rtbStorage.TabIndex = 15;
             this.rtbStorage.Text = "";
             //
             // rtbStore
             //
             this.rtbStore.Location = new System.Drawing.Point(6, 83);
             this.rtbStore.Name = "rtbStore";
             this.rtbStore.Size = new System.Drawing.Size(198, 91);
             this.rtbStore.TabIndex = 14;
             this.rtbStore.Text = "";
             //
             // btnExit
             //
             this.btnExit.Location = new System.Drawing.Point(448, 197);
             this.btnExit.Name = "btnExit";
             this.btnExit.Size = new System.Drawing.Size(75, 23);
             this.btnExit.TabIndex = 13;
             this.btnExit.Text = "Exit";
             this.btnExit.UseVisualStyleBackColor = true;
             this.btnExit.Click += new System.EventHandler(this.btnExit_Click);
             //
             // btnSave
             //
             this.btnSave.Location = new System.Drawing.Point(448, 168);
             this.btnSave.Name = "btnSave";
             this.btnSave.Size = new System.Drawing.Size(75, 23);
             this.btnSave.TabIndex = 12;
             this.btnSave.Text = "Write";
             this.btnSave.UseVisualStyleBackColor = true;
             this.btnSave.Click += new System.EventHandler(this.btnSave_Click);
             //
             // btnOpen
             //
             this.btnOpen.Location = new System.Drawing.Point(448, 139);
             this.btnOpen.Name = "btnOpen";
             this.btnOpen.Size = new System.Drawing.Size(75, 23);
             this.btnOpen.TabIndex = 11;
             this.btnOpen.Text = "Read";
             this.btnOpen.UseVisualStyleBackColor = true;
             this.btnOpen.Click += new System.EventHandler(this.btnOpen_Click);
             //
             // btnFile
             //
             this.btnFile.Location = new System.Drawing.Point(448, 12);
             this.btnFile.Name = "btnFile";
             this.btnFile.Size = new System.Drawing.Size(75, 23);
             this.btnFile.TabIndex = 10;
             this.btnFile.Text = "Browse...";
             this.btnFile.UseVisualStyleBackColor = true;
             this.btnFile.Click += new System.EventHandler(this.btnFile_Click);
             //
             // OpenFileDialog1
             //
             this.OpenFileDialog1.FileName = "OpenFileDialog1";
             //
             // txtFileName
             //
             this.txtFileName.Location = new System.Drawing.Point(12, 12);
             this.txtFileName.Name = "txtFileName";
             this.txtFileName.Size = new System.Drawing.Size(430, 20);
             this.txtFileName.TabIndex = 9;
             //
             // groupBox1
             //
             this.groupBox1.Controls.Add(this.label3);
             this.groupBox1.Controls.Add(this.txtStreamName);
             this.groupBox1.Controls.Add(this.label1);
             this.groupBox1.Controls.Add(this.txtStoreName);
             this.groupBox1.Controls.Add(this.rtbStore);
             this.groupBox1.Location = new System.Drawing.Point(13, 39);
             this.groupBox1.Name = "groupBox1";
             this.groupBox1.Size = new System.Drawing.Size(210, 180);
             this.groupBox1.TabIndex = 18;
             this.groupBox1.TabStop = false;
             this.groupBox1.Text = "Store:";
             //
             // txtStoreName
             //
             this.txtStoreName.Location = new System.Drawing.Point(88, 17);
             this.txtStoreName.Name = "txtStoreName";
             this.txtStoreName.Size = new System.Drawing.Size(116, 20);
             this.txtStoreName.TabIndex = 15;
             //
             // label1
             //
             this.label1.AutoSize = true;
             this.label1.Location = new System.Drawing.Point(7, 20);
             this.label1.Name = "label1";
             this.label1.Size = new System.Drawing.Size(63, 13);
             this.label1.TabIndex = 16;
             this.label1.Text = "StoreName:";
             //
             // label3
             //
             this.label3.AutoSize = true;
             this.label3.Location = new System.Drawing.Point(7, 53);
             this.label3.Name = "label3";
             this.label3.Size = new System.Drawing.Size(75, 13);
             this.label3.TabIndex = 18;
             this.label3.Text = "StorageName:";
             //
             // txtStreamName
             //
             this.txtStreamName.Location = new System.Drawing.Point(88, 50);
             this.txtStreamName.Name = "txtStreamName";
             this.txtStreamName.Size = new System.Drawing.Size(116, 20);
             this.txtStreamName.TabIndex = 17;
             //
             // groupBox2
             //
             this.groupBox2.Controls.Add(this.rtbStorage);
             this.groupBox2.Controls.Add(this.label5);
             this.groupBox2.Controls.Add(this.txtStorageName);
             this.groupBox2.Location = new System.Drawing.Point(232, 39);
             this.groupBox2.Name = "groupBox2";
             this.groupBox2.Size = new System.Drawing.Size(210, 180);
             this.groupBox2.TabIndex = 19;
             this.groupBox2.TabStop = false;
             this.groupBox2.Text = "Storage:";
             //
             // label5
             //
             this.label5.AutoSize = true;
             this.label5.Location = new System.Drawing.Point(7, 20);
             this.label5.Name = "label5";
             this.label5.Size = new System.Drawing.Size(75, 13);
             this.label5.TabIndex = 16;
             this.label5.Text = "StorageName:";
             //
             // txtStorageName
             //
             this.txtStorageName.Location = new System.Drawing.Point(88, 17);
             this.txtStorageName.Name = "txtStorageName";
             this.txtStorageName.Size = new System.Drawing.Size(116, 20);
             this.txtStorageName.TabIndex = 15;
             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(536, 231);
             this.Controls.Add(this.btnExit);
             this.Controls.Add(this.btnSave);
             this.Controls.Add(this.btnOpen);
             this.Controls.Add(this.btnFile);
             this.Controls.Add(this.txtFileName);
             this.Controls.Add(this.groupBox1);
             this.Controls.Add(this.groupBox2);
             this.MaximumSize = new System.Drawing.Size(552, 269);
             this.MinimumSize = new System.Drawing.Size(552, 269);
             this.Name = "Form1";
             this.Text = "DocManager Test";
             this.groupBox1.ResumeLayout(false);
             this.groupBox1.PerformLayout();
             this.groupBox2.ResumeLayout(false);
             this.groupBox2.PerformLayout();
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.RichTextBox rtbStorage;
         internal System.Windows.Forms.RichTextBox rtbStore;
         internal System.Windows.Forms.Button btnExit;
         internal System.Windows.Forms.Button btnSave;
         internal System.Windows.Forms.Button btnOpen;
         internal System.Windows.Forms.Button btnFile;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog1;
         internal System.Windows.Forms.TextBox txtFileName;
         private System.Windows.Forms.GroupBox groupBox1;
         private System.Windows.Forms.Label label3;
         private System.Windows.Forms.TextBox txtStreamName;
         private System.Windows.Forms.Label label1;
         private System.Windows.Forms.TextBox txtStoreName;
         private System.Windows.Forms.GroupBox groupBox2;
         private System.Windows.Forms.Label label5;
         private System.Windows.Forms.TextBox txtStorageName;
     }
 }
```
