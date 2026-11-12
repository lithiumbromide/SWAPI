---
title: "Add Files to Vault Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Add_Files_to_Vault_Example_VBNET.htm"
---

# Add Files to Vault Example (VB.NET)

This example shows how to add files to a vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 '    a. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms Application.
 '    b. Type AddFiles in Project name.
 '    c. For Location, click ... and navigate to the folder where to create the project.
'      d. Click Next.
'    e. Select Framework.
'    f. Click Create.
'    g. Click Show All Files in the Solution Explorer toolbar and expand
'       Form1.vb in the Solution Explorer.
 '    h. Replace the code in Form1.vb with this code.
 '    i. To create the form, replace the code in Form1.Designer.vb with this code.
 ' 2. Add dependencies and safely pass arrays of structures.
 ' 3. Ensure that the vault workflow contains the Waiting for Approval state.
 ' 4. Ensure that the vault workflow contains the Submit for Approval transition
 '    to the Waiting for Approval state.
 ' 5. Ensure that the logged-in PDM user has permission to move files.
  ' 6. Modify password in IEdmFile13::ChangeState3 to
 '    match the password of your logged-in PDM user.
 ' 7. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Add files to vault dialog box.
 '    a. Select a vault view.
 '    b. Click Browse.
  '       1. Locate and click three files outside the vault.
 '       2. Click Open.
 '    c. Click Add files.
 '       1. Adds the selected files to the root folder of the vault.
 '       2. Checks in the files.
 '       3. Creates path \temp\files in the root folder.
 '       4. Moves one of the files to subfolder  \temp\files.
 '       5. Copies one of the files to subfolder \temp.
 '       6. Changes the state of one of the files in the root folder to
 '          Waiting for Approval.
 ' 2. Click OK to close each message box.
 ' 3. Examine the vault.
  ' 4. Close the Add files to vault dialog box.
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
     Implements IEdmCallback6

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

     Public Sub BrowseButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BrowseButton.Click
         Try
             ListBox.Items.Clear()

             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             If Not vault1.IsLoggedIn Then
                 'Log into selected vault as the current user
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             'Set the initial directory in the Open dialog
             OpenFileDialog.InitialDirectory = vault1.RootFolderPath
             'Show the Open dialog
             Dim DialogResult As System.Windows.Forms.DialogResult = Nothing
             DialogResult = OpenFileDialog.ShowDialog()
             'If the user didn't click Open, exit
             If Not (DialogResult = System.Windows.Forms.DialogResult.OK) Then
                 Return
             End If

             For Each FileName As String In OpenFileDialog.FileNames
                 ListBox.Items.Add(FileName)
             Next
         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub AddFiles_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles AddFiles.Click
         Try

             Dim vault2 As IEdmVault16 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault16)
             If Not vault1.IsLoggedIn Then
                 'Log into selected vault as the current user
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             If Not ListBox.Items.Count = 3 Then
                 MessageBox.Show("Please click three files that are not in the vault.")
                 Exit Sub
             End If

             'MessageBox.Show("Vault type as defined in EdmVaultType: " + vault2.GetVaultType().ToString())

             Dim aFile As IEdmFile13

             ' Add selected files to the root folder of the vault
             Dim Folder As IEdmFolder9
             Folder = vault2.RootFolder

             Dim Files() As EdmAddFileInfo
             ReDim Files(ListBox.Items.Count - 1)

             Dim FileNames(2) As String
             Dim Index As Integer = 0
             Dim fileStr = ""
             For Each FileName In ListBox.Items
                 fileStr = FileName.ToString()
                 FileNames(Index) = fileStr.Substring(fileStr.LastIndexOf("\"))
                 Index = Index + 1
             Next

             Dim Path As String
             Index = 0
             For Each FileName In ListBox.Items
                 Path = FileName
                 Files(Index).mbsPath = Path
                 Files(Index).mlEdmAddFlags = EdmAddFlag.EdmAdd_Simple
                 Files(Index).mlFileID = 0
                 Files(Index).mlSrcDocumentID = 0
                 Files(Index).mlSrcProjectID = 0
                 Files(Index).mbsNewName = ""

                 Index = Index + 1
             Next

             Folder.AddFiles(Me.Handle.ToInt32(), Files, Me)

             ' Check in the files
             Dim arrFiles(3) As IEdmFile13
             Index = 0
             For Each FileName In FileNames
                 aFile = vault2.GetFileFromPath(Folder.LocalPath + "\" + FileName)
                 'MessageBox.Show("User can rename " + aFile.Name + " in this folder? " + Folder.HasRenameRights(Me.Handle.ToInt32(), aFile.ID, FileName, "new", True).ToString())
                 'MessageBox.Show(aFile.Name + " is in a private state? " + aFile.PrivateStateFile.ToString())
```

```
		Dim ID As Integer
		Dim fName As String
		Dim vaultName As String
		Dim vaultObject As IEdmVault5
		ID = aFile.ID
		fName = aFile.Name
		vaultObject = aFile.Vault
		vaultName = vaultObject.Name
		MessageBox.Show("Database ID: " + ID.ToString() + "; Vault name: " + vaultName + "; File name: " + fName)
```

```vb
                 aFile.UnlockFile(Me.Handle.ToInt32(), "")
                 arrFiles(Index) = aFile

                 Dim thumb As Object
                 thumb = aFile.GetThumbnail

                 Index = Index + 1
             Next

             ' Create \temp\files path in the root folder
             Folder.CreateFolderPath("\temp\files", Me.Handle.ToInt32())

             ' Move one of the files to the \temp\files subfolder
             Dim dest As IEdmFolder5
             dest = vault2.GetFolderFromPath(Folder.LocalPath + "\temp\files")
             aFile = arrFiles(0)
             aFile.Move(Me.Handle.ToInt32(), Folder.ID, dest.ID, 0)

             ' Copy one of the files to the temp subfolder
             aFile = arrFiles(1)
             aFile.GetFileCopy(Me.Handle.ToInt32(), "", Folder.LocalPath + "\temp\")

             ' Change the state of one of the files to Waiting for Approval
             aFile = arrFiles(2)
             aFile.ChangeState3("Waiting for Approval", "Submit for Approval", Folder.ID, "The file is waiting for approval.", Me.Handle.ToInt32(), EdmStateFlags.EdmState_Simple, "password")

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Function IEdmCallback6_MsgBox(ByVal lParentWnd As Integer, ByVal lMsgID As Integer, ByVal bsMsg As String, Optional ByVal eType As EdmMBoxType = 0&) As EdmMBoxResult Implements IEdmCallback6.MsgBox

         MsgBox(bsMsg)
         IEdmCallback6_MsgBox = EdmMBoxResult.EdmMbr_OK

     End Function

     Private Sub IEdmCallback6_Resolve(ByVal lParentWnd As Integer, ByRef ppoItems() As EdmCmdData) Implements IEdmCallback6.Resolve

     End Sub

     Private Function IEdmCallback6_SetProgress(ByVal lBarIndex As Integer, ByVal lPos As Integer, ByVal bsMsg As String) As Boolean Implements IEdmCallback6.SetProgress

         IEdmCallback6_SetProgress = True

     End Function

     Private Sub IEdmCallback6_SetProgressRange(ByVal lBarIndex As Integer, ByVal lMax As Integer) Implements IEdmCallback6.SetProgressRange

     End Sub

     Private Sub IEdmCallback6_SetStatusMessage(ByVal lBarIndex As Integer, ByVal bsMessage As String) Implements IEdmCallback6.SetStatusMessage

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
         Me.BrowseButton = New System.Windows.Forms.Button()
         Me.ListBox = New System.Windows.Forms.ListBox()
         Me.AddFiles = New System.Windows.Forms.Button()
         Me.OpenFileDialog = New System.Windows.Forms.OpenFileDialog()
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
         'BrowseButton
         '
         Me.BrowseButton.Location = New System.Drawing.Point(16, 85)
         Me.BrowseButton.Name = "BrowseButton"
         Me.BrowseButton.Size = New System.Drawing.Size(98, 23)
         Me.BrowseButton.TabIndex = 3
         Me.BrowseButton.Text = "Browse..."
         Me.BrowseButton.UseVisualStyleBackColor = True
         '
         'ListBox
         '
         Me.ListBox.FormattingEnabled = True
         Me.ListBox.HorizontalScrollbar = True
         Me.ListBox.Location = New System.Drawing.Point(16, 114)
         Me.ListBox.Name = "ListBox"
         Me.ListBox.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended
         Me.ListBox.Size = New System.Drawing.Size(259, 43)
         Me.ListBox.TabIndex = 4
         '
         'AddFiles
         '
         Me.AddFiles.Location = New System.Drawing.Point(84, 178)
         Me.AddFiles.Name = "AddFiles"
         Me.AddFiles.Size = New System.Drawing.Size(98, 23)
         Me.AddFiles.TabIndex = 5
         Me.AddFiles.Text = "Add files"
         Me.AddFiles.UseVisualStyleBackColor = True
         '
         'OpenFileDialog
         '
         Me.OpenFileDialog.Multiselect = True
         Me.OpenFileDialog.Title = "Open"
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(317, 215)
         Me.Controls.Add(Me.AddFiles)
         Me.Controls.Add(Me.ListBox)
         Me.Controls.Add(Me.BrowseButton)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Add files to vault"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents BrowseButton As System.Windows.Forms.Button
     Friend WithEvents ListBox As System.Windows.Forms.ListBox
     Friend WithEvents AddFiles As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog As System.Windows.Forms.OpenFileDialog
 End Class
```

[Back to top](#top)
