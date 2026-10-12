---
title: "Create Labels on Folders Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Create_Label_Example_VBNET.htm"
---

# Create Labels on Folders Example (VB.NET)

This example shows how to create a label on a folder and all of its subfolders and files.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 '    a. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms App.
 '    b. Type CreateLabel in Project name.
 '    c. For Location, click ... and navigate to the folder where to create the project.
'      d. Click Next.
'    e. Select Framework.
'    f. Click Create.
'    g. Click Show All Files in the Solution Explorer toolbar and expand
'       Form1.vb in the Solution Explorer.
 '    h. Replace the code in Form1.vb with this code.
 '    i. To create the form, replace the code in Form1.Designer.vb with this code.
 ' 2. Add dependencies and safely pass arrays of structures.
 ' 3. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Create label dialog box.
 '    a. Select a vault view.
 '    b. Click Browse for parent folder.
  '       1. Locate and click a folder in the vault.
 '       2. Click OK.
 '    c. Click Create label.
 '       1. Creates label, MyCompany, on the selected folder and all of its
 '          subfolders and files.
 '       2. Displays a message box with information about all of the labels
 '          on the selected folder.
 '       3. Click OK.
  ' 2. Close the Create label dialog box.
 ' 3. To verify label creation on a folder or file, open a view on the
 '    selected vault, click either a folder or a file, and click
 '    Display > History.
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

             'Show the Browse For Folder dialog
             Dim DialogResult As System.Windows.Forms.DialogResult = Nothing
             DialogResult = FolderBrowserDialog1.ShowDialog()
             'If the user didn't click OK, exit
             If Not (DialogResult = System.Windows.Forms.DialogResult.OK) Then
                 Return
             End If

             ListBox.Items.Add(FolderBrowserDialog1.SelectedPath)

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub CreateLabel_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles CreateLabel.Click
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

             Dim parentFolder As IEdmFolder5
             parentFolder = vault2.GetFolderFromPath(ListBox.Items(0).ToString())

             Dim labelID As Integer
             Dim labelName As String = "MyCompany"
             labelID = parentFolder.CreateLabel(labelName, "Label set by test program", True)

             Dim pos As IEdmPos5
             Dim label As IEdmLabel5
             Dim message As String
             message = "The following labels have been set on folder " + parentFolder.Name + ":" + vbLf
             pos = parentFolder.GetFirstLabelPosition
             While Not pos.IsNull
                 label = parentFolder.GetNextLabel(pos)
                 message = message & label.Name & " (" & label.Comment & ")" & " created by " & label.User.Name & "(ID = " & label.UserID & ")" & " at " & label.Time & vbLf
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
         Me.CreateLabel = New System.Windows.Forms.Button()
         Me.FolderBrowserDialog1 = New System.Windows.Forms.FolderBrowserDialog()
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
         Me.BrowseButton.Size = New System.Drawing.Size(186, 23)
         Me.BrowseButton.TabIndex = 3
         Me.BrowseButton.Text = "Browse for parent folder..."
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
         'CreateLabel
         '
         Me.CreateLabel.Location = New System.Drawing.Point(84, 178)
         Me.CreateLabel.Name = "CreateLabel"
         Me.CreateLabel.Size = New System.Drawing.Size(98, 23)
         Me.CreateLabel.TabIndex = 5
         Me.CreateLabel.Text = "Create label"
         Me.CreateLabel.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(317, 215)
         Me.Controls.Add(Me.CreateLabel)
         Me.Controls.Add(Me.ListBox)
         Me.Controls.Add(Me.BrowseButton)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Create label"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents BrowseButton As System.Windows.Forms.Button
     Friend WithEvents ListBox As System.Windows.Forms.ListBox
     Friend WithEvents CreateLabel As System.Windows.Forms.Button
     Friend WithEvents FolderBrowserDialog1 As System.Windows.Forms.FolderBrowserDialog
 End Class
```

[Back to top](#top)
