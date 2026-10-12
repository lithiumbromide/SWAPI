---
title: "Get Messages Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_Messages_Example_VBNET.htm"
---

# Get Messages Example (VB.NET)

This example shows how to get and encapsulate text messages in the Admin's inbox in a vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Start Microsoft Visual Studio.
' 2. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms App.
' 3. Type MessageVBNET in Project name.
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
'12. Ensure that one or more text messages exist in the inbox of Admin
'    in a vault.
'     a. Log into a vault as Admin.
'     b. Open a File Explorer window for that vault.
'     c. Click Tools > Inbox.
'     d. Click Text Messages.
'     e. If no text messages are listed, send a text message to Admin.
'        1. Click New mail message.
'        2. Type Admin in To.
'        3. Type Test Get messages in Subject.
'        4. Type Testing Get messages in the body of the message.
'        5. Click Send.
'        6. Wait until you receive the SOLIDWORKS PDM Professional
'           message notification before executing the next step.
'13. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays the Get Messages dialog.
'  2. Select the vault that you examined or where you sent Admin
'     a text message in Preconditions step 4.
'  3. Click Get messages.
'  4. Displays a message box for each text message in Admin's inbox
'     in the selected vault. The message box contains encapsulated
'     information about the text message.
'  5. Click OK to close each message box.
'  6. Close the Get Messages dialog box.
'----------------------------------------------------------------------------

'Form1.vb

Imports EPDM.Interop.epdm

Public Class Form1

    Dim vault As IEdmVault8 = New EdmVault5

    Private Sub Form1_Load( _
      ByVal sender As System.Object, _
      ByVal e As System.EventArgs) _
      Handles MyBase.Load

        Try

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

    Private Sub GetMessagesButton_Click( _
      ByVal sender As System.Object, _
      ByVal e As System.EventArgs) _
      Handles GetMessagesButton.Click

        Try
            'Only create a new vault object
            'if one hasn't been created yet
            If vault Is Nothing Then
                vault = New EdmVault5()
            End If

            If Not vault.IsLoggedIn Then
                'Log into selected vault as the current user
                vault.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
            End If

            'Declare an IEdmUserMgr5 object
            Dim userMgr As IEdmUserMgr5

            'The IEdmUserMgr5 interface is implemented by the
            'same class as the IEdmVault5 interface,
            'so you can assign the value of
            'the IEdmVault5 object
            userMgr = vault

            Dim user As IEdmUser5
            user = userMgr.GetLoggedInUser
            Dim inbox As IEdmInbox5 = DirectCast(user, IEdmInbox5)

            'Get first text message in Admin's inbox
            Dim message As IEdmMessage5
            Dim pos As IEdmPos5
            pos = inbox.GetFirstMessagePosition(EdmGetMsgFlag.EdmGetMsg_UserMessages)

            'If no text messages in Admin's inbox, exit application
            If pos.IsNull Then
                MsgBox("No messages in Admin's inbox.")
                Exit Sub
            End If

            'Otherwise, iterate through Admin's inbox and
            'display a message box with each encapsulated text message
            While Not pos.IsNull
                message = inbox.GetNextMessage(pos)
                Dim messageDate As String
                messageDate = message.Date

                MsgBox("Sender name = " + message.SenderName + vbLf + _
                        "Sender ID = " + message.SenderID + vbLF + _
                        "Is read = " + message.IsRead.ToString + vbLf + _
                        "Type = " + message.MessageType.ToString + vbLf + _
                        "Date = " + messageDate + vbLf + _
                        "Subject = " + message.Subject + vbLf + _
                        "Body = " + message.Body + vbLf)

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
        Me.GetMessagesButton = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'VaultsLabel
        '
        Me.VaultsLabel.AutoSize = True
        Me.VaultsLabel.Location = New System.Drawing.Point(13, 22)
        Me.VaultsLabel.Name = "VaultsLabel"
        Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
        Me.VaultsLabel.TabIndex = 0
        Me.VaultsLabel.Text = "Select vault view:"
        '
        'VaultsComboBox
        '
        Me.VaultsComboBox.FormattingEnabled = True
        Me.VaultsComboBox.Location = New System.Drawing.Point(13, 39)
        Me.VaultsComboBox.Name = "VaultsComboBox"
        Me.VaultsComboBox.Size = New System.Drawing.Size(198, 21)
        Me.VaultsComboBox.TabIndex = 1
        '
        'GetMessagesButton
        '
        Me.GetMessagesButton.Location = New System.Drawing.Point(16, 81)
        Me.GetMessagesButton.Name = "GetMessagesButton"
        Me.GetMessagesButton.Size = New System.Drawing.Size(88, 23)
        Me.GetMessagesButton.TabIndex = 2
        Me.GetMessagesButton.Text = "Get messages"
        Me.GetMessagesButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.GetMessagesButton.UseVisualStyleBackColor = True
        '
        'MessageVBNET
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(243, 130)
        Me.Controls.Add(Me.GetMessagesButton)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Controls.Add(Me.VaultsLabel)
        Me.Name = "Form1"
        Me.Text = "Get Messages"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents VaultsLabel As System.Windows.Forms.Label
    Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents GetMessagesButton As System.Windows.Forms.Button

End Class
```

```
Back to top
```
