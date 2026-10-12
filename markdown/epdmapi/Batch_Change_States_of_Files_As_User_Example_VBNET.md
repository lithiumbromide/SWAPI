---
title: "Batch Change States of Files As User Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Batch_Change_States_of_Files_As_User_Example_VBNET.htm"
---

# Batch Change States of Files As User Example (VB.NET)

This example shows how to change the states of several files in one batch using other credentials.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 '    a. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms Application.
 '    b. Type BatchChangeFileStates in Project name.
 '    c. For Location, click ... and navigate to the folder where to create the project.
'      d. Click Next.
'    e. Select Framework.
'    f. Click Create.
'    g. Click Show All Files in the Solution Explorer toolbar and expand
'       Form1.vb in the Solution Explorer.
 '    h. Replace the code in Form1.vb with this code.
 '    i. To create the form, replace the code in Form1.Designer.vb with
 '       this code.
 ' 2. Add dependencies and safely pass arrays of structures.
 ' 3. In the Admin Tool, ensure that a workflow exists with:
 '    a. A Waiting for Approval state.
 '    b. An Approved state.
 '    c. A Passed Approval transition from the Waiting for Approval state to
 '       the Approved state.
 '    d. One or more vault files in the Waiting for Approval state.
 ' 4. If you want to change states as another user, modify the RunAsUser credentials to match a user in your vault.
 ' 5. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. The Approve Files dialog box displays.
 '    a. Select a vault view.
 '    b. Click Select files to approve.
 '    c. In the Select File dialog:
 '       1. Select vault files in the Waiting for Approval state.
 '       2. Click Open.
 '    d. Click Approve all files.
 ' 2. Click OK in the Do Transition dialog box.
 '    The selected files change to the Approved state using the Passed Approval
 '    transition.
 ' 3. Close the Approve Files dialog box.
  '----------------------------------------------------------------------------
 'Form1.vb
 Imports System.IO
 Imports System.Xml.Serialization
 Imports System.Collections
 Imports System.Collections.Generic
 Imports System.Data
 Imports System.Diagnostics
 Imports System.Windows.Forms
 Imports System.ComponentModel
 Imports EPDM.Interop.epdm

 Public Class Form1

     Private vault1 As IEdmVault5 = Nothing
     Dim batchChanger As IEdmBatchChangeState6
     Dim aFile As IEdmFile5
     Dim aFolder As IEdmFolder5
     Dim aPos As IEdmPos5
     Dim retVal As Boolean
     Public Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

         Try
             Dim vault1 As IEdmVault5 = New EdmVault5()
             Dim vault As IEdmVault8 = DirectCast(vault1, IEdmVault8)
             Dim Views As EdmViewInfo() = Nothing

             vault.GetVaultViews(Views, False)
             VaultsComboBox.Items.Clear()
             For Each View As EdmViewInfo In Views
                 VaultsComboBox.Items.Add(View.mbsVaultName)
             Next
             If VaultsComboBox.Items.Count > 0 Then
                 VaultsComboBox.Text = DirectCast(VaultsComboBox.Items(0), String)
             End If
         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub Transition_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Transition.Click
         Try
             'File1List.Items.Clear()

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             'Set the initial directory in the Select File dialog
             OpenFileDialog1.InitialDirectory = vault1.RootFolderPath
             'Show the Select File dialog
             Dim DialogResult As System.Windows.Forms.DialogResult = Nothing
             DialogResult = OpenFileDialog1.ShowDialog()
             'If the user didn't click Open, exit this subroutine
             If Not (DialogResult = System.Windows.Forms.DialogResult.OK) Then
                 Return
             End If

             batchChanger = vault2.CreateUtility(EdmUtility.EdmUtil_BatchChangeState)

             For Each FileName As String In OpenFileDialog1.FileNames
                 File1List.Items.Add(FileName)
                 aFile = vault1.GetFileFromPath(FileName)
                 aPos = aFile.GetFirstFolderPosition
                 aFolder = aFile.GetNextFolder(aPos)
                 ' Add each file selected to the batch
                 batchChanger.AddFile(aFile.ID, aFolder.ID)
             Next

             batchChanger.Comment = "Transition to Approved state."

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub BatchChange_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BatchChange.Click
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             ' Get the available transitions
             Dim ppoTransitions() As EdmChangeStateTransitionInfo = Nothing
             batchChanger.GetAvailableTransitionList(ppoTransitions)

             Dim i As Integer = 0
             Dim str As String = ""
             While i <= ppoTransitions.GetUpperBound(0)
                 If i = 0 Then
                     str = ppoTransitions(i).moName
                 Else
                     str = str + ", " + ppoTransitions(i).moName
                 End If
                 i = i + 1
             End While

             'MsgBox("Transitions available: " & str)

             ' Get list of files affected by the state transition
             Dim selList As IEdmSelectionList6
             selList = batchChanger.GetFileList(EdmChangeStateFileListFlag.Ecsflf_GetActionUpdated + EdmChangeStateFileListFlag.Ecsflf_GetChanged + EdmChangeStateFileListFlag.Ecsflf_GetUnprocessed)

             Dim selObject As EdmSelectionObject = New EdmSelectionObject()

             aPos = selList.GetHeadPosition()
             str = "Files affected by this state transition: "
             i = 0
             While i < selList.Count
                 selList.GetNext2(aPos, selObject)
                 str = str + selObject.mbsPath
                 i = i + 1
             End While

             'MsgBox(str)

             ' Create the file reference tree and verify allowed transitions
```

'''''''''''''''''''''''''''''''''''''RunAsUser API''''''''''''''''''''''''''''''''''''''''''''
' Admin is the logged in user here, but if you uncomment the next line (batchChanger.RunAsUser),
' you will do a state change using the admin_jeda user.
' Change the username and password to match a user that exists in your vault.
' CreateTree, ShowDlg, and ChangeState2 should all be called after RunAsUser.

```vb
            'batchChanger.RunAsUser(Me.Handle.ToInt32(), "Admin_jeda", "abc")
             retVal = batchChanger.CreateTree("Passed Approval")

             Dim retVal2 As Boolean
             If (retVal) Then
                 ' Show all of the items in the batch
                 retVal2 = batchChanger.ShowDlg(Me.Handle.ToInt32())

                 If (retVal2) Then
                     ' User clicked OK; commit all of the items in the batch to the vault
                     batchChanger.ChangeState2(Me.Handle.ToInt32(), "")
                 End If
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
         Me.Transition = New System.Windows.Forms.Button()
         Me.File1List = New System.Windows.Forms.ListBox()
         Me.BatchChange = New System.Windows.Forms.Button()
         Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
         Me.SuspendLayout()
         '
         'VaultsLabel
         '
         Me.VaultsLabel.AutoSize = True
         Me.VaultsLabel.Location = New System.Drawing.Point(36, 24)
         Me.VaultsLabel.Name = "VaultsLabel"
         Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
         Me.VaultsLabel.TabIndex = 0
         Me.VaultsLabel.Text = "Select vault view:"
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(39, 40)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(121, 21)
         Me.VaultsComboBox.TabIndex = 1
         '
         'Transition
         '
         Me.Transition.Location = New System.Drawing.Point(39, 85)
         Me.Transition.Name = "Transition"
         Me.Transition.Size = New System.Drawing.Size(158, 23)
         Me.Transition.TabIndex = 2
         Me.Transition.Text = "Select files to approve..."
         Me.Transition.UseVisualStyleBackColor = True
         '
         'File1List
         '
         Me.File1List.FormattingEnabled = True
         Me.File1List.HorizontalScrollbar = True
         Me.File1List.Location = New System.Drawing.Point(40, 114)
         Me.File1List.Name = "File1List"
         Me.File1List.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended
         Me.File1List.Size = New System.Drawing.Size(220, 43)
         Me.File1List.TabIndex = 4
         '
         'BatchChange
         '
         Me.BatchChange.Location = New System.Drawing.Point(40, 183)
         Me.BatchChange.Name = "BatchChange"
         Me.BatchChange.Size = New System.Drawing.Size(157, 23)
         Me.BatchChange.TabIndex = 6
         Me.BatchChange.Text = "Approve all files"
         Me.BatchChange.UseVisualStyleBackColor = True
         '
         'OpenFileDialog1
         '
         Me.OpenFileDialog1.FileName = "OpenFileDialog1"
         Me.OpenFileDialog1.Multiselect = True
         Me.OpenFileDialog1.Title = "Select File"
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(284, 235)
         Me.Controls.Add(Me.BatchChange)
         Me.Controls.Add(Me.File1List)
         Me.Controls.Add(Me.Transition)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Approve Files"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents Transition As System.Windows.Forms.Button
     Friend WithEvents File1List As System.Windows.Forms.ListBox
     Friend WithEvents BatchChange As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog

 End Class

Back to top
```
