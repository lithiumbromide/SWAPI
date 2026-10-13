---
title: "Batch Check In Files Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Batch_Unlock_Files_Example_VBNET.htm"
---

# Batch Check In Files Example (VB.NET)

This example shows how to check in several files in one batch.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 '  1. Start Microsoft Visual Studio 2010.
 '     a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '     b. Type BatchUnlockFiles in Name.
 '     c. Click Browse and navigate to the folder where to create the project.
 '     d. Click OK.
 '     e. Click Show All Files in the Solution Explorer toolbar and expand
 '        Form1.vb in the Solution Explorer.
 '     f. Replace the code in Form1.vb with this code.
 '     g. To create the form, replace the code in Form1.Designer.vb with
 '        this code.
 '  2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 '     name in the Solution Explorer, click Add Reference, click
 '     Assemblies > Framework in the left-side panel, browse to the top folder of
 '     your SOLIDWORKS PDM Professional installation, locate and click
 '     EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
 '  3. Right-click EPDM.Interop.epdm in References, click Properties, and set
 '     Embed Interop Types to False to handle methods that pass arrays of
 '     structures.
 '  4. Check out a vault file.
 '  5. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 '  1. Displays the Check In Files dialog box.
 '     a. Select a vault view.
 '     b. Click Select files to check out from vault.
 '     c. In the Select File dialog:
 '        1. Click the checked-out vault file.
 '        2. Click Open.
 '     d. Click Check in files.
 '     e. Displays the Check in dialog box with the Reload or Close Files
 '        after Check In dropdown in the toolbar.
 '     f. Click the Check in button.
 '     g. Click OK in the message box.
 '  2. Close the Check In Files dialog box.
  '  3. Observe that the selected file is checked in to the selected vault.
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
     Dim batchUnlocker As IEdmBatchUnlock2
     Dim fileList As IEdmSelectionList6 = Nothing
     Dim poSel As EdmSelectionObject = Nothing
     Dim ppoSelection() As EdmSelItem
     Dim fileCount As Integer = 0
     Dim aFile As IEdmFile5
     Dim aFolder As IEdmFolder5
     Dim aPos As IEdmPos5
     Dim str As String
     Dim retVal As Boolean

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

             batchUnlocker = vault2.CreateUtility(EdmUtility.EdmUtil_BatchUnlock)

             Dim nbrFiles As Integer = 0
             nbrFiles = OpenFileDialog1.FileNames.Count()
             Array.Resize(ppoSelection, nbrFiles)

             'If the user did not click Open, no files selected
             If Not (DialogResult = System.Windows.Forms.DialogResult.OK) Then
                 ' do nothing
             Else
                 Dim i As Integer = 0
                 For Each FileName As String In OpenFileDialog1.FileNames
                     File1List.Items.Add(FileName)
                     aFile = vault1.GetFileFromPath(FileName)
                     aPos = aFile.GetFirstFolderPosition
                     aFolder = aFile.GetNextFolder(aPos)
                     ppoSelection(i) = New EdmSelItem
                     ppoSelection(i).mlDocID = aFile.ID
                     ppoSelection(i).mlProjID = aFolder.ID
                     i = i + 1
                 Next
                 ' Add selections to the batch of files to check in
                 batchUnlocker.AddSelection(vault1, ppoSelection)
             End If

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub BatchUnlock_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BatchUnlock.Click
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             If Not IsNothing(batchUnlocker) Then

                 batchUnlocker.CreateTree(Me.Handle.ToInt32(), EdmUnlockBuildTreeFlags.Eubtf_ShowCloseAfterCheckinOption + EdmUnlockBuildTreeFlags.Eubtf_MayUnlock)

                 batchUnlocker.Comment = "Updates"
                 fileList = batchUnlocker.GetFileList(EdmUnlockFileListFlag.Euflf_GetUnlocked + EdmUnlockFileListFlag.Euflf_GetUndoLocked + EdmUnlockFileListFlag.Euflf_GetUnprocessed)

                 aPos = fileList.GetHeadPosition()

                 str = "Getting " & fileCount & " files: "
                 While Not (aPos.IsNull())
                     fileList.GetNext2(aPos, poSel)
                     str = str + vbLf + poSel.mbsPath
                 End While

                 'MsgBox(str)

                 retVal = batchUnlocker.ShowDlg(Me.Handle.ToInt32())

                 Dim statuses As Object
                 If (retVal) Then
                     batchUnlocker.UnlockFiles(Me.Handle.ToInt32(), Nothing)
                     statuses = batchUnlocker.GetStatus(EdmUnlockStatusFlag.Eusf_CloseAfterCheckinFlag)
                    MsgBox("Close Files after Check In selected? " & statuses)

                 End If

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
         Me.BatchUnlock = New System.Windows.Forms.Button()
         Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
         Me.SuspendLayout()
         '
         'VaultsLabel
         '
         Me.VaultsLabel.AutoSize = True
         Me.VaultsLabel.Location = New System.Drawing.Point(36, 24)
         Me.VaultsLabel.Name = "VaultsLabel"
         Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
         Me.VaultsLabel.TabIndex = 0
         Me.VaultsLabel.Text = "Select vault view:"
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(39, 40)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(121, 21)
         Me.VaultsComboBox.TabIndex = 1
         '
         'SelectFiles
         '
         Me.SelectFiles.Location = New System.Drawing.Point(39, 85)
         Me.SelectFiles.Name = "SelectFiles"
         Me.SelectFiles.Size = New System.Drawing.Size(191, 23)
         Me.SelectFiles.TabIndex = 2
         Me.SelectFiles.Text = "Select files to check in to vault..."
         Me.SelectFiles.UseVisualStyleBackColor = True
         '
         'File1List
         '
         Me.File1List.FormattingEnabled = True
         Me.File1List.HorizontalScrollbar = True
         Me.File1List.Location = New System.Drawing.Point(40, 114)
         Me.File1List.Name = "File1List"
         Me.File1List.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended
         Me.File1List.Size = New System.Drawing.Size(220, 43)
         Me.File1List.TabIndex = 4
         '
         'BatchUnlock
         '
         Me.BatchUnlock.Location = New System.Drawing.Point(40, 183)
         Me.BatchUnlock.Name = "BatchUnlock"
         Me.BatchUnlock.Size = New System.Drawing.Size(157, 23)
         Me.BatchUnlock.TabIndex = 6
         Me.BatchUnlock.Text = "Check in files"
         Me.BatchUnlock.UseVisualStyleBackColor = True
         '
         'OpenFileDialog1
         '
         Me.OpenFileDialog1.FileName = "OpenFileDialog1"
         Me.OpenFileDialog1.Multiselect = True
         Me.OpenFileDialog1.Title = "Select File"
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(284, 242)
         Me.Controls.Add(Me.BatchUnlock)
         Me.Controls.Add(Me.File1List)
         Me.Controls.Add(Me.SelectFiles)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Check In Files"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents SelectFiles As System.Windows.Forms.Button
     Friend WithEvents File1List As System.Windows.Forms.ListBox
     Friend WithEvents BatchUnlock As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog

 End Class
```

[Back to top](#top)
