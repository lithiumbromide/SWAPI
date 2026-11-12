---
title: "Update File Raw References Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Update_File_Raw_References_Example_VBNET.htm"
---

# Update File Raw References Example (VB.NET)

This example shows how to get file references directly from a file and update file references directly in that file.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Start Microsoft Visual Studio.
' 2. Click File > New > Project > Visual Basic,
Windows, Desktop > Windows Forms App

' 3. Type RawReferences in Project
name.
' 4. For Location, click ... and navigate to the folder where to
create the project.

' 5. Click Next.

' 6. Select Framework.

' 7. Click Create.
' 8. Click Show All Files in the Solution Explorer toolbar and expand

'    Form1.vb in the Solution Explorer.
' 9. Add dependencies and
safely pass arrays of structures.
'10. Replace the code in Form1.vb with this code.
'11. To create the form, replace the code in Form1.Designer.vb with
'    this code.
'12. Check out a SOLIDWORKS assembly or drawing document whose file
'    references you want to update and check out all of the document's
'    referenced files.
'13. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays the Update Raw References in File dialog box.
'  2. Select the vault view where the SOLIDWORKS assembly or
'     drawing document that you checked out in
'     Preconditions step 4 resides.
'  3. Click Open file.
'  4. Displays the Open a file dialog box.
'     a. Click the assembly or drawing document you checked
'        out in Preconditions step 4.
'     b. Click Open.
'     The opened file's path and file name appear
'     in the Update Raw References in File dialog box.
'  5. Click Get references.
'     a. Displays a message box for each referenced file.
'        The referenced file's ID, path and file name, file name,
'        type, and number of times referenced appear in the
'        message box.
'     b. Click OK to close each message box.
'  6. Rename one of the referenced files in the selected vault
'     in File Explorer.
'  7. Click Update references.
'     a. Displays a message box confirming that references were updated.
'     b. Click OK to close the message box.
'  8. Click Get references.
'     a. Displays a message box for each referenced file.
'        The referenced file's ID, path and file name, file name,
'        type, and number of times referenced appear in the
'        message box. Note that the renamed file is now a referenced
'        file of the open document.
'     b. Click OK to close each message box.
'  9. Click Close file.
' 10. Click OK to close the message box confirming that the
'     open document was closed.
' 11. Close the Update Raw References in File dialog box.
' 12. Check in the SOLIDWORKS assembly or drawing and its
'     file references.
'----------------------------------------------------------------------------
'Form1.vb
Imports EPDM.Interop.epdm

Public Class Form1

    Private vault1 As IEdmVault5 = Nothing
    Dim aFile As IEdmFile5
    Dim fileName As String
    Dim rawRefs As IEdmRawReferenceMgr
    Dim refs() As EdmRawReference = Nothing

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

    Public Sub UpdateButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles UpdateButton.Click
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

            'Update the file references directly in the file
            rawRefs.UpdateReferences(refs)
            MessageBox.Show("File references updated.")

        Catch ex As System.Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)
        End Try
    End Sub

    Public Sub OpenButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles OpenButton.Click
        Try
            'If one hasn't been created yet
            If vault1 Is Nothing Then
                vault1 = New EdmVault5()
            End If

            If Not vault1.IsLoggedIn Then
                'Log into selected vault as the current user
                vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
            End If
            'Set the initial directory in the Open a file dialog
            OpenFileDialog1.InitialDirectory = vault1.RootFolderPath
            'Show the Open a file dialog
            Dim DialogResult As System.Windows.Forms.DialogResult = Nothing
            DialogResult = OpenFileDialog1.ShowDialog()

            If Not (DialogResult = System.Windows.Forms.DialogResult.OK) Then
                'Do nothing
            Else
                'Open a file
                fileName = OpenFileDialog1.FileName
                FileListBox.Items.Add(fileName)
                aFile = vault1.GetFileFromPath(fileName)

            End If

            'Get IEdmRawReferences interface
            rawRefs = vault1.CreateUtility(EdmUtility.EdmUtil_RawReferenceMgr)
            Dim fileRefsSupported As Boolean
            fileRefsSupported = rawRefs.Open(fileName)
            If Not fileRefsSupported Then
                MessageBox.Show("File's format does not support file references.")
                Exit Sub
            End If

        Catch ex As System.Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)
        End Try
    End Sub

    Private Sub GetButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GetButton.Click
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

            Dim arrSize As Integer
            Dim i As Integer = 0
            Dim message As String
            'Get the file references directly from the file
            rawRefs.GetReferences(refs)
            arrSize = refs.Length
            If arrSize = 0 Then
                MessageBox.Show("No file references for opened file.")
                Exit Sub
            End If
            While i < arrSize
                message = "File reference information: " + vbLf + vbLf
                message = message + "  Internal ID: " + refs(i).mbsRefID + vbLf
                message = message + "  Referenced how: " + refs(i).mbsIncludePath + vbLf
                message = message + "  Reference name: " + refs(i).mbsRefName + vbLf
                message = message + "  Number of times file referenced = " + refs(i).mlCount.ToString + vbLf
                Select Case refs(i).mlFlags
                    Case EdmRawRefFlags.Edmrrf_Ghost
                        message = message + "  Type = DWG files can store grandchildren as references" + vbLf
                    Case EdmRawRefFlags.Edmrrf_InternalComponent
                        message = message + "  Type = Not used" + vbLf
                    Case EdmRawRefFlags.Edmrrf_Nothing
                        message = message + "  Type = Normal file reference" + vbLf
                End Select
                i = i + 1
                MessageBox.Show(message)
            End While

        Catch ex As System.Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)
        End Try
    End Sub

    Private Sub CloseButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles CloseButton.Click
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

            'Close the file
            rawRefs.Close()
            MessageBox.Show("File closed.")

        Catch ex As System.Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)
        End Try
    End Sub
End Class
```

```
Back to top
```

```
'Form.Designer.vb
```

```
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
        Me.Label1 = New System.Windows.Forms.Label()
        Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
        Me.OpenButton = New System.Windows.Forms.Button()
        Me.GetButton = New System.Windows.Forms.Button()
        Me.UpdateButton = New System.Windows.Forms.Button()
        Me.CloseButton = New System.Windows.Forms.Button()
        Me.FileListBox = New System.Windows.Forms.ListBox()
        Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
        Me.SuspendLayout()
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(88, 26)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(91, 13)
        Me.Label1.TabIndex = 0
        Me.Label1.Text = "Select vault view:"
        '
        'VaultsComboBox
        '
        Me.VaultsComboBox.FormattingEnabled = True
        Me.VaultsComboBox.Location = New System.Drawing.Point(55, 42)
        Me.VaultsComboBox.Name = "VaultsComboBox"
        Me.VaultsComboBox.Size = New System.Drawing.Size(154, 21)
        Me.VaultsComboBox.TabIndex = 1
        '
        'OpenButton
        '
        Me.OpenButton.Location = New System.Drawing.Point(55, 88)
        Me.OpenButton.Name = "OpenButton"
        Me.OpenButton.Size = New System.Drawing.Size(154, 23)
        Me.OpenButton.TabIndex = 2
        Me.OpenButton.Text = "Open file"
        Me.OpenButton.UseVisualStyleBackColor = True
        '
        'GetButton
        '
        Me.GetButton.Location = New System.Drawing.Point(12, 165)
        Me.GetButton.Name = "GetButton"
        Me.GetButton.Size = New System.Drawing.Size(108, 23)
        Me.GetButton.TabIndex = 3
        Me.GetButton.Text = "Get references"
        Me.GetButton.UseVisualStyleBackColor = True
        '
        'UpdateButton
        '
        Me.UpdateButton.Location = New System.Drawing.Point(164, 165)
        Me.UpdateButton.Name = "UpdateButton"
        Me.UpdateButton.Size = New System.Drawing.Size(108, 23)
        Me.UpdateButton.TabIndex = 4
        Me.UpdateButton.Text = "Update references"
        Me.UpdateButton.UseVisualStyleBackColor = True
        '
        'CloseButton
        '
        Me.CloseButton.Location = New System.Drawing.Point(55, 222)
        Me.CloseButton.Name = "CloseButton"
        Me.CloseButton.Size = New System.Drawing.Size(154, 23)
        Me.CloseButton.TabIndex = 5
        Me.CloseButton.Text = "Close file"
        Me.CloseButton.UseVisualStyleBackColor = True
        '
        'FileListBox
        '
        Me.FileListBox.FormattingEnabled = True
        Me.FileListBox.Location = New System.Drawing.Point(12, 118)
        Me.FileListBox.Name = "FileListBox"
        Me.FileListBox.Size = New System.Drawing.Size(260, 30)
        Me.FileListBox.TabIndex = 6
        '
        'OpenFileDialog1
        '
        Me.OpenFileDialog1.FileName = "OpenFileDialog1"
        Me.OpenFileDialog1.Multiselect = True
        Me.OpenFileDialog1.Title = "Open a file"
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(284, 264)
        Me.Controls.Add(Me.FileListBox)
        Me.Controls.Add(Me.CloseButton)
        Me.Controls.Add(Me.UpdateButton)
        Me.Controls.Add(Me.GetButton)
        Me.Controls.Add(Me.OpenButton)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Controls.Add(Me.Label1)
        Me.Name = "Form1"
        Me.Text = "Update References in File"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents OpenButton As System.Windows.Forms.Button
    Friend WithEvents GetButton As System.Windows.Forms.Button
    Friend WithEvents UpdateButton As System.Windows.Forms.Button
    Friend WithEvents CloseButton As System.Windows.Forms.Button
    Friend WithEvents FileListBox As System.Windows.Forms.ListBox
    Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog

End Class
```

```
Back to top
```
