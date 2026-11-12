---
title: "Add and Remove User and Group from Folder Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Add_and_Remove_User_and_Group_from_Folder_Example_VBNET.htm"
---

# Add and Remove User and Group from Folder Example (VB.NET)

This example shows how to:

- add and remove users to and from a vault.
- add a user of a group to a folder in a vault.
- remove a user of a group from a folder and from a vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'--------------------------------------------------------------------
' Preconditions:
'  1. Start Microsoft Visual Studio.
'     a. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms Application.
'     b. Type AddRemoveUsersGroupsVBNET in Project name.
'     c. For Location, click ... and navigate to the folder where to
create the project.
'       d. Click Next.
'     e. Select Framework.
'     f. Click Create.
'     g. Click Show All Files in the Solution Explorer toolbar and expand
'        Form1.vb in the Solution Explorer.
'     h. Replace the code in Form1.vb with this code.
'     i. To create the form, replace the code in Form1.Designer.vb with
'        this code.
'  2. Add dependencies and safely pass arrays of structures.
'  3. Ensure that the following folder and group exist in the targeted vault:
'     * Folder in the vault root named Test.
'     * Group named Management.
'  4. Click Debug > Start Debugging or press F5.
'
'Postconditions:
' 1. Displays a dialog.
' 2. Select a vault.
' 3. Perform these user actions. Click OK to close each message box.
'    a. Click Traverse users.
'       Displays a message box showing the users in the vault.
'    b. Click Add users.
'       Displays a message box informing you that rrabbit
'       and efudd were added as users to the vault.
'    c. Click Traverse users to verify that rrabbit and efudd
'       were added to the vault.
'       Displays a message box showing the users in the vault.
'    d. Click Remove user.
'       Displays a message box informing you that rrabbit was
'       removed from the vault.
'    e. Click Traverse users to verify that rrabbit was removed
'       from the vault.
'       Displays a message box showing the users in the vault.
' 4. Perform these group actions. Click OK to close each message box.
'    a. Click Traverse groups.
'       Displays a message box showing the groups in the vault.
'    b. Click Traverse group members.
'       Displays a message box showing the users in the groups
'       in the vault.
'    c. Click Add group member.
'       Displays a message box informing you that efudd
'       was added to the Management group.
'    d. Click Traverse group members to verify that
'       efudd is shown in the Management group.
'       Displays a message box showing the users in the
'       groups in the vault.
'    e. Click Add group member to folder.
'       Displays a message box informing you that efudd in
'       the Management group was added to the Test folder.
'    f. To verify the previous step:
'       1. Open a File Explorer window.
'       2. Right-click the Test folder in the selected vault
'          and click Properties to open the Test Properties
'          dialog box.
'       3. Click Group Memberships.
'       4. Click Management to verify that efudd is selected.
'       5. Click OK to close the Test Properties dialog box.
'    g. Click Remove group member and user.
'       Displays a message box informing you that efudd was
'       removed from the vault.
'    h. Click Traverse group members to verify that
'       efudd was removed from the Management group.
'       Displays a message box showing the users in the
'       groups in the vault.
'    i. Click Traverse users to verify that efudd was
'       removed as a user from the vault.
'       Displays a message box showing the users in the vault.
' 5. Close the dialog.
'    Sends two SOLIDWORKS PDM Professional messages
'    to logged-in users and group members who have
'    permission to update users and groups.
' 6. To open these messages, click:
'    * the SOLIDWORKS PDM Professional tray icon.
'     - or -
'    * Tools > Inbox in File Explorer.
'--------------------------------------------------------------------
'Form1.vb

Imports EPDM.Interop.epdm

Public Class Form1

    Dim vault As IEdmVault8
    Dim vault1 As EdmVault5
    Dim UserData(1) As EdmUserData2
    Dim UsrMgr As IEdmUserMgr10
    Dim user As IEdmUser9
    Dim mngmtGroup As IEdmUserGroup8
    Dim folderMembers(0) As EdmMemberFolder

    Private Sub AddRemoveUsersGroupsVBNET_Load(ByVal sender As  _
          System.Object, ByVal e As System.EventArgs) _
          Handles MyBase.Load

        vault1 = New EdmVault5()
        vault = DirectCast(vault1, IEdmVault8)
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

    Private Sub TraverseUsersButton_Click(ByVal sender As  _
          System.Object, ByVal e As System.EventArgs) _
          Handles TraverseUsersButton.Click
        Try

            If Not vault.IsLoggedIn Then
                'Log into selected vault as the current user
                vault.LoginAuto(VaultsComboBox.Text, _
                                Me.Handle.ToInt32())
            End If

            UsrMgr = vault

            'Traverse users
            Dim Users As String = vbNullString
            Dim UserPos As IEdmPos5
            UserPos = UsrMgr.GetFirstUserPosition()
            While Not UserPos.IsNull
                user = UsrMgr.GetNextUser(UserPos)
                Users = Users + user.Name + vbCrLf
            End While
            MessageBox.Show(Users, vault.Name + _
               " Vault Users", MessageBoxButtons.OK, _
               MessageBoxIcon.Information)

        Catch ex As Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + _
            ex.ErrorCode.ToString("X") + vbCrLf + _
            ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)

        End Try
    End Sub

    Private Sub TraverseGroupsButton_Click(ByVal sender _
          As System.Object, ByVal e As System.EventArgs) _
          Handles TraverseGroupsButton.Click
        Try

            If Not vault.IsLoggedIn Then
                'Log into selected vault as the current user
                vault.LoginAuto(VaultsComboBox.Text, _
                                Me.Handle.ToInt32())
            End If

            UsrMgr = vault

            'Traverse groups
            Dim Groups As String = vbNullString
            Dim UserGroupPos As IEdmPos5
            UserGroupPos = UsrMgr.GetFirstUserGroupPosition()
            While Not UserGroupPos.IsNull
                mngmtGroup = UsrMgr.GetNextUserGroup _
                   (UserGroupPos)
                Groups = Groups + mngmtGroup.Name + vbCrLf
            End While
            MessageBox.Show(Groups, vault.Name + _
               " Vault Groups", MessageBoxButtons.OK, _
               MessageBoxIcon.Information)

        Catch ex As Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + _
            ex.ErrorCode.ToString("X") + vbCrLf + _
            ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)

        End Try
    End Sub

    Private Sub TraverseGroupMembersButton_Click( _
          ByVal sender As System.Object, _
          ByVal e As System.EventArgs) _
          Handles TraverseGroupMembersButton.Click
        Try

            If Not vault.IsLoggedIn Then
                'Log into selected vault as the current user
                vault.LoginAuto(VaultsComboBox.Text, _
                                Me.Handle.ToInt32())
            End If

            UsrMgr = vault

            'Traverse group members
            Dim Groups As String = vbNullString
            Dim UserGroupPos As IEdmPos5
            UserGroupPos = UsrMgr.GetFirstUserGroupPosition()
            While Not UserGroupPos.IsNull
                mngmtGroup = UsrMgr.GetNextUserGroup _
                   (UserGroupPos)
                Groups = Groups + mngmtGroup.Name + " Members:" _
                   + vbCrLf
                Groups = Groups + GetMembers(mngmtGroup)
            End While
            MessageBox.Show(Groups, vault.Name + _
               " Vault Group Users", _
            MessageBoxButtons.OK, MessageBoxIcon.Information)

        Catch ex As Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + _
            ex.ErrorCode.ToString("X") + vbCrLf + _
            ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)

        End Try
    End Sub

    Private Function GetMembers(ByVal UserGroup _
          As IEdmUserGroup8) As String
        Try

            If Not vault.IsLoggedIn Then
                'Log into selected vault as the current user
                vault.LoginAuto(VaultsComboBox.Text, _
                                Me.Handle.ToInt32())
            End If

            'Get group members
            GetMembers = vbNullString
            Dim Users As String = vbNullString
            Dim UserPos As IEdmPos5
            UserPos = UserGroup.GetFirstUserPosition()
            While Not UserPos.IsNull
                user = UserGroup.GetNextUser(UserPos)
                Users = Users + " " + user.Name + vbCrLf
            End While
            GetMembers = Users

        Catch ex As Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + _
            ex.ErrorCode.ToString("X") + vbCrLf + _
            ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)
        End Try

    End Function

    Private Sub AddUsersButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles AddUsersButton.Click
        Try
            If Not vault.IsLoggedIn Then
                'Log into selected vault as the current user
                vault.LoginAuto(VaultsComboBox.Text, _
                                Me.Handle.ToInt32())
            End If

            UsrMgr = vault

            'Add users
            UserData(0).mbsCompleteName = "Roger Rabbit"
            UserData(0).mbsEmail = "rrabbit@animatedcharacters.com"
            UserData(0).mbsInitials = "RR"
            UserData(0).mbsUserName = "rrabbit"

            UserData(1).mbsCompleteName = "Elmer J. Fudd"
            UserData(1).mbsEmail = "efudd@animatedcharacters.com"
            UserData(1).mbsInitials = "EJF"
            UserData(1).mbsUserName = "efudd"

            'Return user's interface in mpoUser
            UserData(0).mlFlags = EdmUserDataFlags.Edmudf_GetInterface
            UserData(1).mlFlags = EdmUserDataFlags.Edmudf_GetInterface

            'Add these users even if other users in the array cannot be added
            UserData(0).mlFlags += EdmUserDataFlags.Edmudf_ForceAdd
            UserData(1).mlFlags += EdmUserDataFlags.Edmudf_ForceAdd

            'Set permissions
            Dim perms(1) As EdmSysPerm
            perms(0) = EdmSysPerm.EdmSysPerm_EditReportQuery
            perms(1) = EdmSysPerm.EdmSysPerm_MandatoryVersionComments
            UserData(0).moSysPerms = perms
            UserData(1).moSysPerms = perms

            'Add users to the vault
            UsrMgr.AddUsers3(UserData, EdmUserType.Edmuser_PDM)

            Dim msg As String = ""
            For Each usr As EdmUserData2 In UserData
                If usr.mhStatus = 0 Then
                    msg += "Added user " + usr.mpoUser.Name _
                        + ". ID = " _
                        + usr.mpoUser.ID.ToString() + "." + vbCrLf
                Else
                    msg += "Error adding user " _
                        + usr.mbsUserName + ". " _
                        + vault.GetErrormessage(usr.mhStatus) + vbCrLf
                End If
            Next

            MessageBox.Show(msg)

        Catch ex As Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + _
            ex.ErrorCode.ToString("X") + vbCrLf + _
            ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)

        End Try

    End Sub

    Private Sub RemoveUsersButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles RemoveUsersButton.Click
        Try
            If Not vault.IsLoggedIn Then
                'Log into selected vault as the current user
                vault.LoginAuto(VaultsComboBox.Text, _
                                Me.Handle.ToInt32())
            End If

            'Remove rrabbit from the vault
            UsrMgr = vault1.CreateUtility(EdmUtility.EdmUtil_UserMgr)
            user = UsrMgr.GetUser("rrabbit")
            If IsNothing(user) Then
                MessageBox.Show("No user set to remove. Click Add users.")
                Exit Sub
            End If

            Dim users(0) As Integer
            users(0) = user.ID
            UsrMgr.RemoveUsers(users)

            MessageBox.Show("User " + user.Name + " removed.")

            'Send message to all users with permission
            'to update users and groups
            Dim UserPos As IEdmPos5
            UserPos = UsrMgr.GetFirstUserPosition()
            While Not UserPos.IsNull
                Dim userWithPerm As IEdmUser9
                userWithPerm = UsrMgr.GetNextUser(UserPos)
                If userWithPerm.IsLoggedIn Then
                    If userWithPerm.HasSysRightEx(EdmSysPerm. _
                      EdmSysPerm_EditUserMgr) _
                      Then
                        userWithPerm.SendMsg("ALERT: user removed", "User " + user.Name + " removed.")
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

    Private Sub RemoveGroupMembersButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles RemoveGroupMembersButton.Click
        Try
            If Not vault.IsLoggedIn Then
                'Log into selected vault as the current user
                vault.LoginAuto(VaultsComboBox.Text, _
                                Me.Handle.ToInt32())
            End If

            If IsNothing(mngmtGroup) Then
                MessageBox.Show("No group set from which to remove group member. Click Add group member.")
                Exit Sub
            End If

            'Remove user efudd from Test folder, Management group, and vault
            mngmtGroup.RemoveMembers(folderMembers)
            user = UsrMgr.GetUser("efudd")

            If IsNothing(user) Then
                MessageBox.Show("No user set to remove from group. Click Add users.")
                Exit Sub
            End If

            Dim users(0) As Integer
            users(0) = user.ID
            UsrMgr.RemoveUsers(users)

            MessageBox.Show("User " + user.Name + " removed from group and vault.")

        Catch ex As Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + _
            ex.ErrorCode.ToString("X") + vbCrLf + _
            ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)

        End Try
    End Sub

    Private Sub AddGroupMembersWithFoldersButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles AddGroupMembersWithFoldersButton.Click
        Try
            If Not vault.IsLoggedIn Then
                'Log into selected vault as the current user
                vault.LoginAuto(VaultsComboBox.Text, _
                                Me.Handle.ToInt32())
            End If

            UsrMgr = vault

            'Add efudd to Test folder
            Dim folder As IEdmFolder6
            folder = vault.RootFolder.GetSubFolder("Test")

            'Get user interface for user efudd
            user = UsrMgr.GetUser("efudd")

            If IsNothing(user) Then
                MessageBox.Show("No user set to add to group. Click Add users.")
                Exit Sub
            End If

            'Get the group interface for Management
            mngmtGroup = UsrMgr.GetUserGroup("Management")

            'Find out if the Management user group has
            'permission to update users and groups
            If mngmtGroup.HasSysRightEx(EdmSysPerm.EdmSysPerm_EditUserMgr) Then
                mngmtGroup.SendMsg("PERMISSIONS INFO", "Management group has permission to update groups and users.", False)
            Else
                mngmtGroup.SendMsg("PERMISSIONS INFO", "Management group does not have permission to update groups and users.", False)
                Exit Sub
            End If

            'Add efudd as member of Management to Test folder
            Dim folderMembers(0) As EdmMemberFolder
            folderMembers(0).mlFolderID = folder.ID
            folderMembers(0).mlUserID = user.ID
            mngmtGroup.AddMembersWithFolders(folderMembers)

            'Verify that efudd in Management was added to
            'Test folder
            Dim groups() As Object
            groups = user.GetGroupMembershipsInFolder(folder.ID)
            Dim i As Integer = 0
            i = groups.GetUpperBound(0)
            Dim j As Integer = 0

            Dim UserGroupPos As IEdmPos5
            UserGroupPos = UsrMgr.GetFirstUserGroupPosition()
            While Not UserGroupPos.IsNull
                mngmtGroup = UsrMgr.GetNextUserGroup(UserGroupPos)
                If (mngmtGroup.Name = groups(i).Name) Then
                    If j <= i Then
                        MessageBox.Show("User " + user.Name + " in the " + mngmtGroup.Name + " group was added to the " + folder.Name + " folder.")
                        j = j + 1
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

    Private Sub AddGroupMembersButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles AddGroupMembersButton.Click
        Try
            If Not vault.IsLoggedIn Then
                'Log into selected vault as the current user
                vault.LoginAuto(VaultsComboBox.Text, _
                                Me.Handle.ToInt32())
            End If

            UsrMgr = vault

            'Add efudd to Management group
            mngmtGroup = UsrMgr.GetUserGroup("Management")

            If IsNothing(mngmtGroup) Then
                MessageBox.Show("Management group does not exist. Create a Management group.")
                Exit Sub
            End If

            user = UsrMgr.GetUser("efudd")

            If IsNothing(user) Then
                MessageBox.Show("No user set to add to group. Click Add users.")
                Exit Sub
            End If

            Dim groupMbrIDs(0) As Integer
            groupMbrIDs(0) = user.ID
            mngmtGroup.AddMembers(groupMbrIDs)

            MessageBox.Show("User " + user.Name + " added to " + mngmtGroup.Name + " group.")

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
        Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
        Me.VaultsLabel = New System.Windows.Forms.Label()
        Me.TraverseUsersButton = New System.Windows.Forms.Button()
        Me.TraverseGroupsButton = New System.Windows.Forms.Button()
        Me.TraverseGroupMembersButton = New System.Windows.Forms.Button()
        Me.AddUsersButton = New System.Windows.Forms.Button()
        Me.RemoveUsersButton = New System.Windows.Forms.Button()
        Me.AddGroupMembersButton = New System.Windows.Forms.Button()
        Me.RemoveGroupMembersButton = New System.Windows.Forms.Button()
        Me.UserActionLabel = New System.Windows.Forms.Label()
        Me.GroupActionLabel = New System.Windows.Forms.Label()
        Me.AddGroupMembersWithFoldersButton = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'VaultsComboBox
        '
        Me.VaultsComboBox.FormattingEnabled = True
        Me.VaultsComboBox.Location = New System.Drawing.Point(121, 11)
        Me.VaultsComboBox.Margin = New System.Windows.Forms.Padding(2)
        Me.VaultsComboBox.Name = "VaultsComboBox"
        Me.VaultsComboBox.Size = New System.Drawing.Size(176, 21)
        Me.VaultsComboBox.TabIndex = 10
        '
        'VaultsLabel
        '
        Me.VaultsLabel.AutoSize = True
        Me.VaultsLabel.Location = New System.Drawing.Point(12, 9)
        Me.VaultsLabel.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.VaultsLabel.Name = "VaultsLabel"
        Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
        Me.VaultsLabel.TabIndex = 11
        Me.VaultsLabel.Text = "Select vault view:"
        '
        'TraverseUsersButton
        '
        Me.TraverseUsersButton.Location = New System.Drawing.Point(124, 59)
        Me.TraverseUsersButton.Margin = New System.Windows.Forms.Padding(2)
        Me.TraverseUsersButton.Name = "TraverseUsersButton"
        Me.TraverseUsersButton.Size = New System.Drawing.Size(173, 25)
        Me.TraverseUsersButton.TabIndex = 15
        Me.TraverseUsersButton.Text = "Traverse users"
        Me.TraverseUsersButton.UseVisualStyleBackColor = True
        '
        'TraverseGroupsButton
        '
        Me.TraverseGroupsButton.Location = New System.Drawing.Point(121, 166)
        Me.TraverseGroupsButton.Margin = New System.Windows.Forms.Padding(2)
        Me.TraverseGroupsButton.Name = "TraverseGroupsButton"
        Me.TraverseGroupsButton.Size = New System.Drawing.Size(176, 25)
        Me.TraverseGroupsButton.TabIndex = 16
        Me.TraverseGroupsButton.Text = "Traverse groups"
        Me.TraverseGroupsButton.UseVisualStyleBackColor = True
        '
        'TraverseGroupMembersButton
        '
        Me.TraverseGroupMembersButton.Location = New System.Drawing.Point(121, 197)
        Me.TraverseGroupMembersButton.Margin = New System.Windows.Forms.Padding(2)
        Me.TraverseGroupMembersButton.Name = "TraverseGroupMembersButton"
        Me.TraverseGroupMembersButton.Size = New System.Drawing.Size(176, 27)
        Me.TraverseGroupMembersButton.TabIndex = 17
        Me.TraverseGroupMembersButton.Text = "Traverse group members"
        Me.TraverseGroupMembersButton.UseVisualStyleBackColor = True
        '
        'AddUsersButton
        '
        Me.AddUsersButton.Location = New System.Drawing.Point(124, 89)
        Me.AddUsersButton.Name = "AddUsersButton"
        Me.AddUsersButton.Size = New System.Drawing.Size(173, 23)
        Me.AddUsersButton.TabIndex = 18
        Me.AddUsersButton.Text = "Add users"
        Me.AddUsersButton.UseVisualStyleBackColor = True
        '
        'RemoveUsersButton
        '
        Me.RemoveUsersButton.Location = New System.Drawing.Point(124, 118)
        Me.RemoveUsersButton.Name = "RemoveUsersButton"
        Me.RemoveUsersButton.Size = New System.Drawing.Size(173, 24)
        Me.RemoveUsersButton.TabIndex = 19
        Me.RemoveUsersButton.Text = "Remove user"
        Me.RemoveUsersButton.UseVisualStyleBackColor = True
        '
        'AddGroupMembersButton
        '
        Me.AddGroupMembersButton.Location = New System.Drawing.Point(121, 229)
        Me.AddGroupMembersButton.Name = "AddGroupMembersButton"
        Me.AddGroupMembersButton.Size = New System.Drawing.Size(176, 23)
        Me.AddGroupMembersButton.TabIndex = 20
        Me.AddGroupMembersButton.Text = "Add group member"
        Me.AddGroupMembersButton.UseVisualStyleBackColor = True
        '
        'RemoveGroupMembersButton
        '
        Me.RemoveGroupMembersButton.Location = New System.Drawing.Point(121, 287)
        Me.RemoveGroupMembersButton.Name = "RemoveGroupMembersButton"
        Me.RemoveGroupMembersButton.Size = New System.Drawing.Size(176, 25)
        Me.RemoveGroupMembersButton.TabIndex = 21
        Me.RemoveGroupMembersButton.Text = "Remove group member and user"
        Me.RemoveGroupMembersButton.UseVisualStyleBackColor = True
        '
        'UserActionLabel
        '
        Me.UserActionLabel.AutoSize = True
        Me.UserActionLabel.Location = New System.Drawing.Point(12, 59)
        Me.UserActionLabel.Name = "UserActionLabel"
        Me.UserActionLabel.Size = New System.Drawing.Size(69, 13)
        Me.UserActionLabel.TabIndex = 22
        Me.UserActionLabel.Text = "User actions:"
        '
        'GroupActionLabel
        '
        Me.GroupActionLabel.AutoSize = True
        Me.GroupActionLabel.Location = New System.Drawing.Point(12, 166)
        Me.GroupActionLabel.Name = "GroupActionLabel"
        Me.GroupActionLabel.Size = New System.Drawing.Size(76, 13)
        Me.GroupActionLabel.TabIndex = 23
        Me.GroupActionLabel.Text = "Group actions:"
        '
        'AddGroupMembersWithFoldersButton
        '
        Me.AddGroupMembersWithFoldersButton.Location = New System.Drawing.Point(121, 258)
        Me.AddGroupMembersWithFoldersButton.Name = "AddGroupMembersWithFoldersButton"
        Me.AddGroupMembersWithFoldersButton.Size = New System.Drawing.Size(176, 23)
        Me.AddGroupMembersWithFoldersButton.TabIndex = 24
        Me.AddGroupMembersWithFoldersButton.Text = "Add group member to folder"
        Me.AddGroupMembersWithFoldersButton.UseVisualStyleBackColor = True
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(333, 329)
        Me.Controls.Add(Me.AddGroupMembersWithFoldersButton)
        Me.Controls.Add(Me.GroupActionLabel)
        Me.Controls.Add(Me.UserActionLabel)
        Me.Controls.Add(Me.RemoveGroupMembersButton)
        Me.Controls.Add(Me.AddGroupMembersButton)
        Me.Controls.Add(Me.RemoveUsersButton)
        Me.Controls.Add(Me.AddUsersButton)
        Me.Controls.Add(Me.TraverseGroupMembersButton)
        Me.Controls.Add(Me.TraverseGroupsButton)
        Me.Controls.Add(Me.TraverseUsersButton)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Controls.Add(Me.VaultsLabel)
        Me.Margin = New System.Windows.Forms.Padding(2)
        Me.Name = "Form1"
        Me.Text = "Add and remove users and groups"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents VaultsLabel As System.Windows.Forms.Label
    Friend WithEvents TraverseUsersButton As System.Windows.Forms.Button
    Friend WithEvents TraverseGroupsButton As System.Windows.Forms.Button
    Friend WithEvents TraverseGroupMembersButton As System.Windows.Forms.Button
    Friend WithEvents AddUsersButton As System.Windows.Forms.Button
    Friend WithEvents RemoveUsersButton As System.Windows.Forms.Button
    Friend WithEvents AddGroupMembersButton As System.Windows.Forms.Button
    Friend WithEvents RemoveGroupMembersButton As System.Windows.Forms.Button
    Friend WithEvents UserActionLabel As System.Windows.Forms.Label
    Friend WithEvents GroupActionLabel As System.Windows.Forms.Label
    Friend WithEvents AddGroupMembersWithFoldersButton As System.Windows.Forms.Button

End Class
```

```
Back to top
```
