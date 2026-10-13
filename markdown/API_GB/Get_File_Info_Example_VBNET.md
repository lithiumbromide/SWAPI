---
title: "Get File Information Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Get_File_Info_Example_VBNET.htm"
---

# Get File Information Example (VB.NET)

This example shows how to access a file and get information about it.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio 2010.
 '    a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '    b. Type Files in Name.
 '    c. Click Browse and navigate to the folder where to create
 '       the project.
 '    d. Click OK.
 '    e. Click Show All Files in the Solution Explorer toolbar and expand
 '       Form1.vb in the Solution Explorer.
 '    f. Replace the code in Form1.vb with this code.
 '    g. To create the form, replace the code in Form1.Designer.vb with this code.
 ' 2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 '    name in the Solution Explorer, click Add Reference, click
 '    Assemblies > Framework in the left-side panel, browse to the top folder of
 '    your SOLIDWORKS PDM Professional installation, locate and click
 '    EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
 ' 3. Right-click EPDM.Interop.epdm in References, click Properties, and set
 '    Embed Interop Types to False to handle methods that pass arrays of
 '    structures.
 ' 4. Check out a file in the vault.
 ' 5. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Get file information dialog box.
 '    a. Select a vault view.
 '    b. Click Browse.
  '       1. Locate and select the file checked out in Preconditions step 4.
 '       2. Click Open.
 '    c. Click Get information.
 '    d. Displays a message box with information about the selected file.
 '    e. Click OK.
  ' 2. Close the Get file information dialog box.
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

     Public Sub GetInfo_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GetInfo.Click
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 'Log into selected vault as the current user
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim aFile As IEdmFile17
             aFile = vault2.GetFileFromPath(ListBox.Items(0).ToString())

             'Get configurations
             Dim msg As String = "Configurations: " & vbLf
             Dim folder As IEdmFolder5
             folder = vault2.RootFolder

             Dim cfgList As EdmStrLst5
             cfgList = aFile.GetConfigurations

             Dim pos As IEdmPos5
             pos = cfgList.GetHeadPosition
             Dim cfgName As String
             While Not pos.IsNull
                 cfgName = cfgList.GetNext(pos)
                 msg = msg & cfgName & vbLf
             End While

             msg = msg & vbLf

             'Get type of file
             Dim typ As Integer
             typ = aFile.FileType
             msg = msg & "EdmFileType: " & typ & vbLf

             msg = msg & vbLf

             'Get category of file
             Dim cat As IEdmCategory6
             cat = aFile.Category
             If Not IsNothing(cat) Then
                 msg = msg & "Category: " & cat.Name & ", Category ID: " & aFile.CategoryID & vbLf
                 msg = msg & vbLf
             End If

             'Get local file timestamp
             Dim filePath As String = aFile.Name
             Dim fileDate As Object
             fileDate = aFile.GetLocalFileDate(filePath)

             If Not IsNothing(fileDate) Then
                 Dim text As String
                 text = fileDate
                 msg = msg & aFile.GetLocalPath(folder.ID) & " was modified " & text & vbLf
             Else
                 msg = msg & "There is no local copy of the file" & vbLf
             End If

             msg = msg & vbLf

             'Get local version number
             Dim versionNo As Integer
             versionNo = aFile.GetLocalVersionNo(aFile.GetLocalPath(folder.ID))

             If versionNo = -1 Then
                 msg = msg & "The local copy of " & aFile.Name & " does not match any existing versions" & vbLf
             Else
                 Dim versionStr As String
                 versionStr = versionNo
                 msg = msg & "The local copy of " & aFile.Name & " has version " & versionStr & vbLf
             End If

             msg = msg & vbLf

             'Get current version
             Dim ver As Integer
             ver = aFile.CurrentVersion
             msg = msg & "Current version: " & ver & vbLf

             msg = msg & vbLf

             'Get local revision name
             Dim revName As String
             revName = aFile.GetLocalRevisionName(aFile.GetLocalPath(folder.ID))

             If revName = "" Then
                 msg = msg & "The local copy of " & aFile.Name & " does not match any existing revisions" & vbLf
             Else
                 msg = msg & "The local copy of " & aFile.Name & " has revision name " & revName & vbLf
             End If

             msg = msg & vbLf

             'Get current revision
             revName = aFile.CurrentRevision
             msg = msg & "Current revision: " & revName & vbLf

             msg = msg & vbLf

             'Get local file size
             Dim fileSize As Integer
             fileSize = aFile.GetLocalFileSize2(aFile.GetLocalPath(folder.ID))

             If fileSize = -1 Then
                 msg = msg & "The local copy of " & aFile.Name & " is missing" & vbLf
             Else
                 msg = msg & "The local copy of " & aFile.Name & " has size " & fileSize & " bytes" & vbLf
             End If

             msg = msg & vbLf

             'Get current workflow state
             Dim state As IEdmState5
             state = aFile.CurrentState
             msg = msg & "Current workflow state: " & state.Name & vbLf

             msg = msg & vbLf

             'Get whether the file is checked out
             Dim checkedOut As Boolean
             checkedOut = aFile.IsLocked
             msg = msg & "File is checked out? " & checkedOut & vbLf
             If checkedOut Then
                 msg = msg & "Lock path: " & aFile.LockPath & vbLf
                 msg = msg & "Locked by: " & aFile.LockedByUser.Name & ", User ID: " & aFile.LockedByUserID & vbLf
                 msg = msg & "Locked in: " & aFile.LockedInFolder.Name & ", Folder ID: " & aFile.LockedInFolderID & vbLf
                 msg = msg & "Locked on: " & aFile.LockedOnComputer  & ", Vault View ID: " & aFile.LockedOnViewID
             End If

             msg = msg & vbLf

              'Get whether the file has cut list items
              Dim hasCutListItems  As Boolean
            hasCutListItems = aFile.HasCutlistItems
              msg = msg & "File has cut list items? " & hasCutListItems & vbLf

             msg = msg & vbLf
              'Create a label
              Dim labelID  As Integer
            labelID = aFile.CreateLabel("File label", "Label description shows in the history dialog box")
              msg = msg & "File label ID: " & labelID & vbLf

            MessageBox.Show(msg)

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
         Me.GetInfo = New System.Windows.Forms.Button()
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
         Me.ListBox.Size = New System.Drawing.Size(259, 43)
         Me.ListBox.TabIndex = 4
         '
         'GetInfo
         '
         Me.GetInfo.Location = New System.Drawing.Point(84, 178)
         Me.GetInfo.Name = "GetInfo"
         Me.GetInfo.Size = New System.Drawing.Size(98, 23)
         Me.GetInfo.TabIndex = 5
         Me.GetInfo.Text = "Get information"
         Me.GetInfo.UseVisualStyleBackColor = True
         '
         'OpenFileDialog
         '
         Me.OpenFileDialog.Title = "Open"
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(317, 215)
         Me.Controls.Add(Me.GetInfo)
         Me.Controls.Add(Me.ListBox)
         Me.Controls.Add(Me.BrowseButton)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Get file information"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents BrowseButton As System.Windows.Forms.Button
     Friend WithEvents ListBox As System.Windows.Forms.ListBox
     Friend WithEvents GetInfo As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog As System.Windows.Forms.OpenFileDialog
 End Class
```

[Back to top](#top)
