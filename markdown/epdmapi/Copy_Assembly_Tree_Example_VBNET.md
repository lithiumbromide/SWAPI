---
title: "Copy Assembly Tree of Files Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Copy_Assembly_Tree_Example_VBNET.htm"
---

# Copy Assembly Tree of Files Example (VB.NET)

This example shows how to copy an assembly and its tree of reference files to a destination folder in the vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 '    a. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms App.
 '    b. Type CopyTree in Project name.
 '    c. For Location, click ... and navigate to the folder where to create the project.
'      d. Click Next.
'    e. Select Framework.
'    f. Click Create.
'    g. Click Show All Files in the Solution Explorer toolbar and expand
'       Form1.vb in the Solution Explorer.
 '    h. Replace the code in Form1.vb with this code.
 '    i. To create the form, replace the code in Form1.Designer.vb with this code.
 ' 2. Add dependencies and safely pass arrays of structures.
 ' 3. Ensure that the vault root folder contains an assembly that is checked
 '    in with its referenced parts and drawings.
 ' 4. Create a destination folder called New Folder in the vault.
 ' 5. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Copy Assembly dialog box.
 '    a. Select a vault view.
 '    b. Click Select assembly.
  '       Locate and double-click an assembly.
 '    c. Click Select a destination folder.
 '       1. Locate and select New Folder.
 '       2. Click OK.
 '    d. Click Copy tree.
 '       The Copy Tree dialog shows the files to copy.
 '    e. Click Copy.
 '       The Copying tree progress bar appears.
 '    f. Inspect the destination folder.
  ' 2. Close the Copy Assembly dialog box.
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

     Public Sub BrowseButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BrowseAssembly.Click
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

     Public Sub Button1_Click(sender As Object, e As EventArgs) Handles BrowseDestFolder.Click
         Try
             ListBox1.Items.Clear()

             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             If Not vault1.IsLoggedIn Then
                 'Log into selected vault as the current user
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim rootFolder As IEdmFolder10
             rootFolder = vault1.RootFolder

             Dim aFolder As IEdmFolder10
             aFolder = vault1.BrowseForFolder(Me.Handle.ToInt32(), "Select a destination folder")

             ListBox1.Items.Add(rootFolder.LocalPath + "\" + aFolder.Name)

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub AddFiles_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles CopyTree.Click
         Try

             Dim vault2 As IEdmVault19 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault19)
             If Not vault1.IsLoggedIn Then
                 'Log into selected vault as the current user
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             If Not ListBox.Items.Count = 1 Then
                 MessageBox.Show("Please select an assembly.")
                 Exit Sub
             End If

             If Not ListBox1.Items.Count = 1 Then
                 MessageBox.Show("Please select a destination folder.")
                 Exit Sub
             End If

             Dim aFile As IEdmFile12
             Dim destFolder As String
             Dim Folder As IEdmFolder9

             Folder = vault2.RootFolder

             Dim FileNames(2) As String
             Dim Index As Integer = 0
             Dim fileStr = ""
             For Each FileName In ListBox.Items
                 fileStr = FileName.ToString()
                 FileNames(Index) = fileStr.Substring(fileStr.LastIndexOf("\"))
                 Index = Index + 1
             Next

             ' Copy the assembly's tree of files to the specified destination folder
             Dim copyTreeOptions As EdmCopyTreeOptions = Nothing
             copyTreeOptions.mbsPrefix = "Copy_"
             copyTreeOptions.mbsSuffix = ""
             copyTreeOptions.mbIncludeDrawings = -1
             copyTreeOptions.mbUseLatestVersion = -1

             aFile = vault2.GetFileFromPath(Folder.LocalPath + "\" + FileNames(0))
             destFolder = ListBox1.Items(0)
             vault2.CopyTree(aFile.ID, Folder.ID, destFolder, True, True, copyTreeOptions, Me.Handle.ToInt32())

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

 End Class

 Back to top
 'Form1.Designer.vb
 <Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
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
         Me.BrowseAssembly = New System.Windows.Forms.Button()
         Me.ListBox = New System.Windows.Forms.ListBox()
         Me.CopyTree = New System.Windows.Forms.Button()
         Me.OpenFileDialog = New System.Windows.Forms.OpenFileDialog()
         Me.BrowseDestFolder = New System.Windows.Forms.Button()
         Me.ListBox1 = New System.Windows.Forms.ListBox()
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
         'BrowseAssembly
         '
         Me.BrowseAssembly.Location = New System.Drawing.Point(16, 85)
         Me.BrowseAssembly.Name = "BrowseAssembly"
         Me.BrowseAssembly.Size = New System.Drawing.Size(108, 23)
         Me.BrowseAssembly.TabIndex = 3
         Me.BrowseAssembly.Text = "Select assembly..."
         Me.BrowseAssembly.UseVisualStyleBackColor = True
         '
         'ListBox
         '
         Me.ListBox.FormattingEnabled = True
         Me.ListBox.HorizontalScrollbar = True
         Me.ListBox.Location = New System.Drawing.Point(16, 114)
         Me.ListBox.Name = "ListBox"
         Me.ListBox.SelectionMode = System.Windows.Forms.SelectionMode.None
         Me.ListBox.Size = New System.Drawing.Size(259, 17)
         Me.ListBox.TabIndex = 4
         '
         'CopyTree
         '
         Me.CopyTree.Location = New System.Drawing.Point(86, 226)
         Me.CopyTree.Name = "CopyTree"
         Me.CopyTree.Size = New System.Drawing.Size(98, 23)
         Me.CopyTree.TabIndex = 5
         Me.CopyTree.Text = "Copy tree"
         Me.CopyTree.UseVisualStyleBackColor = True
         '
         'OpenFileDialog
         '
         Me.OpenFileDialog.Multiselect = True
         Me.OpenFileDialog.Title = "Open"
         '
         'BrowseDestFolder
         '
         Me.BrowseDestFolder.Location = New System.Drawing.Point(16, 152)
         Me.BrowseDestFolder.Name = "BrowseDestFolder"
         Me.BrowseDestFolder.Size = New System.Drawing.Size(155, 23)
         Me.BrowseDestFolder.TabIndex = 6
         Me.BrowseDestFolder.Text = "Select a destination folder..."
         Me.BrowseDestFolder.UseVisualStyleBackColor = True
         '
         'ListBox1
         '
         Me.ListBox1.FormattingEnabled = True
         Me.ListBox1.Location = New System.Drawing.Point(16, 181)
         Me.ListBox1.Name = "ListBox1"
         Me.ListBox1.Size = New System.Drawing.Size(259, 17)
         Me.ListBox1.TabIndex = 7
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(317, 280)
         Me.Controls.Add(Me.ListBox1)
         Me.Controls.Add(Me.BrowseDestFolder)
         Me.Controls.Add(Me.CopyTree)
         Me.Controls.Add(Me.ListBox)
         Me.Controls.Add(Me.BrowseAssembly)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Copy Assembly"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents BrowseAssembly As System.Windows.Forms.Button
     Friend WithEvents ListBox As System.Windows.Forms.ListBox
     Friend WithEvents CopyTree As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog As System.Windows.Forms.OpenFileDialog
     Friend WithEvents BrowseDestFolder As Button
     Friend WithEvents ListBox1 As ListBox
 End Class
```

[Back to top](#top)
