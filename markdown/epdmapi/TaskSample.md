---
title: "Task Add-in Sample"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/TaskSample.htm"
---

# Task Add-in Sample

The following shows the entire source code of a task add-in
written in VB.NET. The add-in:

- Implements

  [IEdmAddIn5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.html)

  .
- Creates custom pages in the Task property dialog box.
- Customizes the task details page.
- Displays a message box on launch.

NOTE: To populate the GUID attribute below, click**Tools > Create GUID**in the IDE, select GUID Format 6, click**Copy**, and click**Exit**.
Replace <Guid("")>
with the copied string.

| Imports EPDM.Interop.epdm Imports System.Runtime.InteropServices < Guid ( "" )> _ < ComVisible ( True )> _ Public Class TaskAddIn Implements IEdmAddIn5 Public Sub GetAddInInfo(ByRef poInfo As EdmAddInInfo, ByVal poVault
As IEdmVault5 ,
ByVal poCmdMgr As IEdmCmdMgr5 )
Implements IEdmAddIn5.GetAddInInfo On Error GoTo ErrHand ' Fill in the add-in's description poInfo.mbsAddInName = "Task Test Add-in" poInfo.mbsCompany = "SOLIDWORKS" poInfo.mbsDescription = "Add-in used to test the task execution system" poInfo.mlAddInVersion = 1 ' Minimum SOLIDWORKS PDM Professional version
needed for VB.NET add-ins is 2010 poInfo.mlRequiredVersionMajor = 10 poInfo.mlRequiredVersionMinor = 0 'Register this task add-in hook to run a task add-in poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskRun) 'Register this task add-in hook to append
information to the task property pages in the Administration tool poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskSetup) 'Register this task add-in hook to display a
dialog or form before the task is launched on the client computer poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskLaunch) 'Register this task add-in hook to provide
extra details in the Details dialog box in the task list in the Administration tool poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskDetails) 'Register this task add-in hook to perform some
action after a
task launch dialog box or form button is clicked poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskLaunchButton) 'Register this task add-in hook to be called when the
task set-up wizard is closed poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskSetupButton) Exit Sub ErrHand: Dim v11 As IEdmVault11 v11 = poVault MsgBox(v11.GetErrorMessage(Err.Number)) End Sub |
| --- |
| Private Sub
OnTaskDetails(ByRef poCmd As EdmCmd, ByRef ppoData As EdmCmdData [] ) Dim inst As IEdmTaskInstance inst = poCmd.mpoExtra 'Create a custom page in the task properties
dialog box; TaskDetailsPage is a 'user control; TaskDetailsPage::LoadData fills in some edit boxes with 'values from IEdmTaskInstance::GetValEx Dim myPage As TaskDetailsPage myPage = New TaskDetailsPage myPage.CreateControl() poCmd.mpoExtra = myPage poCmd.mlParentWnd = myPage.Handle.ToInt32 poCmd.mbsComment = "My Test Page" myPage.LoadData(inst) End Sub |
| Private Sub
OnTaskLaunch(ByRef poCmd As EdmCmd, ByRef ppoData As EdmCmdData [] ) 'Display a message box on task launch 'You can also display a form to collect data to pass back to the
task add-in Dim v11 As IEdmVault11 v11 = poCmd.mpoVault If v11.MsgBox(poCmd.mlParentWnd, "Hello!" + vbLf + "Are you sure you want
to launch the test task?", EdmMBoxType.EdmMbt_YesNo) <> EdmMBoxResult.EdmMbr_Yes
Then poCmd.mbCancel = True Exit Sub End If End Sub |
| Private Sub OnTaskLaunchButton(ByRef
poCmd As EdmCmd, ByRef ppoData As EdmCmdData [] ) 'Code
here is executed when the user clicks OK or Cancel in the dialog
returned by OnTaskLaunch If poCmd. mbsComment = "OK" poCmd. mbCancel = False; Else poCmd. mbCancel = True; End If End Sub |
| Private Sub
OnTaskRun(ByRef poCmd As EdmCmd, ByRef ppoData As EdmCmdData [] ) 'Get the property interface used to access the
framework Dim inst As IEdmTaskInstance inst = poCmd.mpoExtra On Error GoTo ErrHand 'Inform the framework that the task has started inst.SetStatus(EdmTaskStatus.EdmTaskStat_Running) 'Format a message to be displayed in the task
list Dim msg As String msg = "Test is running:" msg = msg + " MyTestSetupVar='" + CStr(inst.GetValEx("MyTestSetupVar")) msg = msg + "' MyLaunchVar='" + inst.GetValEx("MyLaunchVar") msg = msg + "' Idx=" 'This is the main worker loop that does all
of the important work; 'it just beeps and sleeps Dim idx As Integer idx = 1 Dim maxPos As Integer maxPos = 200 inst.SetProgressRange(maxPos, 0, msg + CStr(idx)) While idx < maxPos 'Update progress bar that shows in the
task list inst.SetProgressPos(idx, msg + CStr(idx)) idx = idx + 1 'Do some important work here System.Media.SystemSounds.Beep.Play() System.Threading.Thread.Sleep(60000 / maxPos) 'Handle the cancel button in the task
list If inst.GetStatus() = EdmTaskStatus.EdmTaskStat_CancelPending Then inst.SetStatus(EdmTaskStatus.EdmTaskStat_DoneCancelled) Exit Sub End If 'Handle temporary suspension of the task If inst.GetStatus() = EdmTaskStatus.EdmTaskStat_SuspensionPending
Then inst.SetStatus(EdmTaskStatus.EdmTaskStat_Suspended) While inst.GetStatus() = EdmTaskStatus.EdmTaskStat_Suspended System.Threading.Thread.Sleep(1000) End While If inst.GetStatus() = EdmTaskStatus.EdmTaskStat_ResumePending
Then inst.SetStatus(EdmTaskStatus.EdmTaskStat_Running) End If End If End While 'Inform the framework that the task has successfully completed inst.SetStatus(EdmTaskStatus.EdmTaskStat_DoneOK) Exit Sub ErrHand: 'Return errors to the framework by failing the
task inst.SetStatus(EdmTaskStatus.EdmTaskStat_DoneFailed, Err.Number,
"The test task failed!") End Sub |
| 'Store the custom set-up page here so it
can be accessed from both OnTaskSetup and OnTaskSetupButton Dim currentSetupPage As SetupPage |
| Private Sub
OnTaskSetup(ByRef poCmd As EdmCmd, ByRef ppoData As EdmCmdData [] ) 'Get the property interface used to access the
framework Dim props As IEdmTaskProperties props = poCmd.mpoExtra 'Turn on some properties, e.g., the task can
be launched during a 'state change, can
extend the details page, is called when the 'task is launched, and supports scheduling props.TaskFlags = EdmTaskFlag.EdmTask_SupportsChangeState
+ EdmTaskFlag.EdmTask_SupportsDetails + EdmTaskFlag.EdmTask_SupportsInitExec
+ EdmTaskFlag.EdmTask_SupportsScheduling 'Set menu commands that launch this task from
File Explorer Dim cmds(0) As EdmTaskMenuCmd cmds(0).mbsMenuString = "Run the test task" cmds(0).mbsStatusBarHelp = "This command runs the task add-in" cmds(0).mlCmdID = 1 cmds(0).mlEdmMenuFlags = EdmMenuFlags.EdmMenu_Nothing props.SetMenuCmds(cmds) 'Add a custom setup page; SetupPage is a user
control with an 'edit box; SetupPage::LoadData populates the edit box from a 'variable in IEdmTaskProperties; saving of properties is handled 'by OnTaskSetupButton currentSetupPage = New SetupPage currentSetupPage.CreateControl() currentSetupPage.LoadData(poCmd) Dim pages(0) As EdmTaskSetupPage pages(0).mbsPageName = "Test Add-in page" pages(0).mlPageHwnd = currentSetupPage.Handle.ToInt32 pages(0).mpoPageImpl = currentSetupPage props.SetSetupPages(pages) End Sub |
| 'Called when the user clicks OK or Cancel
in the 'task property dialog box Private Sub OnTaskSetupButton(ByRef poCmd As EdmCmd, ByRef ppoData As EdmCmdData [] ) 'The custom set-up page in currentSetupPage 'was created in method OnTaskSetup; 'StoreData saves the contents of the edit 'box in the user control
to 'IEdmTaskProperties in poCmd.mpoExtra If poCmd.mbsComment = "OK" And Not currentSetupPage Is
Nothing Then currentSetupPage.StoreData(poCmd) End If currentSetupPage = Nothing End Sub |
| 'Main entry point of the add-in; called
by SOLIDWORKS 'PDM Professional for all task-related events Public Sub OnCmd(ByRef poCmd As EdmCmd, ByRef ppoData As EdmCmdData [] )
Implements IEdmAddIn5.OnCmd On Error GoTo ErrHand 'Check the command type and call the right procedure Select Case poCmd.meCmdType Case EdmCmdType.EdmCmd_TaskDetails OnTaskDetails(poCmd, ppoData) Case EdmCmdType.EdmCmd_TaskLaunch OnTaskLaunch(poCmd, ppoData) Case EdmCmdType.EdmCmd_TaskLaunchButton OnTaskLaunchButton(poCmd, ppoData) Case EdmCmdType.EdmCmd_TaskRun OnTaskRun(poCmd, ppoData) Case EdmCmdType.EdmCmd_TaskSetup OnTaskSetup(poCmd, ppoData) Case EdmCmdType.EdmCmd_TaskSetupButton OnTaskSetupButton(poCmd, ppoData) End Select Exit Sub ErrHand: Dim v11 As IEdmVault11 v11 = poCmd.mpoVault MsgBox(v11.GetErrorMessage(Err.Number)) End Sub End Class |

The following is a resource template of the custom set-up page that is displayed
in the Task property dialog box by TaskAddIn::OnTaskSetup .
It is a user control in Visual Studio with an edit box named TextBox1 and a
button named TestButton.

The code behind the custom set-up page is as follows.

Imports EPDM.Interop.epdm Public Class SetupPage 'Button handler for a button on the page Private Sub TestButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs)
Handles TestButton.Click MsgBox("You pressed the test button") End Sub

Public Sub LoadData(ByRef poCmd As

[EdmCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.html)

)

'Get the property interface used to
access the framework

Dim props As

[IEdmTaskProperties](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html)

props = poCmd.mpoExtra

'Populate the edit box from a variable

TextBox1.Text = props.GetValEx("MyTestSetupVar")

End Sub

Public Sub StoreData(ByRef
poCmd As

[EdmCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.html)

)

'Get the property interface used to access the
framework

Dim props As

[IEdmTaskProperties](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html)

props = poCmd.mpoExtra

'Make sure the user has typed a value in the
edit box

If TextBox1.Text = "" Then

MsgBox("Enter a test value for the add-in!")

poCmd.mbCancel = True

Exit Sub

End If

'Save the value entered by the user

props.SetValEx("MyTestSetupVar", TextBox1.Text)

End Sub

End Class

The following
is the resource
template of the extra details page added by TaskAddIn::OnTaskDetails . It is a user control in Visual Studio that displays two task variables:

The code behind the extra details
page:

Imports EPDM.Interop.epdm Public Class TaskDetailsPage Public Sub LoadData(ByRef inst As IEdmTaskInstance) 'Populate the editboxes from the variables in the task TextBoxSetupVar.Text = CStr(inst.GetValEx("MyTestSetupVar")) TextBoxLaunchVar.Text = CStr(inst.GetValEx("MyLaunchVar")) End Sub End Class

The following is the set-up page
when the add-in is used in a task.

The following is the task details
page when opened from the task list.

The following is the task list during task execution.

**See Also**

[Programming
Tasks](tasks.htm)

[Standard Task Add-in](standardtaskaddin.htm)

[Task Sample (C#)](TaskSample_CSharp.htm)
