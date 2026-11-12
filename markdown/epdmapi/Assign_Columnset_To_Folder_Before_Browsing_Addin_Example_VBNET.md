---
title: "Assign Columnset to Folder before Browsing Add-in Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Assign_Columnset_To_Folder_Before_Browsing_Addin_Example_VBNET.htm"
---

# Assign Columnset to Folder before Browsing Add-in Example (VB.NET)

This example shows how to create an add-in that triggers a pre-browse event and assigns a columnset to a folder before it is browsed.

```vb
  '--------------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio as Administrator.
 ' 2. Click File > New > Project > Visual Basic, Windows, Library > Class Library (.NET Framework).
 ' 3. Select .NET Framework 4.5 or later in the dropdown.
 ' 4. Type ClassLibrary1 in Project name.
 ' 5.      For Location, click ... and navigate to the folder where to create the project.
 ' 6. Click Create.
  ' 7. Add dependencies and safely pass arrays of structures.
  ' 8. Right-click the project name in the Solution Explorer and click Properties.
 ' 9. In the Properties window:
 '    a. On the Application tab, click Assembly Information....
 '    b. De-select Make assembly COM-Visible.
 '    c. On the Compile tab, select x64 in the Target CPU dropdown, de-select Prefer 32-bit, and select Register for COM interop.
 '10. Save the project.
 '11. Copy the code below to your project's Class1.vb.
 '12. To populate the GUID attribute, click Tools > Create GUID in the IDE,
 '    select GUID Format 6, click Copy, and click Exit. Replace <Guid("")> with
 '    the copied string.
 '13. Open the SOLIDWORKS PDM Professional Administration tool, expand a vault_name node,
 '    and log in as Admin.
 '14. Under vault_name, right-click Add-ins, and click New Add-in.
  '    a. Navigate to the bin directory of your built project.
 '    b. Select ClassLibrary1.dll.
 '    c. Click Open.
 '    d. Click OK.
  '15. Click OK after reading the SOLIDWORKS PDM Professional warning dialog.
 '16. Expand Columns under the vault_name in the Admin Tool.
'17. Right click File List Columns and select  New Column Set.
'18. Change the order of existing columns or add a custom column and name the new column set.
'19. Click  OK.
 '20. Change the ID parameter in SetColumnSetID of the code to match your new column set ID. As none of the other folders and column sets exist, the code will only execute the Case Else section.
'21. Save the project.
'22. Select Release in the Solution Configurations dropdown and x64 in the Solution Platforms dropdown.
 '23. Click Build > Build Solution.
 '
 ' Postconditions:
 ' 1. Open File Explorer on a view of vault_name and log in as Admin.
 ' 2. This add-in triggers a pre-browse event before the root folder is browsed.
' 3. Click OK on each dialog as it appears.
' 4. This add-in registers and loads a user's column set into the root folder before it is browsed.
  '---------------------------------------------------------------------------------------

 Imports EPDM.Interop.epdm
 Imports System.Runtime.InteropServices

 <Guid("")>
 <ComVisible(True)>
```

Public Class APIs

Implements IEdmAddIn5

Public vault As IEdmVault22

Dim ppocolumnset As EdmColumnSet

Dim ppocolumnsets As EdmColumnSet()

Public Sub GetAddInInfo(ByRef poInfo As EdmAddInInfo, ByVal poVault As IEdmVault5, ByVal poCmdMgr As IEdmCmdMgr5) Implements IEdmAddIn5.GetAddInInfo

Try

poInfo.mbsAddInName = "VB.NET Add-In"

poInfo.mbsCompany = "Dassault Systemes"

poInfo.mbsDescription = "Responding to folder browse events"

poInfo.mlAddInVersion = Now.ToString("yyyyMMdd")

poInfo.mlRequiredVersionMajor = 29

poInfo.mlRequiredVersionMinor = 0

poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreBrowseFolder)

Catch ex As Runtime.InteropServices.COMException

MsgBox("HRESULT = 0x" + ex.ErrorCode.ToString("X") + vbCrLf + ex.Message)

Catch ex As Exception

MsgBox(ex.Message)

End Try

End Sub

Public Sub OnCmd(ByRef poCmd As EdmCmd, ByRef ppoData As EdmCmdData()) Implements IEdmAddIn5.OnCmd

Dim FolderID As Integer

Dim AffectedFile As EdmCmdData

Dim ID As Integer

Dim Name As String

Name = " "

MsgBox("poCmd.meCmdType = " + poCmd.meCmdType.ToString)

If poCmd.meCmdType = EdmCmdType.EdmCmd_PreBrowseFolder Then

vault = poCmd.mpoVault

Getcolumnsets(ID, Name)

vault.**SetColumnSetID**(ID)

For Each AffectedFile In ppoData

FolderID = AffectedFile.mlObjectID1

'Set the column set for the folder to be browsed

Select Case FolderID

Case 3

'vault.SetColumnSetID(5)

'GetCurrentColumnSet(ID, Name)

'MsgBox("Browsing Folder ID=3")

Case 4

'vault.SetColumnSetID(6)

'MsgBox("Browsing Folder ID=4")

Case 5

'vault.SetColumnSetID(7)

'GetCurrentColumnSet(ID, Name)

'MsgBox("Browsing Folder ID=5")

Case 6

'vault.SetColumnSetID(8)

'MsgBox("Browsing Folder ID=6")

Case 7

'vault.SetColumnSetID(9)

'GetCurrentColumnSet(ID, Name)

'MsgBox("Browsing Folder ID=7")

Case 8

'vault.SetColumnSetID(10)

'MsgBox("Browsing Folder ID=8")

Case Else

GetCurrentColumnSet(ID, Name)

MsgBox("Browsing Folder ID=" + FolderID.ToString())

End Select

Next

End If

End Sub

Public Sub GetCurrentColumnSet(ByRef ColumnID As Integer, ByRef ColumnName As String)

vault.**GetCurrentColumnSet**(ppocolumnset)

ColumnName = ppocolumnset.**mbsColumnSetName**

ColumnID = ppocolumnset.**mlColumnSetID**

MsgBox("Current column set ID = " + ColumnID.ToString + " Current column set name = " + ColumnName)

End Sub

Public Sub Getcolumnsets(ByRef ColumnID As Integer, ByRef ColumnName As String)

vault.**GetColumnSets**(ppocolumnsets)

Dim item As EdmColumnSet

For Each item In ppocolumnsets

ColumnName = item.**mbsColumnSetName**

ColumnID = item.**mlColumnSetID**

MsgBox("User's column set ID = " + ColumnID.ToString + " User's column set name = " + ColumnName)

Next

End Sub

End Class

[Back to top](#top)
