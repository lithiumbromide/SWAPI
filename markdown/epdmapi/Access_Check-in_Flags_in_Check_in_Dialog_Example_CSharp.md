---
title: "Access Check-in Flags in Check in Dialog Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Access_Check-in_Flags_in_Check_in_Dialog_Example_CSharp.htm"
---

# Access Check-in Flags in Check in Dialog Example (C#)

This example shows how to access the check-in flags in the SOLIDWORKS PDM Professional Check in dialog.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
//--------------------------------------------------------------------------------------
// Preconditions:
//  1. Start Microsoft Visual Studio.
//     a. Click File > New > Project > C#, Windows, Desktop > Windows Forms Application.
//     b. Type RefItemContainerCSharp in Project name.
//     c. For Location, click ... and navigate to the folder where to
create the project.
//     d. Click Next.
//     e. Select Framework.
//     f. Click Create.

//     g. Click Show All Files in the Solution Explorer
toolbar and expand

//        Form1.cs in the Solution Explorer.
//     h. Replace the code in Form1.cs with this code.
//     i. To create the form, replace the code in Form1.Designer.cs with
//        this code.
//     j. To create the class for the callback:
//        1. Right-click RefItemContainerCSharp in the Solution Explorer.
//        2. Click Add > Class.
//        3. Type Callback.cs in Name and click Add.
//        4. Replace the code in Callback.cs with this code.
//  2. Add dependencies and safely pass arrays of structures.
//  3. Click Debug > Start Debugging or press F5.
//
// Postconditions:
//  1. Displays the Access Check-in Flags in Check in Dialog dialog box.
//  2. Select a vault view.
//  3. Click Select checked-out files to check in.
//     a. Displays the Select files dialog box.
//     b. Click one or more checked-out files to check in.
//     c. Click Open.
//  4. Click Create batch check-in.
//     a. At the end of an attempted check-in, displays three message
//        boxes containing ProgressEnd called. Three operations occur for an
//        attempted check-in.
//     b. Click OK to close each message box.
//     c. Displays either:
//        * Message box containing Batch check-in created. Click OK to
//          close the message box.
//          - or -
//        * Message box containing You did not select a file to check in. Please try
//          again. Click OK to close the message box, and repeat steps 3 and 4.
//  5. Click Update check-in flags.
//  6. Click OK to close the message box.
//  7. Click Check in files.
//  8. Displays the Check in dialog box.
//  9. Click Check in to check in the files or Cancel to cancel the check in.
// 10. Displays a message box containing ProgressEnd called. Click OK to close
//     the message box.
// 11. Examine the files in the vault to verify their checked-in or checked-out status.
// 12. Close the Access Check-in Flags in Check in Dialog dialog box.
//--------------------------------------------------------------------------------------

//Form1.cs
using System;
using System.Windows.Forms;
using EPDM.Interop.epdm;

namespace RefItemContainerCSharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        IEdmVault5 vault1 = null;
        IEdmVault8 vault = null;
        EdmSelItem[] selFiles = null;
        IEdmBatchUnlock bUnlock = null;

        void Form1_Load(System.Object sender, System.EventArgs e)
        {

            try
            {
                vault1 = new EdmVault5();
                vault = (IEdmVault8)vault1;
                EdmViewInfo[] Views = { };

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

        private void BrowseButton_Click(object sender, EventArgs e)
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

                //Display the Select file dialog for user to
                //select the files
                EdmStrLst5 pathList = default(EdmStrLst5);
                pathList = vault.BrowseForFile(this.Handle.ToInt32(),
		(int)EdmBrowseFlag.EdmBws_ForOpen + (int)EdmBrowseFlag.EdmBws_PermitMultipleSel +
		(int)EdmBrowseFlag.EdmBws_PermitVaultFiles, "SOLIDWORKS files " +
		"(*.sldprt; *.sldasm; *.slddrw)|" + "*.sldprt;*.sldasm;*.slddrw|" + "All Files (*.*)|*.*||", "",
		"", vault.RootFolderPath, "Select files");

                //Exit if the user clicks Cancel
                if (pathList == null)
                    return;

                //Traverse the selected files
                IEdmPos5 pos = default(IEdmPos5);
                pos = pathList.GetHeadPosition();

                //Convert the selected files to an
                //array of EdmSelItem structs
                int nbrFiles = 0;
                nbrFiles = pathList.Count;
                Array.Resize(ref selFiles, nbrFiles);

                int i = 0;
                while (!pos.IsNull)
                {
                    //Get each file path from the selected files list
                    string filePath = null;
                    IEdmFile5 file = default(IEdmFile5);
                    IEdmFolder5 retFolder = default(IEdmFolder5);
                    filePath = pathList.GetNext(pos);
                    file = vault.GetFileFromPath(filePath, out retFolder);
                    selFiles[i].mlDocID = file.ID;
                    selFiles[i].mlProjID = retFolder.ID;
                    i = i + 1;
                }

            }catch (System.Runtime.InteropServices.COMException ex)
            {
                MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

        }

        private void CreateBatchCheckinButton_Click(object sender, EventArgs e)
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

                IEdmVault7 vault2 = (IEdmVault7)vault1;
                bUnlock = (IEdmBatchUnlock)vault2.CreateUtility(EdmUtility.EdmUtil_BatchUnlock);
                bUnlock.AddSelection((EdmVault5)vault1, ref selFiles);
                bool tree = false;
	       Callback myCallback = new Callback();
                tree = bUnlock.CreateTree(this.Handle.ToInt32(), (int)EdmUnlockBuildTreeFlags.Eubtf_MayUnlock, myCallback);
                if (tree == false)
                {
                    MessageBox.Show("You did not select a file to check in. Please try again.");
                    return;
                }

                MessageBox.Show("Batch check in created.");

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

        private void UpdateBatchCheckInButton_Click(object sender, EventArgs e)
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
                    IEdmRefItemContainer container = null;
                    container = (IEdmRefItemContainer)bUnlock;
                    object[] items = null;
                    IEdmRefItem theItem = null;
                    container.GetItems(EdmRefItemType.Edmrit_All, out items);
                    int j = 0;
                    while (j < items.Length)
                    {
                        IEdmRefItem aItem = null;
                        theItem = (IEdmRefItem)items[j];
                        aItem = theItem;
                        object value = null;
                        aItem.SetProperty(EdmRefItemProperty.Edmrip_CheckKeepLocked, value);
                        j = j + 1;
                    }

                    MessageBox.Show("Check-in flags updated.");
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

        private void CheckInButton_Click(object sender, EventArgs e)
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

                if (bUnlock.ShowDlg(this.Handle.ToInt32()))
                {
                    Callback myCallback = new Callback();
                    bUnlock.UnlockFiles(this.Handle.ToInt32(), myCallback);
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
namespace RefItemContainerCSharp
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
            this.CreateBatchCheckinButton = new System.Windows.Forms.Button();
            this.UpdateBatchCheckInButton = new System.Windows.Forms.Button();
            this.CheckInButton = new System.Windows.Forms.Button();
            this.BrowseButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            //
            // VaultsLabel
            //
            this.VaultsLabel.AutoSize = true;
            this.VaultsLabel.Location = new System.Drawing.Point(24, 29);
            this.VaultsLabel.Name = "VaultsLabel";
            this.VaultsLabel.Size = new System.Drawing.Size(91, 13);
            this.VaultsLabel.TabIndex = 0;
            this.VaultsLabel.Text = "Select vault view:";
            //
            // VaultsComboBox
            //
            this.VaultsComboBox.FormattingEnabled = true;
            this.VaultsComboBox.Location = new System.Drawing.Point(27, 45);
            this.VaultsComboBox.Name = "VaultsComboBox";
            this.VaultsComboBox.Size = new System.Drawing.Size(187, 21);
            this.VaultsComboBox.TabIndex = 1;
            //
            // CreateBatchCheckinButton
            //
            this.CreateBatchCheckinButton.Location = new System.Drawing.Point(27, 122);
            this.CreateBatchCheckinButton.Name = "CreateBatchCheckinButton";
            this.CreateBatchCheckinButton.Size = new System.Drawing.Size(125, 23);
            this.CreateBatchCheckinButton.TabIndex = 4;
            this.CreateBatchCheckinButton.Text = "Create batch check-in";
            this.CreateBatchCheckinButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.CreateBatchCheckinButton.UseVisualStyleBackColor = true;
            this.CreateBatchCheckinButton.Click += new System.EventHandler(this.CreateBatchCheckinButton_Click);
            //
            // UpdateBatchCheckInButton
            //
            this.UpdateBatchCheckInButton.Location = new System.Drawing.Point(27, 164);
            this.UpdateBatchCheckInButton.Name = "UpdateBatchCheckInButton";
            this.UpdateBatchCheckInButton.Size = new System.Drawing.Size(125, 23);
            this.UpdateBatchCheckInButton.TabIndex = 5;
            this.UpdateBatchCheckInButton.Text = "Update check-in flags";
            this.UpdateBatchCheckInButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.UpdateBatchCheckInButton.UseVisualStyleBackColor = true;
            this.UpdateBatchCheckInButton.Click += new System.EventHandler(this.UpdateBatchCheckInButton_Click);
            //
            // CheckInButton
            //
            this.CheckInButton.Location = new System.Drawing.Point(27, 209);
            this.CheckInButton.Name = "CheckInButton";
            this.CheckInButton.Size = new System.Drawing.Size(125, 23);
            this.CheckInButton.TabIndex = 6;
            this.CheckInButton.Text = "Check in files";
            this.CheckInButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.CheckInButton.UseVisualStyleBackColor = true;
            this.CheckInButton.Click += new System.EventHandler(this.CheckInButton_Click);
            //
            // BrowseButton
            //
            this.BrowseButton.Location = new System.Drawing.Point(27, 82);
            this.BrowseButton.Name = "BrowseButton";
            this.BrowseButton.Size = new System.Drawing.Size(125, 23);
            this.BrowseButton.TabIndex = 7;
            this.BrowseButton.Text = "Select checked-out files to check in";
            this.BrowseButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.BrowseButton.UseVisualStyleBackColor = true;
            this.BrowseButton.Click += new System.EventHandler(this.BrowseButton_Click);
            //
            // Form1
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(384, 254);
            this.Controls.Add(this.BrowseButton);
            this.Controls.Add(this.CheckInButton);
            this.Controls.Add(this.UpdateBatchCheckInButton);
            this.Controls.Add(this.CreateBatchCheckinButton);
            this.Controls.Add(this.VaultsComboBox);
            this.Controls.Add(this.VaultsLabel);
            this.Name = "Form1";
            this.Text = "Access Check-in Flags in Check in Dialog";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label VaultsLabel;
        private System.Windows.Forms.ComboBox VaultsComboBox;
        private System.Windows.Forms.Button CreateBatchCheckinButton;
        private System.Windows.Forms.Button UpdateBatchCheckInButton;
        private System.Windows.Forms.Button CheckInButton;
        private System.Windows.Forms.Button BrowseButton;
    }
}
```

```
Back to top
```

```
//Callback.cs
```

```
using EPDM.Interop.epdm;
using System.Windows.Forms;

namespace RefItemContainerCSharp
{
    class Callback : IEdmUnlockOpCallback
    {
        #region IEdmUnlockOpCallback Members
```

```
        public EdmUnlockOpReply MsgBox(EdmUnlockOpMsg mssge, int docId, int projID, string path, ref EdmUnlockErrInfo err)
        {
            return EdmUnlockOpReply.Euor_OK;
        }

        public void ProgressBegin(EdmProgressType type, EdmUnlockEvent events, int steps)
        {
            return;
        }

        public void ProgressEnd(EdmProgressType type)
        {
            //Demonstrates callback
            MessageBox.Show("ProgressEnd called.");
            return;
        }

        public bool ProgressStep(EdmProgressType type, string msgText, int progressPos)
        {
            return true;
        }

        public bool ProgressStepEvent(EdmProgressType type, EdmUnlockEventMsg opText, int progressPos)
        {
            return true;
        }

        #endregion

    }
}
```

```
Back to top
```
