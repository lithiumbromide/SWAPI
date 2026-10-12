---
title: "Batch Add Files and Folders to Vault Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Batch_Add_Files_and_Folders_Example_VBNET.htm"
---

# Batch Add Files and Folders to Vault Example (VB.NET)

This example shows how to add several files and folders to the vault in one batch.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 '  1. Start Microsoft Visual Studio 2010.
 '     a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '     b. Type BatchAddFiles in Name.
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
 '  4. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 '  1. The Batch add files to vault dialog box displays.
 '     a. Select a vault view.
 '     b. Click Select file outside vault to copy to vault.
 '     c. In the Select File dialog:
 '        1. Click a file outside the vault.
 '        2. Click Open.
 '     d. Click Select file inside vault to copy to vault.
 '     e. In the Select File dialog:
 '        1. Click a file in the vault.
 '        2. Click Open.
 '     f. Click Commit all files to vault.
 '  2. Click Add in the Batch Items dialog box.
 '  3. Click OK to close the message box.
 '     Two new folders, Folder1 and Folder2, are created in the vault's
 '     root directory. The first selected file is copied to Folder1.
 '     The second selected file is copied to Folder2.
 '  4. Close the Batch add files to vault dialog box.
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
     Dim batchAdder As IEdmBatchAdd2
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

     Public Sub CopyToVault_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles CopyToVault.Click
         Try
             FileList1.Items.Clear()

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             'Set the initial directory in the Select File dialog
             SelectFileDialog.InitialDirectory = vault1.RootFolderPath
             'Show the Select File dialog
             Dim DialogResult As System.Windows.Forms.DialogResult = Nothing
             DialogResult = SelectFileDialog.ShowDialog()
             'If the user did not click Open, exit this subroutine
             If Not (DialogResult = System.Windows.Forms.DialogResult.OK) Then
                 Return
             End If

             batchAdder = vault2.CreateUtility(EdmUtility.EdmUtil_BatchAdd)

             ' Add Folder1 to the batch
             Dim newFolder As String = vault1.RootFolderPath + "\Folder1"
             batchAdder.AddFolderPath(newFolder, 0, EdmBatchAddFolderFlag.Ebaff_Nothing)

             For Each FileName As String In SelectFileDialog.FileNames

                 FileList1.Items.Add(FileName)

                 ' Add each selected file to the batch
                 batchAdder.AddFileFromPathToPath(FileName, newFolder, 0)

             Next
         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub
     Public Sub CopyFromVault_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles CopyFromVault.Click
         Try
             FileList2.Items.Clear()

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             'Set the initial directory in the Select File dialog
             SelectFileDialog.InitialDirectory = vault1.RootFolderPath
             'Show the Select File dialog
             Dim DialogResult As System.Windows.Forms.DialogResult = Nothing
             DialogResult = SelectFileDialog.ShowDialog()
             'If the user didn't click Open, exit this subroutine
             If Not (DialogResult = System.Windows.Forms.DialogResult.OK) Then
                 Return
             End If

             ' Add Folder2 to the batch
             batchAdder.AddFolder(vault1.RootFolderID, "Folder2", 0, EdmBatchAddFolderFlag.Ebaff_Nothing)

             Dim aFile As IEdmFile5
             Dim aFolder As IEdmFolder5
             Dim aPos As IEdmPos5
             For Each FileName As String In SelectFileDialog.FileNames

                 FileList2.Items.Add(FileName)

                 aFile = vault1.GetFileFromPath(FileName)
                 aPos = aFile.GetFirstFolderPosition
                 aFolder = aFile.GetNextFolder(aPos)

                 ' Add each selected file to the batch
                 batchAdder.AddFileFromVaultToPath(aFile.ID, aFolder.ID, vault1.RootFolderPath + "\Folder2")

             Next
         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub BatchAdd_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BatchAdd.Click
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             ' Show all of the items in the batch
             batchAdder.ShowDlg(Me.Handle.ToInt32(), EdmAddFileDlgFlag.Eafdf_Nothing, "Files and folders in the batch:", "Batch Items")

             Dim ppoAddedFiles() As EdmFileInfo = Nothing

             ' Commit all of the items in the batch to the vault
             batchAdder.CommitAdd(Me.Handle.ToInt32(), ppoAddedFiles)

             'Display the returned information in a message box
             Dim idx As Integer
             idx = LBound(ppoAddedFiles)
             Dim msg As String = ""

             While idx <= UBound(ppoAddedFiles)

                 Dim row As String
                 row = "(" + ppoAddedFiles(idx).mbsPath + ") arg = " + CStr(ppoAddedFiles(idx).mlArg)

                 If ppoAddedFiles(idx).mhResult = 0 Then
                     row = row + " status = OK "
                 Else
                     Dim oErrName As String = ""
                     Dim oErrDesc As String = ""

                     vault1.GetErrorString(ppoAddedFiles(idx).mhResult, oErrName, oErrDesc)
                     row = row + " status = " + oErrName
                 End If

                 idx = idx + 1
                 msg = msg + vbLf + row

             End While

             MsgBox(msg)

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
         Me.BatchAdd = New System.Windows.Forms.Button()
         Me.CopyToVault = New System.Windows.Forms.Button()
         Me.FileList1 = New System.Windows.Forms.ListBox()
         Me.CopyFromVault = New System.Windows.Forms.Button()
         Me.FileList2 = New System.Windows.Forms.ListBox()
         Me.SelectFileDialog = New System.Windows.Forms.OpenFileDialog()
         Me.SuspendLayout()
         '
         'VaultsLabel
         '
         Me.VaultsLabel.AutoSize = True
         Me.VaultsLabel.Location = New System.Drawing.Point(12, 27)
         Me.VaultsLabel.Name = "VaultsLabel"
         Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
         Me.VaultsLabel.TabIndex = 0
         Me.VaultsLabel.Text = "Select vault view:"
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(12, 43)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(121, 21)
         Me.VaultsComboBox.TabIndex = 1
         '
         'BatchAdd
         '
         Me.BatchAdd.Location = New System.Drawing.Point(67, 236)
         Me.BatchAdd.Name = "BatchAdd"
         Me.BatchAdd.Size = New System.Drawing.Size(123, 23)
         Me.BatchAdd.TabIndex = 2
         Me.BatchAdd.Text = "Commit all files to vault"
         Me.BatchAdd.UseVisualStyleBackColor = True
         '
         'CopyToVault
         '
         Me.CopyToVault.Location = New System.Drawing.Point(12, 80)
         Me.CopyToVault.Name = "CopyToVault"
         Me.CopyToVault.Size = New System.Drawing.Size(239, 23)
         Me.CopyToVault.TabIndex = 3
         Me.CopyToVault.Text = "Select file outside vault to copy to vault..."
         Me.CopyToVault.UseVisualStyleBackColor = True
         '
         'FileList1
         '
         Me.FileList1.FormattingEnabled = True
         Me.FileList1.Location = New System.Drawing.Point(12, 109)
         Me.FileList1.Name = "FileList1"
         Me.FileList1.Size = New System.Drawing.Size(239, 30)
         Me.FileList1.TabIndex = 4
         '
         'CopyFromVault
         '
         Me.CopyFromVault.Location = New System.Drawing.Point(12, 160)
         Me.CopyFromVault.Name = "CopyFromVault"
         Me.CopyFromVault.Size = New System.Drawing.Size(239, 23)
         Me.CopyFromVault.TabIndex = 5
         Me.CopyFromVault.Text = "Select file inside vault to copy to vault..."
         Me.CopyFromVault.UseVisualStyleBackColor = True
         '
         'FileList2
         '
         Me.FileList2.FormattingEnabled = True
         Me.FileList2.Location = New System.Drawing.Point(12, 189)
         Me.FileList2.Name = "FileList2"
         Me.FileList2.Size = New System.Drawing.Size(239, 30)
         Me.FileList2.TabIndex = 6
         '
         'SelectFileDialog
         '
         Me.SelectFileDialog.Title = "Select File"
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(284, 291)
         Me.Controls.Add(Me.FileList2)
         Me.Controls.Add(Me.CopyFromVault)
         Me.Controls.Add(Me.FileList1)
         Me.Controls.Add(Me.CopyToVault)
         Me.Controls.Add(Me.BatchAdd)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Batch add files to vault"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents BatchAdd As System.Windows.Forms.Button
     Friend WithEvents CopyToVault As System.Windows.Forms.Button
     Friend WithEvents FileList1 As System.Windows.Forms.ListBox
     Friend WithEvents CopyFromVault As System.Windows.Forms.Button
     Friend WithEvents FileList2 As System.Windows.Forms.ListBox
     Friend WithEvents SelectFileDialog As System.Windows.Forms.OpenFileDialog

 End Class
```

[Back to top](#top)
