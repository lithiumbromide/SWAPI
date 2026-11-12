---
title: "Create a Task that Finds Files in Workflow States Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm"
---

# Create a Task that Finds Files in Workflow States Example (VB.NET)

This example shows how to create a task add-in that finds files that have been in specified workflow states a specified number of days.

```vb
  '--------------------------------------------------------------------------------------
 ' Preconditions:
 '  1. Start Microsoft Visual Studio 2010.
 '  2. Click File > New > Project > Visual Basic > Class Library (.NET Framework).
 '  3. Select .NET Framework 4.5 or later in the dropdown.
 '  4. Click Browse and navigate to the folder where to create the project.
 '  5. Type StateAgeTask in Name.
 '  6. Click OK.
 '  7. Right-click the project in the Solution Explorer and click Add > User Control.
 '  8. In the Add New Item dialog, keep the default name and click Add.
 '  9. Create a user control similar to the one shown above and change:
 '     a. Top label to WorkflowLabel.
 '     b. Combo box to WorkflowsComboBox.
 '     c. Second label to StatesLabel.
 '     d. List box to StatesListBox.
 '     e. Third label to DaysLabel.
 '     f. Numeric spin box to DaysNumericUpDown.
 ' 10. Click Show All Files in the Solution Explorer toolbar and expand  UserControl1.vb.
 ' 11. Replace the code in Class1.vb with this code.
 ' 12. Replace the code in UserControl1.Designer.vb with this code.
 ' 13. Replace the code in UserControl1.vb with this code.
  ' 14. Right-click the project name in the Solution Explorer and click Add Reference.
 ' 15. In the Add Reference dialog:
 '     a. Add the SOLIDWORKS PDM Professional  interop assembly as a reference (click Browse in the
 //       left-side panel, click EPDM.Interop.epdm.dll,
 //       and click OK).
 '     b. Click Close.
 ' 16. Right-click the project name in the Solution Explorer and click  Properties.
 ' 17. In the Properties window:
 '     a. On the Application tab, click Assembly Information.
 '     b. De-select Make assembly COM-Visible.
 '     c. On the Compile tab,  select Any CPU, de-select Prefer 32-bit, and select Register for COM interop.
 ' 18. Save the project.
 ' 19. To populate the GUID attribute, click Tools > Create GUID in the IDE,
 '     select GUID Format 6, click Copy, and click Exit. Replace <Guid("")> with
 '     the copied string.
 ' 20. Click Build > Build Solution.
 '
 ' Postconditions:
 '  1. Open the SOLIDWORKS PDM Professional Administration tool, expand a vault_name node,
 '     and log in as Admin.
 '  2. Under vault_name, right-click Add-ins and click New Add-in.
 '     a. Navigate to the  bin\Debug directory of your built project.
 '     b. Click EPDM.Interop.epdm.dll and StateAgeTask.dll.
 '     c. Click Open.
 '     d. Click OK.
 '  3. Click OK after reading the SOLIDWORKS PDM Professional warning dialog.
  '  4. In the taskbar notification area:
 '     a. Click the SOLIDWORKS PDM Professional icon.
 '     b. Click Task Host Configuration.
 '     c. Select vault_name in the File Vault dropdown.
 '     d. Select Permit next to the add-in you just installed.
 '     e. Click OK.
 '  5. In the Administration tool under vault_name,  right-click Tasks and click New Task.
 '  6. In the New task dialog:
 '     a. Type State Age Task in the upper-left text box.
 '     b. Select the VB.NET Workflow State Age Task Add-in from the Add-in dropdown.
 '     c. Click Next.
 '     d. On the Execution Method properties page, select the local computer.
 '     e. Click Next.
 '     f. On the Scheduling properties page, select This task is not scheduled.
 '     g. Click Next.
 '     h. On the Choose states to check page, select the file search criteria in:
 '        1. Choose Workflow.
 '        2. Select States.
 '        3. Number of Days in State.
 '     i. Click Next.
 '     j. On the Permissions property page, select Admin.
 '     k. Click Next.
 '     l. On the Success Notification property page:
 '        1. Select Notify the user who launched the task.
 '        2. In the Subject field, type Success.
 '        3. In the Text field, type The task successfully completed at, type a space,
 '           click >, and click Current Time.
 '     m. Click OK to close the New Task dialog.
 '  7. Expand vault_name > Tasks and double-click Task List.
 '  8. Click Add Task.
 '  9. In the Add Task dialog:
 '     a. Select State Age Task from the dropdown.
 '     b. Click OK.
 ' 10. The task appears in the Pending tasks list. Observe the task status.
  ' 11. When the task completes, the task moves to the Completed tasks
 '     list. After a minute or so, the logged-in user receives a notification
 '     with the list of files that have been in the specified workflow states a
 '     specified number of days.
  '---------------------------------------------------------------------------------------
```

[Back to top](#top)

```vb
 'UserControl1.vb
 Imports EPDM.Interop.epdm

  ' Setup page used in the task setup and task details dialogs must be a
 ' System.Windows.Forms.UserControl
 Public Class SetupPage

   Private mVault As IEdmVault7
   Private mTaskProps As IEdmTaskProperties
   Private mTaskInst As IEdmTaskInstance
     ' Constructor called from task setup
   Public Sub New(ByVal Vault As IEdmVault7, _
       ByVal Props As IEdmTaskProperties)
     Try
       InitializeComponent()
       mVault = Vault
       mTaskProps = Props
       mTaskInst = Nothing

     Catch ex As Runtime.InteropServices.COMException
       MsgBox("HRESULT = 0x" + _
          ex.ErrorCode.ToString("X") + vbCrLf + _
          ex.Message)
     Catch ex As Exception
       MsgBox(ex.Message)
     End Try
   End Sub

     ' Constructor called from task details
   Public Sub New(ByVal Vault As IEdmVault7, _
       ByVal Props As IEdmTaskInstance)
     Try
       InitializeComponent()
       mVault = Vault
       mTaskProps = Nothing
       mTaskInst = Props

     Catch ex As Runtime.InteropServices.COMException
       MsgBox("HRESULT = 0x" + _
          ex.ErrorCode.ToString("X") + vbCrLf + _
          ex.Message)
     Catch ex As Exception
       MsgBox(ex.Message)
     End Try
   End Sub

   Public Sub LoadData(ByVal poCmd As EdmCmd)
     Try
       'Add the names of the available workflows to WorkflowsComboBox
       WorkflowsComboBox.Items.Clear()
       Dim WorkflowMgr As IEdmWorkflowMgr6
       WorkflowMgr = mVault.CreateUtility( _
         EdmUtility.EdmUtil_WorkflowMgr)
       Dim WorkflowPos As IEdmPos5 = _
         WorkflowMgr.GetFirstWorkflowPosition()
       While Not WorkflowPos.IsNull
         Dim Workflow As IEdmWorkflow6
         Workflow = _
           WorkflowMgr.GetNextWorkflow(WorkflowPos)
         WorkflowsComboBox.Items.Add(Workflow.Name)
       End While

       Dim SelectedWorkflow As String = ""
       Dim NoDays As String = ""
       If Not mTaskProps Is Nothing Then
         'Retrieve the name of the workflow that was
         'selected by the user
         SelectedWorkflow = _
           mTaskProps.GetValEx("SelectedWorkflowVar")
         'Retrieve the number of days in a state
         'before sending a message
         NoDays = mTaskProps.GetValEx("NoDaysVar")
       ElseIf Not mTaskInst Is Nothing Then
         'Retrieve the name of the workflow that
         'was selected by the user
         SelectedWorkflow = _
           mTaskInst.GetValEx("SelectedWorkflowVar")
         'Retrieve the number of days in a state
         'before sending a message
         NoDays = mTaskInst.GetValEx("NoDaysVar")
       End If

       'Select the workflow to display in
       'WorkflowsComboBox; setting this also
       'causes SetupPage::WorkflowsComboBox_SelectedIndexChanged
       'to be called to fill StatesListBox
       'with the available states for this workflow
       If SelectedWorkflow = "" Then
         WorkflowsComboBox.SelectedIndex = 0
       Else
         WorkflowsComboBox.Text = SelectedWorkflow
       End If

       'Retrieve the number of days in a state
       'before sending a message
       If IsNumeric(NoDays) Then
         DaysNumericUpDown.Value = _
           Convert.ToDecimal(NoDays)
       Else
         DaysNumericUpDown.Value = 0
       End If

     Catch ex As Runtime.InteropServices.COMException
       MsgBox("HRESULT = 0x" + _
          ex.ErrorCode.ToString("X") + vbCrLf + _
          ex.Message)
     Catch ex As Exception
       MsgBox(ex.Message)
     End Try
   End Sub

   Public Sub StoreData()
     Try
       'Add the selected states to StatesList
       Dim StatesList As String = ""
       For Each SelectedStateIndex As Integer _
           In StatesListBox.SelectedIndices
         StatesList += _
           StatesListBox.Items(SelectedStateIndex) + _
             vbCrLf
       Next
       'Save the states selected by the user
       mTaskProps.SetValEx("SelectedStatesVar", _
         StatesList)
       'Save the workflow selected by the user
       mTaskProps.SetValEx("SelectedWorkflowVar", _
         WorkflowsComboBox.Text)
       'Save the number of days selected by the user
       mTaskProps.SetValEx("NoDaysVar", _
         DaysNumericUpDown.Value.ToString())

     Catch ex As Runtime.InteropServices.COMException
       MsgBox("HRESULT = 0x" + _
          ex.ErrorCode.ToString("X") + vbCrLf + _
          ex.Message)
     Catch ex As Exception
       MsgBox(ex.Message)
     End Try
   End Sub

   Private Sub WorkflowsComboBox_SelectedIndexChanged( _
       ByVal sender As System.Object, _
       ByVal e As System.EventArgs) _
       Handles WorkflowsComboBox.SelectedIndexChanged
     Try
       'Find the IEdmWorkflow corresponding to the
       'selected workflow name
       Dim WorkflowMgr As IEdmWorkflowMgr6
       WorkflowMgr = mVault.CreateUtility( _
         EdmUtility.EdmUtil_WorkflowMgr)
       Dim WorkflowPos As IEdmPos5 = _
         WorkflowMgr.GetFirstWorkflowPosition()
       Dim Workflow As IEdmWorkflow6 = Nothing
       Dim SelectedWorkflow As IEdmWorkflow6 = Nothing
       While Not WorkflowPos.IsNull
         Workflow = _
           WorkflowMgr.GetNextWorkflow(WorkflowPos)
         If Workflow.Name = WorkflowsComboBox.Text Then
           SelectedWorkflow = Workflow
           Exit While
         End If
       End While

       'Add the names of the available states for the
       'selected workflow to StatesListBox
       StatesListBox.Items.Clear()
       If Not SelectedWorkflow Is Nothing Then
         Dim StatePos As IEdmPos5 = _
           SelectedWorkflow.GetFirstStatePosition()
         While Not StatePos.IsNull
           Dim State As IEdmState6
           State = SelectedWorkflow.GetNextState(StatePos)
           StatesListBox.Items.Add(State.Name)
         End While
       End If

       Dim SelectedStates As String = ""
       If Not mTaskProps Is Nothing Then
         SelectedStates = _
           mTaskProps.GetValEx("SelectedStatesVar")
       ElseIf Not mTaskInst Is Nothing Then
         SelectedStates = _
           mTaskInst.GetValEx("SelectedStatesVar")
       End If

       Dim States As Object = _
         Split(SelectedStates, vbCrLf)
       For Each State As String In States
         If Not Trim(State) = "" Then
           StatesListBox.SelectedItems.Add(State)
         End If
       Next

     Catch ex As Runtime.InteropServices.COMException
       MsgBox("HRESULT = 0x" + _
          ex.ErrorCode.ToString("X") + vbCrLf + _
          ex.Message)
     Catch ex As Exception
       MsgBox(ex.Message)
     End Try
   End Sub

   Public Sub DisableControls()
     Try
       WorkflowsComboBox.Enabled = False
       StatesListBox.Enabled = False
       DaysNumericUpDown.Enabled = False
     Catch ex As Runtime.InteropServices.COMException
       MsgBox("HRESULT = 0x" + _
          ex.ErrorCode.ToString("X") + vbCrLf + _
          ex.Message)
     Catch ex As Exception
       MsgBox(ex.Message)
     End Try
   End Sub

 End Class
```

[Back to top](#top)

```
'UserControl1.Designer.vb
```

```vb
 <Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
 Partial Class SetupPage
     Inherits System.Windows.Forms.UserControl

     'UserControl overrides dispose to clean up the component list.
     <System.Diagnostics.DebuggerNonUserCode()> _
     Protected Overrides Sub Dispose(ByVal disposing As Boolean)
         Try
             If disposing AndAlso components IsNot Nothing Then
                 components.Dispose()
             End If
         Finally
             MyBase.Dispose(disposing)
         End Try
     End Sub

     'Required by the Windows Form Designer
     Private components As System.ComponentModel.IContainer

     'NOTE: The following procedure is required by the Windows Form Designer;
     'It can be modified using the Windows Form Designer;
     'Do not modify it using the code editor
     <System.Diagnostics.DebuggerStepThrough()> _
     Private Sub InitializeComponent()
         Me.StatesListBox = New System.Windows.Forms.ListBox
         Me.WorkflowsComboBox = New System.Windows.Forms.ComboBox
         Me.WorkflowLabel = New System.Windows.Forms.Label
         Me.StatesLabel = New System.Windows.Forms.Label
         Me.DaysLabel = New System.Windows.Forms.Label
         Me.DaysNumericUpDown = New System.Windows.Forms.NumericUpDown
         CType(Me.DaysNumericUpDown, System.ComponentModel.ISupportInitialize).BeginInit()
         Me.SuspendLayout()
         '
         'StatesListBox
         '
         Me.StatesListBox.FormattingEnabled = True
         Me.StatesListBox.ItemHeight = 16
         Me.StatesListBox.Location = New System.Drawing.Point(25, 119)
         Me.StatesListBox.Name = "StatesListBox"
         Me.StatesListBox.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended
         Me.StatesListBox.Size = New System.Drawing.Size(164, 132)
         Me.StatesListBox.TabIndex = 0
         '
         'WorkflowsComboBox
         '
         Me.WorkflowsComboBox.FormattingEnabled = True
         Me.WorkflowsComboBox.Location = New System.Drawing.Point(25, 43)
         Me.WorkflowsComboBox.Name = "WorkflowsComboBox"
         Me.WorkflowsComboBox.Size = New System.Drawing.Size(164, 24)
         Me.WorkflowsComboBox.TabIndex = 1
         '
         'WorkflowLabel
         '
         Me.WorkflowLabel.AutoSize = True
         Me.WorkflowLabel.Location = New System.Drawing.Point(27, 15)
         Me.WorkflowLabel.Name = "WorkflowLabel"
         Me.WorkflowLabel.Size = New System.Drawing.Size(117, 17)
         Me.WorkflowLabel.TabIndex = 2
         Me.WorkflowLabel.Text = "Choose Workflow"
         '
         'StatesLabel
         '
         Me.StatesLabel.AutoSize = True
         Me.StatesLabel.Location = New System.Drawing.Point(27, 89)
         Me.StatesLabel.Name = "StatesLabel"
         Me.StatesLabel.Size = New System.Drawing.Size(101, 17)
         Me.StatesLabel.TabIndex = 3
         Me.StatesLabel.Text = "Select State(s)"
         '
         'DaysLabel
         '
         Me.DaysLabel.AutoSize = True
         Me.DaysLabel.Location = New System.Drawing.Point(27, 275)
         Me.DaysLabel.Name = "DaysLabel"
         Me.DaysLabel.Size = New System.Drawing.Size(162, 17)
         Me.DaysLabel.TabIndex = 4
         Me.DaysLabel.Text = "Number of Days in State"
         '
         'DaysNumericUpDown
         '
         Me.DaysNumericUpDown.Location = New System.Drawing.Point(30, 304)
         Me.DaysNumericUpDown.Name = "DaysNumericUpDown"
         Me.DaysNumericUpDown.Size = New System.Drawing.Size(159, 22)
         Me.DaysNumericUpDown.TabIndex = 5
         '
         'SetupPage
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(8.0!, 16.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.Controls.Add(Me.DaysNumericUpDown)
         Me.Controls.Add(Me.DaysLabel)
         Me.Controls.Add(Me.StatesLabel)
         Me.Controls.Add(Me.WorkflowLabel)
         Me.Controls.Add(Me.WorkflowsComboBox)
         Me.Controls.Add(Me.StatesListBox)
         Me.Name = "SetupPage"
         Me.Size = New System.Drawing.Size(216, 342)
         CType(Me.DaysNumericUpDown, System.ComponentModel.ISupportInitialize).EndInit()
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents StatesListBox As System.Windows.Forms.ListBox
     Friend WithEvents WorkflowsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents WorkflowLabel As System.Windows.Forms.Label
     Friend WithEvents StatesLabel As System.Windows.Forms.Label
     Friend WithEvents DaysLabel As System.Windows.Forms.Label
     Friend WithEvents DaysNumericUpDown As System.Windows.Forms.NumericUpDown

 End Class
```

[Back to top](#top)

```
'Class1.vb
```

```vb
 Imports EPDM.Interop.epdm
 Imports System.Runtime.InteropServices

 <Guid("")>
 <ComVisible(True)>
 Public Class Class1
     Implements IEdmAddIn5

     Dim SetupPageObj As SetupPage

     Public Sub GetAddInInfo( _
           ByRef poInfo As EdmAddInInfo, _
           ByVal poVault As IEdmVault5, _
           ByVal poCmdMgr As IEdmCmdMgr5) _
           Implements IEdmAddIn5.GetAddInInfo
         Try

             poInfo.mbsAddInName = "VB.NET Workflow State Age Task Add-In"
             poInfo.mbsCompany = "Dassault Systemes"
             poInfo.mbsDescription = "Example demonstrates " _
       + "a scheduled task that finds files that have been in selected workflow states a selected number of days"
             poInfo.mlAddInVersion = 1
             'Minimum SOLIDWORKS PDM Professional version
             'needed for tasks is 10.0
             poInfo.mlRequiredVersionMajor = 10
             poInfo.mlRequiredVersionMinor = 0

             'Register to call OnCmd on task-related events
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskSetup)
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskSetupButton)
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskRun)
             poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskDetails)
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

             Select Case poCmd.meCmdType

                 'Called from the Administration tool when
                 'the user selects this task add-in from the
                 'drop-down list and whenever this task is
                 'subsequently edited in the Administration tool
                 Case EdmCmdType.EdmCmd_TaskSetup
                     OnTaskSetup(poCmd, ppoData)

                 'Sent when the user clicks OK or
                 'Cancel in the task property dialog box
                 Case EdmCmdType.EdmCmd_TaskSetupButton
                     OnTaskSetupButton(poCmd, ppoData)

                 'Called whenever an instance of the
                 'task is run
                 Case EdmCmdType.EdmCmd_TaskRun
                     OnTaskRun(poCmd, ppoData)

                 'Called from the Task List in the
                 'Administration tool whenever the task details
                 'dialog is displayed
                 Case EdmCmdType.EdmCmd_TaskDetails
                     OnTaskDetails(poCmd, ppoData)
             End Select

         Catch ex As Runtime.InteropServices.COMException
             MsgBox("HRESULT = 0x" + _
                ex.ErrorCode.ToString("X") + vbCrLf + _
                ex.Message)
         Catch ex As Exception
             MsgBox(ex.Message)
         End Try

     End Sub

     Private Sub OnTaskSetup(ByRef poCmd As EdmCmd, _
         ByRef ppoData As System.Array)
         Try
             Dim props As IEdmTaskProperties = poCmd.mpoExtra
             If Not props Is Nothing Then
                 'Set the task properties
                 props.TaskFlags = _
                   EdmTaskFlag.EdmTask_SupportsScheduling + _
                   EdmTaskFlag.EdmTask_SupportsDetails

                 SetupPageObj = New SetupPage( _
                   poCmd.mpoVault, props)
                 'Force immediate creation of the control
                 'and its handle
                 SetupPageObj.CreateControl()
                 SetupPageObj.LoadData(poCmd)

                 Dim pages(0) As EdmTaskSetupPage
                 'Name that appears in the
                 'navigation pane of the Add Task dialog
                 'in the Administration tool
                 pages(0).mbsPageName = "Choose states to check"
                 pages(0).mlPageHwnd = SetupPageObj.Handle.ToInt32
                 pages(0).mpoPageImpl = SetupPageObj

                 props.SetSetupPages(pages)

             End If

         Catch ex As Runtime.InteropServices.COMException
             MsgBox("HRESULT = 0x" + _
                ex.ErrorCode.ToString("X") + vbCrLf + _
                ex.Message)
         Catch ex As Exception
             MsgBox(ex.Message)
         End Try
     End Sub

     Private Sub OnTaskSetupButton(ByRef poCmd As EdmCmd, _
         ByRef ppoData As System.Array)
         Try
             'Custom setup page, SetupPageObj, is created
             'in method SetupPage::OnTaskSetup; SetupPage::StoreData
             'saves the contents of the list box to poCmd.mpoExtra
             'in the IEdmTaskProperties interface
             If poCmd.mbsComment = "OK" And _
                 Not SetupPageObj Is Nothing Then
                 SetupPageObj.StoreData()
             End If
             SetupPageObj = Nothing

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
         Try
             Dim TaskInstance As IEdmTaskInstance
             TaskInstance = poCmd.mpoExtra
             If Not TaskInstance Is Nothing Then
                 TaskInstance.SetStatus( _
                   EdmTaskStatus.EdmTaskStat_Running)
                 TaskInstance.SetProgressRange(100, 0, _
                   "Task is running.")

                 Dim NoDays As String
                 NoDays = TaskInstance.GetValEx("NoDaysVar")

                 Dim States As String = ""
                 States = TaskInstance.GetValEx( _
                   "SelectedStatesVar")

                 Dim Items As List(Of EdmSelItem2) = _
                   New List(Of EdmSelItem2)

                 DoSearch(poCmd.mpoVault, States, NoDays, Items)

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

                 TaskInstance.SetProgressPos(100, ProgresssMsg)
                 TaskInstance.SetStatus( _
                   EdmTaskStatus.EdmTaskStat_DoneOK, 0, "", _
                   NotificationArray, ProgresssMsg)
             End If

         Catch ex As Runtime.InteropServices.COMException
             MsgBox("HRESULT = 0x" + _
                ex.ErrorCode.ToString("X") + vbCrLf + _
                ex.Message)
         Catch ex As Exception
             MsgBox(ex.Message)
         End Try
     End Sub

     Public Sub DoSearch(ByVal Vault As IEdmVault11, _
         ByVal States As String, ByVal Days As String, _
         ByVal Items As List(Of EdmSelItem2))
         Try
             'Calculate date to use in file search
             Dim dt As DateTime = DateTime.Today
             Dim DaysInt As Integer = Convert.ToInt32(Days) - 1
             Dim ts As TimeSpan = New TimeSpan(DaysInt, 0, 0, 0)
             dt = dt.Subtract(ts)

             'Split States into an array of strings
             Dim StatesObj As Object = Split(States, vbCrLf)
             'Search for files with the specified state age
             For Each State As String In StatesObj
                 'Skip empty strings
                 If Trim(State) = "" Then
                     Continue For
                 End If

                 Dim Search As IEdmSearch6 = Vault.CreateSearch()
                 If Search Is Nothing Then Return

                 Search.FindFiles = True
                 Search.SetToken( _
                   EdmSearchToken.Edmstok_StateBefore, dt)
                 Search.SetToken( _
                   EdmSearchToken.Edmstok_StateName, State)

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
             Next State

         Catch ex As Runtime.InteropServices.COMException
             MsgBox("HRESULT = 0x" + _
                ex.ErrorCode.ToString("X") + vbCrLf + _
                ex.Message)
         Catch ex As Exception
             MsgBox(ex.Message)
         End Try
     End Sub

     Private Sub OnTaskDetails(ByRef poCmd As EdmCmd, _
         ByRef ppoData As System.Array)
         Try
             Dim TaskInstance As IEdmTaskInstance = _
               poCmd.mpoExtra
             If Not TaskInstance Is Nothing Then
                 SetupPageObj = New SetupPage( _
                   poCmd.mpoVault, TaskInstance)
                 'Force immediate creation of the control
                 'and its handle
                 SetupPageObj.CreateControl()
                 SetupPageObj.LoadData(poCmd)
                 SetupPageObj.DisableControls()
                 poCmd.mbsComment = "State Age Details"
                 poCmd.mlParentWnd = SetupPageObj.Handle.ToInt32()
             End If

         Catch ex As Runtime.InteropServices.COMException
             MsgBox("HRESULT = 0x" + _
                ex.ErrorCode.ToString("X") + vbCrLf + _
                ex.Message)
         Catch ex As Exception
             MsgBox(ex.Message)
         End Try
     End Sub

 End Class
```

[Back to top](#top)
