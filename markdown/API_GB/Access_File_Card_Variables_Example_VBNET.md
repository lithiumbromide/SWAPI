---
title: "Access File Card Variables Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Access_File_Card_Variables_Example_VBNET.htm"
---

# Access File Card Variables Example (VB.NET)

This example shows how to access file card variables.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio 2010.
 '    a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '    b. Type CardVars in Name.
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
 ' 4. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Access file variables dialog box.
 '    a. Select a vault view.
 '    b. Click Browse.
  '       1. Locate and click a file in the vault.
 '       2. Click Open.
 '    c. Click Get variables.
 '       1. Checks out the selected file in the root folder of the vault.
 '       2. Displays a message box with all of the card variables that can be
 '          updated for the selected file in configuration, @.
 '    d. Click OK.
 '    e. Undoes the check-out of the selected file.
  ' 2. Close the Access file variables dialog box.
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

     Public Sub GetVars_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GetVars.Click
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

             Dim parentFolder As IEdmFolder5 = Nothing
             Dim aFile As IEdmFile5  = Nothing
             aFile = vault2.GetFileFromPath(ListBox.Items(0).ToString(), parentFolder)

             'Get card variables only from a file checked into the vault
             If Not aFile.IsLocked Then
                 aFile.LockFile(parentFolder.ID, Me.Handle.ToInt32(), EdmLockFlag.EdmLock_Simple)

                 Dim varEnum As IEdmEnumeratorVariable5
                 varEnum = aFile.GetEnumeratorVariable

                 Dim valueList() As Object = Nothing
                 varEnum.GetUpdateVars(aFile.LockedInFolderID, valueList)

                 Dim idx As Integer
                 idx = LBound(valueList)
                 Dim upper As Integer
                 upper = UBound(valueList)

                 Dim msg As String
                 msg = "Card variables for " & aFile.Name & " in configuration, @:" & vbLf & vbLf

                 Dim varMgr As IEdmVariableMgr5
                 varMgr = aFile.Vault

                 Dim var As IEdmVariable5
                 Dim value As IEdmVariableValue6
                 While idx <= upper
                     value = valueList(idx)
                     idx = idx + 1
                     var = varMgr.GetVariable(value.VariableID)
                     msg = msg & value.VariableName & " = > " & value.GetValue("@").ToString() & vbLf
                     msg = msg & "EdmVariableFlags: " & var.Flags & ", EdmVariableType: " & var.VariableType & vbLf & vbLf
                     'msg = msg & "EdmVariableFlags: " & value.VariableFlags & ", EdmVariableType: " & value.VariableType & vbLf & vbLf
                 End While

                 MessageBox.Show(msg)

                 aFile.UndoLockFile(Me.Handle.ToInt32())
             Else
                 'User selected a checked-out file
                 MessageBox.Show("Please select a checked-in file.")
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
         Me.GetVars = New System.Windows.Forms.Button()
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
         'GetVars
         '
         Me.GetVars.Location = New System.Drawing.Point(84, 178)
         Me.GetVars.Name = "GetVars"
         Me.GetVars.Size = New System.Drawing.Size(98, 23)
         Me.GetVars.TabIndex = 5
         Me.GetVars.Text = "Get variables"
         Me.GetVars.UseVisualStyleBackColor = True
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
         Me.Controls.Add(Me.GetVars)
         Me.Controls.Add(Me.ListBox)
         Me.Controls.Add(Me.BrowseButton)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Access file variables"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents BrowseButton As System.Windows.Forms.Button
     Friend WithEvents ListBox As System.Windows.Forms.ListBox
     Friend WithEvents GetVars As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog As System.Windows.Forms.OpenFileDialog
 End Class
```

[Back to top](#top)
