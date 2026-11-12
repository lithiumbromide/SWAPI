---
title: "Create a Task that Finds Approved Files Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Schedule_Task_Addin_Example_VBNET.htm"
---

# Create a Task that Finds Approved Files Example (VB.NET)

This example shows how to create a task add-in that notifies the logged-in user as to which files in the vault are in the Approved state.

```vb
  '--------------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 ' 2. Click File > New > Project > Visual Basic > Class Library (.NET Framework).
  ' 3. Select .NET Framework 4.5 or later in the dropdown.
 ' 4. Type TaskAddinExample in Name.
 ' 5. Click Browse and navigate to the folder where to create the project.
 ' 6. Click OK.
  ' 7. Right-click the project name in the Solution Explorer and click Add Reference.
 ' 8. In the Add Reference dialog:
 '    a. Add the SOLIDWORKS PDM Professional  interop assembly as a reference (click Browse in the
 //       left-side panel, click EPDM.Interop.epdm.dll,
 //       and click OK).
 '    b. Add System.Windows.Forms as a reference (click Assemblies > Framework in the
 '       left-side panel, click System.Windows.Forms, and click Add).
 '    c. Click Close.
 ' 9. Right-click the project name in the Solution Explorer and click  Properties.
 '10. In the Properties window:
 '    a. On the Application tab, click Assembly Information.
 '    b. De-select Make assembly COM-Visible.
 '    c. On the Compile tab,  select Any CPU, de-select  Prefer 32-bit, and select Register for COM interop.
 '11. Save the project.
 '12. Copy the code below to Class1.vb.
 '13. To populate the GUID attribute, click Tools > Create GUID in the IDE,
 '    select GUID Format 6, click Copy, and click Exit. Replace <Guid("")> with the
 '    copied string.
 '14. Click Build > Build Solution.
 '
 ' Postconditions:
 '  1. Open the SOLIDWORKS PDM Professional Administration tool, expand a vault_name node,
 '     and log in as Admin.
 '  2. Ensure that Default Workflow with an Approved state exists
 '     under vault_name > Workflows.
 '  3. Under vault_name, right-click Add-ins and click New Add-in.
 '     a. Navigate to the  bin\Debug directory of your built project.
 '     b. Click EPDM.Interop.epdm.dll and TaskAddinExample.dll.
 '     c. Click Open.
 '     d. Click OK.
 '  4. Click OK after reading the SOLIDWORKS PDM Professional warning dialog.
  '  5. In the taskbar notification area:
 '     a. Click the SOLIDWORKS PDM icon.
 '     b. Click Task Host Configuration.
 '     c. Select vault_name in the File Vault dropdown.
 '     d. Select Permit next to the add-in you installed in step 3.
 '     e. Click OK.
 '  6. In the Administration tool under vault_name,  right-click Tasks and click New Task.
 '     a. Type Approved Files Task in the upper-left text box.
 '     b. Select the VB.NET Task Add-in from the Add-in dropdown.
 '     c. When the attach debugger message box appears:
 '        1. In the IDE, click Debug > Attach to Process > ConisioAdmin.exe.
 '        2. Click Attach.
 '        3. Click OK to close the message box.
 '     d. Click Next.
 '     e. On the Execution Method properties page, select the local computer.
 '     f. Click Next.
 '     g. On the Scheduling properties page, select This task is not scheduled.
 '     h. Click Next.
 '     i. On the Permissions property page, select Admin.
 '     j. Click Next.
 '     k. On the Success Notification property page:
 '        1. Select Notify the user who launched the task.
 '        2. In the Subject field, type Success.
 '        3. In the Text field, type The task successfully completed at, type a space,
 '           click >, and click Current Time.
 '     l. Click OK to close the New Task dialog.
 '  7. Expand vault_name > Tasks and double-click Task List.
 '  8. Click Add Task.
 '  9. In the Add Task dialog:
 '     a. Select Approved Files Task from the dropdown.
 '     b. Click OK.
 ' 10. When the attach debugger message box appears:
 '     a. In the IDE, click Debug > Attach to Process > TaskExecutor.exe.
 '     b. Click Attach.
 '     c. Click OK to close the message box.
 ' 11. The task appears in the Pending tasks list. Observe the task status.
  ' 12. When the task completes, the task moves to the Completed tasks
 '     list. The logged-in user receives a notification with the list of approved files.
  '---------------------------------------------------------------------------------------

 Imports EPDM.Interop.epdm
 Imports System.Runtime.InteropServices

 <Guid("")>
 <ComVisible(True)>
 Public Class TaskAddinExample
     Implements IEdmAddIn5

     Public Sub GetAddInInfo( _
       ByRef poInfo As EdmAddInInfo, _
       ByVal poVault As IEdmVault5, _
       ByVal poCmdMgr As IEdmCmdMgr5) _
       Implements IEdmAddIn5.GetAddInInfo

         Try
             poInfo.mbsAddInName = _
               "VB.NET Task Add-In"
             poInfo.mbsCompany = "Dassault Systemes"
             poInfo.mbsDescription = _
               "Exercise demonstrating a task that lists " _
               + "files in the Approved state."
             poInfo.mlAddInVersion = 1

             'Minimum SOLIDWORKS PDM Professional version
             'needed for VB.Net Task Add-Ins is 10.0
             poInfo.mlRequiredVersionMajor = 10
             poInfo.mlRequiredVersionMinor = 0

             'Register this add-in as a task add-in
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskRun)
             'Register this add-in to be called when
             'selected as a task in the Administration tool
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskSetup)
         Catch ex As Runtime.InteropServices.COMException
             MsgBox("HRESULT = 0x" + _
               ex.ErrorCode.ToString("X") + vbCrLf + _
               ex.Message)
         Catch ex As Exception
             MsgBox(ex.Message)
         End Try
     End Sub

     Public Sub OnCmd(ByRef poCmd As EdmCmd, _
       ByRef ppoData As System.Array) _
       Implements IEdmAddIn5.OnCmd

         Try
             PauseToAttachProcess(poCmd.meCmdType.ToString())

             Select Case poCmd.meCmdType
                 Case EdmCmdType.EdmCmd_TaskRun
                     OnTaskRun(poCmd, ppoData)
                 Case EdmCmdType.EdmCmd_TaskSetup
                     OnTaskSetup(poCmd, ppoData)
             End Select
         Catch ex As Runtime.InteropServices.COMException
             MsgBox("HRESULT = 0x" + _
               ex.ErrorCode.ToString("X") + vbCrLf + _
               ex.Message)
         Catch ex As Exception
             MsgBox(ex.Message)
         End Try
     End Sub

     Private Sub OnTaskRun(ByRef poCmd As EdmCmd, _
       ByRef ppoData As System.Array)

         'Get the task instance interface
         Dim inst As IEdmTaskInstance
         inst = poCmd.mpoExtra
         Try
             'Keep the task list status up to date
             inst.SetStatus _
               (EdmTaskStatus.EdmTaskStat_Running)

             'Format a message that will be displayed
             'in the task list
             inst.SetProgressRange(10, 1, "Task is running.")

             Dim Items As List(Of EdmSelItem2) = _
               New List(Of EdmSelItem2)
             inst.SetProgressPos(4, "Task is searching.")

             Dim Search As IEdmSearch6 = _
               poCmd.mpoVault.CreateSearch()
             If Search Is Nothing Then Return

             Search.SetToken( _
               EdmSearchToken.Edmstok_FindFiles, True)
             Search.SetToken( _
               EdmSearchToken.Edmstok_WorkflowName, _
               "Default Workflow")
             Search.SetToken( _
               EdmSearchToken.Edmstok_StateName, "Approved")

             'Uncomment and modify the following lines to look for files
             'that have a card variable with values in a specific range
            'Dim varName1 As Object = "Card_Variable_ID_or_Name"
             'Dim varValue1 As Object = "Card_Variable_Value_1"
             'Dim varOp1 as Integer = EdmVarOp_NumberGreaterThan
             'Dim varValue2 As Object = "Card_Variable_Value_2"
             'Dim varOp2 as Integer = EdmVarOp_NumberLessThan
             'Search.BeginAND
                'Search.AddVariable2(varName1, varValue1, varOp1)
                'Search.AddVariable2(varName1, varValue2, varOp2)
             'Search.EndAND

             Dim SearchResult As IEdmSearchResult5 = _
               Search.GetFirstResult()
             While Not SearchResult Is Nothing
                 Dim SelItem As EdmSelItem2 = New EdmSelItem2()
                 SelItem.mlID = SearchResult.ID
                 SelItem.mlParentID = SearchResult.ParentFolderID
                 SelItem.meType = SearchResult.ObjectType
                 SelItem.mlVersion = SearchResult.Version

                 Items.Add(SelItem)
                 SearchResult = Search.GetNextResult()
             End While
             inst.SetProgressPos(7, "Task finished searching.")

             Dim NotificationArray(Items.Count - 1) _
               As EdmSelItem2
             Items.CopyTo(NotificationArray)

             Dim ProgresssMsg As String
             If (Items.Count > 0) Then
                 ProgresssMsg = "Found " + _
                   Items.Count.ToString() + " files."
             Else
                 ProgresssMsg = ("No files found.")
             End If

             inst.SetProgressPos(10, ProgresssMsg)
             inst.SetStatus( _
               EdmTaskStatus.EdmTaskStat_DoneOK, 0, "", _
               NotificationArray, ProgresssMsg)
         Catch ex As Runtime.InteropServices.COMException
             inst.SetStatus _
               (EdmTaskStatus.EdmTaskStat_DoneFailed, _
               ex.ErrorCode, "The test task failed!")
         Catch ex As Exception
             inst.SetStatus _
               (EdmTaskStatus.EdmTaskStat_DoneFailed, _
               0, "Non COM test task failure!")
         End Try
     End Sub

     Private Sub OnTaskSetup(ByRef poCmd As EdmCmd, _
       ByRef ppoData As System.Array)

         Try
             'Get the property interface used to
             'access the framework
             Dim props As IEdmTaskProperties
             props = poCmd.mpoExtra

             'Set the property flag that says you want a
             'menu item for the user to launch the task
             'and a flag to support scheduling
             props.TaskFlags = _
               EdmTaskFlag.EdmTask_SupportsInitExec + _
               EdmTaskFlag.EdmTask_SupportsScheduling

             'Set up the menu commands to launch this task
             Dim cmds(0) As EdmTaskMenuCmd
             cmds(0).mbsMenuString = "List Approved files task"
             cmds(0).mbsStatusBarHelp = _
               "This command runs the task add-in to get the" + _
               " names of the files in the Approved state."
             cmds(0).mlCmdID = 1
             cmds(0).mlEdmMenuFlags = _
               EdmMenuFlags.EdmMenu_Nothing
             props.SetMenuCmds(cmds)
         Catch ex As Runtime.InteropServices.COMException
             MsgBox("HRESULT = 0x" + _
               ex.ErrorCode.ToString("X") + vbCrLf + _
               ex.Message)
         Catch ex As Exception
             MsgBox(ex.Message)
         End Try
     End Sub

     Private Sub PauseToAttachProcess( _
       ByVal callbackType As String)

         Try
             'If the debugger isn't already attached to a
             'process,
             If Not Debugger.IsAttached() Then
                 'Launch the debug dialog
                 'Debugger.Launch()
                 'or
                 'use a MsgBox dialog to pause execution
                 'and allow the user time to attach it
                 MsgBox("Attach debugger to process """ + _
                   Process.GetCurrentProcess.ProcessName() + _
                   """ for callback """ + callbackType + _
                   """ before clicking OK.")
             End If

         Catch ex As Exception
             MsgBox(ex.Message)
         End Try
     End Sub

 End Class
```
