---
title: "Traverse Users and Groups in Vault Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Traverse_Users_and_Groups_in_Vault_Example_VBNET.htm"
---

# Traverse Users and Groups in Vault Example (VB.NET)

This example shows how to traverse the users and groups in a vault and send a message, also called a notification, to all logged-in users of the vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Start Microsoft Visual Studio.
'    a. Click File > New > Project > Visual Basic > Windows Forms Application.
'    b. Type UsersAndGroups in Name.
'    c. Click Browse and navigate to the folder where to create the project.
'    d. Click OK.
'    e. Click Show All Files in the Solution Explorer toolbar and expand
'       Form1.vb in the Solution Explorer.
'    f. Replace the code in Form1.vb with this code.
'    g. Replace the code in Form1.Designer.vb with this code.
' 2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
'    name in the Solution Explorer, click Add Reference, click
'    Assemblies > Framework in the left-side panel, browse to the top folder
'    of your SOLIDWORKS PDM Professional installation, locate and click
'    EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
' 3. Right-click EPDM.Interop.epdm in References, click Properties, and set
'    Embed Interop Types to False to handle methods that pass arrays of
'    structures.
' 4. Ensure that the vault contains one or more users and one or more
'    workflows.
' 5. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays a dialog.
'  2. Select a vault.
'  3. Click Traverse users.
'     Three message boxes report:
'     * users in the vault,
'     * state permissions for a user in the vault,
'       - and -
'     * transition permissions for a user in the vault.
'  4. Click OK to close each message box.
'  5. Click Traverse groups.
'     A message box reports the groups in the vault.
'  6. Click OK to close the message box.
'  7. Click Traverse group members.
'     A message box reports the users of each group in the vault.
'  8. Click OK to close the message box.
'  9. Click Send consultation request.
'     After several minutes, a SOLIDWORKS PDM Professional notification
'     appears only to logged-in users.
' 10. To open the message, click:
'     * the notification while it is displayed,
'     * the SOLIDWORKS PDM Professional tray icon,
'       - or -
'     * Tools > Inbox in the vault view.
' 11. Close the dialog.
'----------------------------------------------------------------------------
'Form1.vb
Imports System.IO
Imports System.Xml.Serialization
Imports EPDM.Interop.epdm

Public Class UsersAndGroups

   Private Sub UsersAndGroups_Load(ByVal sender As _
         System.Object, ByVal e As System.EventArgs) _
         Handles MyBase.Load

      Dim vault As IEdmVault8 = New EdmVault5
      Dim Views() As EdmViewInfo = {}

      vault.GetVaultViews(Views, False)
      VaultsComboBox.Items.Clear()
      For Each View As EdmViewInfo In Views
         VaultsComboBox.Items.Add(View.mbsVaultName)
      Next
      If VaultsComboBox.Items.Count > 0 Then
         VaultsComboBox.Text = VaultsComboBox.Items(0)
      End If
   End Sub
```

```vb
     Private Sub TraverseUsersButton_Click(ByVal sender As _
              System.Object, ByVal e As System.EventArgs) _
              Handles TraverseUsersButton.Click

         Dim vault As IEdmVault5 = New EdmVault5()
         Dim vault1 As IEdmVault7 = Nothing

         If vault Is Nothing Then
             vault = New EdmVault5()
         End If

         vault1 = DirectCast(vault, IEdmVault7)

         'Log into selected vault as the current user
         vault1.LoginAuto(VaultsComboBox.Text,
   Me.Handle.ToInt32())

         'Declare an IEdmUserMgr9 object
         Dim UserMgr As IEdmUserMgr9
         UserMgr = vault1.CreateUtility(EdmUtility.EdmUtil_UserMgr)

         Dim ppoPermissions() As EdmStatePermission = {}
         Dim ppoTransitionPermissions() As EdmTransitionPermission = {}

         Dim Users As String = vbNullString
         Dim UserPos As IEdmPos5
         Dim User As IEdmUser5
         UserPos = UserMgr.GetFirstUserPosition()
         While Not UserPos.IsNull

             User = UserMgr.GetNextUser(UserPos)
             Users = Users & User.Name & " ID: " & User.ID & vbCrLf
         End While

         MessageBox.Show(Users, vault1.Name +
         " Vault Users", MessageBoxButtons.OK,
         MessageBoxIcon.Information)

         'Get permissions for all states for a user
         UserMgr.GetStatePermissions(User.ID, EdmObjectType.EdmObject_User, 0, ppoPermissions)
         Dim str As String
         str = "EdmStatePermissions for a user in the vault" & vbLf
         str = str & vbLf
         For Each item As EdmStatePermission In ppoPermissions

             str = str & "mlOwnerID: " & item.mlOwnerID & vbLf
             str = str & "meOwnerType (EdmObjectType.EdmObject_User (7) or EdmObjectType.EdmObject_UserGroup (8)): " & item.meOwnerType & vbLf
             str = str & "mlStateID: " & item.mlStateID & vbLf
             str = str & "mlEdmRightFlag as defined in EdmRightFlags: " & item.mlEdmRightFlag & vbLf
             str = str & vbLf

         Next
         MessageBox.Show(str)

         'Get permissions for all transitions for a user
         UserMgr.GetTransitionPermissions(User.ID, EdmObjectType.EdmObject_User, 0, ppoTransitionPermissions)
         str = "EdmTransitionPermissions for a user in the vault" & vbLf
         str = str & vbLf
         For Each item As EdmTransitionPermission In ppoTransitionPermissions

             str = str & "mlOwnerID: " & item.mlOwnerID & vbLf
             str = str & "meOwnerType (EdmObjectType.EdmObject_User (7) or EdmObjectType.EdmObject_UserGroup (8)): " & item.meOwnerType & vbLf
             str = str & "mlTransitionID: " & item.mlTransitionID & vbLf
             str = str & "mlEdmRightFlag as defined in EdmTransitionRightFlags: " & item.mlEdmRightFlag & vbLf
             str = str & vbLf

         Next
         MessageBox.Show(str)

     End Sub
```

```
   Private Sub TraverseGroupsButton_Click(ByVal sender _
         As System.Object, ByVal e As System.EventArgs) _
         Handles TraverseGroupsButton.Click

      'Declare and create an instance of IEdmVault5 object
      Dim vault As IEdmVault5 = New EdmVault5()
      'Log into selected vault as the current user
      vault.LoginAuto(VaultsComboBox.Text, _
         Me.Handle.ToInt32())

      'Declare an IEdmUserMgr5 object
      Dim UserMgr As IEdmUserMgr5
      'The IEdmUserMgr5 interface is implemented by the
      'same class as the IEdmVault5 interface,
      'so assign the value of the IEdmVault5 object
      UserMgr = vault

      Dim Groups As String = vbNullString
      Dim UserGroupPos As IEdmPos5
      UserGroupPos = UserMgr.GetFirstUserGroupPosition()
      While Not UserGroupPos.IsNull
         Dim UserGroup As IEdmUserGroup5
         UserGroup = UserMgr.GetNextUserGroup _
            (UserGroupPos)
         Groups = Groups + UserGroup.Name + vbCrLf
      End While
      MessageBox.Show(Groups, vault.Name + _
         " Vault Groups", MessageBoxButtons.OK, _
         MessageBoxIcon.Information)
   End Sub

   Private Sub TraverseGroupMembersButton_Click( _
         ByVal sender As System.Object, _
         ByVal e As System.EventArgs) _
         Handles TraverseGroupMembersButton.Click

      'Declare and create an instance of IEdmVault5 object
      Dim vault As IEdmVault5 = New EdmVault5()
      'Log into selected vault as the current user
      vault.LoginAuto(VaultsComboBox.Text, _
         Me.Handle.ToInt32())

      'Declare an IEdmUserMgr5 object
      Dim UserMgr As IEdmUserMgr5
        'The IEdmUserMgr5 interface is implemented by the
        'same class as the IEdmVault5 interface,
        'so assign the value of the IEdmVault5 object
      UserMgr = vault

      Dim Groups As String = vbNullString
      Dim UserGroupPos As IEdmPos5
      UserGroupPos = UserMgr.GetFirstUserGroupPosition()
      While Not UserGroupPos.IsNull
         Dim UserGroup As IEdmUserGroup5
         UserGroup = UserMgr.GetNextUserGroup _
            (UserGroupPos)
         Groups = Groups + UserGroup.Name + " Members:" _
            + vbCrLf
         Groups = Groups + GetMembers(UserGroup)
      End While
      MessageBox.Show(Groups, vault.Name + _
         " Vault Group Users", _
      MessageBoxButtons.OK, MessageBoxIcon.Information)
   End Sub

   Private Function GetMembers(ByVal UserGroup _
         As IEdmUserGroup5) As String

      GetMembers = vbNullString
      Dim Users As String = vbNullString
      Dim UserPos As IEdmPos5
      UserPos = UserGroup.GetFirstUserPosition()
      While Not UserPos.IsNull
         Dim User As IEdmUser5
         User = UserGroup.GetNextUser(UserPos)
         Users = Users + " " + User.Name + vbCrLf
      End While
      GetMembers = Users
   End Function

   Private Sub SendConsultationRequestButton_Click( _
         ByVal sender As System.Object, _
         ByVal e As System.EventArgs) _
         Handles SendConsultationRequestButton.Click

      'Declare and create an instance of IEdmVault5 object
      Dim vault As IEdmVault5 = New EdmVault5()
      'Log into selected vault as the current user
      vault.LoginAuto(VaultsComboBox.Text, _
         Me.Handle.ToInt32())

      'Declare an IEdmUserMgr5 object
      Dim UserMgr As IEdmUserMgr5
        'The IEdmUserMgr5 interface is implemented by the
        'same class as the IEdmVault5 interface,
        'so assign the value of the IEdmVault5 object
      UserMgr = vault

      Dim UserGroup As IEdmUserGroup5
        UserGroup = UserMgr.GetUserGroup("All Users")
      If Not UserGroup Is Nothing Then
         Dim UserPos As IEdmPos5
         UserPos = UserGroup.GetFirstUserPosition()
         While Not UserPos.IsNull
            Dim User As IEdmUser5
            User = UserGroup.GetNextUser(UserPos)
            If User.IsLoggedIn Then
                    User.SendMsg("Informal review request", _
                    "Please stop by my office sometime " + _
                    "this morning for a quick informal " + _
                    "review of my design changes before " + _
                    "I submit them for approval.")
            End If
         End While
      End If
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
Partial Class UsersAndGroups
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
        Me.VaultsLabel = New System.Windows.Forms.Label()
        Me.TraverseUsersButton = New System.Windows.Forms.Button()
        Me.TraverseGroupsButton = New System.Windows.Forms.Button()
        Me.TraverseGroupMembersButton = New System.Windows.Forms.Button()
        Me.SendConsultationRequestButton = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'VaultsComboBox
        '
        Me.VaultsComboBox.FormattingEnabled = True
        Me.VaultsComboBox.Location = New System.Drawing.Point(49, 34)
        Me.VaultsComboBox.Margin = New System.Windows.Forms.Padding(2, 2, 2, 2)
        Me.VaultsComboBox.Name = "VaultsComboBox"
        Me.VaultsComboBox.Size = New System.Drawing.Size(146, 21)
        Me.VaultsComboBox.TabIndex = 10
        '
        'VaultsLabel
        '
        Me.VaultsLabel.AutoSize = True
        Me.VaultsLabel.Location = New System.Drawing.Point(46, 9)
        Me.VaultsLabel.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.VaultsLabel.Name = "VaultsLabel"
        Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
        Me.VaultsLabel.TabIndex = 11
        Me.VaultsLabel.Text = "Select vault view:"
        '
        'TraverseUsersButton
        '
        Me.TraverseUsersButton.Location = New System.Drawing.Point(49, 69)
        Me.TraverseUsersButton.Margin = New System.Windows.Forms.Padding(2, 2, 2, 2)
        Me.TraverseUsersButton.Name = "TraverseUsersButton"
        Me.TraverseUsersButton.Size = New System.Drawing.Size(146, 41)
        Me.TraverseUsersButton.TabIndex = 15
        Me.TraverseUsersButton.Text = "Traverse users"
        Me.TraverseUsersButton.UseVisualStyleBackColor = True
        '
        'TraverseGroupsButton
        '
        Me.TraverseGroupsButton.Location = New System.Drawing.Point(49, 126)
        Me.TraverseGroupsButton.Margin = New System.Windows.Forms.Padding(2, 2, 2, 2)
        Me.TraverseGroupsButton.Name = "TraverseGroupsButton"
        Me.TraverseGroupsButton.Size = New System.Drawing.Size(146, 41)
        Me.TraverseGroupsButton.TabIndex = 16
        Me.TraverseGroupsButton.Text = "Traverse groups"
        Me.TraverseGroupsButton.UseVisualStyleBackColor = True
        '
        'TraverseGroupMembersButton
        '
        Me.TraverseGroupMembersButton.Location = New System.Drawing.Point(49, 183)
        Me.TraverseGroupMembersButton.Margin = New System.Windows.Forms.Padding(2, 2, 2, 2)
        Me.TraverseGroupMembersButton.Name = "TraverseGroupMembersButton"
        Me.TraverseGroupMembersButton.Size = New System.Drawing.Size(146, 41)
        Me.TraverseGroupMembersButton.TabIndex = 17
        Me.TraverseGroupMembersButton.Text = "Traverse group members"
        Me.TraverseGroupMembersButton.UseVisualStyleBackColor = True
        '
        'SendConsultationRequestButton
        '
        Me.SendConsultationRequestButton.Location = New System.Drawing.Point(49, 240)
        Me.SendConsultationRequestButton.Margin = New System.Windows.Forms.Padding(2, 2, 2, 2)
        Me.SendConsultationRequestButton.Name = "SendConsultationRequestButton"
        Me.SendConsultationRequestButton.Size = New System.Drawing.Size(146, 41)
        Me.SendConsultationRequestButton.TabIndex = 18
        Me.SendConsultationRequestButton.Text = "Send consultation request"
        Me.SendConsultationRequestButton.UseVisualStyleBackColor = True
        '
        'UsersAndGroups
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(291, 317)
        Me.Controls.Add(Me.SendConsultationRequestButton)
        Me.Controls.Add(Me.TraverseGroupMembersButton)
        Me.Controls.Add(Me.TraverseGroupsButton)
        Me.Controls.Add(Me.TraverseUsersButton)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Controls.Add(Me.VaultsLabel)
        Me.Margin = New System.Windows.Forms.Padding(2, 2, 2, 2)
        Me.Name = "UsersAndGroups"
        Me.Text = "Traverse users and groups"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
   Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
   Friend WithEvents VaultsLabel As System.Windows.Forms.Label
   Friend WithEvents TraverseUsersButton As System.Windows.Forms.Button
   Friend WithEvents TraverseGroupsButton As System.Windows.Forms.Button
   Friend WithEvents TraverseGroupMembersButton As System.Windows.Forms.Button
   Friend WithEvents SendConsultationRequestButton As System.Windows.Forms.Button

End Class
```

```
Back to top
```
