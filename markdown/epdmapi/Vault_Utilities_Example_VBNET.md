---
title: "Vault Utilities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Vault_Utilities_Example_VBNET.htm"
---

# Vault Utilities Example (VB.NET)

This example shows how to:

- Verify installed SOLIDWORKS PDM Professional version is at least 5.3.
- Get installed SOLIDWORKS PDM Professional licenses.
- Add a group.
- Remove a group.
- Add a user.
- Remove a user.
- Copy a file.
- Delete a file.
- Get check-out permission for a file.
- Delete a folder.
- Restore deleted items to the vault view.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
  ' 2. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms App
 ' 3. Type VaultUtilities in Project name.
  ' 4. For Location, click ... and navigate to the folder where to create the project.
 ' 5. Click Next.
 ' 6. Select Framework.
 ' 7. Click Create.
' 8. Click Show All Files in the Solution Explorer toolbar and expand
 '    Form1.vb in the Solution Explorer.
 ' 9.    Add dependencies and safely pass arrays of structures.
 '10. Replace the code in Form1.vb with this code.
 '11. To create the form, replace the code in Form1.Designer.vb with this code.
 '12. Ensure that an empty folder exists in the vault.
 '13. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Vault utilities dialog box.
 '    a. Select a vault view.
 '    b. Click Verify SOLIDWORKS PDM Professional 5.3.
  '       1. Displays message about the installed version.
 '       2. Click OK.
 '    c. Click Get SOLIDWORKS Professional PDM licenses.
 '       1. Displays a message with the installed licenses.
  '       2. Click OK.
 '    d. Click Add group.
 '       1. Displays a message that group, My Group, is created.
 '       2. Click OK.
 '    e. Click Add user.
 '       1. Displays a message that user, Temp, is created.
 '       2. Click OK.
 '    f. Click Remove group.
 '       1. Displays a message with the removal status.
 '       2. Click OK.
 '    g. Click Remove user.
 '       1. Displays a message with the removal status.
 '       2. Click OK.
 '    h. Click Copy file.
 '       1. In the Open dialog, click a vault file.
 '       2. Click Open.
 '       3. In the Select Folder dialog, click a folder to which to copy
 '          the selected file.
 '       4. Click OK.
 '       5. Displays a message with the file copy status.
 '       6. Click OK.
 '    i. Click Delete file.
 '       1. In the Select Files to Delete dialog box, click a vault file
 '          to delete.
 '       2. Click Open.
 '       3. Displays a message with the file deletion status.
 '       4. Click OK.
 '    j. Click Check-out permission.
 '       1. In the Open dialog, click a file for which to get the check-out
 '          permission.
 '       2. Click Open.
 '       3. Displays a message with the user's permission.
 '       4. Click OK.
 '    k. Click Delete folder.
 '       1. In the Select Folder dialog, click an empty vault folder to delete.
 '       2. Click OK.
 '       3. Displays a message with the status of the folder deletion.
 '       4. Click OK.
 '    l. Click Restore deleted items.
 '       1. In the Select Folder dialog, click the folder from which you deleted
 '          a file in step 1i.
 '       2. Click OK.
 '       3. Displays a message with the status of the folder restoration.
 '       4. Click OK.
  ' 2. Close the Vault utilities dialog box.
  '----------------------------------------------------------------------------

 'Form1.vb

 Imports System.IO
 Imports System.Xml.Serialization
 Imports System.Collections
 Imports System.Collections.Generic
 Imports System.Data
 Imports System.Diagnostics
 Imports System.Windows.Forms
 Imports System.ComponentModel
 Imports EPDM.Interop.epdm

 Public Class Form1

     Private vault1 As IEdmVault5 = Nothing

     Public Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

         Try
             Dim vault1 As IEdmVault5 = New EdmVault5()
             Dim vault As IEdmVault8 = DirectCast(vault1, IEdmVault8)
             Dim Views As EdmViewInfo() = Nothing

             vault.GetVaultViews(Views, False)
             VaultsComboBox.Items.Clear()
             For Each View As EdmViewInfo In Views
                 VaultsComboBox.Items.Add(View.mbsVaultName)
             Next
             If VaultsComboBox.Items.Count > 0 Then
                 VaultsComboBox.Text = DirectCast(VaultsComboBox.Items(0), String)
             End If
         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button5_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button5.Click
         'Verify SOLIDWORKS PDM Professional version is 5.3 or higher
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             vault2.VerifyVersion(5, 3)

             MessageBox.Show("SOLIDWORKS PDM Professional version is at least 5.3")

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button6_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button6.Click
         'Get licenses
         Try

             Dim vault2 As IEdmVault11 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault11)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim msg As String
             msg = "Installed licenses:" + vbLf
             Dim lics() As EdmLicense
             lics = Nothing
             vault2.GetLicense(lics)
             Dim idx As Integer
             idx = LBound(lics)
             While (idx <= UBound(lics))
                 msg = msg + "Type="
                 Select Case lics(idx).meType
                     Case EdmLicenseType.EdmLic_Editor
                         msg = msg + "Editor"
                     Case EdmLicenseType.EdmLic_Contributor
                         msg = msg + "Contributor"
                     Case EdmLicenseType.EdmLic_Viewer
                         msg = msg + "Viewer"
                     Case EdmLicenseType.EdmLic_Processor
                         msg = msg + "Processor"
                     Case Else
                         msg = msg + CStr(lics(idx).meType)
                 End Select

                 msg = msg + " Users=" + CStr(lics(idx).mlUserCount) + vbLf
                 idx = idx + 1
             End While

             vault2.MsgBox(Me.Handle.ToInt32, msg)

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button7_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button7.Click
         'Add group, My Group
         Try

             Dim vault2 As IEdmVault11 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault11)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim userMgr As IEdmUserMgr7
             userMgr = vault2.CreateUtility(EdmUtility.EdmUtil_UserMgr)

             Dim admin As IEdmUser7
             admin = userMgr.GetUser("Admin")

             Dim groups(0) As EdmGroupData2
             groups(0).mbAutoAdd = 0
             groups(0).mbsDescription = "A group created by the API"
             groups(0).mbsName = "My Group"
             groups(0).mlFlags = EdmGroupDataFlags.Edmgdf_GetInterface
             Dim members(0) As Integer
             members(0) = admin.ID
             groups(0).moMembers = members
             Dim perms(0) As EdmSysPerm
             perms(0) = EdmSysPerm.EdmSysPerm_ModifyToolbox
             groups(0).moSysPerms = perms

             userMgr.AddGroups2(groups)

             Dim msg As String
             msg = ""
             Dim idx As Integer
             idx = LBound(groups)
             While (idx <= UBound(groups))
                 If groups(idx).mhStatus <> 0 Then
                     msg = msg & "Error creating group, '" & groups(idx).mbsName & "' - " & vault2.GetErrorMessage(groups(idx).mhStatus) & vbLf
                 Else
                     msg = msg & "Created group, '" & groups(idx).mpoGroup.Name & "', successfully with ID, " & CStr(groups(idx).mpoGroup.ID) & vbLf
                 End If
                 idx = idx + 1
             End While

             vault2.MsgBox(Me.Handle.ToInt32, msg)

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button8_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button8.Click
         'Remove group, My Group
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim userMgr As IEdmUserMgr7
             userMgr = vault2.CreateUtility(EdmUtility.EdmUtil_UserMgr)
             Dim group As IEdmUserGroup6
             group = userMgr.GetUserGroup("My Group")
             If group Is Nothing Then Exit Sub

             Dim groups(0) As Integer
             groups(0) = group.ID
             userMgr.RemoveGroups(groups)

             MessageBox.Show("Group, My Group, removed")

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button9_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button9.Click
         'Add user, Temp
         Try

             Dim vault2 As IEdmVault11 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault11)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim UsrMgr As IEdmUserMgr7 = vault2
             Dim UserData(0) As EdmUserData2

             UserData(0).mbsCompleteName = "Temp"
             UserData(0).mbsEmail = "Temp"
             UserData(0).mbsInitials = "TJ"
             UserData(0).mbsUserName = "Temp"
             UserData(0).mlFlags = _
                 EdmUserDataFlags.Edmudf_GetInterface
             UserData(0).mlFlags += _
                 EdmUserDataFlags.Edmudf_ForceAdd
             Dim perms(2) As EdmSysPerm
             perms(0) = EdmSysPerm.EdmSysPerm_EditUserMgr
             perms(1) = EdmSysPerm.EdmSysPerm_EditReportQuery
             perms(2) = EdmSysPerm.EdmSysPerm_MandatoryVersionComments
             UserData(0).moSysPerms = perms

             UsrMgr.AddUsers2(UserData)

             Dim msg As String = ""
             For Each usr As EdmUserData2 In UserData
                 If usr.mhStatus = 0 Then
                     msg += "Created user, """ + usr.mpoUser.Name _
                         + """, successfully with ID, " _
                         + usr.mpoUser.ID.ToString() + vbCrLf
                 Else
                     msg &= "Error creating user, """ _
                         & usr.mbsUserName & """ - " _
                         & vault2.GetErrorMessage(usr.mhStatus) & vbCrLf
                 End If
             Next
             MessageBox.Show(msg)

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button10_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button10.Click
         'Remove user, Temp
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim userMgr As IEdmUserMgr7
             userMgr = vault2.CreateUtility(EdmUtility.EdmUtil_UserMgr)
             Dim user As IEdmUser7
             user = userMgr.GetUser("Temp")
             If user Is Nothing Then Exit Sub

             Dim users(0) As Integer
             users(0) = user.ID
             userMgr.RemoveUsers(users)

             MessageBox.Show("User, Temp, removed")

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button4.Click
         'Get user's check-out permission for a file
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim pathList As EdmStrLst5
             pathList = vault2.BrowseForFile(Me.Handle.ToInt32(), EdmBrowseFlag.EdmBws_ForOpen + EdmBrowseFlag.EdmBws_PermitVaultFiles)
             If pathList Is Nothing Then Exit Sub

             Dim file As IEdmFile5
             Dim srcFolder As IEdmFolder5 = Nothing
             file = vault2.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition), srcFolder)

             If srcFolder.HasRightsEx(EdmRightFlags.EdmRight_Lock, file.ID) Then
                 MsgBox("User can check out this file")
             Else
                 MsgBox("User does not have check-out permission")
             End If

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
         'Copy file
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim pathList As EdmStrLst5
             pathList = vault2.BrowseForFile(Me.Handle.ToInt32(), EdmBrowseFlag.EdmBws_ForOpen + EdmBrowseFlag.EdmBws_PermitVaultFiles)
             If pathList Is Nothing Then Exit Sub

             Dim file As IEdmFile5
             Dim srcFolder As IEdmFolder5 = Nothing
             file = vault2.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition), srcFolder)

             Dim destFolder As IEdmFolder5
             destFolder = vault2.BrowseForFolder(Me.Handle.ToInt32(), "Select destination folder:")
             If destFolder Is Nothing Then Exit Sub

             Dim fileID As Integer
             fileID = destFolder.CopyFile(file.ID, srcFolder.ID, Me.Handle.ToInt32(), "", EdmCopyFlag.EdmCpy_Simple)
             MsgBox("Copied file successfully to new file with ID, " & fileID)

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
         'Delete file
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim pathList As EdmStrLst5
             pathList = vault2.BrowseForFile(Me.Handle.ToInt32(), _
                                      EdmBrowseFlag.EdmBws_ForOpen + _
                                      EdmBrowseFlag.EdmBws_PermitVaultFiles + _
                                      EdmBrowseFlag.EdmBws_PermitMultipleSel, _
                                      "", "", "", "", _
                                      "Select Files to Delete")
             If pathList Is Nothing Then Exit Sub

             Dim pos As IEdmPos5
             pos = pathList.GetHeadPosition
             While Not pos.IsNull
                 Dim file As IEdmFile5
                 Dim folder As IEdmFolder5 = Nothing
                 file = vault2.GetFileFromPath(pathList.GetNext(pos), folder)
                 folder.DeleteFile(Me.Handle.ToInt32(), file.ID)
             End While

             Dim strCount As String
             strCount = pathList.Count.ToString
             MessageBox.Show("Deleted " + strCount + " file")

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
         'Delete folder
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim folder As IEdmFolder5
             folder = vault2.BrowseForFolder(Me.Handle.ToInt32(), "Select folder to delete:")
             If folder Is Nothing Then Exit Sub

             Dim parentFolder As IEdmFolder5
             parentFolder = folder.ParentFolder

             If parentFolder Is Nothing Then
                 MsgBox("You cannot delete the vault root folder")
                 Exit Sub
             End If

             parentFolder.DeleteFolder(Me.Handle.ToInt32(), folder.ID)

             MessageBox.Show(folder.Name & " deleted")

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button11_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button11.Click
         'Restore folder
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim folder As IEdmFolder11
             folder = vault2.BrowseForFolder(Me.Handle.ToInt32(), "Select folder to restore:")
             If folder Is Nothing Then Exit Sub

             Dim arrayEdmDeletedItems() As EdmDeletedItems = Nothing

             folder.GetDeletedItems(arrayEdmDeletedItems, True)
             folder.RecoverDeletedItems(arrayEdmDeletedItems)

             MessageBox.Show(folder.Name & " restored")

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

 End Class
 Back to top
 'Form1.Designer.vb
 <Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
 Partial Class Form1
     Inherits System.Windows.Forms.Form
     ''' <summary>
     ''' Required designer variable.
     ''' </summary>
     Private components As System.ComponentModel.IContainer = Nothing

     ''' <summary>
     ''' Clean up any resources being used.
     ''' </summary>
     ''' <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
     Protected Overrides Sub Dispose(ByVal disposing As Boolean)
         If disposing AndAlso (components IsNot Nothing) Then
             components.Dispose()
         End If
         MyBase.Dispose(disposing)
     End Sub

 #Region "Windows Form Designer generated code"

     ''' <summary>
     ''' Required method for Designer support - do not modify
     ''' the contents of this method with the code editor.
     ''' </summary>
     Private Sub InitializeComponent()
         Me.VaultsLabel = New System.Windows.Forms.Label()
         Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
         Me.Button1 = New System.Windows.Forms.Button()
         Me.Button2 = New System.Windows.Forms.Button()
         Me.Button3 = New System.Windows.Forms.Button()
         Me.Button4 = New System.Windows.Forms.Button()
         Me.Button5 = New System.Windows.Forms.Button()
         Me.Button6 = New System.Windows.Forms.Button()
         Me.Button7 = New System.Windows.Forms.Button()
         Me.Button8 = New System.Windows.Forms.Button()
         Me.Button9 = New System.Windows.Forms.Button()
         Me.Button10 = New System.Windows.Forms.Button()
         Me.Button11 = New System.Windows.Forms.Button()

         Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
         Me.SuspendLayout()
         '
         'VaultsLabel
         '
         Me.VaultsLabel.AutoSize = True
         Me.VaultsLabel.Location = New System.Drawing.Point(13, 26)
         Me.VaultsLabel.Name = "VaultsLabel"
         Me.VaultsLabel.Size = New System.Drawing.Size(94, 13)
         Me.VaultsLabel.TabIndex = 0
         Me.VaultsLabel.Text = " Select vault view:"
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(16, 42)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(121, 21)
         Me.VaultsComboBox.TabIndex = 1
         '
         'Button1
         '
         Me.Button1.Location = New System.Drawing.Point(16, 223)
         Me.Button1.Name = "Button1"
         Me.Button1.Size = New System.Drawing.Size(91, 23)
         Me.Button1.TabIndex = 6
         Me.Button1.Text = "Copy file..."
         Me.Button1.UseVisualStyleBackColor = True
         '
         'Button2
         '
         Me.Button2.Location = New System.Drawing.Point(113, 223)
         Me.Button2.Name = "Button2"
         Me.Button2.Size = New System.Drawing.Size(96, 23)
         Me.Button2.TabIndex = 7
         Me.Button2.Text = "Delete file..."
         Me.Button2.UseVisualStyleBackColor = True
         '
         'Button3
         '
         Me.Button3.Location = New System.Drawing.Point(69, 281)
         Me.Button3.Name = "Button3"
         Me.Button3.Size = New System.Drawing.Size(96, 23)
         Me.Button3.TabIndex = 8
         Me.Button3.Text = "Delete folder..."
         Me.Button3.UseVisualStyleBackColor = True
         '
         'Button4
         '
         Me.Button4.Location = New System.Drawing.Point(43, 252)
         Me.Button4.Name = "Button4"
         Me.Button4.Size = New System.Drawing.Size(156, 23)
         Me.Button4.TabIndex = 9
         Me.Button4.Text = "Check-out permission..."
         Me.Button4.UseVisualStyleBackColor = True
         '
         'Button5
         '
         Me.Button5.Location = New System.Drawing.Point(16, 83)
         Me.Button5.Name = "Button5"
         Me.Button5.Size = New System.Drawing.Size(233, 23)
         Me.Button5.TabIndex = 10
         Me.Button5.Text = "Verify SOLIDWORKS PDM Professional 5.3"
         Me.Button5.UseVisualStyleBackColor = True
         '
         'Button6
         '
         Me.Button6.Location = New System.Drawing.Point(16, 121)
         Me.Button6.Name = "Button6"
         Me.Button6.Size = New System.Drawing.Size(233, 23)
         Me.Button6.TabIndex = 11
         Me.Button6.Text = "Get SOLIDWORKS PDM Professional licenses"
         Me.Button6.UseVisualStyleBackColor = True
         '
         'Button7
         '
         Me.Button7.Location = New System.Drawing.Point(16, 165)
         Me.Button7.Name = "Button7"
         Me.Button7.Size = New System.Drawing.Size(91, 23)
         Me.Button7.TabIndex = 12
         Me.Button7.Text = "Add group"
         Me.Button7.UseVisualStyleBackColor = True
         '
         'Button8
         '
         Me.Button8.Location = New System.Drawing.Point(16, 194)
         Me.Button8.Name = "Button8"
         Me.Button8.Size = New System.Drawing.Size(91, 23)
         Me.Button8.TabIndex = 13
         Me.Button8.Text = "Remove group"
         Me.Button8.UseVisualStyleBackColor = True
         '
         'Button9
         '
         Me.Button9.Location = New System.Drawing.Point(113, 165)
         Me.Button9.Name = "Button9"
         Me.Button9.Size = New System.Drawing.Size(96, 23)
         Me.Button9.TabIndex = 14
         Me.Button9.Text = "Add user"
         Me.Button9.UseVisualStyleBackColor = True
         '
         'Button10
         '
         Me.Button10.Location = New System.Drawing.Point(113, 194)
         Me.Button10.Name = "Button10"
         Me.Button10.Size = New System.Drawing.Size(96, 23)
         Me.Button10.TabIndex = 15
         Me.Button10.Text = "Remove user"
         Me.Button10.UseVisualStyleBackColor = True

         'Button11
         '
         Me.Button11.Location = New System.Drawing.Point(43, 310)
         Me.Button11.Name = "Button11"
         Me.Button11.Size = New System.Drawing.Size(156, 29)
         Me.Button11.TabIndex = 16
         Me.Button11.Text = "Restore deleted items"
         Me.Button11.UseVisualStyleBackColor = True

         '
         'OpenFileDialog1
         '
         Me.OpenFileDialog1.FileName = "OpenFileDialog1"
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(276, 330)
         Me.Controls.Add(Me.Button11)
         Me.Controls.Add(Me.Button10)
         Me.Controls.Add(Me.Button9)
         Me.Controls.Add(Me.Button8)
         Me.Controls.Add(Me.Button7)
         Me.Controls.Add(Me.Button6)
         Me.Controls.Add(Me.Button5)
         Me.Controls.Add(Me.Button4)
         Me.Controls.Add(Me.Button3)
         Me.Controls.Add(Me.Button2)
         Me.Controls.Add(Me.Button1)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Vault utilities"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents Button1 As System.Windows.Forms.Button
     Friend WithEvents Button2 As System.Windows.Forms.Button
     Friend WithEvents Button3 As System.Windows.Forms.Button
     Friend WithEvents Button4 As System.Windows.Forms.Button
     Friend WithEvents Button5 As System.Windows.Forms.Button
     Friend WithEvents Button6 As System.Windows.Forms.Button
     Friend WithEvents Button7 As System.Windows.Forms.Button
     Friend WithEvents Button8 As System.Windows.Forms.Button
     Friend WithEvents Button9 As System.Windows.Forms.Button
     Friend WithEvents Button10 As System.Windows.Forms.Button
     Friend WithEvents Button11 As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog
 End Class
```

[Back to top](#top)
