---
title: "Change Card Variables Add-in Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Change_Card_Variables_Addin_Example_VBNET.htm"
---

# Change Card Variables Add-in Example (VB.NET)

This example shows how to create an add-in that modifies a data card variable when another data card variable changes.

```vb
  '--------------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 ' 2. Click File > New > Project > Visual Basic, Windows, Library > Class Library (.NET Framework).
 ' 3. Select .NET Framework 4.5 or later in the dropdown.
 ' 4. Type CardVariables in Project name.
 ' 5. Click Browse and navigate to the folder where to create the project.
 ' 6. Click OK.
  ' 7. Right-click the project name in the Solution Explorer and click Add > Reference....
 ' 8. In the Reference Manager dialog:
 '    a. Add dependencies and safely pass arrays of structures.
  ' 9. Right-click the project name in the Solution Explorer and click Properties.
 '10. In the Properties window:
 '    a. On the Application tab, click Assembly Information....
 '    b. De-select Make assembly COM-Visible.
 '    c. On the Compile tab, select Any CPU, de-select Prefer 32-bit, and select Register for COM interop.
 '11. Save the project.
 '12. Copy the code below to Class1.vb.
 '13. To populate the GUID attribute, click Tools > Create GUID in the IDE,
 '    select GUID Format 6, click Copy, and click Exit. Replace <Guid("")> with
 '    the copied string.
 '14. Click Build > Build Solution.
 '
 ' Postconditions:
 ' 1. Open the SOLIDWORKS PDM Professional Administration tool, expand a vault_name node,
 '    and log in as Admin.
 ' 2. Under vault_name, right-click Add-ins, and click New Add-in.
  '    a. Navigate to the bin\Debug  directory of your built project.
 '    b. Click EPDM.Interop.epdm.dll and CardVariables.dll.
 '    c. Click Open.
 '    d. Click OK.
 ' 3. Click OK after reading the SOLIDWORKS PDM Professional warning dialog.
 ' 4. In the taskbar, click the Administration tool icon and click Log Off > vault_name.
 ' 5. Open File Explorer on a view of vault_name to:
 '    a. Log in as Admin.
 '    b. Create, check in, and check out a file whose data card contains Project Name
 '       and Project Number.
 '    c. Click the Data Card tab.
 '    d. In Project Name, type Mercury, Venus, Earth, Mars, Jupiter, or Saturn.
 '    e. Observe the change in Project Number.
 '    f. In Project Number, type a number between 1000 and 1005.
 '    g. Observe the change in Project Name.
  '---------------------------------------------------------------------------------------

 Imports EPDM.Interop.epdm
 Imports System.Runtime.InteropServices

 <Guid("")>
 <ComVisible(True)>
 Public Class CardVariables
     Implements IEdmAddIn5

     Public Sub GetAddInInfo( _
           ByRef poInfo As EdmAddInInfo, _
           ByVal poVault As IEdmVault5, _
           ByVal poCmdMgr As IEdmCmdMgr5) _
           Implements IEdmAddIn5.GetAddInInfo
         Try
             poInfo.mbsAddInName = "VB.NET Card Variable Add-In"
             poInfo.mbsCompany = "Dassault Systemes"
             poInfo.mbsDescription = "Example demonstrating " _
               + "updating a card variable based on another card variable"
             poInfo.mlAddInVersion = 1
             'Minimum SOLIDWORKS PDM Professional version
             'needed for VB.Net Add-Ins is 6.4
             poInfo.mlRequiredVersionMajor = 6
             poInfo.mlRequiredVersionMinor = 4

             'Register to receive a notification when
             'a data card variable value changes
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_CardInput)

             Dim ProjectDictionary As IEdmDictionary5
             ProjectDictionary = poVault.GetDictionary( _
               "Projects", True) 'Create it if it doesn't exist

             Dim SuccessSet As Boolean = False
             SuccessSet = ProjectDictionary.StringTestAndSetAt _
               ("1000", "Mercury")
             SuccessSet = ProjectDictionary.StringTestAndSetAt _
               ("1001", "Venus")
             SuccessSet = ProjectDictionary.StringTestAndSetAt _
               ("1002", "Earth")
             SuccessSet = ProjectDictionary.StringTestAndSetAt _
               ("1003", "Mars")
             SuccessSet = ProjectDictionary.StringTestAndSetAt _
               ("1004", "Jupiter")
             SuccessSet = ProjectDictionary.StringTestAndSetAt _
               ("1005", "Saturn")

         Catch ex As Runtime.InteropServices.COMException
             MsgBox("HRESULT = 0x" + _
                ex.ErrorCode.ToString("X") + vbCrLf + _
                ex.Message)
         Catch ex As Exception
             MsgBox(ex.Message)
         End Try
     End Sub

     'A data card variable value has changed
     Public Sub OnCmd( _
           ByRef poCmd As EdmCmd, _
           ByRef ppoData As EdmCmdData()) _
           Implements IEdmAddIn5.OnCmd
         Try

             Select Case poCmd.meCmdType

                 Case EdmCmdType.EdmCmd_CardInput
                     Static VariableChangeInProgress As Boolean = _
                        False
                     Dim vars As IEdmEnumeratorVariable5 = _
                        poCmd.mpoExtra
                     Dim ConfigNames As IEdmStrLst5 = _
                         DirectCast(ppoData(0), EdmCmdData).mpoExtra
                     Dim Config As String
                     If IsConfigInList(ConfigNames, "@") Then
                         Config = "@"
                     Else
                         Config = ""
                     End If

                     'Take appropriate action based on the data card variable that has changed
                     Select Case poCmd.mbsComment

                         'The Project Name variable has changed
                         Case "Project Name"
                             If VariableChangeInProgress = True Then
                                 VariableChangeInProgress = False
                                 Exit Select
                             End If
                             Dim ProjectName As String = ""
                             vars.GetVar("Project Name", Config, _
                               ProjectName)

                             'Get the old Project Number
                             Dim ProjectNumber As String = ""
                             vars.GetVar("Project number", Config, _
                                ProjectNumber)

                             'Get the existing Projects dictionary
                             Dim ProjectDictionary As IEdmDictionary5
                             ProjectDictionary = poCmd.mpoVault. _
                               GetDictionary("Projects", False)

                             'Look up the new project number
                             Dim NewProjectNumber As String = ""
                             'Find all values containing the substring
                             'stored in ProjectName
                             Dim key As String = ""
                             Dim value As String = ""
                             Dim pos As IEdmPos5
                             pos = ProjectDictionary.StringFindValues( _
                               ProjectName)
                             While Not pos.IsNull
                                 ProjectDictionary.StringGetNextAssoc( _
                                   pos, key, value)
                                 'Traverse the values until a match
                                 'is found
                                 If value = ProjectName Then
                                     NewProjectNumber = key
                                     Exit While
                                 End If
                             End While

                             'Only update the variable if it changed
                             If Not NewProjectNumber = ProjectNumber _
                                   Then
                                 VariableChangeInProgress = True
                                 vars.SetVar("Project number", Config, _
                                    NewProjectNumber)

                             End If

                             'The Project Number variable has changed
                         Case "Project number"
                             If VariableChangeInProgress = True Then
                                 VariableChangeInProgress = False
                                 Exit Select
                             End If

                             Dim ProjectNumber As String = ""
                             vars.GetVar("Project number", Config, _
                                ProjectNumber)

                             'Get the old Project Name
                             Dim ProjectName As String = ""
                             vars.GetVar("Project Name", Config, _
                                ProjectName)

                             'Get the existing Projects dictionary
                             Dim ProjectDictionary As IEdmDictionary5
                             ProjectDictionary = poCmd.mpoVault. _
                               GetDictionary("Projects", False)

                             'Look up the project name
                             Dim NewProjectName As String = ""
                             ProjectDictionary.StringGetAt( _
                               ProjectNumber, NewProjectName)

                             'Only update the variable if it's changed
                             If Not NewProjectName = ProjectName Then
                                 VariableChangeInProgress = True
                                 vars.SetVar("Project Name", Config, _
                                    NewProjectName)
                             End If
                     End Select
             End Select
         Catch ex As Runtime.InteropServices.COMException
             MsgBox("HRESULT = 0x" + _
                ex.ErrorCode.ToString("X") + vbCrLf + _
                ex.Message)
         Catch ex As Exception
             MsgBox(ex.Message)
         End Try
     End Sub

     Private Function IsConfigInList(ByVal ConfigNames As IEdmStrLst5, ByVal ConfigName As String) As Boolean
         IsConfigInList = False
         Try
             Dim CurConfig As String
             Dim Pos As IEdmPos5 = ConfigNames.GetHeadPosition()
             While Not Pos.IsNull
                 CurConfig = ConfigNames.GetNext(Pos)
                 If CurConfig = ConfigName Then
                     IsConfigInList = True
                     Exit While
                 End If
             End While
             Return IsConfigInList
         Catch ex As Runtime.InteropServices.COMException
             MsgBox("HRESULT = 0x" + _
                ex.ErrorCode.ToString("X") + vbCrLf + _
                ex.Message)
         Catch ex As Exception
             MsgBox(ex.Message)
         End Try
     End Function

 End Class
```

[Back to top](#top)
