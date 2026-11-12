---
title: "Send Message to Users Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Send_Message_to_Users_Example_VBNET.htm"
---

# Send Message to Users Example (VB.NET)

This example shows how to send a message, also called a notification, to logged-in users who have permission to modify Categories.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
'  1. Start Microsoft Visual Studio 2010.
'  2. Click File > New > Project > Visual Basic > Windows Forms Application.
'  3. Type Exercise3 in Name.
'  4. Click the Browse button and browse to the folder where to create the project.
'  5. Click OK.
'  6. Create a form similar to the form shown above and change:
'     a. Label to VaultsLabel.
'     b. Combo box to VaultsComboBox.
'     c. Button to TraverseUsersButton.
'  7. Replace the code in Form1.vb with this code.
'  8. Replace the code in Form1.Designer.vb with this code.
'  9. Add EPDM.Interop.epdm.dll as a reference (right-click the project
'     name in the Solution Explorer, click Add Reference, click
'     Framework in the left-side panel, browse to the top folder of your
'     SOLIDWORKS PDM Professional installation, locate and click
'     EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
' 10. Right-click EPDM.Interop.epdm in References, click Properties, and set
'     Embed Interop Types to False to handle methods that pass arrays of
'     structures.
' 11. Switch back to the Form1.vb code window.
' 12. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays a dialog.
'  2. Select a vault.
'  3. Click the Send message to users who can modify Categories button.
'  4. After several minutes, a SOLIDWORKS PDM Professional notification
'     is displayed only to logged-in users who have permission
'     to modify Categories.
'  5. To open the the message, click:
'     * either the notification while it is displayed or
'       the SOLIDWORKS PDM Professional tray icon.
'       - or -
'     * Tools > Inbox in File Explorer.
'  6. Close the dialog.
'----------------------------------------------------------------------------
```

```
'Form1.vb

Imports EPDM.Interop.epdm

Public Class Exercise3

  Private Sub Exercise3_Load( _
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

  Private Sub TraverseUsersButton_Click( _
    ByVal sender As System.Object, _
    ByVal e As System.EventArgs) _
    Handles TraverseUsersButton.Click

    Try
      'Declare and create an instance of IEdmVault5 object
      Dim vault As IEdmVault5 = New EdmVault5()
      'Log into selected vault as the current user
      vault.LoginAuto(VaultsComboBox.Text, _
        Me.Handle.ToInt32())

      'Declare an IEdmUserMgr5 object
      Dim UserMgr As IEdmUserMgr5
      'The IEdmUserMgr5 interface is implemented by the
      'same class as the IEdmVault5 interface,
      'so in VB we can simply assign the value of
      'the IEdmVault5 object
      UserMgr = vault

      Dim UserPos As IEdmPos5
      UserPos = UserMgr.GetFirstUserPosition()
      While Not UserPos.IsNull
        Dim User As IEdmUser7
        User = UserMgr.GetNextUser(UserPos)
        If User.IsLoggedIn Then
          If User.HasSysRightEx(EdmSysPerm. _
            EdmSysPerm_ModifyCategories) _
            Then
            User.SendMsg("Category request", _
              "Please stop by my office sometime " + _
              "this morning to discuss adding " + _
              "a new file type to a Category.")
          End If
        End If
      End While

    Catch ex As Runtime.InteropServices.COMException
      MessageBox.Show("HRESULT = 0x" + _
        ex.ErrorCode.ToString("X") + vbCrLf + _
        ex.Message)
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
Partial Class Exercise3
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
        Me.TraverseUsersButton = New System.Windows.Forms.Button()
        Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
        Me.VaultsLabel = New System.Windows.Forms.Label()
        Me.SuspendLayout()
        '
        'TraverseUsersButton
        '
        Me.TraverseUsersButton.Location = New System.Drawing.Point(57, 90)
        Me.TraverseUsersButton.Margin = New System.Windows.Forms.Padding(2, 2, 2, 2)
        Me.TraverseUsersButton.Name = "TraverseUsersButton"
        Me.TraverseUsersButton.Size = New System.Drawing.Size(136, 67)
        Me.TraverseUsersButton.TabIndex = 18
        Me.TraverseUsersButton.Text = "Send message to users who can modify Categories"
        Me.TraverseUsersButton.UseVisualStyleBackColor = True
        '
        'VaultsComboBox
        '
        Me.VaultsComboBox.FormattingEnabled = True
        Me.VaultsComboBox.Location = New System.Drawing.Point(57, 41)
        Me.VaultsComboBox.Margin = New System.Windows.Forms.Padding(2, 2, 2, 2)
        Me.VaultsComboBox.Name = "VaultsComboBox"
        Me.VaultsComboBox.Size = New System.Drawing.Size(136, 21)
        Me.VaultsComboBox.TabIndex = 16
        '
        'VaultsLabel
        '
        Me.VaultsLabel.AutoSize = True
        Me.VaultsLabel.Location = New System.Drawing.Point(71, 9)
        Me.VaultsLabel.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.VaultsLabel.Name = "VaultsLabel"
        Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
        Me.VaultsLabel.TabIndex = 17
        Me.VaultsLabel.Text = "Select vault view:"
        '
        'Exercise3
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(252, 168)
        Me.Controls.Add(Me.TraverseUsersButton)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Controls.Add(Me.VaultsLabel)
        Me.Margin = New System.Windows.Forms.Padding(2, 2, 2, 2)
        Me.Name = "Exercise3"
        Me.Text = "Send Message to Users"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
   Friend WithEvents TraverseUsersButton As System.Windows.Forms.Button
   Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
   Friend WithEvents VaultsLabel As System.Windows.Forms.Label

End Class
```

```
Back to top
```
