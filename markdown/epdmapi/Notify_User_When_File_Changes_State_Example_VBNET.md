---
title: "Notify User When File Changes State Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Notify_User_When_File_Changes_State_Example_VBNET.htm"
---

# Notify User When File Changes State Example (VB.NET)

This example shows how to create an add-in that pops up a message box when a file is approved.

```vb
'--------------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 ' 2. Click File > New > Project > Visual Basic, Windows, Library > Class Library (.NET Framework).
 ' 3. Select .NET Framework 4.5 in the dropdown.
 ' 4. Type StateChangeNotificationAddin in Name.
 ' 5.     For Location, click ... and navigate to the folder where to create the project.
 ' 6. Click Create.
 ' 7. Add dependencies and safely pass arrays of structures.
 ' 8. Add System.Windows.Forms as a reference (click Assemblies > Framework in the
 '    left-side panel, select System.Windows.Forms, and click OK).
  ' 9. Right-click the project name in the Solution Explorer and click Properties.
 '10. In the Properties window:
 '    a. On the Application tab, click Assembly Information.
 '    b. De-select Make assembly COM-Visible.
 '    c. On the Compile tab,  select Any CPU, de-select Prefer 32-bit, and select Register for COM interop.
 '11. Save the project.
 '12. Copy the code below to Class1.vb.
 '13. To populate the GUID attribute, click Tools > Create GUID in the IDE,
 '    select GUID Format 6, click Copy, and click Exit. Replace <Guid("")> with the
 '    copied string.
 '14. Click Build > Build Solution.
 '
 ' Postconditions:
 ' 1. Open the SOLIDWORKS PDM Professional Administration tool, expand a vault_name node,
 '    and log in as Admin.
 ' 2. Ensure that Default Workflow exists under vault_name > Workflows.
 '    a. Ensure that the workflow has an Approved state.
 '    b. Ensure that the workflow has a Change Approved transition.
 ' 3. Under vault_name, right-click Add-ins and click New Add-in.
 '    a. Navigate to the  bin\Debug directory of your built project.
 '    b. Click EPDM.Interop.epdm.dll and StateChangeNotificationAddin.dll
 '    c. Click Open.
 '    d. Click OK.
 ' 4. Click OK after reading the SOLIDWORKS PDM Professional warning dialog.
 ' 5. Open File Explorer on a view of vault_name and:
 '    a. Log in as Admin.
 '    b. Create a new file in the root directory of  vault_name and check it in.
 '    c. Right-click the file and click Change State > transition.
 '    d. Click OK in the Do Transition dialog.
 '    e. Repeat steps c and d until the file is in a state that it can be Approved.
 '    g. Right-click the file and click Change State > Change Approved.
 '    h. Click OK in the Do Transition dialog.
 ' 6. A message box pops up notifying the user whether the file changing state is a
 '    top node. Click OK.
 ' 7. A message box pops up notifying the user that the file has been approved.
 '    Click OK.
 '---------------------------------------------------------------------------------------
 Imports System.Windows.Forms
 Imports EPDM.Interop.epdm
 Imports System.Runtime.InteropServices

 <Guid("")>
 <ComVisible(True)>
 Public Class ChangeStateNotification
     Implements IEdmAddIn5

     Public Sub GetAddInInfo(ByRef poInfo As EdmAddInInfo, ByVal poVault As IEdmVault5, ByVal poCmdMgr As IEdmCmdMgr5) Implements IEdmAddIn5.GetAddInInfo

         Try
             poInfo.mbsAddInName = "VB.NET Add-In"
             poInfo.mbsCompany = "Dassault Systemes"
             poInfo.mbsDescription = "Exercise demonstrating responding to a change state event."
             poInfo.mlAddInVersion = 1

             'Minimum SOLIDWORKS PDM Professional version
             'needed for VB.Net Add-Ins is 6.4
             poInfo.mlRequiredVersionMajor = 6
             poInfo.mlRequiredVersionMinor = 4

             'Register to receive a notification when
             'a file has changed state
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_PostState)
         Catch ex As Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + vbCrLf + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub OnCmd(ByRef poCmd As EdmCmd, ByRef ppoData As EdmCmdData()) Implements IEdmAddIn5.OnCmd

         Try
             Dim AffectedFile As EdmCmdData
             Dim AffectedFileNames As String = ""
             Dim cmdNode As IEdmCmdNode
             Dim topNode As Boolean
             Select Case poCmd.meCmdType
                 'A file has changed state
                 Case EdmCmdType.EdmCmd_PostState
                     For Each AffectedFile In ppoData
                         If AffectedFile.mbsStrData2 = "Approved" Then
                             AffectedFileNames += AffectedFile.mbsStrData1 + vbCrLf
                         End If
                        cmdNode = AffectedFile.mpoExtra
                         topNode = cmdNode.GetProperty(EdmCmdNodeProp.EdmCmdNode_IsTopNode)
                         MessageBox.Show("File changing state is a top node? " + topNode)

                     Next AffectedFile

                     If AffectedFileNames.Length > 0 Then
                         poCmd.mpoVault.MsgBox(poCmd.mlParentWnd, AffectedFileNames + " has been approved.")
                     End If

                     'The event isn't registered
                 Case Else
                     poCmd.mpoVault.MsgBox(poCmd.mlParentWnd, "An unknown command type was issued.")
             End Select
         Catch ex As Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + vbCrLf + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub
 End Class
```
