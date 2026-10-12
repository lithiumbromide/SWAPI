---
title: "Creating Menu Commands (VB.NET)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/vbmenuitem.htm"
---

# Creating Menu Commands (VB.NET)

This topic shows how to create a VB.NET add-in in Microsoft Visual Studio that adds menu commands to the context-sensitive and Tools menus of vaults in File Explorer.

**NOTE:** Because SOLIDWORKS PDM Professional cannot force a reload of add-ins if they are written in .NET, all client machines must be restarted to ensure that the latest version of the add-in is used.

1. Start Microsoft Visual Studio.
2. Click **File >** **New** **>** **Project > Visual Basic, Windows, Library**.
3. Select **Class Library** **(.NET Framework)** as the template.
4. Enter **Project** **n****ame, Location, Solution, Solution name,** and click **Create**.
5. From the VS menu, click **Project > Add Reference... >** **Browse...**, locate and select **EPDM.Interop.epdm.dll**, and click **OK**.
6. From the Solution Explorer, right-click **E****pdm.Interop.epdm**, select **Properties**, and set **Embed Interop Types** to **False** to handle methods that pass arrays of structures.
7. From the VS menu, click **Project > Add Reference... >** **Assemblies > Framework**, select **System.Drawing,** and click **OK**.
8. Right-click the name of the project in the Solution Explorer and select **Properties**.

  1. On the Application tab, click **Assembly Information....**
  2. De-select **Make assembly COM-Visible****. Click OK.**
  3. ##### On the Compile tab, select AnyCPU for the Target CPU, de-select Prefer 32-bit , and select Register for COM interop .
9. Save the project.
10. Double-click **Class1.vb** in the Solution Explorer to open the code window.

  1. Before **Public Class Class1** type:

    **Imports EPDM.Interop.epdm**
    **Imports System.Runtime.InteropServices**
    <Guid("")> _
    <ComVisible(True)> _
  2. To populate the GUID attribute above, click **Tools > Create GUID** in the IDE, select GUID Format 6, click **Copy**, and click **Exit**. Replace <Guid("")> with the copied string.
  3. Type **Implements IEdmAddIn5** after **Public Class Class1** and make sure that the GetAddInInfo and OnCmd methods are generated after you press **Enter**.
  4. Replace your add-in's implementation of the [IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html) method with the following code:

  Public Sub GetAddInInfo(ByRef poInfo As EdmAddInInfo, ByVal poVault As EIEdmVault5, ByVal poCmdMgr As IEdmCmdMgr5) Implements IEdmAddIn5.GetAddInInfo

  'Specify the add-in information
  poInfo.mbsAddInName = "Menu command sample"
  poInfo.mbsCompany = "SOLIDWORKS Corporation"
  poInfo.mbsDescription = "Adds menu command items"
  poInfo.mlAddInVersion = 1
  poInfo.mlRequiredVersionMajor = 5
  poInfo.mlRequiredVersionMinor = 2

  'Add menu command items (the command-ID numbers 1000 and 1001 are
  'arbitrary; PDM does not use them; instead, PDM only passes them to the
  'implementation of OnCmd to know which command was selected)
  poCmdMgr.AddCmd(1000, "First command", EdmMenuFlags.EdmMenu_Nothing, "This is the first command", "First command", 0, 99)
  poCmdMgr.AddCmd(1001, "Second command", EdmMenuFlags.EdmMenu_MustHaveSelection, "This is the second command", "Second command", 1, 99)

  End Sub

  The flag [EdmMenuFlags.EdmMenu_MustHaveSelection](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMenuFlags.html) means that the second command is only available if the user has selected one or more files or folders.

  1. Replace your add-in's implementation of the [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) method with the following code (IEdmAddIn5::OnCmd is called when a menu command is selected by the user):

  Public Sub OnCmd(ByRef poCmd As EdmCmd, ByRef ppoData As EdmCmdData()) Implements IEdmAddIn5.OnCmd

  'Check the command ID to see which command was selected
  '(This only affects the caption of the message box below)
  Dim CommandName As String

  If poCmd.mlCmdID = 1000 Then
  CommandName = "The first command."

  Else
  CommandName = "The second command."

  End If

  'Retrieve the bounds of the array containing the selected files and folders
  Dim index As Long

  Dim last As Long

  index = LBound(ppoData)

  last = UBound(ppoData)

  Dim StrID As String

  'Create a message showing the names and IDs of all selected files and folders
  Dim message As String

  message = "You have selected the following files and folders: " + vbLf

  While index <= last
  If ppoData(index).mlObjectID1 = 0 Then
  message = message + "Folder: (ID="

  StrID = ppoData(index).mlObjectID2

  message = message + StrID + ") "
  Else
  message = message + "File: (ID="

  StrID = ppoData(index).mlObjectID1

  message = message + StrID + ") "
  End If

  message = message + ppoData(index).mbsStrData1 + vbLf
  index = index + 1
  End While

  'Display the message
  Dim v As EdmVault5
  v = poCmd.mpoVault
  v.MsgBox(poCmd.mlParentWnd, message, EdmMBoxType.EdmMbt_OKOnly, CommandName)

  End Sub
11. Click **Build > Build Solution** to build the add-in.
12. Install the add-in through the SOLIDWORKS PDM Professional Administration tool:

  1. Open the SOLIDWORKS PDM Professional Administration tool.
  2. Expand the vault where you want to install this add-in and log in as Admin.
  3. Right-click **Add-ins** and click **New Add-in**.
  4. Browse to `project_path``\``project_name\project_name`**\bin\Debug**, click `project_name`**.dll** and **EPDM.Interop.epdm.dll**.
  5. Click **Open**.
  6. Click **OK**.
  7. Click **OK**.
13. The first menu command appears in the context-sensitive and Tools menus of vault files in File Explorer. The second menu command appears in the context-sensitive menus only when one or more files or folders are selected. Right-click a file in the vault and select **Second command**. A dialog similar to the following is displayed:
