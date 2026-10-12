---
title: "Get File's State Transitions Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_Files_State_Transitions_Example_VBNET.htm"
---

# Get File's State Transitions Example (VB.NET)

This example shows how to get a file's current and next possible state transitions.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 ' 2. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms Application.
 ' 3. Type StatesVBNET in Project name.
  ' 4. For Location, click ... and navigate to the folder where to create the project.
 ' 5. Click Next.
 ' 6. Select Framework.
 ' 7. Click Create.
 ' 8. Click Show All Files in the Solution Explorer toolbar and expand
 '    Form1.vb in the Solution Explorer.
 ' 9.  Add dependencies and safely pass arrays of structures.
 '10. Replace the code in Form1.vb with this code.
 '11. To create the form, replace the code in Form1.Designer.vb with
 '    this code.
 '12. Ensure that the vault contains a file in a workflow state.
 '13. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the State Transitions dialog box.
 ' 2. Select a vault view.
 ' 3. Click Browse.
 ' 4. Displays the Select a file dialog box.
 '    a. Select a file in the selected vault.
 '    b. Click Open.
 '    The selected file's path and file name appear
 '    in the Select a file dialog box.
 ' 5. Click Get state transitions.
 ' 6. Displays a message box showing the name of the selected
 '    file and its current and next possible state transitions.
 ' 7. Click OK to close the message box.
 ' 8. Displays a message box showing whether the logged-in user must
 '    add a comment when transitioning the selected file to one of its next
 '    possible states.
 ' 9. Click OK to close the message box.
 '10. Displays a message box with the archive server log.
 '11. Click OK to close the message box.
 '12. Close the State Transitions dialog box.
 '----------------------------------------------------------------------------
 'Form1.vb
 Imports EPDM.Interop.epdm

 Public Class Form1

     Private vault1 As IEdmVault5 = Nothing
     Dim aFile As IEdmFile5

     Private Sub Form1_Load( _
       ByVal sender As System.Object, _
       ByVal e As System.EventArgs) _
       Handles MyBase.Load

         Try
             Dim vault As IEdmVault8 = New EdmVault5
             Dim Views() As EdmViewInfo = Nothing

             vault.GetVaultViews(Views, False)
             VaultsComboBox.Items.Clear()
             For Each View As EdmViewInfo In Views
                 VaultsComboBox.Items.Add(View.mbsVaultName)
             Next
             If VaultsComboBox.Items.Count > 0 Then
                 VaultsComboBox.Text = VaultsComboBox.Items(0)
             End If

         Catch ex As Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + _
               ex.ErrorCode.ToString("X") + vbCrLf + _
               ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub GetTransitionButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GetTransitionButton.Click
         Try
             'Only create a new vault object
             'if one hasn't been created yet
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If

             If Not vault1.IsLoggedIn Then
                 'Log into selected vault as the current user
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim vault2 As IEdmVault20
             vault2 = vault1

             'Get the file's current workflow state
             Dim workflowState As IEdmState5
             workflowState = aFile.CurrentState

             'Start an enumeration of the transitions to
             'and from the file's current workflow state
             Dim pos As IEdmPos5
             pos = workflowState.GetFirstTransitionPosition

             'Make sure current workflow state
             'has a next transition state
             'If not, exit application
             If pos.IsNull Then
                 MessageBox.Show("No next possible transition states.")
                 Exit Sub
             End If

             Dim transition As IEdmTransition10

             'Get the file's next possible transition to or from
             'the file's current workflow state
             transition = workflowState.GetNextTransition(pos)

             Dim message As String = "Current state for " + aFile.Name + ": " + vbLf
             message = message + "  * " + workflowState.Name + vbLf + vbLf
             message = message + "Next possible state transitions for " + aFile.Name + ":" + vbLf
             message = message + "  * " + transition.Name + vbLf
             'message = message + "    Requires authentication? " + transition.Authentication.ToString + vbLf

             'Iterate through the file's remaining next possible
             'transitions to or from the file's current workflow state
             While (Not pos.IsNull)
                 transition = workflowState.GetNextTransition(pos)
                 message = message + "  * " + transition.Name + vbLf
                 'message = message + "    Requires authentication? " + transition.Authentication.ToString + vbLf
             End While

             'Display a message box showing the file's name and its
             'next possible state transitions
             MessageBox.Show(message)
```

```
	    Dim userMgr As IEdmUserMgr10
            userMgr = vault2.CreateUtility(EdmUtility.EdmUtil_UserMgr)
            Dim user As IEdmUser5
            user = userMgr.GetLoggedInUser()
            Dim files(0) As Integer
            files(0) = aFile.ID
            Dim transitions(0) As String
            transitions(0) = transition.Name 'a possible transition
            Dim permBool As Object

            permBool = vault2.GetTransitionCommentPermissions(user.ID, files, transitions)
            message = "Logged-in user, " & user.Name & ", must add a state change comment on " & transition.Name & " for " & aFile.Name & "? " & permBool(0)

	    'Display a message box showing whether the logged-in user must add a comment
            'when transitioning the file to one of the next possible states
            MessageBox.Show(message)
```

```vb
             'Display a message box with the archive server log
             Dim asLog As String = ""
             vault1.GetArchiveServerLog(asLog)
             message = "Archive server log: " & asLog
             MessageBox.Show(message)

         Catch ex As System.Runtime.InteropServices.COMException

             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)

         Catch ex As Exception

             MessageBox.Show(ex.Message)

         End Try

     End Sub

     Public Sub BrowseButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BrowseButton.Click

         Try

             'If one hasn't been created yet

             If vault1 Is Nothing Then

                 vault1 = New EdmVault5()

             End If

             If Not vault1.IsLoggedIn Then

                 'Log into selected vault as the current user

                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())

             End If

             'Set the initial directory in the Select a file dialog

             OpenFileDialog1.InitialDirectory = vault1.RootFolderPath

             'Show the Select a file dialog

             Dim DialogResult As System.Windows.Forms.DialogResult = Nothing

             DialogResult = OpenFileDialog1.ShowDialog()

             If Not (DialogResult = System.Windows.Forms.DialogResult.OK) Then

                 'Do nothing

             Else

                 'Browse for a file whose next possible state

                 'transitions to get

                 Dim fileName As String = OpenFileDialog1.FileName

                 FileListBox.Items.Add(fileName)

                 aFile = vault1.GetFileFromPath(fileName)

             End If

         Catch ex As System.Runtime.InteropServices.COMException

             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)

         Catch ex As Exception

             MessageBox.Show(ex.Message)

         End Try

     End Sub

 End Class

Back to top
 'Form1.Designer.vb
<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
 Partial Class Form1
     Inherits System.Windows.Forms.Form

     'Form overrides dispose to clean up the component list.
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

     'NOTE: The following procedure is required by the Windows Form Designer
     'It can be modified using the Windows Form Designer.
     'Do not modify it using the code editor.
     <System.Diagnostics.DebuggerStepThrough()> _
     Private Sub InitializeComponent()
         Me.VaultsLabel = New System.Windows.Forms.Label()
         Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
         Me.FileListBox = New System.Windows.Forms.ListBox()
         Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
         Me.BrowseButton = New System.Windows.Forms.Button()
         Me.GetTransitionButton = New System.Windows.Forms.Button()
         Me.SuspendLayout()
         '
         'VaultsLabel
         '
         Me.VaultsLabel.AutoSize = True
         Me.VaultsLabel.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
         Me.VaultsLabel.Location = New System.Drawing.Point(25, 28)
         Me.VaultsLabel.Name = "VaultsLabel"
         Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
         Me.VaultsLabel.TabIndex = 0
         Me.VaultsLabel.Text = "Select vault view:"
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(28, 44)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(190, 21)
         Me.VaultsComboBox.TabIndex = 1
         '
         'FileListBox
         '
         Me.FileListBox.FormattingEnabled = True
         Me.FileListBox.Location = New System.Drawing.Point(28, 97)
         Me.FileListBox.Name = "FileListBox"
         Me.FileListBox.Size = New System.Drawing.Size(190, 17)
         Me.FileListBox.TabIndex = 3
         '
         'OpenFileDialog1
         '
         Me.OpenFileDialog1.FileName = "OpenFileDialog1"
         Me.OpenFileDialog1.Multiselect = True
         Me.OpenFileDialog1.Title = "Select a file"
         '
         'BrowseButton
         '
         Me.BrowseButton.Location = New System.Drawing.Point(236, 97)
         Me.BrowseButton.Name = "BrowseButton"
         Me.BrowseButton.Size = New System.Drawing.Size(56, 23)
         Me.BrowseButton.TabIndex = 4
         Me.BrowseButton.Text = "Browse..."
         Me.BrowseButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
         Me.BrowseButton.UseVisualStyleBackColor = True
         '
         'GetTransitionButton
         '
         Me.GetTransitionButton.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
         Me.GetTransitionButton.Location = New System.Drawing.Point(28, 152)
         Me.GetTransitionButton.Name = "GetTransitionButton"
         Me.GetTransitionButton.Size = New System.Drawing.Size(201, 23)
         Me.GetTransitionButton.TabIndex = 5
         Me.GetTransitionButton.Text = "Get next possible state transitions"
         Me.GetTransitionButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
         Me.GetTransitionButton.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(323, 184)
         Me.Controls.Add(Me.GetTransitionButton)
         Me.Controls.Add(Me.BrowseButton)
         Me.Controls.Add(Me.FileListBox)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Workflow State Transitions"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents FileListBox As System.Windows.Forms.ListBox
     Friend WithEvents BrowseButton As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog
     Friend WithEvents GetTransitionButton As System.Windows.Forms.Button

 End Class
Back to top
```
