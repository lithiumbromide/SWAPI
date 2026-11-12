---
title: "Update References Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Update_References_Example_VBNET.htm"
---

# Update References Example (VB.NET)

This example shows how to update the references of a file in a vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Start Microsoft Visual Studio.
' 2. Click File > New > Project > Visual Basic,
Windows, Desktop > Windows Forms App

' 3. Type UpdateReferences in Project
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
'12. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays your Update References dialog box.
'  2. Select a vault view.
'  3. Click Browse.
'  4. Displays the Select a file dialog box.
'     a. Click a file in the selected vault.
'     b. Click Open.
'     The selected file's path and file name appear
'     in the Select a file dialog box.
'  5. Click Update references.
'  6. Initializes and displays SOLIDWORKS PDM Professional's Update References
'     dialog box, which shows the name of the selected file whose file references
'     to update and the names of the file references, if any.
'  7. Click Close.
'  8. Close your Update References dialog box.
'----------------------------------------------------------------------------
'Form1.vb
Imports EPDM.Interop.epdm

Public Class Form1

    Private vault1 As IEdmVault5 = Nothing
    Dim aFile As IEdmFile5
    Dim fileName As String

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

    Public Sub UpdateReferencesButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles UpdateReferencesButton.Click
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

            'Update the references for the selected document
            'and show SOLIDWORKS PDM Professional Update References dialog
            Dim updateRefs As IEdmUpdateReferences
            updateRefs = vault1.CreateUtility(EdmUtility.EdmUtil_UpdateReferences)
            updateRefs.AddFile(fileName)
            updateRefs.ShowDlg(Me.Handle.ToInt32(), 0, 0)

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
                fileName = OpenFileDialog1.FileName
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
```

```
Back to top
```

```
'Form1.Designer.vb
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
        Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
        Me.FileListBox = New System.Windows.Forms.ListBox()
        Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
        Me.BrowseButton = New System.Windows.Forms.Button()
        Me.UpdateReferencesButton = New System.Windows.Forms.Button()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.SuspendLayout()
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
        'UpdateReferencesButton
        '
        Me.UpdateReferencesButton.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.UpdateReferencesButton.Location = New System.Drawing.Point(28, 152)
        Me.UpdateReferencesButton.Name = "UpdateReferencesButton"
        Me.UpdateReferencesButton.Size = New System.Drawing.Size(109, 23)
        Me.UpdateReferencesButton.TabIndex = 5
        Me.UpdateReferencesButton.Text = "Update references"
        Me.UpdateReferencesButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.UpdateReferencesButton.UseVisualStyleBackColor = True
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(28, 25)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(91, 13)
        Me.Label1.TabIndex = 6
        Me.Label1.Text = "Select vault view:"
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(323, 184)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.UpdateReferencesButton)
        Me.Controls.Add(Me.BrowseButton)
        Me.Controls.Add(Me.FileListBox)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Name = "Form1"
        Me.Text = "Update File References"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents FileListBox As System.Windows.Forms.ListBox
    Friend WithEvents BrowseButton As System.Windows.Forms.Button
    Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog
    Friend WithEvents UpdateReferencesButton As System.Windows.Forms.Button
    Friend WithEvents Label1 As System.Windows.Forms.Label

End Class
```

```
Back to top
```
