---
title: "Set Part Numbers Using Default Serial Numbers Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Set_Part_Number_Using_Default_Serial_Numbers_Example_VBNET.htm"
---

# Set Part Numbers Using Default Serial Numbers Example (VB.NET)

This example shows how to set part numbers using default serial numbers.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Start Microsoft Visual Studio.
' 2. Click File > New > Project > Visual Basic,
Windows, Desktop > Windows Forms App

' 3. Type SerialNumbers in Project
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
'12. Ensure that you have:
'     * a vault with at least one serial number generator.
'     * a checked-out file in that vault with its Part Number variable's
'       default set to a serial number.
'13. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays the Serial Numbers dialog box.
'  2. Select a vault view.
'  3. Click Get Vault Serial Number Names.
'  4. Displays a message box containing the names of the serial number
'     generators for the selected vault.
'  5. Click OK to close the message box.
'  6. Click Browse.
'     a. Click a checked-out file in the selected vault whose
'        data card has a Part Number variable.
'     b. Click Open.
'     The selected file's path and file name appear in the Serial
'     Numbers dialog box.
'  7. Click Set New Serial Number.
'  8. Displays a message box verifying that the Part Number was
'     set and shows the value of that Part Number.
'     NOTES:
'     * The value set for the Part Number is the next number in the first
'       serial number generator shown in the message box displayed in
'       step 3.
'     * Make note of the Part Number.
'  9. Click OK to close the message box.
' 10. Check in the file whose Part Number was set in step 7, then check out
'     file.
' 11. Examine the Part Number on the data card of the checked-out file.
' 12. Close the Serial Numbers dialog box.
'----------------------------------------------------------------------------
'Form1.vb
Imports EPDM.Interop.epdm

Public Class Form1

    Private vault1 As IEdmVault5 = Nothing
    Dim aSerialNbrName As String
    Dim aFileName As String
    Dim aFile As IEdmFile5
    Dim aFolder As String
    Dim serialNbrs As IEdmSerNoGen7

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

    Public Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Try
            'Only create a new vault object
            'if one hasn't been created yet
            Dim vault2 As IEdmVault11 = Nothing
            If vault1 Is Nothing Then
                vault1 = New EdmVault5()
            End If
            vault2 = DirectCast(vault1, IEdmVault7)
            If Not vault1.IsLoggedIn Then
                'Log into selected vault as the current user
                vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
            End If

            serialNbrs = vault2.CreateUtility(EdmUtility.EdmUtil_SerNoGen)
            Dim names() As String = {}
            serialNbrs.GetSerialNumberNames(names)
            Dim myMessage As String = ""
            myMessage = "Serial number names in selected vault: " + vbLf + vbLf
            Dim idx As Integer
            idx = LBound(names)
            While (idx <= UBound(names))
                myMessage = myMessage + names(idx) + vbLf
                idx = idx + 1
            End While

            ' Use this serial number generator
            aSerialNbrName = names(0)

            MessageBox.Show(myMessage)

        Catch ex As System.Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)
        End Try
    End Sub

    Public Sub BrowseButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BrowseButton.Click
        Try

            'Set the initial directory in the Select a file dialog
            OpenFileDialog1.InitialDirectory = vault1.RootFolderPath
            'Show the Select a file dialog
            Dim DialogResult As System.Windows.Forms.DialogResult = Nothing
            DialogResult = OpenFileDialog1.ShowDialog()

            If Not (DialogResult = System.Windows.Forms.DialogResult.OK) Then
                ' Do nothing
            Else
                ' Browse for a file whose serial number to set
                ' File's data card must have a Part Number associated
                ' with a serial number generator and must be checked out
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

    Public Sub NewButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles NewButton.Click
        Try

            Dim serialNbrValue As IEdmSerNoValue
            serialNbrValue = serialNbrs.AllocSerNoValue(aSerialNbrName, Me.Handle.ToInt32)
            Dim serialNbrValueValue = serialNbrValue.Value
            Dim enumVariable As IEdmEnumeratorVariable5
            enumVariable = aFile.GetEnumeratorVariable(aFileName)
            Dim serialNbrValueObj As Object = Nothing
            ' Set the Part Number of the selected file
            enumVariable.SetVar("Part Number", "@", serialNbrValueValue)
            enumVariable.CloseFile(True)

            MessageBox.Show("Part Number set to " + serialNbrValueValue.ToString + "." + vbLf)

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
        Me.Button1 = New System.Windows.Forms.Button()
        Me.FileListBox = New System.Windows.Forms.ListBox()
        Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
        Me.BrowseButton = New System.Windows.Forms.Button()
        Me.NewButton = New System.Windows.Forms.Button()
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
        'Button1
        '
        Me.Button1.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.Button1.Location = New System.Drawing.Point(28, 84)
        Me.Button1.Name = "Button1"
        Me.Button1.Size = New System.Drawing.Size(190, 23)
        Me.Button1.TabIndex = 2
        Me.Button1.Text = "Get Vault Serial Number Names"
        Me.Button1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.Button1.UseVisualStyleBackColor = True
        '
        'FileListBox
        '
        Me.FileListBox.FormattingEnabled = True
        Me.FileListBox.Location = New System.Drawing.Point(28, 141)
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
        Me.BrowseButton.Location = New System.Drawing.Point(239, 135)
        Me.BrowseButton.Name = "BrowseButton"
        Me.BrowseButton.Size = New System.Drawing.Size(56, 23)
        Me.BrowseButton.TabIndex = 4
        Me.BrowseButton.Text = "Browse..."
        Me.BrowseButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.BrowseButton.UseVisualStyleBackColor = True
        '
        'NewButton
        '
        Me.NewButton.Location = New System.Drawing.Point(28, 182)
        Me.NewButton.Name = "NewButton"
        Me.NewButton.Size = New System.Drawing.Size(190, 23)
        Me.NewButton.TabIndex = 5
        Me.NewButton.Text = "Set New Serial Number"
        Me.NewButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.NewButton.UseVisualStyleBackColor = True
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(326, 262)
        Me.Controls.Add(Me.NewButton)
        Me.Controls.Add(Me.BrowseButton)
        Me.Controls.Add(Me.FileListBox)
        Me.Controls.Add(Me.Button1)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Controls.Add(Me.VaultsLabel)
        Me.Name = "Form1"
        Me.Text = "Serial Numbers"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents VaultsLabel As System.Windows.Forms.Label
    Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents Button1 As System.Windows.Forms.Button
    Friend WithEvents FileListBox As System.Windows.Forms.ListBox
    Friend WithEvents BrowseButton As System.Windows.Forms.Button
    Friend WithEvents NewButton As System.Windows.Forms.Button
    Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog

End Class
```

```
Back to top
```
