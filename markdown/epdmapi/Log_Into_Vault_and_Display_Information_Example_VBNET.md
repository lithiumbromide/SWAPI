---
title: "Log Into Vault and Display Information Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Log_Into_Vault_and_Display_Information_Example_VBNET.htm"
---

# Log Into Vault and Display Information Example (VB.NET)

This example shows how to create an application that displays a form where a user can select a vault to which to log in and display information about that vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Start Microsoft Visual Studio.
' 2. Click File > New > Project > Visual Basic,
Windows, Desktop > Windows Forms App

' 3. Type Exercise1 in Project
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
'11. To create the form, replace the code in Form1.Designer.vb with this code.
'12. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays a dialog.
'  2. Select a vault.
'  3. Click Log in and display vault information.
'     A message box pops up containing the version of
'     SOLIDWORKS PDM Professional installed on your computer.
'  4. Click OK to close the message box.
'     Another message box pops up containing the path of the selected
'     vault view folder.
'  5. Click OK to close the message box.
'  6. Type the name of a nonexistent vault in the drop-down combo box.
'  7. Click Log in and display vault information.
'  8. A message box pops up instructing you to type or select
'     a valid database.
'  9. Click OK to close the message box.
' 10. Close the dialog box.
'----------------------------------------------------------------------------

'Form1
Imports EPDM.Interop.epdm
Imports EPDM.Interop.EPDMResultCode

Public Class Exercise1

    Private Sub Exercise1_Load( _
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

    Private Sub LoginButton_Click( _
      ByVal sender As System.Object, _
      ByVal e As System.EventArgs) _
      Handles LoginButton.Click

        Try
            'Declare and create an instance of IEdmVault5 object
            Dim vault As IEdmVault5 = New EdmVault5()
            'Log into the selected vault as the current user
            vault.LoginAuto(VaultsComboBox.Text, _
              Me.Handle.ToInt32())

            'Display the SOLIDWORKS PDM Professional version
            Dim VerMajor As Integer
            Dim VerMinor As Integer
            vault.GetVersion(VerMajor, VerMinor)
            MessageBox.Show("SOLIDWORKS PDM Professional " + _
              "version is " + VerMajor.ToString() + "." + _
              VerMinor.ToString())

            'Display the path of the vault view folder
            MessageBox.Show("The path of the vault view " + _
              "folder is """ + vault.RootFolderPath + """.")

        Catch ex As Runtime.InteropServices.COMException

            Select Case ex.ErrorCode
                Case EdmResultErrorCodes_e.E_EDM_CANT_OPEN_DATABASE
                    MessageBox.Show("Could not open database. Select or type the name of valid database.")
                Case Else
                    MessageBox.Show("HRESULT = 0x" + _
                    ex.ErrorCode.ToString("X") + vbCrLf + _
                    ex.Message)
            End Select

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
Partial Class Exercise1
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
        Me.LoginButton = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'VaultsLabel
        '
        Me.VaultsLabel.AutoSize = True
        Me.VaultsLabel.Location = New System.Drawing.Point(42, 9)
        Me.VaultsLabel.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.VaultsLabel.Name = "VaultsLabel"
        Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
        Me.VaultsLabel.TabIndex = 4
        Me.VaultsLabel.Text = "Select vault view:"
        Me.VaultsLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        '
        'VaultsComboBox
        '
        Me.VaultsComboBox.FormattingEnabled = True
        Me.VaultsComboBox.Location = New System.Drawing.Point(19, 41)
        Me.VaultsComboBox.Margin = New System.Windows.Forms.Padding(2, 2, 2, 2)
        Me.VaultsComboBox.Name = "VaultsComboBox"
        Me.VaultsComboBox.Size = New System.Drawing.Size(132, 21)
        Me.VaultsComboBox.TabIndex = 3
        '
        'LoginButton
        '
        Me.LoginButton.Location = New System.Drawing.Point(19, 88)
        Me.LoginButton.Margin = New System.Windows.Forms.Padding(2, 2, 2, 2)
        Me.LoginButton.Name = "LoginButton"
        Me.LoginButton.Size = New System.Drawing.Size(132, 37)
        Me.LoginButton.TabIndex = 5
        Me.LoginButton.Text = "Log in and display vault information"
        Me.LoginButton.UseVisualStyleBackColor = True
        '
        'Exercise1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(176, 154)
        Me.Controls.Add(Me.LoginButton)
        Me.Controls.Add(Me.VaultsLabel)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Margin = New System.Windows.Forms.Padding(2, 2, 2, 2)
        Me.Name = "Exercise1"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
   Friend WithEvents VaultsLabel As System.Windows.Forms.Label
   Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
   Friend WithEvents LoginButton As System.Windows.Forms.Button

End Class
```

```
Back to top
```
