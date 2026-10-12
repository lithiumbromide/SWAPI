---
title: "Get Files in Workflow State Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_Files_in_State_Example_VBNET.htm"
---

# Get Files in Workflow State Example (VB.NET)

This example shows how to get all of the files in a particular workflow state.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 ' 2. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms App.
 ' 3. Type GetFilesInState in Project name.
  ' 4. For Location, click ... and navigate to the folder where to create the project.
 ' 5. Click Next.
 ' 6. Select Framework.
 ' 7. Click Create.
 ' 8. Click Show All Files in the Solution Explorer toolbar and expand
 '    Form1.vb in the Solution Explorer.
 ' 9.  Add dependencies and safely pass arrays of structures.
 '10. Replace the code in Form1.vb with this code.
 '11. To create the form, replace the code in Form1.Designer.vb with this code.
 '12. Ensure that you have at least one approved file in the vault.
 '13. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Get files in state dialog box.
 ' 2. Select a vault view.
 ' 3. Click Get approved files.
  ' 4. Displays a message box with all of the files in the Approved state
 '    for each workflow in the vault.
 ' 5. Click OK in each message box.
  ' 6. Close the Get files in state dialog box.
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
     Dim item As IEdmItem
     Dim fileInt As IEdmFile8

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

     Public Sub GetApprovedFiles_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GetApprovedFiles.Click
         'Get approved files
         Try

             Dim vault2 As IEdmVault7
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If

             vault2 = vault1
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim wfmgr As IEdmWorkflowMgr6 = vault2.CreateUtility(EdmUtility.EdmUtil_WorkflowMgr)

             Dim pos As IEdmPos5
             pos = wfmgr.GetFirstWorkflowPosition()
             While Not pos.IsNull
                 Dim wf As IEdmWorkflow6 = wfmgr.GetNextWorkflow(pos)

                 Dim state As IEdmState6
                 state = wf.GetState("Approved")

                 If Not state Is Nothing Then
                     Dim message As String
                     Dim file As IEdmFile5
                     Dim pos2 As IEdmPos5
                     pos2 = state.GetFirstFilePosition

                     If Not pos2.IsNull Then
                         message = "These files are approved in workflow, " & wf.Name & ":" + vbLf
                         While Not pos2.IsNull
                             file = state.GetNextFile(pos2)
                             message = message + file.Name + vbLf
                         End While
                         MessageBox.Show(message)
                     End If
                 End If
             End While

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
     ''' <summary>
     ''' Required designer variable.
     ''' </summary>
     Private components As System.ComponentModel.IContainer = Nothing

     ''' <summary>
     ''' Clean up any resources being used.
     ''' </summary>
     ''' <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
     Protected Overrides Sub Dispose(ByVal disposing As Boolean)
         If disposing AndAlso (components IsNot Nothing) Then
             components.Dispose()
         End If
         MyBase.Dispose(disposing)
     End Sub

 #Region "Windows Form Designer generated code"

     ''' <summary>
     ''' Required method for Designer support - do not modify
     ''' the contents of this method with the code editor.
     ''' </summary>
     Private Sub InitializeComponent()
         Me.VaultsLabel = New System.Windows.Forms.Label()
         Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
         Me.GetApprovedFiles = New System.Windows.Forms.Button()
         Me.SuspendLayout()
         '
         'VaultsLabel
         '
         Me.VaultsLabel.AutoSize = True
         Me.VaultsLabel.Location = New System.Drawing.Point(13, 26)
         Me.VaultsLabel.Name = "VaultsLabel"
         Me.VaultsLabel.Size = New System.Drawing.Size(94, 13)
         Me.VaultsLabel.TabIndex = 0
         Me.VaultsLabel.Text = " Select vault view:"
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(16, 42)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(121, 21)
         Me.VaultsComboBox.TabIndex = 1
         '
         'GetApprovedFiles
         '
         Me.GetApprovedFiles.Location = New System.Drawing.Point(16, 86)
         Me.GetApprovedFiles.Name = "GetApprovedFiles"
         Me.GetApprovedFiles.Size = New System.Drawing.Size(139, 23)
         Me.GetApprovedFiles.TabIndex = 5
         Me.GetApprovedFiles.Text = "Get approved files"
         Me.GetApprovedFiles.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(216, 137)
         Me.Controls.Add(Me.GetApprovedFiles)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Get files in state"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents GetApprovedFiles As System.Windows.Forms.Button
 End Class
```

[Back to top](#top)
