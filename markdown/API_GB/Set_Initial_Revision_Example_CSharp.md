---
title: "Set Initial Revision Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Set_Initial_Revision_Example_CSharp.htm"
---

# Set Initial Revision Example (C#)

This example shows how to set the initial revision of a file.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //--------------------------------------------------------------------------------------
 // Preconditions:
 //  1. Start Microsoft Visual Studio 2010.
  //  2. Click File > New > Project > Visual C# > Windows Forms Application.
 //  3. Select .NET Framework 4 in the top dropdown.
 //  4. Click Browse and navigate to the folder where to create the project.
 //  5. Type SetRevision_CSharp in Name.
 //  6. Click OK.
 //  7. Right-click the project name in the Solution Explorer and click Add Reference.
 //  8. In the Add Reference dialog:
  //     a. Click Assemblies > Framework in the left-side panel,
 //        browse to the top folder of your SOLIDWORKS PDM Professional installation,
 //        locate and click EPDM.Interop.epdm.dll, click Open, and click Add.
  //     b. Click Assemblies > Framework in the left-side panel, click
 //        Microsoft.VisualBasic, and click Add.
 //     c. Click Close.
 //  9. Right-click References > EPDM.Interop.epdm in the Solution Explorer,
 //     click Properties, and set Embed Interop Types to False to handle methods
 //     that pass arrays of structures.
  // 10. Create a form similar to the form shown above and change:
 //     a. Label to VaultsLabel.
 //     b. Combo box to VaultsComboBox.
 //     c. Button to SetInitialRevisionButton.
 // 11. Click Show All Files in the Solution Explorer toolbar and expand  Form1.cs.
 // 12. Replace the code in Form1.cs with this code.
  // 13. Replace the code in Form1.Designer.cs with this code.
 // 14. Copy a SOLIDWORKS part to a PDM vault view.
 //     a. Check in the part.
 //     b. Right-click the part and click Change State > No Approval Required.
 //        Part is now in the Approved state, and data card Revision is A.
 //     c. Check out the part.
 //     d. In the part's data card, type G in Revision.
 //     e. Save the data card.
 //     f. Check in the part.
 // 15. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. The Set Revision dialog opens.
 // 2. Select the vault containing the SOLIDWORKS part you just checked in.
 // 3. Click Set Initial Revision.
  // 4. In the Select files on which to set initial revision dialog, click the
 //    SOLIDWORKS part you just checked in and click Open.
  // 5. In the File already has a revision dialog, click OK to set the initial
  //    revision.
 // 6. Refresh the vault view, click the SOLIDWORKS part, and click the Version tab.
  //    Observe that the local revision of the file is now G.
 // 7. Close the Set Revision dialog.
  //--------------------------------------------------------------------------------------
```

```
//Form1.cs
```

```vb
 using System;
 using System.Windows.Forms;
 using EPDM.Interop.epdm;
 using Microsoft.VisualBasic;

 namespace SetRevision_CSharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void SetRevision_CSharp_Load(System.Object sender, System.EventArgs e)
    {

    try {
              IEdmVault5 vault = new EdmVault5();
             EdmViewInfo[] Views = {};

            ((IEdmVault8)vault).GetVaultViews(out Views, false);
            VaultsComboBox.Items.Clear();
            foreach (EdmViewInfo View in Views) {
                VaultsComboBox.Items.Add(View.mbsVaultName);
            }
            if (VaultsComboBox.Items.Count > 0) {
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

    private void SetInitialRevisionButton_Click(System.Object sender, System.EventArgs e)
    {

    try {
            //Declare and create an instance of IEdmVault5
            IEdmVault5 vault = new EdmVault5();

            //Log into selected vault as the current user
            vault.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());

            //Display a File Open dialog for user to
            //choose the files on which set the initial revision
            EdmStrLst5 PathList = default(EdmStrLst5);
            PathList = vault.BrowseForFile(this.Handle.ToInt32(), (int)EdmBrowseFlag.EdmBws_ForOpen + (int)EdmBrowseFlag.EdmBws_PermitMultipleSel + (int)EdmBrowseFlag.EdmBws_PermitVaultFiles, "SOLIDWORKS files " + "(*.sldprt; *.sldasm; *.slddrw)|" + "*.sldprt;*.sldasm;*.slddrw|" + "All Files (*.*)|*.*||", "", "", vault.RootFolderPath, "Select Files to Set Initial Revision on");

            //Exit if the user clicks Cancel
             if (PathList == null)
            return;

            //Traverse the selected files
            IEdmPos5 pos = default(IEdmPos5);
            pos = PathList.GetHeadPosition();
            while (!pos.IsNull) {
                //Get each file path from the selected files list
                string FilePath = null;
                FilePath = PathList.GetNext(pos);
                //Get the IEdmFile5 object corresponding
                //to the path
                IEdmFile5 FileObj = default(IEdmFile5);
                    IEdmFolder5 retfold = default(IEdmFolder5);
                FileObj = vault.GetFileFromPath(FilePath, out retfold);

                //Skip any files that are checked out
                if (FileObj.IsLocked) {
                    MessageBox.Show    (FilePath + " is checked out." + Constants.vbCrLf + "Check it in and try again." + Constants.vbCrLf + "Skipping this file.", "File is checked out.", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    continue;
                }

                //Get the value of the file data
                //card variable named Revision
                IEdmEnumeratorVariable8 EnumVarObj = default(IEdmEnumeratorVariable8);
                //Keeps the file open
                EnumVarObj = (IEdmEnumeratorVariable8)FileObj.GetEnumeratorVariable();

                bool GetVarSuccess = false;
                //GetVar returns a Variant
                object RevisionObj = null;
                GetVarSuccess = EnumVarObj.GetVar("Revision", "@", out RevisionObj);
                EnumVarObj.CloseFile(false);
                //Pass True to flush

                //Skip any files without a Revision
                //card variable value
                if (RevisionObj == null) {
                    MessageBox.Show("The \"Revision\" custom " + "property of " + FilePath + " is not set to a value." + Constants.vbCrLf + "Skipping this file.", "Revision custom property empty.", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    continue;
                }

                //Check type
                System.Type RevType = default(System.Type);
                RevType = RevisionObj.GetType();
                if (!(RevType.Name == "String")) {
                    MessageBox.Show("The \"Revision\" " + "variable type is not \"String\"." + Constants.vbCrLf + "Skipping this file.", "Revision custom property empty.", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    continue;
                }

                string RevisionProp = null;
                RevisionProp = (string)RevisionObj;

                //Skip any files whose Revision value
                //is not formatted appropriately
                if (!(RevisionProp.Length == 1)) {
                    MessageBox.Show("The \"Revision\" custom " + "property of " + FilePath + " does not conform to the expected " + "revision number format." + Constants.vbCrLf + "Skipping this file.", "Revision custom property in the wrong format.", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    continue;
                }

                //Create an IEdmRevisionMgr2 object
                IEdmRevisionMgr2 RevMgr = default(IEdmRevisionMgr2);
                RevMgr = (IEdmRevisionMgr2)((IEdmVault7)vault).CreateUtility(EdmUtility.EdmUtil_RevisionMgr);

                //Get the revision number ID
                bool CanIncrement = false;
                long RevisionNumberID = 0;
                //Return 0 if there is no revision number
                //generator defined for the file's current state
                RevisionNumberID = RevMgr.GetRevisionNumberIDFromFile(FileObj.ID, out CanIncrement);

                //Skip this file if there is no
                //revision number generator for it
                if (RevisionNumberID == 0) {
                    MessageBox.Show("Move " + FilePath + " to a state where a Revision Number " + "is defined." + Constants.vbCrLf + "Skipping this file.", "No Revision Number is defined " + "for this state.", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    continue;
                }

                //Get the revision number info for this file
                EdmRevNo[] RevNumbers = {

                };
                RevMgr.GetRevisionNumbers(RevisionNumberID, out RevNumbers);
                string RevNoFormatString = null;
                RevNoFormatString = RevNumbers[0].mbsData;
                string RevNoFormatLiteral = null;
                int PercentPos = 0;
                PercentPos = RevNoFormatString.IndexOf("%");
                RevNoFormatLiteral = RevNoFormatString.Substring(0, PercentPos);
                string NewRev = null;
                NewRev = RevNoFormatLiteral + RevisionProp;

                //Check the file's current revision
                string CurRev = null;
                CurRev = FileObj.CurrentRevision;

                //Give the user the option to skip this file
                //if it already has a revision set
                if (!(CurRev == string.Empty)) {
                    System.Windows.Forms.DialogResult MsgBoxResult = default(System.Windows.Forms.DialogResult);
                    MsgBoxResult = MessageBox.Show("The current revision of " + FilePath + " is \"" + CurRev + "\"." + Constants.vbCrLf + "The new revision will be \"" + NewRev + "\"" + Constants.vbCrLf + "Would you like to continue?", "File already has a revision", MessageBoxButtons.OKCancel, MessageBoxIcon.Question);
                    if (MsgBoxResult == System.Windows.Forms.DialogResult.Cancel)
                    continue;
                }

                //Get the revision number components for the
                //revision number used by this file
                EdmRevComponent2[] RevComponents = {

                };
                RevMgr.GetRevisionNumberComponents2(-RevisionNumberID, out RevComponents);
                string RevComponentName = null;
                RevComponentName = RevComponents[0].mbsComponentName;

                //Declare an array of EdmRevCounter structures,
                //even though only one is used,
                //and assign the values to set
                EdmRevCounter[] RevCounters = new EdmRevCounter[1];
                //Assign the name of the revision counter
                //to set
                RevCounters[0].mbsComponentName = RevComponentName;
                //Assign the new revision counter value to the
                //value stored in the Revision card variable
                //converted to an integer
                long RevInt = 0;
                RevInt = Strings.Asc(RevisionProp.ToUpper()) - Strings.Asc("A") + 1;
                RevCounters[0].mlCounter = (int)RevInt;

                //Set the revision counter to the new values
                RevMgr.SetRevisionCounters(FileObj.ID, RevCounters);

                //Set the revision of the file to the new values
                RevMgr.IncrementRevision(FileObj.ID);

                //Save the new values to the database
                EdmRevError[] RevErrors = {

                };
                RevMgr.Commit("Set starting revision for " + "legacy file.", out RevErrors);
            }
           }
          catch (System.Runtime.InteropServices.COMException ex) {
                MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);
          }
           catch (Exception ex) {
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
 namespace SetRevision_CSharp
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
             this.SetInitialRevisionButton = new System.Windows.Forms.Button();
             this.SuspendLayout();
             //
             // VaultsLabel
             //
             this.VaultsLabel.AutoSize = true;
             this.VaultsLabel.Location = new System.Drawing.Point(52, 28);
             this.VaultsLabel.Name = "VaultsLabel";
             this.VaultsLabel.Size = new System.Drawing.Size(136, 13);
             this.VaultsLabel.TabIndex = 0;
             this.VaultsLabel.Text = "Select Preferred Vault View";
             //
             // VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(55, 58);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             // SetInitialRevisionButton
             //
             this.SetInitialRevisionButton.Location = new System.Drawing.Point(55, 97);
             this.SetInitialRevisionButton.Name = "SetInitialRevisionButton";
             this.SetInitialRevisionButton.Size = new System.Drawing.Size(121, 23);
             this.SetInitialRevisionButton.TabIndex = 2;
             this.SetInitialRevisionButton.Text = "Set Initial Revision";
             this.SetInitialRevisionButton.UseVisualStyleBackColor = true;
             this.SetInitialRevisionButton.Click += new System.EventHandler(this.SetInitialRevisionButton_Click);
             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(284, 262);
             this.Controls.Add(this.SetInitialRevisionButton);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Set Revision";
             this.Load += new System.EventHandler(this.SetRevision_CSharp_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         private System.Windows.Forms.Label VaultsLabel;
         private System.Windows.Forms.ComboBox VaultsComboBox;
         private System.Windows.Forms.Button SetInitialRevisionButton;
     }
 }
```

```
Back to top
```
