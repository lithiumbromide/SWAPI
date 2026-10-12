---
title: "Create Vault View Tab Add-in Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Create_Vault_View_Tab_Addin_Example_CSharp.htm"
---

# Create Vault View Tab Add-in Example (C#)

This example shows how to create an add-in that adds a custom tab to the bottom panel of a vault view when it is opened in File Explorer.

```vb
 //--------------------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 // 2. Click File > New > Project > Visual C# > Class Library (.NET Framework).
 // 3. Type SWEPDMAddin1 in Name.
 // 4. Click Browse and navigate to the folder where to create the project.
 // 5. Click OK.
 // 6. Right-click the project name in the Solution Explorer and select Add > Reference.
 // 7. In the Reference Manager dialog:
 //    a. Click the Browse tab.
 //    b. Click Browse at the bottom.
 //    c. Navigate to the SOLIDWORKS PDM Client installation folder.
 //    d. Select EPDM.Interop.epdm.dll and click Add.
 //    e. Ensure that EPDM.Interop.epdm.dll is checked in the Reference Manager dialog.
 //    f. Click OK.
 // 8. Right-click the project name in the Solution Explorer and select Properties.
 // 9. In the Properties window:
 //    a. On the Application tab, click Assembly Information.
 //    b. De-select Make assembly COM-Visible.
 //    c. On the Build tab, select Any CPU, de-select Prefer 32-bit, and select  Register for COM interop.
 //10. Save the project.
 //11. Copy SWEPDMADDin1 code to a new class, SWEPDMAddin1.cs.
 //12. Right-click the project and select Add > User Control.
 //13. Type "UserControl1.cs" in Name and click Add.
 //14. Copy UserControl1 code to the code behind UserControl1.cs.
 //15. Copy UserControl1.Designer code to UserControl1.Designer.cs.
 //16. To populate the GUID attribute in SWEPDMAddin1.cs:
 //    a. Click Tools > Create GUID in the IDE.
 //    b. Select GUID Format 5.
 //    c. Click Copy.
 //    d. Click Exit.
 //    e. Populate Guid("") in the code with the copied string.
 //17. Copy a *.png file to the project folder.
 //18. Right-click the project and select Add > Existing item.
 //19. Select the *.png file and click Add.
 //20. Right-click the *.png file in Solution Explorer and select  Exclude from Project.
 //21. Replace the png_path in SWEPDMAddin1.cs with the full path name of the *.png
 //    you just added to the project.
 //22. Click Build > Build Solution.
 //23. Ensure you have a vault, a vault view, and a file in the vault.
 //
// Postconditions:
 // 1. Open the SOLIDWORKS PDM Professional Administration tool, expand a vault_name node,
 //    and log in as Admin.
 // 2. Under vault_name, right-click Add-ins, and click New Add-in.
 //    a. Navigate to the bin\Debug directory of your SWEPDMAddin1 project.
 //    b. Click SWEPDMAddin1.dll.
 //    c. Click Open.
 //    d. Click OK.
 // 3. Click OK after reading the SOLIDWORKS PDM Professional warning dialog.
 // 4. In the taskbar, click the Administration tool icon and click Log Off > vault_name.
 // 5. Open File Explorer on a view of vault_name:
 //    a. Log in as Admin.
 //    b. Click UserTab1 in the bottom panel of the vault view.
 //       One or more message boxes display. Click OK in the message boxes.
 //    c. Select a file in the vault.
 //       The custom tab's text box is populated with the name of the file.
 //    d. Right-click the file in the vault.
 //    e. Select Test menu item #1.
 //    f. Click OK in the message box.
 //---------------------------------------------------------------------------------------

 //SWEPDMADDin1
 using System;
 using System.Collections.Generic;
 using System.Diagnostics;
 using EPDM.Interop.epdm;
 using System.Runtime.InteropServices;

 namespace SWEPDMAddin1
 {
     [Guid(""), ComVisible(true)]
     public class SWPDMAddin : IEdmAddIn5
     {
         Dictionary<string, UserControl1> ControlMaps = new Dictionary<string, UserControl1>();
         static long Identifier = 1;
         public void GetAddInInfo(ref EdmAddInInfo poInfo, IEdmVault5 poVault, IEdmCmdMgr5 poCmdMgr)
         {
             //Add-in information
             poInfo.mbsAddInName = "SWPDMAddin1";
             poInfo.mbsCompany = "your_company_name";
             poInfo.mbsDescription = "This add-in adds a tab to the bottom panel of the vault view before it is opened in File Explorer. It also adds context-sensitive menu items to the right-click menus of files in the vault.";
             poInfo.mlAddInVersion = 1;

             //Minimum Conisio version needed for .Net add-Ins is 6.4
             poInfo.mlRequiredVersionMajor = 6;
             poInfo.mlRequiredVersionMinor = 4;

             //Adds context-sensitive menu items to the right-click menus of files in the vault
             poCmdMgr.AddCmd(1, "Test menu item #1", (int)EdmMenuFlags.EdmMenu_Nothing, "", "", 0, 0);
             poCmdMgr.AddCmd(1, "Test menu item #2", (int)EdmMenuFlags.EdmMenu_Nothing, "", "", 0, 0);

             AddAllHooks(poCmdMgr);

         }

         public void OnCmd(ref EPDM.Interop.epdm.EdmCmd poCmd, ref EdmCmdData[] ppoData)
         {
             Debug.Print("Command Type: " + poCmd.meCmdType.ToString() + "\n  " + System.DateTime.Now.ToString());

             IEdmVault5 edmVault = poCmd.mpoVault as IEdmVault5;

             try
             {
                 switch (poCmd.meCmdType)

                 {
                     case EdmCmdType.EdmCmd_CardButton:
                         break;
                     case EdmCmdType.EdmCmd_CardInput:
                         break;
                     case EdmCmdType.EdmCmd_CardListSrc:
                         break;
                     case EdmCmdType.EdmCmd_InstallAddIn:
                         break;
                     case EdmCmdType.EdmCmd_Menu:
                         //File's right-click menu item is selected
                         edmVault.MsgBox(0, " Context-sensitive menu item selected", EdmMBoxType.EdmMbt_OKOnly, "PDM Pro add-in");
                         break;
                     case EdmCmdType.EdmCmd_PostAdd:
                         break;
                     case EdmCmdType.EdmCmd_PostAddFolder:
                         break;
                     case EdmCmdType.EdmCmd_PostCopy:
                         break;
                     case EdmCmdType.EdmCmd_PostCopyFolder:
                         break;
                     case EdmCmdType.EdmCmd_PostDelete:
                         break;
                     case EdmCmdType.EdmCmd_PostDeleteFolder:
                         break;
                     case EdmCmdType.EdmCmd_PostGet:
                         break;
                     case EdmCmdType.EdmCmd_PostLock:
                         break;
                     case EdmCmdType.EdmCmd_PostMove:
                         break;
                     case EdmCmdType.EdmCmd_PostMoveFolder:
                         break;
                     case EdmCmdType.EdmCmd_PostRename:
                         break;
                     case EdmCmdType.EdmCmd_PostRenameFolder:
                         break;
                     case EdmCmdType.EdmCmd_PostShare:
                         break;
                     case EdmCmdType.EdmCmd_PostState:
                         break;
                     case EdmCmdType.EdmCmd_PostUndoLock:
                         break;
                     case EdmCmdType.EdmCmd_PostUnlock:
                         break;
                     case EdmCmdType.EdmCmd_PreAdd:
                         break;
                     case EdmCmdType.EdmCmd_PreAddFolder:
                         break;
                     case EdmCmdType.EdmCmd_PreCopy:
                         break;
                     case EdmCmdType.EdmCmd_PreCopyFolder:
                         break;
                     case EdmCmdType.EdmCmd_PreDelete:
                         break;
                     case EdmCmdType.EdmCmd_PreDeleteFolder:
                         break;
                     case EdmCmdType.EdmCmd_PreGet:
                         break;
                     case EdmCmdType.EdmCmd_PreLock:
                         break;
                     case EdmCmdType.EdmCmd_PreMove:
                         break;
                     case EdmCmdType.EdmCmd_PreMoveFolder:
                         break;
                     case EdmCmdType.EdmCmd_PreRename:
                         break;
                     case EdmCmdType.EdmCmd_PreRenameFolder:
                         break;
                     case EdmCmdType.EdmCmd_PreShare:
                         break;
                     case EdmCmdType.EdmCmd_PreState:
                         break;
                     case EdmCmdType.EdmCmd_PreUndoLock:
                         break;
                     case EdmCmdType.EdmCmd_PreUnlock:
                         break;
                     case EdmCmdType.EdmCmd_SerialNo:
                         break;
                     case EdmCmdType.EdmCmd_UninstallAddIn:
                         break;
                     case EdmCmdType.EdmCmd_TaskDetails:
                         break;
                     case EdmCmdType.EdmCmd_PreExploreInit:
                         {
                             // File Explorer is about to be opened
                             IEdmCmdMgr6 poCmdMgr6 = poCmd.mpoExtra as IEdmCmdMgr6;
                             UserControl1 myControl1 = new UserControl1();
                             // Add a custom tab to the bottom panel of the vault view
                             poCmdMgr6.AddVaultViewTab(myControl1.Handle.ToInt64(), "UserTab1", @"png_path", "UserTab1", Identifier.ToString());
                             ControlMaps.Add(Identifier.ToString(), myControl1);
                             Identifier++;

                             break;
                         }
                     case EdmCmdType.EdmCmd_SelectItem:
                         {
                             // If a file is selected, populate the textBox1 control
                             EdmCmdData poobject = (EdmCmdData)ppoData.GetValue(0);
                             string Id = poobject.mbsStrData3;
                             UserControl1 myControl;
                             bool exist = ControlMaps.TryGetValue(Id, out myControl);
                             if (exist)
                             {
                                 if (poobject.mbsStrData1.Length != 0)
                                     myControl.SetFileName(poobject.mbsStrData1);
                                 else
                                     myControl.SetFileName(poobject.mbsStrData2);
                             }
                             break;
                         }

                     case EdmCmdType.EdmCmd_DeSelectItem:
                         {
                             // If a file is de-selected, empty the textBox1 control
                             EdmCmdData poobject = (EdmCmdData)ppoData.GetValue(0);
                             string Id = poobject.mbsStrData3;
                             UserControl1 myControl;
                             bool exist = ControlMaps.TryGetValue(Id, out myControl);
                             if (exist)
                             {
                                 myControl.SetFileName("");
                             }
                             break;
                         }
                     case EdmCmdType.EdmCmd_UserTabDelete:
                         {
                             // When File Explorer is closed, this event is called; perform cleanup here
                             EdmCmdData poobject = (EdmCmdData)ppoData.GetValue(0);
                             string Id = poobject.mbsStrData3;
                             ControlMaps.Remove(Id);
                             break;
                         }
                     case EdmCmdType.EdmCmd_ActivateAPITab:
                         {
                             // UserTab1 is selected
                             edmVault.MsgBox(0, " UserTab1 selected", EdmMBoxType.EdmMbt_OKOnly, "PDM Pro add-in");
                             break;
                         }
                     default:
                         break;
                 }
             }
             catch (COMException exp)
             {
                 string errorName, errorDesc;
                 edmVault.GetErrorString(exp.ErrorCode, out errorName, out errorDesc);
                 edmVault.MsgBox(0, errorDesc, EdmMBoxType.EdmMbt_OKOnly, errorName);
             }
         }

         void AddAllHooks(IEdmCmdMgr5 poCmdMgr)
         {
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_CardButton, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_CardInput, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_CardListSrc, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_InstallAddIn, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_Menu, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostAdd, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostAddFolder, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostCopy, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostCopyFolder, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostDelete, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostDeleteFolder, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostGet, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostLock, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostMove, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostMoveFolder, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostRename, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostRenameFolder, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostShare, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostState, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostUndoLock, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostUnlock, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreAdd, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreAddFolder, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreCopy, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreCopyFolder, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreDeleteFolder, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreGet, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreLock, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreMove, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreMoveFolder, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreRename, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreRenameFolder, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreShare, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreState, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreUndoLock, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreUnlock, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_SerialNo, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreExploreInit, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_UninstallAddIn, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskDetails, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_SelectItem, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_DeSelectItem, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_ActivateAPITab, null);
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_UserTabDelete, null);

         }
     }

 }
```

[Back to top](#top)

//UserControl1.Designer

```vb
 namespace SWEPDMAddin1
 {
     partial class UserControl1
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

         #region Component Designer generated code

         /// <summary>
         /// Required method for Designer support - do not modify
         /// the contents of this method with the code editor.
         /// </summary>
         private void InitializeComponent()
         {
             this.textBox1 = new System.Windows.Forms.TextBox();
             this.label1 = new System.Windows.Forms.Label();
             this.label2 = new System.Windows.Forms.Label();
             this.SuspendLayout();
             //
             // textBox1
             //
             this.textBox1.Location = new System.Drawing.Point(128, 42);
             this.textBox1.Name = "textBox1";
             this.textBox1.Size = new System.Drawing.Size(414, 20);
             this.textBox1.TabIndex = 4;
             //
             // label1
             //
             this.label1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
             | System.Windows.Forms.AnchorStyles.Left)
             | System.Windows.Forms.AnchorStyles.Right)));
             this.label1.AutoSize = true;
             this.label1.Location = new System.Drawing.Point(3, 0);
             this.label1.Name = "label1";
             this.label1.Size = new System.Drawing.Size(54, 13);
             this.label1.TabIndex = 5;
             this.label1.Text = "UserTab1";
             //
             // label2
             //
             this.label2.AutoSize = true;
             this.label2.Location = new System.Drawing.Point(47, 45);
             this.label2.Name = "label2";
             this.label2.Size = new System.Drawing.Size(75, 13);
             this.label2.TabIndex = 6;
             this.label2.Text = "Selected Item ";
             //
             // UserControl1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.Controls.Add(this.label2);
             this.Controls.Add(this.label1);
             this.Controls.Add(this.textBox1);
             this.Name = "UserControl1";
             this.Size = new System.Drawing.Size(559, 243);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion
         private System.Windows.Forms.TextBox textBox1;
         private System.Windows.Forms.Label label1;
         private System.Windows.Forms.Label label2;
     }
 }
 Back to top
```

//UserControl1

```vb
 using System;
 using System.Collections.Generic;
 using System.ComponentModel;
 using System.Drawing;
 using System.Data;
 using System.Text;
 using System.Windows.Forms;

 namespace SWEPDMAddin1
 {
     public partial class UserControl1 : UserControl
     {
         public UserControl1()
         {
             InitializeComponent();
         }

         public void SetFileName(string strFileName)
         {

             textBox1.Text = strFileName;
         }

     }
 }

 Back to top
```
