---
title: "Access Custom File References Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Access_Custom_File_References_Example_VBNET.htm"
---

# Access Custom File References Example (VB.NET)

This example shows how to access custom file references.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 '    a. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms Application.
 '    b. Type AccessCustRef in Project name.
 '    c. For Location, click ... and navigate to the folder where to create the project.
'      d. Click Next.
'    e. Select Framework.
'    f. Click Create.
'    g. Click Show All Files in the Solution Explorer toolbar and expand
'        Form1.vb in the Solution Explorer.
 '    h. Replace the code in Form1.vb with this code.
 '    i. To create the form, replace the code in Form1.Designer.vb with
 '       this code.
 ' 2. Add dependencies and safely pass arrays of structures.
 ' 3. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Add custom file reference dialog box.
 '    a. Select a vault view.
 '    b. Click Browse for two files.
  '       1. Locate and click two files in the root folder of the vault.
 '       2. Click Open.
 '       3. Checks out the first file.
 '    c. Click Add custom file reference.
  '    d. Click OK to close each message box.
  ' 2. Close the Add custom file reference dialog.
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
     Dim addCustRefs As IEdmEnumeratorCustomReference7
     Dim file1 As IEdmFile5 = Nothing
     Dim file2 As IEdmFile5 = Nothing
     Dim parentFolder As IEdmFolder5 = Nothing

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
             CustRefListBox.Items.Clear()

             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             If Not vault1.IsLoggedIn Then
                 'Log into selected vault as the current user
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             'Set the initial directory in the Open dialog
             CustRefOpenFileDialog.InitialDirectory = vault1.RootFolderPath
             'Show the Open dialog
             Dim DialogResult As System.Windows.Forms.DialogResult = Nothing
             DialogResult = CustRefOpenFileDialog.ShowDialog()
             'If the user didn't click Open, exit
             If Not (DialogResult = System.Windows.Forms.DialogResult.OK) Then
                 Return
             End If

             For Each FileName As String In CustRefOpenFileDialog.FileNames
                 CustRefListBox.Items.Add(FileName)
             Next
         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub AddCustomFileReference_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles AddCustomFileReference.Click
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

             'Get the two selected files
             file1 = vault2.GetFileFromPath(CustRefListBox.Items(0), parentFolder)
             file2 = vault2.GetFileFromPath(CustRefListBox.Items(1), parentFolder)

            'Check out the first file
             If Not file1.IsLocked Then
                 file1.LockFile(parentFolder.ID, Me.Handle.ToInt32(), CInt(EdmLockFlag.EdmLock_Simple))
             End If

             'Add the second file as a custom reference to the first file
             addCustRefs = file1
             addCustRefs.AddReference3(file2.ID, parentFolder.ID, 1, True)
             MessageBox.Show(file2.Name & " added as reference to " & file1.Name)
             Dim shownInBOM As Boolean
             shownInBOM = addCustRefs.GetShowInBOM(file2.ID, parentFolder.ID)
             MessageBox.Show(file2.Name & " shown in BOM? " & shownInBOM

             'Check in the first file
             file1.UnlockFile(Me.Handle.ToInt32(), "Custom reference added")

             'Display all of the custom references of the first file
             ShowFileRefs()

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub ShowFileRefs()
         Try
             Dim enumRef As IEdmEnumeratorCustomReference6
             enumRef = file1
             Dim pos As IEdmPos5
             pos = enumRef.GetFirstRefPosition
             Dim fileID As Integer
             Dim folderID As Integer
             Dim message As String
             Dim quant As Integer = 1
             Dim pbsRetPath As String = ""
             message = "Custom references of " + file1.Name + ":" + vbLf
             While Not pos.IsNull
                 enumRef.GetNextRef2(pos, fileID, folderID, pbsRetPath, quant)
                 message = message + pbsRetPath + " (fileID=" + Str(fileID) + ", folderID=" + Str(folderID) + ", quantity=" + Str(quant) + ")" + vbLf
             End While
             MsgBox(message)
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
         Me.CustRefListBox = New System.Windows.Forms.ListBox()
         Me.AddCustomFileReference = New System.Windows.Forms.Button()
         Me.CustRefOpenFileDialog = New System.Windows.Forms.OpenFileDialog()
         Me.SuspendLayout()
         '
         'VaultsLabel
         '
         Me.VaultsLabel.AutoSize = True
         Me.VaultsLabel.Location = New System.Drawing.Point(13, 26)
         Me.VaultsLabel.Name = "VaultsLabel"
         Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
         Me.VaultsLabel.TabIndex = 0
         Me.VaultsLabel.Text = "Select vault view:"
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
         Me.BrowseButton.Location = New System.Drawing.Point(16, 78)
         Me.BrowseButton.Name = "BrowseButton"
         Me.BrowseButton.Size = New System.Drawing.Size(146, 23)
         Me.BrowseButton.TabIndex = 3
         Me.BrowseButton.Text = "Browse for two files..."
         Me.BrowseButton.UseVisualStyleBackColor = True
         '
         'CustRefListBox
         '
         Me.CustRefListBox.FormattingEnabled = True
         Me.CustRefListBox.HorizontalScrollbar = True
         Me.CustRefListBox.Location = New System.Drawing.Point(16, 107)
         Me.CustRefListBox.Name = "CustRefListBox"
         Me.CustRefListBox.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended
         Me.CustRefListBox.Size = New System.Drawing.Size(259, 56)
         Me.CustRefListBox.TabIndex = 4
         '
         'AddCustomFileReference
         '
         Me.AddCustomFileReference.Location = New System.Drawing.Point(68, 175)
         Me.AddCustomFileReference.Name = "AddCustomFileReference"
         Me.AddCustomFileReference.Size = New System.Drawing.Size(150, 23)
         Me.AddCustomFileReference.TabIndex = 5
         Me.AddCustomFileReference.Text = "Add custom file reference"
         Me.AddCustomFileReference.UseVisualStyleBackColor = True
         '
         'CustRefOpenFileDialog
         '
         Me.CustRefOpenFileDialog.Multiselect = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(287, 222)
         Me.Controls.Add(Me.AddCustomFileReference)
         Me.Controls.Add(Me.CustRefListBox)
         Me.Controls.Add(Me.BrowseButton)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Add custom file reference"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents BrowseButton As System.Windows.Forms.Button
     Friend WithEvents CustRefListBox As System.Windows.Forms.ListBox
     Friend WithEvents AddCustomFileReference As System.Windows.Forms.Button
     Friend WithEvents CustRefOpenFileDialog As System.Windows.Forms.OpenFileDialog
 End Class
```

[Back to top](#top)
