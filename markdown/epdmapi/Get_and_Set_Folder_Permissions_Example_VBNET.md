---
title: "Get and Set Folder Permissions Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_and_Set_Folder_Permissions_Example_VBNET.htm"
---

# Get and Set Folder Permissions Example (VB.NET)

This example shows how to create an application that displays a form in which a user can assign permissions to folders for users and groups in a vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
'----------------------------------------------------------------------------
' Preconditions:
' 1. Start Microsoft Visual Studio.
' 2. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms App.
' 3. Type the name of your project in  Project name.
 ' 4. For Location, click ... and navigate to the folder where to create the project.
 ' 5. Click Next.
 ' 6. Select Framework.
 ' 7. Click Create.
 ' 8. Click Show All Files in the Solution Explorer toolbar and expand
 '    Form1.vb in the Solution Explorer.
 ' 9.  Add dependencies and safely pass arrays of structures.
'10. Replace the code in Form1.vb with this code.
 '11. Replace the code in Form1.Designer.vb with this code.
'12. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. In the Form1 dialog, select a vault and click Log In.
 '    Wait for the application to populate the Users and Groups list boxes.
 ' 2. Click permissions in the list box located left of the Reverse Order check box.
 ' 3. Optionally select the Reverse Order check box.
 ' 4. Select the check boxes in front of the users and folders to which to assign permissions.
 ' 5. Click Apply Permissions.
 '    Wait for the application to populate the Users list.
 '    The folder permissions are updated for the selected users.
 ' 6. Select the check boxes in front of the groups and folders to which to assign permissions.
 ' 7. Click Apply Permissions.
 '    Wait for the application to populate the Groups list.
 '    The folder permissions are updated for the selected groups.
 '----------------------------------------------------------------------------

 ' Form1.vb
 Imports EPDM.Interop.epdm

 Public Class Form1

     Private vault As IEdmVault8
     Private folders As Dictionary(Of Integer, String)

     Private Enum MyEdmRightsFlags As Integer
         MyRight_All = EdmRightFlags.EdmRight_All
         MyRight_None = EdmRightFlags.EdmRight_None
         MyRight_Read = EdmRightFlags.EdmRight_Read
         MyRight_Lock = EdmRightFlags.EdmRight_Lock
         MyRight_Delete = EdmRightFlags.EdmRight_Delete
         MyRight_AddRename = EdmRightFlags.EdmRight_Add
         MyRight_Share = EdmRightFlags.EdmRight_Share
         MyRight_IncrementRevision = EdmRightFlags.EdmRight_IncrementRevision
         MyRight_AddDeleteFolder = EdmRightFlags.EdmRight_AddFolder
         MyRight_RecoverTrash = EdmRightFlags.EdmRight_RecoverTrash
         MyRight_DestroyTrash = EdmRightFlags.EdmRight_DestroyTrash
         MyRight_EditFolderCard = EdmRightFlags.EdmRight_EditFolderCard
         MyRight_BomActivate = EdmRightFlags.EdmRight_BomActivate
         MyRight_MaySeeComputedBOM = EdmRightFlags.EdmRight_MaySeeComputedBOM
         MyRight_AssignGroupMembership = &H1000
         MyRightAssignFilePermissions = &H2000
         MyRight_PermitGroupAccess = &H4000
         MyRight_ReadNamedBOM = &H8000
         MyRight_ChangeCard = EdmRightFlags.EdmRight_ChangeCard
         MyRight_ShowWorkingVersion = EdmRightFlags.EdmRight_ShowWorkingVersion
         MyRight_Rollback = EdmRightFlags.EdmRight_Rollback
         MyRight_ColdStoreRestore = EdmRightFlags.EdmRight_ColdStoreRestore
         MyRight_EditVerFreeVarData = EdmRightFlags.EdmRight_EditVerFreeVarData
     End Enum

     Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
         vault = New EdmVault5
         Dim aViews As Array = Nothing
         vault.GetVaultViews(aViews, False)
         If aViews IsNot Nothing Then
             For Each View As EdmViewInfo In aViews
                 comboVault.Items.Add(View.mbsVaultName)
             Next
             comboVault.SelectedIndex = 0
         End If

         Dim RightLabels As Dictionary(Of MyEdmRightsFlags, String) = New Dictionary(Of MyEdmRightsFlags, String) From _
             { _
                 {MyEdmRightsFlags.MyRight_Read, "Read file contents"}, _
                 {MyEdmRightsFlags.MyRight_Lock, "Check out file"}, _
                 {MyEdmRightsFlags.MyRight_Delete, "Delete file"}, _
                 {MyEdmRightsFlags.MyRight_AddRename, "Add or rename file"}, _
                 {MyEdmRightsFlags.MyRight_Share, "Share file to another folder"}, _
                 {MyEdmRightsFlags.MyRight_IncrementRevision, "Increment revision of a file"}, _
                 {MyEdmRightsFlags.MyRight_AddDeleteFolder, "Add or delete a folder"}, _
                 {MyEdmRightsFlags.MyRight_RecoverTrash, "Recover files from recycle bin"}, _
                 {MyEdmRightsFlags.MyRight_DestroyTrash, "Destroy"}, _
                 {MyEdmRightsFlags.MyRight_EditFolderCard, "Edit folder card data"}, _
                 {MyEdmRightsFlags.MyRight_BomActivate, "Activate computed BOM"}, _
                 {MyEdmRightsFlags.MyRight_MaySeeComputedBOM, "See computed BOM"}, _
                 {MyEdmRightsFlags.MyRight_AssignGroupMembership, "Assign group membership"}, _
                 {MyEdmRightsFlags.MyRightAssignFilePermissions, "Assign file permissions"}, _
                 {MyEdmRightsFlags.MyRight_PermitGroupAccess, "Permit or deny group-level access to files"}, _
                 {MyEdmRightsFlags.MyRight_ReadNamedBOM, "Read named bill of materials"}, _
                 {MyEdmRightsFlags.MyRight_ChangeCard, "Can update the design of cards"}, _
                 {MyEdmRightsFlags.MyRight_ShowWorkingVersion, "Show working versions of files"}, _
                 {MyEdmRightsFlags.MyRight_Rollback, "Roll back"}, _
                 {MyEdmRightsFlags.MyRight_ColdStoreRestore, "Restore file from cold storage"}, _
                 {MyEdmRightsFlags.MyRight_EditVerFreeVarData, "Edit version-free variable data"}
             }

         For Each flag As MyEdmRightsFlags In [Enum].GetValues(GetType(MyEdmRightsFlags))
             If RightLabels.ContainsKey(flag) Then
                 Dim rightItem As ListViewItem = listViewPermissions.Items.Add(RightLabels(flag))
                 rightItem.Tag = flag
             End If
         Next
     End Sub

     Private Sub buttonLogIn_Click(sender As Object, e As System.EventArgs) Handles buttonLogIn.Click
         vault.LoginAuto(comboVault.Text, Me.Handle)
         comboVault.Enabled = False
         buttonLogIn.Enabled = False
         buttonApply.Enabled = True
         buttonRefresh.Enabled = True

         folders = New Dictionary(Of Integer, String)()

         Dim rootFolder As IEdmFolder7 = vault.RootFolder
         BuildFolderDictionary(rootFolder)

         ShowAllUserPermissions()
         ShowAllGroupPermissions()
     End Sub

     Private Sub BuildFolderDictionary(folder As IEdmFolder7)
         folders.Add(folder.ID, folder.LocalPath)

         Dim posSubFolder As IEdmPos5 = folder.GetFirstSubFolderPosition()
         Do Until posSubFolder.IsNull
             Dim subFolder As IEdmFolder7 = folder.GetNextSubFolder(posSubFolder)
             BuildFolderDictionary(subFolder)
         Loop
     End Sub

     Private Sub ShowAllUserPermissions()
         listViewUsers.Items.Clear()
         Dim userMgr As IEdmUserMgr7 = vault
         Dim userPos As IEdmPos5 = userMgr.GetFirstUserPosition()
         Do Until userPos.IsNull
             Dim user As IEdmUser5 = userMgr.GetNextUser(userPos)

             For Each folderID As Integer In folders.Keys
                 Dim aPermissions As Array = Nothing
                 userMgr.GetFolderPermissions(user.ID, user.ObjectType, folderID, EdmGetPermFlag.EdmGetPerm_OnlyExplicitlySet, aPermissions)

                 If aPermissions IsNot Nothing AndAlso aPermissions.Length > 0 Then
                     Dim itemUser As ListViewItem = listViewUsers.Items.Add(user.ID.ToString())
                     itemUser.SubItems.Add(user.Name)
                     itemUser.SubItems.Add(folderID)
                     itemUser.SubItems.Add(folders(folderID))
                     Dim folderPermission As EdmFolderPermission = aPermissions.GetValue(0)
                     itemUser.SubItems.Add(folderPermission.mlEdmRightFlag.ToString())
                 End If
             Next
         Loop
     End Sub

     Private Sub ShowAllGroupPermissions()
         listViewGroups.Items.Clear()
         Dim userMgr As IEdmUserMgr7 = vault
         Dim groupPos As IEdmPos5 = userMgr.GetFirstUserGroupPosition()
         Do Until groupPos.IsNull
             Dim group As IEdmUserGroup5 = userMgr.GetNextUserGroup(groupPos)

             For Each folderID As Integer In folders.Keys
                 Dim aPermissions As Array = Nothing
                 userMgr.GetFolderPermissions(group.ID, group.ObjectType, folderID, 0, aPermissions)

                 If aPermissions IsNot Nothing AndAlso aPermissions.Length > 0 Then
                     Dim itemGroup As ListViewItem = listViewGroups.Items.Add(group.ID.ToString())
                     itemGroup.SubItems.Add(group.Name)
                     itemGroup.SubItems.Add(folderID)
                     itemGroup.SubItems.Add(folders(folderID))
                     Dim folderPermission As EdmFolderPermission = aPermissions.GetValue(0)
                     itemGroup.SubItems.Add(folderPermission.mlEdmRightFlag.ToString())
                 End If
             Next
         Loop
     End Sub

     Private Sub buttonApply_Click(sender As System.Object, e As System.EventArgs) Handles buttonApply.Click
         Dim assignedRights As Integer = 0
         For Each rightItem As ListViewItem In listViewPermissions.Items
             If rightItem.Checked Then
                 assignedRights = assignedRights Or rightItem.Tag
             End If
         Next

         Dim userMgr As IEdmUserMgr7 = vault

         Dim listPermissions As List(Of EdmFolderPermission) = New List(Of EdmFolderPermission)
         For Each itemUser As ListViewItem In listViewUsers.Items
             If itemUser.Checked Then
                 Dim folderID As Integer = CInt(itemUser.SubItems(2).Text)
                 Dim permission As EdmFolderPermission
                 With permission
                     .mlFolderID = folderID
                     .mlOwnerID = CInt(itemUser.SubItems(0).Text)
                     .meOwnerType = EdmObjectType.EdmObject_User
                     .mlEdmRightFlag = assignedRights
                 End With
                 listPermissions.Add(permission)
             End If
         Next

         For Each itemGroup As ListViewItem In listViewGroups.Items
             If itemGroup.Checked Then
                 Dim folderID As Integer = CInt(itemGroup.SubItems(2).Text)
                 Dim permission As EdmFolderPermission
                 With permission
                     .mlFolderID = folderID
                     .mlOwnerID = CInt(itemGroup.SubItems(0).Text)
                     .meOwnerType = EdmObjectType.EdmObject_UserGroup
                     .mlEdmRightFlag = assignedRights
                 End With
                 listPermissions.Add(permission)
             End If
         Next

         If checkboxReverseOrder.Checked Then listPermissions.Reverse()

         Dim permissions() As EdmFolderPermission = listPermissions.ToArray()
         userMgr.SetFolderPermissions(permissions)

         ShowAllGroupPermissions()
         ShowAllUserPermissions()
     End Sub

     Private Sub buttonRefresh_Click(sender As System.Object, e As System.EventArgs) Handles buttonRefresh.Click
         ShowAllGroupPermissions()
         ShowAllUserPermissions()
     End Sub
 End Class

 ' Form1.Designer.vb
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
         Me.comboVault = New System.Windows.Forms.ComboBox()
         Me.buttonLogIn = New System.Windows.Forms.Button()
         Me.Label2 = New System.Windows.Forms.Label()
         Me.listViewUsers = New System.Windows.Forms.ListView()
         Me.ColumnHeader1 = CType(New System.Windows.Forms.ColumnHeader(), System.Windows.Forms.ColumnHeader)
         Me.ColumnHeader2 = CType(New System.Windows.Forms.ColumnHeader(), System.Windows.Forms.ColumnHeader)
         Me.ColumnHeader3 = CType(New System.Windows.Forms.ColumnHeader(), System.Windows.Forms.ColumnHeader)
         Me.ColumnHeader7 = CType(New System.Windows.Forms.ColumnHeader(), System.Windows.Forms.ColumnHeader)
         Me.ColumnHeader8 = CType(New System.Windows.Forms.ColumnHeader(), System.Windows.Forms.ColumnHeader)
         Me.Label3 = New System.Windows.Forms.Label()
         Me.buttonApply = New System.Windows.Forms.Button()
         Me.buttonRefresh = New System.Windows.Forms.Button()
         Me.listViewGroups = New System.Windows.Forms.ListView()
         Me.ColumnHeader4 = CType(New System.Windows.Forms.ColumnHeader(), System.Windows.Forms.ColumnHeader)
         Me.ColumnHeader5 = CType(New System.Windows.Forms.ColumnHeader(), System.Windows.Forms.ColumnHeader)
         Me.ColumnHeader6 = CType(New System.Windows.Forms.ColumnHeader(), System.Windows.Forms.ColumnHeader)
         Me.ColumnHeader9 = CType(New System.Windows.Forms.ColumnHeader(), System.Windows.Forms.ColumnHeader)
         Me.ColumnHeader10 = CType(New System.Windows.Forms.ColumnHeader(), System.Windows.Forms.ColumnHeader)
         Me.listViewPermissions = New System.Windows.Forms.ListView()
         Me.checkboxReverseOrder = New System.Windows.Forms.CheckBox()
         Me.SuspendLayout()
         '
         'Label1
         '
         Me.Label1.AutoSize = True
         Me.Label1.Location = New System.Drawing.Point(12, 9)
         Me.Label1.Name = "Label1"
         Me.Label1.Size = New System.Drawing.Size(66, 13)
         Me.Label1.TabIndex = 0
         Me.Label1.Text = "Select vault:"
         '
         'comboVault
         '
         Me.comboVault.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
         Me.comboVault.FormattingEnabled = True
         Me.comboVault.Location = New System.Drawing.Point(84, 6)
         Me.comboVault.Name = "comboVault"
         Me.comboVault.Size = New System.Drawing.Size(357, 21)
         Me.comboVault.TabIndex = 1
         '
         'buttonLogIn
         '
         Me.buttonLogIn.Location = New System.Drawing.Point(447, 6)
         Me.buttonLogIn.Name = "buttonLogIn"
         Me.buttonLogIn.Size = New System.Drawing.Size(98, 21)
         Me.buttonLogIn.TabIndex = 2
         Me.buttonLogIn.Text = "Log In"
         Me.buttonLogIn.UseVisualStyleBackColor = True
         '
         'Label2
         '
         Me.Label2.AutoSize = True
         Me.Label2.Location = New System.Drawing.Point(12, 51)
         Me.Label2.Name = "Label2"
         Me.Label2.Size = New System.Drawing.Size(34, 13)
         Me.Label2.TabIndex = 3
         Me.Label2.Text = "Users"
         '
         'listViewUsers
         '
         Me.listViewUsers.CheckBoxes = True
         Me.listViewUsers.Columns.AddRange(New System.Windows.Forms.ColumnHeader() {Me.ColumnHeader1, Me.ColumnHeader2, Me.ColumnHeader3, Me.ColumnHeader7, Me.ColumnHeader8})
         Me.listViewUsers.Location = New System.Drawing.Point(12, 67)
         Me.listViewUsers.Name = "listViewUsers"
         Me.listViewUsers.Size = New System.Drawing.Size(533, 107)
         Me.listViewUsers.TabIndex = 4
         Me.listViewUsers.UseCompatibleStateImageBehavior = False
         Me.listViewUsers.View = System.Windows.Forms.View.Details
         '
         'ColumnHeader1
         '
         Me.ColumnHeader1.Text = "ID"
         Me.ColumnHeader1.Width = 41
         '
         'ColumnHeader2
         '
         Me.ColumnHeader2.Text = "Name"
         Me.ColumnHeader2.Width = 137
         '
         'ColumnHeader3
         '
         Me.ColumnHeader3.Text = "Folder ID"
         '
         'ColumnHeader7
         '
         Me.ColumnHeader7.Text = "Folder"
         Me.ColumnHeader7.Width = 152
         '
         'ColumnHeader8
         '
         Me.ColumnHeader8.Text = "Folder Permissions"
         Me.ColumnHeader8.Width = 108
         '
         'Label3
         '
         Me.Label3.AutoSize = True
         Me.Label3.Location = New System.Drawing.Point(12, 182)
         Me.Label3.Name = "Label3"
         Me.Label3.Size = New System.Drawing.Size(41, 13)
         Me.Label3.TabIndex = 5
         Me.Label3.Text = "Groups"
         '
         'buttonApply
         '
         Me.buttonApply.Enabled = False
         Me.buttonApply.Location = New System.Drawing.Point(428, 420)
         Me.buttonApply.Name = "buttonApply"
         Me.buttonApply.Size = New System.Drawing.Size(117, 23)
         Me.buttonApply.TabIndex = 7
         Me.buttonApply.Text = "Apply Permissions"
         Me.buttonApply.UseVisualStyleBackColor = True
         '
         'buttonRefresh
         '
         Me.buttonRefresh.Enabled = False
         Me.buttonRefresh.Location = New System.Drawing.Point(428, 38)
         Me.buttonRefresh.Name = "buttonRefresh"
         Me.buttonRefresh.Size = New System.Drawing.Size(117, 23)
         Me.buttonRefresh.TabIndex = 8
         Me.buttonRefresh.Text = "Refresh Permissions"
         Me.buttonRefresh.UseVisualStyleBackColor = True
         '
         'listViewGroups
         '
         Me.listViewGroups.CheckBoxes = True
         Me.listViewGroups.Columns.AddRange(New System.Windows.Forms.ColumnHeader() {Me.ColumnHeader4, Me.ColumnHeader5, Me.ColumnHeader6, Me.ColumnHeader9, Me.ColumnHeader10})
         Me.listViewGroups.Location = New System.Drawing.Point(12, 198)
         Me.listViewGroups.Name = "listViewGroups"
         Me.listViewGroups.Size = New System.Drawing.Size(533, 107)
         Me.listViewGroups.TabIndex = 9
         Me.listViewGroups.UseCompatibleStateImageBehavior = False
         Me.listViewGroups.View = System.Windows.Forms.View.Details
         '
         'ColumnHeader4
         '
         Me.ColumnHeader4.Text = "ID"
         Me.ColumnHeader4.Width = 41
         '
         'ColumnHeader5
         '
         Me.ColumnHeader5.Text = "Name"
         Me.ColumnHeader5.Width = 137
         '
         'ColumnHeader6
         '
         Me.ColumnHeader6.Text = "Folder ID"
         '
         'ColumnHeader9
         '
         Me.ColumnHeader9.Text = "Folder"
         Me.ColumnHeader9.Width = 152
         '
         'ColumnHeader10
         '
         Me.ColumnHeader10.Text = "Folder Permissions"
         Me.ColumnHeader10.Width = 108
         '
         'listViewPermissions
         '
         Me.listViewPermissions.CheckBoxes = True
         Me.listViewPermissions.Location = New System.Drawing.Point(12, 328)
         Me.listViewPermissions.Name = "listViewPermissions"
         Me.listViewPermissions.Size = New System.Drawing.Size(410, 115)
         Me.listViewPermissions.TabIndex = 10
         Me.listViewPermissions.UseCompatibleStateImageBehavior = False
         Me.listViewPermissions.View = System.Windows.Forms.View.List
         '
         'checkboxReverseOrder
         '
         Me.checkboxReverseOrder.AutoSize = True
         Me.checkboxReverseOrder.Location = New System.Drawing.Point(428, 328)
         Me.checkboxReverseOrder.Name = "checkboxReverseOrder"
         Me.checkboxReverseOrder.Size = New System.Drawing.Size(95, 17)
         Me.checkboxReverseOrder.TabIndex = 11
         Me.checkboxReverseOrder.Text = "Reverse Order"
         Me.checkboxReverseOrder.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(557, 455)
         Me.Controls.Add(Me.checkboxReverseOrder)
         Me.Controls.Add(Me.listViewPermissions)
         Me.Controls.Add(Me.listViewGroups)
         Me.Controls.Add(Me.buttonRefresh)
         Me.Controls.Add(Me.buttonApply)
         Me.Controls.Add(Me.Label3)
         Me.Controls.Add(Me.listViewUsers)
         Me.Controls.Add(Me.Label2)
         Me.Controls.Add(Me.buttonLogIn)
         Me.Controls.Add(Me.comboVault)
         Me.Controls.Add(Me.Label1)
         Me.Name = "Form1"
         Me.Text = "Folder Permissions"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents Label1 As System.Windows.Forms.Label
     Friend WithEvents comboVault As System.Windows.Forms.ComboBox
     Friend WithEvents buttonLogIn As System.Windows.Forms.Button
     Friend WithEvents Label2 As System.Windows.Forms.Label
     Friend WithEvents listViewUsers As System.Windows.Forms.ListView
     Friend WithEvents ColumnHeader1 As System.Windows.Forms.ColumnHeader
     Friend WithEvents ColumnHeader2 As System.Windows.Forms.ColumnHeader
     Friend WithEvents ColumnHeader3 As System.Windows.Forms.ColumnHeader
     Friend WithEvents Label3 As System.Windows.Forms.Label
     Friend WithEvents buttonApply As System.Windows.Forms.Button
     Friend WithEvents buttonRefresh As System.Windows.Forms.Button
     Friend WithEvents ColumnHeader7 As System.Windows.Forms.ColumnHeader
     Friend WithEvents ColumnHeader8 As System.Windows.Forms.ColumnHeader
     Friend WithEvents listViewGroups As System.Windows.Forms.ListView
     Friend WithEvents ColumnHeader4 As System.Windows.Forms.ColumnHeader
     Friend WithEvents ColumnHeader5 As System.Windows.Forms.ColumnHeader
     Friend WithEvents ColumnHeader6 As System.Windows.Forms.ColumnHeader
     Friend WithEvents ColumnHeader9 As System.Windows.Forms.ColumnHeader
     Friend WithEvents ColumnHeader10 As System.Windows.Forms.ColumnHeader
     Friend WithEvents listViewPermissions As System.Windows.Forms.ListView
     Friend WithEvents checkboxReverseOrder As System.Windows.Forms.CheckBox

 End Class
```
