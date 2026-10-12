---
title: "Get and Set Item References Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Get_and_Set_Item_References_Example_CSharp.htm"
---

# Get and Set Item References Example (C#)

This example shows how to get and set item references.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio 2010.
 //    a. Click File > New > Project > Visual C# > Windows Forms Application.
 //    b. Type ItemRefs_CSharp in Name.
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
 // 5. Ensure that an item folder with at least one item is checked into the vault.
 // 6. Click Debug > Start Debugging or press F5.
 //
 // Postconditions:
 // 1. Displays the Get and set item references dialog box.
 // 2. Select a vault view.
 // 3. Click Get item references.
 //    a. Click an item folder in the vault.
 //    b. Click OK.
 //    c. Displays a message box confirming your folder selection.
 //    d. Click OK.
 //    e. Displays a message box with item references for the first item found
 //       in the selected folder.
 //    f. Click OK.
 // 4. Click Set item references.
 //    a. Click one or more files to add as references to the item.
 //    b. Click Open.
 //    c. Displays a message box with the updated references.
 //       - or -
 //       Displays a message box with errors.
 //    d. Click OK.
 // 5. Close the Get and set item references dialog box.
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

 namespace ItemRefs_CSharp
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }
         private IEdmVault5 vault1 = null;
         IEdmItem item;

         IEdmFile8 fileInt;

         public void Form1_Load(System.Object sender, System.EventArgs e)
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

                 Button1.Enabled = false;

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

         public void GetItemRefs_Click(System.Object sender, System.EventArgs e)
         {

             try
             {
                 IEdmVault11 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault11)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     //Log into selected vault as the current user
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 IEdmFolder6 folder = default(IEdmFolder6);
                 folder = (IEdmFolder6)vault2.BrowseForFolder2(this.Handle.ToInt32(), "Select a folder", vault2.RootFolder, (int)EdmBrowseForFolderFlag.EdmBwsFld_None);
                 if ((folder != null))
                 {
                     if (folder.ObjectType == EdmObjectType.EdmObject_Folder)
                     {
                         Interaction.MsgBox("You selected the file folder: " + Constants.vbLf + folder.LocalPath);
                     }
                     else
                     {
                         Interaction.MsgBox("You selected the item folder: " + Constants.vbLf + folder.LocalPath);
                     }
                 }

                 //Get the first item in the selected folder
                 IEdmPos5 pos = default(IEdmPos5);
                 string msg = null;

                 pos = folder.GetFirstFilePosition();
                 fileInt = (IEdmFile8)folder.GetNextFile(pos);

                 //Search for item by name to get its ID
                 IEdmSearch7 search = default(IEdmSearch7);
                 search = (IEdmSearch7)vault2.CreateUtility(EdmUtility.EdmUtil_Search);
                 search.FindFiles = true;
                 search.FindFolders = false;
                 search.Recursive = true;
                 search.SetToken(EdmSearchToken.Edmstok_FindItems, true);
                 search.StartFolderID = vault2.ItemRootFolderID;
                 search.FileName = fileInt.Name;

                 IEdmSearchResult5 result = default(IEdmSearchResult5);
                 result = search.GetFirstResult();

                 if (result == null)
                 {
                     Interaction.MsgBox("The item '" + fileInt.Name + "' was not found.");
                 }

                 while ((result != null))
                 {
                     if ((result.IsKindOf(EdmObjectType.EdmObject_Item)))
                     {
                         fileInt = (IEdmFile8)result;
                         item = (IEdmItem)fileInt;

                         //Create a message about the item and its references
                         msg = "Name=" + item.Name + Constants.vbLf;
                         msg = msg + "ID = " + item.ID.ToString() + Constants.vbLf;
                         msg = msg + "Descriptive name = " + item.ItemDescriptiveName + Constants.vbLf;
                         msg = msg + "Check-out path = " + fileInt.LockPath + Constants.vbLf;
                         msg = msg + "Workflow state = " + fileInt.CurrentState.Name + Constants.vbLf;
                         msg = msg + Constants.vbLf + "Referenced files:" + Constants.vbLf;

                         EdmItemRef[] refs = null;
                         item.GetReferences((int)EdmRefFlags.EdmRef_Dynamic + (int)EdmRefFlags.EdmRef_Static + (int)EdmRefFlags.EdmRef_Item + (int)EdmRefFlags.EdmRef_File, out refs);

                         int idx = 0;
                         idx = Information.LBound(refs);

                         while ((idx <= Information.UBound(refs)))
                         {
                             msg = msg + "File ID=(" + Convert.ToString(refs[idx].moNamePathOrID) + ") ";
                             msg = msg + "Parent Item ID=(" + Convert.ToString(refs[idx].moParentNamePathOrItemID) + ") ";
                             msg = msg + "Configuration='" + refs[idx].mbsConfiguration + "' ";

                             if ((refs[idx].mlEdmRefFlags & (int)EdmRefFlags.EdmRef_Dynamic) == (int)EdmRefFlags.EdmRef_Dynamic)
                             {
                                 msg = msg + " (auto-update reference)";
                             }
                             else
                             {
                                 if ((refs[idx].mlEdmRefFlags & (int)EdmRefFlags.EdmRef_Static) == (int)EdmRefFlags.EdmRef_Static)
                                 {
                                     msg = msg + " (static reference)";
                                 }
                             }
                             idx = idx + 1;
                             msg = msg + Constants.vbLf;
                         }

                         MessageBox.Show(msg);
                         Button1.Enabled = true;

                     }
                     return;
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

         private void Button1_Click(System.Object sender, System.EventArgs e)
         {
             //Set item references

             try
             {
                 IEdmVault11 vault2 = null;
                 if (vault1 == null)
                 {
                     vault1 = new EdmVault5();
                 }
                 vault2 = (IEdmVault11)vault1;
                 if (!vault1.IsLoggedIn)
                 {
                     vault1.LoginAuto(VaultsComboBox.Text, this.Handle.ToInt32());
                 }

                 //Get the current item references
                 EdmItemRef[] oldRefs = null;
                 item.GetReferences((int)EdmRefFlags.EdmRef_Dynamic + (int)EdmRefFlags.EdmRef_Static + (int)EdmRefFlags.EdmRef_Item + (int)EdmRefFlags.EdmRef_File, out oldRefs);

                 //Let the user browse for new file references
                 IEdmStrLst5 pathList = vault2.BrowseForFile(this.Handle.ToInt32(), (int)EdmBrowseFlag.EdmBws_ForOpen + (int)EdmBrowseFlag.EdmBws_PermitVaultFiles + (int)EdmBrowseFlag.EdmBws_PermitMultipleSel, "All Files|*.*||");

                 if (pathList == null)
                     return;

                 //Create an array of new item references
                 EdmItemRef[] newRefs = new EdmItemRef[pathList.Count];
                 int idx = 0;
                 IEdmPos5 pos = default(IEdmPos5);
                 pos = pathList.GetHeadPosition();

                 while (!pos.IsNull)
                 {
                     string path = null;
                     path = pathList.GetNext(pos);
                     newRefs[idx].moNamePathOrID = path;
                     newRefs[idx].mlEdmRefFlags = (int)EdmRefFlags.EdmRef_Static + (int)EdmRefFlags.EdmRef_File;
                     newRefs[idx].moParentNamePathOrItemID = item.ID;
                     idx = idx + 1;
                 }

                 //Check out the item
                 fileInt.LockFile(vault2.ItemRootFolderID, this.Handle.ToInt32());

                 //Update the item references
                 item.UpdateReferences(newRefs, oldRefs);

                 //Collect all errors
                 string msg = "";
                 string errstr = "";
                 idx = Information.LBound(newRefs);

                 while ((idx <= Information.UBound(newRefs)))
                 {
                     if (newRefs[idx].mhResult != 0)
                     {
                         errstr = vault2.GetErrorName(newRefs[idx].mhResult);
                         msg = msg + "Failed to save ref: '" + Convert.ToString(newRefs[idx].moNamePathOrID) + "' (" + errstr + ")" + Constants.vbLf;
                     }
                     idx = idx + 1;
                 }

                 idx = Information.LBound(oldRefs);

                 while ((idx <= Information.UBound(oldRefs)))
                 {
                     if (oldRefs[idx].mhResult != 0)
                     {
                         errstr = vault2.GetErrorName(oldRefs[idx].mhResult);
                         msg = msg + "Failed to delete ref: '" + Convert.ToString(oldRefs[idx].moNamePathOrID) + "' (" + errstr + ")" + Constants.vbLf;
                     }
                     idx = idx + 1;
                 }

                 //Display a status message
                 if (string.IsNullOrEmpty(msg))
                 {
                     msg = "Updated references successfully!" + Constants.vbLf;

                     EdmItemRef[] refs = null;
                     item.GetReferences((int)EdmRefFlags.EdmRef_Dynamic + (int)EdmRefFlags.EdmRef_Static + (int)EdmRefFlags.EdmRef_Item + (int)EdmRefFlags.EdmRef_File, out refs);
                     idx = Information.LBound(refs);

                     //Construct a message about the reference updates

                     while ((idx <= Information.UBound(refs)))
                     {
                         msg = msg + "File ID=(" + Convert.ToString(refs[idx].moNamePathOrID) + ") ";
                         msg = msg + "Parent Item ID=(" + Convert.ToString(refs[idx].moParentNamePathOrItemID) + ") ";
                         msg = msg + "Configuration='" + refs[idx].mbsConfiguration + "' ";

                         if ((refs[idx].mlEdmRefFlags & (int)EdmRefFlags.EdmRef_Dynamic) == (int)EdmRefFlags.EdmRef_Dynamic)
                         {
                             msg = msg + " (auto-update reference)";
                         }
                         else
                         {
                             if ((refs[idx].mlEdmRefFlags & (int)EdmRefFlags.EdmRef_Static) == (int)EdmRefFlags.EdmRef_Static)
                             {
                                 msg = msg + " (static reference)";
                             }
                         }
                         idx = idx + 1;
                         msg = msg + Constants.vbLf;
                     }

                     MessageBox.Show(msg);
                 }
                 else
                 {
                     MessageBox.Show("Errors detected: " + Constants.vbLf + msg);
                 }

                 //Check in the item
                 fileInt.UnlockFile(this.Handle.ToInt32(), "Updated item references", (int)EdmUnlockFlag.EdmUnlock_IgnoreRefsNotLockedByCaller);

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
 namespace ItemRefs_CSharp
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
             this.GetItemRefs = new System.Windows.Forms.Button();
             this.OpenFileDialog = new System.Windows.Forms.OpenFileDialog();
             this.Button1 = new System.Windows.Forms.Button();
             this.SuspendLayout();
             //
             //VaultsLabel
             //
             this.VaultsLabel.AutoSize = true;
             this.VaultsLabel.Location = new System.Drawing.Point(13, 26);
             this.VaultsLabel.Name = "VaultsLabel";
             this.VaultsLabel.Size = new System.Drawing.Size(94, 13);
             this.VaultsLabel.TabIndex = 0;
             this.VaultsLabel.Text = " Select vault view:";
             //
             //VaultsComboBox
             //
             this.VaultsComboBox.FormattingEnabled = true;
             this.VaultsComboBox.Location = new System.Drawing.Point(16, 42);
             this.VaultsComboBox.Name = "VaultsComboBox";
             this.VaultsComboBox.Size = new System.Drawing.Size(121, 21);
             this.VaultsComboBox.TabIndex = 1;
             //
             //GetItemRefs
             //
             this.GetItemRefs.Location = new System.Drawing.Point(16, 86);
             this.GetItemRefs.Name = "GetItemRefs";
             this.GetItemRefs.Size = new System.Drawing.Size(139, 23);
             this.GetItemRefs.TabIndex = 5;
             this.GetItemRefs.Text = "Get item references...";
             this.GetItemRefs.UseVisualStyleBackColor = true;
             this.GetItemRefs.Click +=new System.EventHandler(GetItemRefs_Click);
             //
             //OpenFileDialog
             //
             this.OpenFileDialog.Title = "Open";
             //
             //Button1
             //
             this.Button1.Location = new System.Drawing.Point(16, 127);
             this.Button1.Name = "Button1";
             this.Button1.Size = new System.Drawing.Size(139, 23);
             this.Button1.TabIndex = 6;
             this.Button1.Text = "Set item references...";
             this.Button1.UseVisualStyleBackColor = true;
             this.Button1.Click +=new System.EventHandler(Button1_Click);
             //
             //Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(317, 185);
             this.Controls.Add(this.Button1);
             this.Controls.Add(this.GetItemRefs);
             this.Controls.Add(this.VaultsComboBox);
             this.Controls.Add(this.VaultsLabel);
             this.Name = "Form1";
             this.Text = "Get and set item references";
             this.Load += new System.EventHandler(this.Form1_Load);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         internal System.Windows.Forms.Label VaultsLabel;
         internal System.Windows.Forms.ComboBox VaultsComboBox;
         internal System.Windows.Forms.Button GetItemRefs;
         internal System.Windows.Forms.OpenFileDialog OpenFileDialog;
         internal System.Windows.Forms.Button Button1;
     }
 }
```

[Back to top](#top)
