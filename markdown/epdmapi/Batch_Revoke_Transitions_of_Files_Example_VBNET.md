---
title: "Batch Revoke State Transitions of Files Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Batch_Revoke_Transitions_of_Files_Example_VBNET.htm"
---

# Batch Revoke State Transitions of Files Example (VB.NET)

This example shows how to revoke the state transitions of several files in one batch.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 '  1. Start Microsoft Visual Studio.
 '     a. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms Application.
 '     b. Type BatchChangeFileStates in Project name.
 '     c. For Location, click ... and navigate to the folder where to create the project.
'       d. Click Next.
'     e. Select Framework.
'     f. Click Create.
'     g. Click Show All Files in the Solution Explorer toolbar and expand
'        Form1.vb in the Solution Explorer.
 '     h. Replace the code in Form1.vb with this code.
 '     i. To create the form, replace the code in Form1.Designer.vb with
 '        this code.
 '  2. Add dependencies and safely pass arrays of structures.
 '  3. Ensure that:
 '     a. A workflow exists with a No Approval Required transition.
 '     b. One or more vault files are transitioned to the Approved state using the
 '        No Approval Required transition.
 '  4. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 '  1. The Revoke state transitions dialog box displays.
 '     a. Select a vault view.
 '     b. Click Select files for which to revoke transitions.
 '     c. In the Select File dialog:
 '        1. Select a file that transitioned to the Approved state using the
 '           No Approval Required transition.
 '        2. Click Open.
 '  2. Click Revoke transitions.
 '  3. Click OK in the Revoke Transition dialog box.
 '     The selected file's No Approval Required transition is revoked.
 '  4. Close the Revoke state transitions dialog box.
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
     Dim batchChanger As IEdmBatchChangeState3
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

     Public Sub SelectFiles_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles SelectFiles.Click
         Try
             File1List.Items.Clear()

             Dim vault2 As IEdmVault11 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault11)

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

             batchChanger.Comment = "Revoke transitions."
             batchChanger.AllowAdminToRevoke(True)
             'batchChanger.SetRevokeUserID(vault2.GetLoggedInWindowsUserID(vault2.Name))

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub RevokeTransitions_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles RevokeTransitions.Click
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             ' Get list of files affected by the transition revocation
             Dim selList As IEdmSelectionList6
             selList = batchChanger.GetFileList(EdmChangeStateFileListFlag.Ecsflf_GetChanged)

             Dim selObject As EdmSelectionObject = New EdmSelectionObject()

             Dim str As String
             Dim i As Integer
             aPos = selList.GetHeadPosition()
             str = "Files affected by this transition revocation: "
             i = 0
             While i < selList.Count
                 selList.GetNext2(aPos, selObject)
                 str = str + selObject.mbsPath
                 i = i + 1
             End While

             'MsgBox(str)

             ' Create the file reference tree and verify transition revocation
             retVal = batchChanger.CreateTreeForRevoke("No Approval Required")

             Dim retVal2 As Boolean
             If (retVal) Then
                 ' Show all of the items in the batch
                 retVal2 = batchChanger.ShowDlg(Me.Handle.ToInt32())

                 If (retVal2) Then
                     ' Commit all of the items in the batch to the vault
                     batchChanger.ChangeState(Me.Handle.ToInt32())
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
         Me.SelectFiles = New System.Windows.Forms.Button()
         Me.File1List = New System.Windows.Forms.ListBox()
         Me.RevokeTransitions = New System.Windows.Forms.Button()
         Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
         Me.SuspendLayout()
         '
         'VaultsLabel
         '
         Me.VaultsLabel.AutoSize = True
         Me.VaultsLabel.Location = New System.Drawing.Point(12, 24)
         Me.VaultsLabel.Name = "VaultsLabel"
         Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
         Me.VaultsLabel.TabIndex = 0
         Me.VaultsLabel.Text = "Select vault view:"
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(15, 40)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(121, 21)
         Me.VaultsComboBox.TabIndex = 1
         '
         'SelectFiles
         '
         Me.SelectFiles.Location = New System.Drawing.Point(15, 85)
         Me.SelectFiles.Name = "SelectFiles"
         Me.SelectFiles.Size = New System.Drawing.Size(233, 23)
         Me.SelectFiles.TabIndex = 2
         Me.SelectFiles.Text = "Select files for which to revoke transitions..."
         Me.SelectFiles.UseVisualStyleBackColor = True
         '
         'File1List
         '
         Me.File1List.FormattingEnabled = True
         Me.File1List.HorizontalScrollbar = True
         Me.File1List.Location = New System.Drawing.Point(15, 114)
         Me.File1List.Name = "File1List"
         Me.File1List.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended
         Me.File1List.Size = New System.Drawing.Size(257, 43)
         Me.File1List.TabIndex = 4
         '
         'RevokeTransitions
         '
         Me.RevokeTransitions.Location = New System.Drawing.Point(40, 183)
         Me.RevokeTransitions.Name = "RevokeTransitions"
         Me.RevokeTransitions.Size = New System.Drawing.Size(157, 23)
         Me.RevokeTransitions.TabIndex = 6
         Me.RevokeTransitions.Text = "Revoke transitions"
         Me.RevokeTransitions.UseVisualStyleBackColor = True
         '
         'OpenFileDialog1
         '
         Me.OpenFileDialog1.FileName = "OpenFileDialog1"
         Me.OpenFileDialog1.Multiselect = False
         Me.OpenFileDialog1.Title = "Select File"
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(284, 235)
         Me.Controls.Add(Me.RevokeTransitions)
         Me.Controls.Add(Me.File1List)
         Me.Controls.Add(Me.SelectFiles)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Revoke state transitions"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents SelectFiles As System.Windows.Forms.Button
     Friend WithEvents File1List As System.Windows.Forms.ListBox
     Friend WithEvents RevokeTransitions As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog

 End Class
```

[Back to top](#top)
