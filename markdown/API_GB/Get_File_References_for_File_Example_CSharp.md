---
title: "Get File References for a File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Get_File_References_for_File_Example_CSharp.htm"
---

# Get File References for a File Example (C#)

This example shows how to get the file references for a file and export any file references to an XML file. This example also shows how to get whether the file and any file references in local cache are valid or obsolete.

**NOTE:**

- This example does not work with assemblies that contain weldment components.
- If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//----------------------------------------------------------------------------
// Preconditions:
//  1. Start Microsoft Visual Studio 2015.
//     a. Click File > New > Project > C# > Windows Forms Application.
//     b. Type GetFiles2CSharp in Name.
//     c. Click Browse and navigate to the folder where to create
//        the project.
//     d. Click OK.
//     e. Click Show All Files in the Solution Explorer toolbar and expand
//        Form1.cs in the Solution Explorer.
//     f. Replace the code in Form1.cs with this code.
//     g. To create the form, replace the code in Form1.Designer.cs with this code.
//     h. Right-click the GetFiles2CSharp project name in the Solution Explorer.
//        1. Click Add > Class > Class.
//        2. Type FileRef.cs in Name.
//        3. Click Add.
//        4. Replace the code in FileRef.cs with this code.
//  2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
//     name in the Solution Explorer, click Add > Reference, click
//     Assemblies > Framework in the left-side panel, browse to the top folder of
//     your SOLIDWORKS PDM Professional installation, locate and click
//     EPDM.Interop.epdm.dll, click Add > OK).
//  3. Right-click EPDM.Interop.epdm in References, click Properties, and set
//     Embed Interop Types to False to handle methods that pass arrays of
//     structures.
//  4. Verify that C:\temp exists.
//  5. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays a dialog.
//  2. Select a vault.
//  3. Click Browse, locate and select a file in the vault that
//     has file references, and click Open.
//  4. Click Write file references to an XML file, which exports
//     the names of any file references to C:\temp\BatchFileRefInfo.xml.
//  5. Displays a message box that says file references were exported
//     to an XML file.
//  6. Click OK to close the message box.
//  7. Double-click C:\temp\BatchFileRefInfo.xml and examine its contents.
//----------------------------------------------------------------------------

//Form1.cs
using System.IO;
using System.Xml.Serialization;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using System.Windows.Forms;
using System.ComponentModel;
using EPDM.Interop.epdm;

namespace GetFiles2CSharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        IEdmVault5 vault1 = null;

        public void FileReferencesCSharp_Load(System.Object sender, System.EventArgs e)
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

        public void BrowseButton_Click(System.Object sender, System.EventArgs e)
        {
            try
            {
                BatchRefListBox.Items.Clear();

                //Only create a new vault object
                //if one hasn't been created yet
                if (vault1 == null)
                    vault1 = new EdmVault5();
                if (!vault1.IsLoggedIn)
                {
                    //Log into selected vault as the current user
                    vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                }

                //Set the initial directory in the File Open dialog
                BatchRefOpenFileDialog.InitialDirectory = vault1.RootFolderPath;
                //Show the File Open dialog
                System.Windows.Forms.DialogResult DialogResult = default(System.Windows.Forms.DialogResult);
                DialogResult = BatchRefOpenFileDialog.ShowDialog();
                //If the user didn't click Open, exit the sub
                if (!(DialogResult == System.Windows.Forms.DialogResult.OK))
                    return;

                foreach (string FileName in BatchRefOpenFileDialog.FileNames)
                {
                    BatchRefListBox.Items.Add(FileName);
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

        public void GetReferencedFiles(IEdmReference10 Reference, string FilePath, int Level, string ProjectName, ref Dictionary<string, string> RefFilesDictionary)
        {
            try
            {
                bool Top = false;
                if (Reference == null)
                {
                    //This is the first time this function is called for this
                    //reference tree; i.e., this is the root
                    Top = true;
                    //Add the top-level file path to the dictionary
                    RefFilesDictionary.Add(FilePath, Level.ToString());
                    IEdmFile5 File = null;
                    IEdmFolder5 ParentFolder = null;
                    File = vault1.GetFileFromPath(FilePath, out ParentFolder);
                    //Get the reference tree for this file
                    Reference = (IEdmReference10)File.GetReferenceTree(ParentFolder.ID);
                    GetReferencedFiles(Reference, "", Level + 1, ProjectName, ref RefFilesDictionary);
                }
                else
                {
                    //Execute this code when this function is called recursively;
                    //i.e., this is not the top-level IEdmReference in the tree

                    //Recursively traverse the references
                    IEdmPos5 pos = default(IEdmPos5);
                    IEdmReference10 Reference2 = (IEdmReference10)Reference;
                    pos = Reference2.GetFirstChildPosition3(ProjectName, Top, true, (int)EdmRefFlags.EdmRef_File, "", 0);
                    IEdmReference10 @ref = default(IEdmReference10);
                    while ((!pos.IsNull))
                    {
                        @ref = (IEdmReference10)Reference.GetNextChild(pos);
                        RefFilesDictionary.Add(@ref.FoundPath, Level.ToString());
                        GetReferencedFiles(@ref, "", Level + 1, ProjectName, ref RefFilesDictionary);
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

        public void WriteXmlButton_Click(System.Object sender, System.EventArgs e)
        {
            try
            {
                //Only create a new vault object
                //if one hasn't been created yet
                IEdmVault7 vault2 = null;
                if (vault1 == null)
                    vault1 = new EdmVault5();
                    vault2 = (IEdmVault7)vault1;
                if (!vault1.IsLoggedIn)
                {
                    //Log into selected vault as the current user
                    vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                }

                //Get the file paths of all of the referenced files
                //and store them in RefFilesDictionary as keys;
                //the levels where they are found in the file hierarchy
                //are stored as values
                Dictionary<string, string> RefFilesDictionary = new Dictionary<string, string>();
                foreach (string FileName in BatchRefListBox.Items)
                {
                    GetReferencedFiles(null, FileName, 0, "A", ref RefFilesDictionary);
                }

                //Because selecting a file in the Open File dialog
                //adds the file and its references to the local cache,
                //clear the local cache to demonstrate that the
                //IEdmBatchListing methods don't add the files to
                //the local cache
```

```vb
                 //Declare and create the IEdmClearLocalCache3 object
                 IEdmClearLocalCache3 ClearLocalCache = default(IEdmClearLocalCache3);
                 ClearLocalCache = (IEdmClearLocalCache3)vault2.CreateUtility(EdmUtility.EdmUtil_ClearLocalCache);
                 ClearLocalCache.IgnoreToolboxFiles = true;
                 ClearLocalCache.UseAutoClearCacheOption = true;

                 //Declare and create the IEdmBatchListing object
                 IEdmBatchListing4 BatchListing = default(IEdmBatchListing4);
                 BatchListing = (IEdmBatchListing4)vault2.CreateUtility(EdmUtility.EdmUtil_BatchList);

                 //Add all of the reference file paths to the
                 //IEdmClearLocalCache object to clear from the
                 //local cache and to the IEdmBatchListing object
                 //to get the file information in batch mode
                 foreach (KeyValuePair<string, string> KvPair in RefFilesDictionary)
                 {
                     ClearLocalCache.AddFileByPath(KvPair.Key);
                     ((IEdmBatchListing4)BatchListing).AddFileCfg(KvPair.Key, DateTime.Now, (Convert.ToInt32(KvPair.Value)), "@", Convert.ToInt32(EdmListFileFlags.EdmList_Nothing));
                 }
                 //Clear the local cache of the reference files
                 ClearLocalCache.CommitClear();

                 //Create the batch file listing along with the file
                 //card variables Description and Number
                 EdmListCol[] BatchListCols = null;
                 ((IEdmBatchListing4)BatchListing).CreateListEx("\n\nDescription\nNumber", Convert.ToInt32(EdmCreateListExFlags.Edmclef_MayReadFiles), ref BatchListCols, null);
                 //Get the generated file information
                 EdmListFile2[] BatchListFiles = null;
                 BatchListing.GetFiles2(ref BatchListFiles);

                 //Create the list where to store all the file information
                 List<FileRef> FileRefs = new List<FileRef>();

                 //Recursively add the file information to the list
                 int j = 0;
                 AddFileRef(ref BatchListFiles, ref j, 0, ref FileRefs);

                 if (!Directory.Exists("C:\\temp"))
                 {
                     MessageBox.Show("Directory \"c:\temp\" does " + "not exist; please create it and try again.");
                 }
                 else
                 {
                     XmlSerializer XmlSer = new XmlSerializer(typeof(List<FileRef>));
                     StreamWriter StrWriter = new StreamWriter("C:\\temp\\BatchFileRefInfo.xml");
                     XmlSer.Serialize(StrWriter, FileRefs);
                     StrWriter.Close();
                     MessageBox.Show("File references successfully exported to an XML file.");
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

         public void AddFileRef(ref EdmListFile2[] BatchListFiles, ref int curIndex, int curLevel, ref List<FileRef> FileRefs)

         {
             try
             {

                 while (curIndex < BatchListFiles.Length)
                 {
                     EdmListFile2 curListFile = BatchListFiles[curIndex];
                     //If the depth level of this listfile is <
                     //the current depth level then...
                     if (curListFile.mlParam > curLevel)
                     {
                         //Create a new FileRefs list
                         FileRefs[FileRefs.Count - 1].FileRefs = new List<FileRef>();
                         List<FileRef> fRef = FileRefs[FileRefs.Count - 1].FileRefs;
                         //Recurse using a new FileRefs list
                          AddFileRef(ref BatchListFiles, ref curIndex, curListFile.mlParam, ref fRef);
                     }
                     else
                     {
                         //Create a new FileRef object to hold
                         //the file information
                         FileRef FileRef = new FileRef();
                         //Assign the FileRef properties
                         FileRef.CheckedOutBy = curListFile.mbsLockUser;
                         FileRef.CurrentState = curListFile.moCurrentState.mbsStateName;
                         object[] columnData = (object[])curListFile.moColumnData;
                         FileRef.Description = (string)columnData[0];
                         IEdmFile5 File = default(IEdmFile5);
                         File = (IEdmFile5)vault1.GetObject(EdmObjectType.EdmObject_File, curListFile.mlFileID);
                         FileRef.FileName = File.Name;
                         FileRef.LatestRevision = curListFile.mbsRevisionName;
                         FileRef.LatestVersion = Convert.ToString(curListFile.mlLatestVersion);
                         FileRef.Number = (string)columnData[1];
                         FileRef.FileRefs = null;
                         //Add the FileRef to this level's list
                         FileRefs.Add(FileRef);
                         curIndex += 1;
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
namespace GetFiles2CSharp
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
            this.BatchRefLabel = new System.Windows.Forms.Label();
            this.BrowseButton = new System.Windows.Forms.Button();
            this.BatchRefListBox = new System.Windows.Forms.ListBox();
            this.WriteXMLButton = new System.Windows.Forms.Button();
            this.BatchRefOpenFileDialog = new System.Windows.Forms.OpenFileDialog();
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
            this.VaultsComboBox.Location = new System.Drawing.Point(16, 59);
            this.VaultsComboBox.Name = "VaultsComboBox";
            this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
            this.VaultsComboBox.TabIndex = 1;
            //
            // BatchRefLabel
            //
            this.BatchRefLabel.AutoSize = true;
            this.BatchRefLabel.Location = new System.Drawing.Point(16, 116);
            this.BatchRefLabel.Name = "BatchRefLabel";
            this.BatchRefLabel.Size = new System.Drawing.Size(160, 13);
            this.BatchRefLabel.TabIndex = 2;
            this.BatchRefLabel.Text = "Files for which to get references:";
            //
            // BrowseButton
            //
            this.BrowseButton.Location = new System.Drawing.Point(197, 106);
            this.BrowseButton.Name = "BrowseButton";
            this.BrowseButton.Size = new System.Drawing.Size(75, 23);
            this.BrowseButton.TabIndex = 3;
            this.BrowseButton.Text = "Browse...";
            this.BrowseButton.UseVisualStyleBackColor = true;
            this.BrowseButton.Click += new System.EventHandler(BrowseButton_Click);
            //
            // BatchRefListBox
            //
            this.BatchRefListBox.FormattingEnabled = true;
            this.BatchRefListBox.Location = new System.Drawing.Point(13, 150);
            this.BatchRefListBox.Name = "BatchRefListBox";
            this.BatchRefListBox.Size = new System.Drawing.Size(259, 95);
            this.BatchRefListBox.TabIndex = 4;
            //
            // WriteXMLButton
            //
            this.WriteXMLButton.Location = new System.Drawing.Point(13, 270);
            this.WriteXMLButton.Name = "WriteXMLButton";
            this.WriteXMLButton.Size = new System.Drawing.Size(259, 23);
            this.WriteXMLButton.TabIndex = 5;
            this.WriteXMLButton.Text = "Write file references to an XML file";
            this.WriteXMLButton.UseVisualStyleBackColor = true;
            this.WriteXMLButton.Click += new System.EventHandler(this.WriteXmlButton_Click);

            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 308);
            this.Controls.Add(this.WriteXMLButton);
            this.Controls.Add(this.BatchRefListBox);
            this.Controls.Add(this.BrowseButton);
            this.Controls.Add(this.BatchRefLabel);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.VaultsLabel);
            this.Name = "Form1";
            this.Text = "Get file references";
            this.Load += new System.EventHandler(this.FileReferencesCSharp_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label VaultsLabel;
        private System.Windows.Forms.ComboBox VaultsComboBox;
        private System.Windows.Forms.Label BatchRefLabel;
        private System.Windows.Forms.Button BrowseButton;
        private System.Windows.Forms.ListBox BatchRefListBox;
        private System.Windows.Forms.Button WriteXMLButton;
        private System.Windows.Forms.OpenFileDialog BatchRefOpenFileDialog;
    }
}
```

```
Back to top
```

```
//FileRef.cs
```

```
using System;
using System.Collections;
using System.Diagnostics;
using System.Collections.Generic;

namespace GetFiles2CSharp
{

    public class FileRef
    {
        private short mLocalOverWrittenVersionObsolete;
        private string mFileName;
        private string mLatestVersion;
        private string mLatestRevision;
        private string mNumber;
        private string mDescription;
        private string mCurrentState;
        private string mCheckedOutBy;
        private List<FileRef> mFileRefs;

        public FileRef()
        {

        }

        public string FileName
        {
            get { return mFileName; }
            set { mFileName = value; }
        }

        public string LatestVersion
        {
            get { return mLatestVersion; }
            set { mLatestVersion = value; }
        }

        public string LatestRevision
        {
            get { return mLatestRevision; }
            set { mLatestRevision = value; }
        }

        public string Number
        {
            get { return mNumber; }
            set { mNumber = value; }
        }

        public string Description
        {
            get { return mDescription; }
            set { mDescription = value; }
        }

        public string CurrentState
        {
            get { return mCurrentState; }
            set { mCurrentState = value; }
        }

        public string CheckedOutBy
        {
            get { return mCheckedOutBy; }
            set { mCheckedOutBy = value; }
        }

	public short LocalOverWrittenVersionObsolete
	{
    	   get { return mLocalOverWrittenVersionObsolete; }
    	   set { mLocalOverWrittenVersionObsolete = value; }
	}

        public List<FileRef> FileRefs
        {
            get { return mFileRefs; }
            set { mFileRefs = value; }
        }
    }

}
```

```
Back to top
```
