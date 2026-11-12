---
title: "Get Revision Names for Local Version of File Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_Revision_Names_for_Local_Version_of_File_Example_VBNET.htm"
---

# Get Revision Names for Local Version of File Example (VB.NET)

This example shows how to get the revision names for a local version of a file.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Start Microsoft Visual Studio.
' 2. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms Application.
' 3. Type RevisionVBNET in Project name.
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
'12. To find a file with a revision scheme:
'     a. Open a vault view in File Explorer.
'     b. Click a file.
'     c. Click Display > History.
'     d. Examine the Event column. If Revision is:
'        * listed in the Event column, then the file has
'          a revision scheme.
'        * not listed in the Event column, then
'          repeat steps 4b - 4d until you find a file with
'          a revision scheme.
'13. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays the Get revision names dialog box.
'  2. Select a vault view.
'  3. Click Browse.
'  4. Displays the Select a file dialog box.
'     a. Click the file identified in Preconditions step 4 in the
'        selected vault.
'     b. Click Open.
'        The selected file's path and file name appear
'        in the Get revision names dialog box.
'  5. Click Get revisions.
'  6. Displays a message box:
'     * telling you that a local copy of the selected file does not exist.
'       - or -
'     * telling you that the selected file does not have a revision scheme.
'       - or -
'     * showing you a list of the names of the revisions for the selected file.
'  7. Click OK to close the message box.
'  8. Close the Get revision names dialog box.
'----------------------------------------------------------------------------
'Form1.vb
Imports EPDM.Interop.epdm

Public Class Form1

    Private vault1 As IEdmVault5 = Nothing
    Dim aFile As IEdmFile5
    Dim folder As IEdmFolder5

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

    Public Sub RevisionButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles RevisionButton.Click
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

            'Get the local version number
            Dim version As Integer
            version = aFile.GetLocalVersionNo(folder.ID)
            If version < 1 Then
                MsgBox("A local copy of " + aFile.Name + " does not exist.")
                Exit Sub
            End If

            'Get the version interface
            Dim verEnum As IEdmEnumeratorVersion5
            verEnum = aFile
            Dim ver As IEdmVersion5
            ver = verEnum.GetVersion(version)

            'Enumerate the revisions
            Dim message As String
            Dim pos As IEdmPos5
            pos = ver.GetFirstRevisionPosition
            If Not pos.IsNull Then

                message = "The following revisions are set on " + aFile.Name + ": " + vbLf
                Dim rev As IEdmRevision5
                While Not pos.IsNull
                    rev = ver.GetNextRevision(pos)
                    message = message + "    " + rev.Name + vbLf
                End While
            Else
                message = "A revision scheme is not defined for " + aFile.Name + "." + vbLf
                MsgBox(message)
                Exit Sub
            End If

            MsgBox(message)

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
                'Browse for a local file whose revisions you want to see
                Dim fileName As String = OpenFileDialog1.FileName
                FileListBox.Items.Add(fileName)
                aFile = vault1.GetFileFromPath(fileName, folder)

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
        Me.VaultsLabel = New System.Windows.Forms.Label()
        Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
        Me.FileListBox = New System.Windows.Forms.ListBox()
        Me.BrowseButton = New System.Windows.Forms.Button()
        Me.RevisionButton = New System.Windows.Forms.Button()
        Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
        Me.SuspendLayout()
        '
        'VaultsLabel
        '
        Me.VaultsLabel.AutoSize = True
        Me.VaultsLabel.Location = New System.Drawing.Point(24, 27)
        Me.VaultsLabel.Name = "VaultsLabel"
        Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
        Me.VaultsLabel.TabIndex = 0
        Me.VaultsLabel.Text = "Select vault view:"
        '
        'VaultsComboBox
        '
        Me.VaultsComboBox.FormattingEnabled = True
        Me.VaultsComboBox.Location = New System.Drawing.Point(27, 44)
        Me.VaultsComboBox.Name = "VaultsComboBox"
        Me.VaultsComboBox.Size = New System.Drawing.Size(166, 21)
        Me.VaultsComboBox.TabIndex = 1
        '
        'OpenFileDialog1
        '
        Me.OpenFileDialog1.FileName = "OpenFileDialog1"
        Me.OpenFileDialog1.Multiselect = True
        Me.OpenFileDialog1.Title = "Select a file"
        '
        'FileListBox
        '
        Me.FileListBox.FormattingEnabled = True
        Me.FileListBox.Location = New System.Drawing.Point(27, 95)
        Me.FileListBox.Name = "FileListBox"
        Me.FileListBox.Size = New System.Drawing.Size(206, 17)
        Me.FileListBox.TabIndex = 2
        '
        'BrowseButton
        '
        Me.BrowseButton.Location = New System.Drawing.Point(239, 89)
        Me.BrowseButton.Name = "BrowseButton"
        Me.BrowseButton.Size = New System.Drawing.Size(62, 23)
        Me.BrowseButton.TabIndex = 3
        Me.BrowseButton.Text = "Browse..."
        Me.BrowseButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.BrowseButton.UseVisualStyleBackColor = True
        '
        'RevisionButton
        '
        Me.RevisionButton.Location = New System.Drawing.Point(27, 140)
        Me.RevisionButton.Name = "RevisionButton"
        Me.RevisionButton.Size = New System.Drawing.Size(88, 23)
        Me.RevisionButton.TabIndex = 4
        Me.RevisionButton.Text = "Get revisions"
        Me.RevisionButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.RevisionButton.UseVisualStyleBackColor = True
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(311, 195)
        Me.Controls.Add(Me.RevisionButton)
        Me.Controls.Add(Me.BrowseButton)
        Me.Controls.Add(Me.FileListBox)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Controls.Add(Me.VaultsLabel)
        Me.Name = "Form1"
        Me.Text = "Get revision names"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents VaultsLabel As System.Windows.Forms.Label
    Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents FileListBox As System.Windows.Forms.ListBox
    Friend WithEvents BrowseButton As System.Windows.Forms.Button
    Friend WithEvents RevisionButton As System.Windows.Forms.Button
    Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog

End Class
```

```
Back to top
```
