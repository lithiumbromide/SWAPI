---
title: "Batch Delete Files and Folders from Vault Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Batch_Delete_Files_and_Folders_Example_VBNET.htm"
---

# Batch Delete Files and Folders from Vault Example (VB.NET)

This example shows how to delete several files and a folder from the vault in one batch.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 '  1. Start Microsoft Visual Studio.
 '     a. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms Application.
 '     b. Type BatchDeleteFiles in Project name.
 '     c. For Location, click ... and navigate to the folder where to create the project.
'       d. Click Next.
'     e. Select Framework.
'     f. Click Create.
'     g. Click Show All Files in the Solution Explorer toolbar and expand
'       Form1.vb in the Solution Explorer.
 '     h. Replace the code in Form1.vb with this code.
 '     i. To create the form, replace the code in Form1.Designer.vb with
 '        this code.
 '  2. Add dependencies and safely pass arrays of structures.
 '  3. Ensure that the root folder of the vault contains an empty Folder1 and at
 '     least one file.
 '  4. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 '  1. The Delete Files dialog box displays.
 '     a. Select a vault view.
 '     b. Click Select files to delete from vault.
 '     c. In the Select File dialog:
 '        1. Click a file inside the vault.
 '        2. Click Open.
 '     d. Click Delete files from vault.
 '  2. Click Delete in the Confirm Multiple File Delete dialog box.
 '     a. If no errors occur, the selected file and  Folder1 are moved
 '        from the vault to the SOLIDWORKS PDM recycling bin. (To see the
 '        SOLIDWORKS PDM recycling bin, right-click your vault, click
 '        Properties, and click  Deleted Items.)
 '     b. If an error dialog box pops up, click OK to close it.
 '  3. Close the Delete Files dialog box.
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
     Dim batchDeleter As IEdmBatchDelete3
     Dim aFile As IEdmFile5
     Dim aFolder As IEdmFolder5
     Dim aPos As IEdmPos5
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
             'File1List.Items.Clear()

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

             batchDeleter = vault2.CreateUtility(EdmUtility.EdmUtil_BatchDelete)

             If Not (DialogResult = System.Windows.Forms.DialogResult.OK) Then
                 ' do nothing
             Else
                 For Each FileName As String In OpenFileDialog1.FileNames
                     File1List.Items.Add(FileName)
                     aFile = vault1.GetFileFromPath(FileName)
                     aPos = aFile.GetFirstFolderPosition
                     aFolder = aFile.GetNextFolder(aPos)
                     ' Add selected file to the batch
                     batchDeleter.AddFileByPath(FileName)
                 Next
             End If

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub BatchDelete_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BatchDelete.Click
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             If Not IsNothing(batchDeleter) Then
                 ' Add Folder1 to the batch of items to be deleted
                 batchDeleter.AddFolder(vault1.RootFolderPath + "\Folder1")

                 ' Move files and folder to the Recycle Bin
                 retVal = batchDeleter.ComputePermissions(False, Nothing)

                 If (Not retVal) Then
                     batchDeleter.ShowWarningDlg2(Me.Handle.ToInt32(), True)
                 End If

                 retVal = batchDeleter.CommitDelete(Me.Handle.ToInt32(), Nothing)

                 Dim ppoDelErrors() As EdmBatchDelErrInfo = Nothing
                 If (Not retVal) Then
                     batchDeleter.ShowCommitErrorsDlg(Me.Handle.ToInt32())
                     batchDeleter.GetCommitErrors(ppoDelErrors)
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
         Me.BatchDelete = New System.Windows.Forms.Button()
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
         Me.SelectFiles.Text = "Select files to delete from vault..."
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
         'BatchDelete
         '
         Me.BatchDelete.Location = New System.Drawing.Point(40, 183)
         Me.BatchDelete.Name = "BatchDelete"
         Me.BatchDelete.Size = New System.Drawing.Size(157, 23)
         Me.BatchDelete.TabIndex = 6
         Me.BatchDelete.Text = "Delete files from vault"
         Me.BatchDelete.UseVisualStyleBackColor = True
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
         Me.ClientSize = New System.Drawing.Size(284, 235)
         Me.Controls.Add(Me.BatchDelete)
         Me.Controls.Add(Me.File1List)
         Me.Controls.Add(Me.SelectFiles)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Delete Files"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents SelectFiles As System.Windows.Forms.Button
     Friend WithEvents File1List As System.Windows.Forms.ListBox
     Friend WithEvents BatchDelete As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog

 End Class
```

[Back to top](#top)
