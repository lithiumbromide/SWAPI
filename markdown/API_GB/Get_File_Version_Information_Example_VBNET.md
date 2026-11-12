---
title: "Get File Version Information Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Get_File_Version_Information_Example_VBNET.htm"
---

# Get File Version Information Example (VB.NET)

This example shows how to get the version information of a file.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
'  1. Start Microsoft Visual Studio 2010.
'     a. Click File > New > Project > Visual Basic > Windows Forms Application.
'     b. Type GetFileVersionsVBNET in Name.
'     c. Click Browse and navigate to the folder where to create the project.
'     d. Click OK.
'     e. Click Show All Files in the Solution Explorer toolbar and expand
'        Form1.vb in the Solution Explorer.
'     f. Replace the code in Form1.vb with this code.
'     g. To create the form, replace the code in Form1.Designer.vb with
'        this code.
'  2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
'     name in the Solution Explorer, click Add Reference, click
'     Assemblies > Framework in the left-side panel, browse to the top folder of
'     your SOLIDWORKS PDM Professional installation, locate and click
'     EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
'  3. Right-click EPDM.Interop.epdm in References, click Properties, and set
'     Embed Interop Types to False to handle methods that pass arrays of
'     structures.
'  4. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays the Version Information dialog box.
'     a. Select a vault view.
'     b. Click Browse.
'     c. In the Select a file dialog:
'        1. Click a file in the vault.
'        2. Click Open.
'  2. Click Get file's version information.
'  3. Displays a message box containing the file name, number of versions, and
'     each version's number, date, user, file size, and comments, if any.
'  4. Click OK to close the message box.
'  5. Close the Version Information dialog box.
'----------------------------------------------------------------------------
```

```
'Form1.vb
Imports EPDM.Interop.epdm

Public Class Form1

    Private vault1 As IEdmVault5 = Nothing
    Dim aFile As IEdmFile5
    Dim aPos As IEdmPos5

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

    Public Sub BrowseButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BrowseButton.Click
        Try
            Dim vault2 As IEdmVault7 = Nothing
            If vault1 Is Nothing Then
                vault1 = New EdmVault5()
            End If
            vault2 = DirectCast(vault1, IEdmVault7)

            If Not vault1.IsLoggedIn Then
                vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
            End If

            'Set the initial directory in the Select a file dialog
            OpenFileDialog1.InitialDirectory = vault1.RootFolderPath
            'Show the Select a file dialog
            Dim DialogResult As System.Windows.Forms.DialogResult = Nothing
            DialogResult = OpenFileDialog1.ShowDialog()

            If Not (DialogResult = System.Windows.Forms.DialogResult.OK) Then
                ' Do nothing
            Else
                ' Browse for file whose versions to get
                Dim FileName As String = OpenFileDialog1.FileName
                FileListBox.Items.Add(FileName)
                aFile = vault1.GetFileFromPath(FileName)
            End If

        Catch ex As System.Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)
        End Try
    End Sub

    Public Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Try
            Dim file As IEdmFile5 = Nothing
            file = aFile
            Dim enumVersion = DirectCast(file, IEdmEnumeratorVersion5)
            Dim pos As IEdmPos5
            pos = enumVersion.GetFirstVersionPosition
            Dim version As IEdmVersion7
            Dim message As String
            message = "History of " + file.Name + ": " + vbLf
            message = message + vbLf + "Number of versions: " + enumVersion.VersionCount.ToString + vbLf
            message = message + vbLf
            Dim str As String
            While Not pos.IsNull
                version = enumVersion.GetNextVersion(pos)
                str = "Version: " + version.VersionNo.ToString
                message = message + str
                str = version.VersionDate
                message = message + ", file date = " & str + ", user = " + version.User.Name
                str = version.FileSize2
                message = message + ", file size = " + str + " bytes, comment = " + version.Comment + vbLf
            End While

            MsgBox(message)

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
        Me.Button1 = New System.Windows.Forms.Button()
        Me.BrowseButton = New System.Windows.Forms.Button()
        Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.FileListBox = New System.Windows.Forms.ListBox()
        Me.SuspendLayout()
        '
        'VaultsComboBox
        '
        Me.VaultsComboBox.Location = New System.Drawing.Point(12, 37)
        Me.VaultsComboBox.Name = "VaultsComboBox"
        Me.VaultsComboBox.Size = New System.Drawing.Size(161, 21)
        Me.VaultsComboBox.TabIndex = 7
        '
        'Button1
        '
        Me.Button1.Location = New System.Drawing.Point(12, 135)
        Me.Button1.Name = "Button1"
        Me.Button1.Size = New System.Drawing.Size(158, 23)
        Me.Button1.TabIndex = 4
        Me.Button1.Text = "Get file's version information"
        Me.Button1.UseVisualStyleBackColor = True
        '
        'BrowseButton
        '
        Me.BrowseButton.ImageAlign = System.Drawing.ContentAlignment.TopLeft
        Me.BrowseButton.Location = New System.Drawing.Point(179, 83)
        Me.BrowseButton.Name = "BrowseButton"
        Me.BrowseButton.Size = New System.Drawing.Size(60, 28)
        Me.BrowseButton.TabIndex = 5
        Me.BrowseButton.Text = "Browse..."
        Me.BrowseButton.UseVisualStyleBackColor = True
        '
        'OpenFileDialog1
        '
        Me.OpenFileDialog1.FileName = "OpenFileDialog1"
        Me.OpenFileDialog1.Multiselect = True
        Me.OpenFileDialog1.Title = "Select a file"
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(12, 21)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(91, 13)
        Me.Label1.TabIndex = 6
        Me.Label1.Text = "Select vault view:"
        '
        'FileListBox
        '
        Me.FileListBox.FormattingEnabled = True
        Me.FileListBox.Location = New System.Drawing.Point(12, 81)
        Me.FileListBox.Name = "FileListBox"
        Me.FileListBox.Size = New System.Drawing.Size(161, 30)
        Me.FileListBox.TabIndex = 8
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(252, 175)
        Me.Controls.Add(Me.FileListBox)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.BrowseButton)
        Me.Controls.Add(Me.Button1)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Name = "Form1"
        Me.Text = "Version Information"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents VaultsLabel As System.Windows.Forms.Label
    Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents BrowseButton As System.Windows.Forms.Button
    Friend WithEvents Button1 As System.Windows.Forms.Button
    Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents FileListBox As System.Windows.Forms.ListBox

End Class
```

```
Back to top
```
