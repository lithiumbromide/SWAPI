---
title: "Creating Menu Commands (C#)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/csharpmenuitem.htm"
---

# Creating Menu Commands (C#)

This topic shows how to create a C# add-in that adds menu commands to the context-sensitive menus of File Explorer vault views.

**NOTE:** Because SOLIDWORKS PDM Professional cannot force a reload of add-ins if they are written in .NET, all client machines must be restarted to ensure that the latest version of the add-in is used.

1. Start Microsoft Visual Studio.
2. Select **File >** **New >** **Project > C#, Windows, Library.**
3. Select **Class Library (.NET Framework)** as the template.
4. In the **.NET Framework** dropdown, keep the default version (recommended) or select another version. See [Using .NET Framework for Add-in Applications](Using_NET_Framework_in_Addins.htm) for more information.
5. Enter **Project n****ame, Solution, and Solution name.**
6. For **Location**, click **Browse****...** and navigate to the folder where to create the project.
7. Click **Create**.
8. Right-click the project name in the Solution Explorer and click **Add > Reference**.

  1. Click **Browse...** in the left-side panel, navigate to and select **EPDM.Interop.epdm.dll**, and click **OK**.
  2. Right-click **E****pdm.Interop.epdm** in the Solution Explorer, select **Properties**, and set **Embed Interop Types** to **False** to handle methods that pass arrays of structures.
  3. Click **Assemblies > Framework** in the left-hand panel, select **System.Windows.Forms**, and click **OK**.
9. Right-click the project name in the Solution Explorer and click **Properties**.

  1. On the Application tab, click **Assembly Information****...**.
  2. De-select **Make assembly COM-Visible****. Click OK.**
  3. ##### On the Build tab, select Any CPU for Platform target, de-select Prefer 32-bit , and select Register for COM interop .
10. Save the project.
11. Double-click **Class1.cs** in the Solution Explorer to open the code window.
12. At the top of the code window, type:

  ```vb
   using EPDM.Interop.epdm;
   using System.Runtime.InteropServices;
   using System.Windows.Forms;
  ```
13. Replace**:**

  ```
  public class Class1
  ```

  with:

  ```vb
   [Guid(""), ComVisible(true)]
   public class Class1 : IEdmAddIn5
  ```
14. To populate the GUID attribute above, click **Tools > Create GUID** in the IDE, select GUID Format 5, click **Copy**, and click **Exit**. Populate [Guid(""), ...] with the copied string.
15. Implement [IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html) by adding the following code to Class1:
16. [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) is called when a menu command is selected by the user. Implement IEdmAddIn5::OnCmd by adding the following code to Class1:
17. Click **Build > Build Solution** to build the add-in.
18. Install the add-in through the SOLIDWORKS PDM Professional Administration tool:

  1. Open the SOLIDWORKS PDM Professional Administration tool.
  2. Expand the vault where you want to install this add-in and log in as Admin.
  3. Right-click **Add-ins** and click **New Add-in**.
  4. Browse to `project_path``\``project_name\project_name`**\bin\Debug**, click `project_name`**.dll** and **EPDM.Interop.**e**pdm.dll**.
  5. Click **Open**.
  6. Click **OK**.
  7. Click **OK**.
19. Right-click inside a vault view in File Explorer. **First command** appears in the context-sensitive menu.
20. Right-click a file in the vault view and click **Second command**. The add-in displays a dialog similar to the following:

### Complete Source Code

##### // Class1.cs

```vb
 using System;
 using System.Collections.Generic;
 using System.Text;
 using EPDM.Interop.epdm;
  using System.Runtime.InteropServices;

 namespace CreateMenuCommand_CSharp
 {
     [Guid(""), ComVisible(true)]    // See step 13 above to create the GUID
     public class Class1 : IEdmAddIn5
     {
         #region IEdmAddIn5 Members

         public void GetAddInInfo(ref EdmAddInInfo poInfo, IEdmVault5 poVault, IEdmCmdMgr5 poCmdMgr)
         {

             poInfo.mbsAddInName = "Menu command sample";
             poInfo.mbsCompany = "SOLIDWORKS Corporation";
             poInfo.mbsDescription = "Adds menu command items";
             poInfo.mlAddInVersion = 1;
             poInfo.mlRequiredVersionMajor = 5;
             poInfo.mlRequiredVersionMinor = 2;

             poCmdMgr.AddCmd(1000, "First command", (int)EdmMenuFlags.EdmMenu_Nothing, "This is the first command", "First command", 0, 99);
             poCmdMgr.AddCmd(1001, "Second command", (int)EdmMenuFlags.EdmMenu_MustHaveSelection, "This is the second command", "Second command", 1, 99);
         }

         public void OnCmd(ref EdmCmd poCmd, ref EdmCmdData[] ppoData)
         {

             {
                 string CommandName = null;
                 if (poCmd.mlCmdID == 1000)
                 {
                     CommandName = "The first command.";
                 }
                 else
                 {
                     CommandName = "The second command.";
                 }

                 int index = 0;
                 int last = 0;
                 index = ppoData.GetLowerBound(0);
                last = ppoData.GetUpperBound(0);
                 string StrID = null;

                 string message = null;
                 message = "You have selected the following files and folders: " + "\r\n";
                 while (index <= last)
                 {
                     if (((EdmCmdData)ppoData.GetValue(index)).mlObjectID1 == 0)
                     {
                         message = message + "Folder: (ID=";
                         StrID = ((EdmCmdData)ppoData.GetValue(index)).mlObjectID2.ToString();
                         message = message + StrID + ") ";
                     }
                     else
                     {
                         message = message + "File: (ID=";
                         StrID = ((EdmCmdData)ppoData.GetValue(index)).mlObjectID1.ToString();
                         message = message + StrID + ") ";
                     }

                     message = message + ((EdmCmdData)ppoData.GetValue(index)).mbsStrData1 + "\r\n";
                     index = index + 1;
                 }

                 EdmVault5 v = default(EdmVault5);
                 v = (EdmVault5)poCmd.mpoVault;
                 v.MsgBox(poCmd.mlParentWnd, message, EdmMBoxType.EdmMbt_OKOnly, CommandName);
             }
         }

         #endregion
     }
 }
```
