---
title: "Get Histories of Files Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Get_Histories_of_Files_Example_VBNET.htm"
---

# Get Histories of Files Example (VB.NET)

This example shows how to update version comments and get histories of files.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
   '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 '    a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '    b. Type GetHistories_VBNET in Name.
 '    c. Click Browse and navigate to the folder where to create the project.
 '    d. Click OK.
 '    e. Click Show All Files in the Solution Explorer toolbar and expand
 '       Form1.vb in the Solution Explorer.
 '    f. Replace the code in Form1.vb with this code.
 '    g. To create the form, replace the code in Form1.Designer.vb with
 '       this code.
 ' 2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 '    name in the Solution Explorer, click Add Reference, click
 '    Assemblies > Framework in the left-side panel, browse to the top folder of
 '    your SOLIDWORKS PDM Professional installation, locate and click
 '    EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
 ' 3. Right-click EPDM.Interop.epdm in References, click Properties, and set
 '    Embed Interop Types to False to handle methods that pass arrays of
 '    structures.
 ' 4. Ensure that the vault contains a checked-in file with two versions.
 ' 5. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Get histories dialog box.
 '    a. Select a vault view.
 '    b. Click Select a file.
 '    c. In the Select File dialog:
 '       1. Select a checked-in vault file.
 '       2. Click Open.
 '       3. Updates all version comments for the selected file to
 '          "New comment".
 '    d. Click Get history.
 '    e. Displays a message box for each history item.
 '    f. Observe the updated version comments.
 '    g. Click OK to close each message box.
 '    h. Click Roll back to first version.
 '       Rolls back the selected file to its first version.
 '    i. Click Get history.
 '       A message box displays one history item.
 ' 2. Close the Get histories dialog box.
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
     Dim history As IEdmHistory3
     Dim historyUpdate As IEdmHistoryUpdate
     Dim aFile As IEdmFile5
     Dim rollbackItem As EdmHistoryItem = Nothing

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

     Public Sub SelectFiles_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles SelectFiles.Click
         Try
             File1List.Items.Clear()

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             'Set the initial directory in the Select File dialog
             OpenFileDialog1.InitialDirectory = vault1.RootFolderPath
             'Show the Select File dialog
             Dim DialogResult As System.Windows.Forms.DialogResult = Nothing
             DialogResult = OpenFileDialog1.ShowDialog()
             If Not (DialogResult = System.Windows.Forms.DialogResult.OK) Then
                 Return
             End If

             historyUpdate = vault2.CreateUtility(EdmUtility.EdmUtil_HistoryUpdate)

             For Each FileName As String In OpenFileDialog1.FileNames
                 File1List.Items.Add(FileName)
                 aFile = vault1.GetFileFromPath(FileName)
                 ' Update all version comments for the selected files
                 historyUpdate.UpdateVersionComment(aFile.ID, -1, "New comment")
             Next

             historyUpdate.CommitUpdates()

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub GetHistories_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GetHistories.Click
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

            history = vault2.CreateUtility(EdmUtility.EdmUtil_History)

             For Each FileName As String In OpenFileDialog1.FileNames
                 aFile = vault1.GetFileFromPath(FileName)
                 ' Add each file selected to the set of files for which to get histories
                 history.AddFile(aFile.ID)
             Next

             Dim ppoRethistory() As EdmHistoryItem = Nothing
             history.GetSortedHistory(ppoRethistory, EdmHistoryType.Edmhist_FileVersion)

             Dim str As String
            Dim evDesc As String

             For Each item As EdmHistoryItem In ppoRethistory
                evDesc = history.GetEventDescription(item, EdmLangCode.LanEng)
                 str = "History of " & item.mbsItemName & vbLf
                str = str & "Event description: " & evDesc & vbLf
                 str = str & "Type of history record as defined in EdmHistoryType: " & item.meType & vbLf
                 str = str & "Date: " & item.moDate & vbLf
                 str = str & "Version: " & item.mlVersion & vbLf
                 str = str & "User ID: " & item.mlUserID & vbLf
                 str = str & "File ID: " & item.mlFileID & vbLf
                 str = str & "Folder ID: " & item.mlFolderID & vbLf
                 str = str & "User name: " & item.mbsUserName & vbLf
                 str = str & "Comment: " & item.mbsComment & vbLf
                 str = str & vbLf
                 MessageBox.Show(str)
                 rollbackItem = item
             Next

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try

     End Sub

     Public Sub Rollback_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GetHistories.Click
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             If Not aFile Is Nothing And Not history Is Nothing Then

                 'Roll back to the file's first version, which is the last history item reported above
                 history.Rollback(rollbackItem)
             End If

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
         Me.SelectFiles = New System.Windows.Forms.Button()
         Me.File1List = New System.Windows.Forms.ListBox()
         Me.GetHistories = New System.Windows.Forms.Button()
         Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
         Me.Rollback = New System.Windows.Forms.Button()
         Me.SuspendLayout()
         '
         'VaultsLabel
         '
         Me.VaultsLabel.AutoSize = True
         Me.VaultsLabel.Location = New System.Drawing.Point(12, 24)
         Me.VaultsLabel.Name = "VaultsLabel"
         Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
         Me.VaultsLabel.TabIndex = 0
         Me.VaultsLabel.Text = "Select vault view:"
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(15, 40)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(121, 21)
         Me.VaultsComboBox.TabIndex = 1
         '
         'SelectFiles
         '
         Me.SelectFiles.Location = New System.Drawing.Point(15, 85)
         Me.SelectFiles.Name = "SelectFiles"
         Me.SelectFiles.Size = New System.Drawing.Size(88, 23)
         Me.SelectFiles.TabIndex = 2
         Me.SelectFiles.Text = "Select a file..."
         Me.SelectFiles.UseVisualStyleBackColor = True
         '
         'File1List
         '
         Me.File1List.FormattingEnabled = True
         Me.File1List.HorizontalScrollbar = True
         Me.File1List.Location = New System.Drawing.Point(15, 114)
         Me.File1List.Name = "File1List"
         Me.File1List.Size = New System.Drawing.Size(257, 43)
         Me.File1List.TabIndex = 4
         '
         'GetHistories
         '
         Me.GetHistories.Location = New System.Drawing.Point(54, 172)
         Me.GetHistories.Name = "GetHistories"
         Me.GetHistories.Size = New System.Drawing.Size(157, 23)
         Me.GetHistories.TabIndex = 6
         Me.GetHistories.Text = "Get history"
         Me.GetHistories.UseVisualStyleBackColor = True
         '
         'OpenFileDialog1
         '
         Me.OpenFileDialog1.FileName = "OpenFileDialog1"
         Me.OpenFileDialog1.Multiselect = False
         Me.OpenFileDialog1.Title = "Select File"
         '
         'Rollback
         '
         Me.Rollback.Location = New System.Drawing.Point(54, 214)
         Me.Rollback.Name = "Rollback"
         Me.Rollback.Size = New System.Drawing.Size(157, 23)
         Me.Rollback.TabIndex = 7
         Me.Rollback.Text = "Roll back to first version"
         Me.Rollback.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(284, 259)
         Me.Controls.Add(Me.Rollback)
         Me.Controls.Add(Me.GetHistories)
         Me.Controls.Add(Me.File1List)
         Me.Controls.Add(Me.SelectFiles)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Get histories"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents SelectFiles As System.Windows.Forms.Button
     Friend WithEvents File1List As System.Windows.Forms.ListBox
     Friend WithEvents GetHistories As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog
     Friend WithEvents Rollback As Button
 End Class
```

[Back to top](#top)
