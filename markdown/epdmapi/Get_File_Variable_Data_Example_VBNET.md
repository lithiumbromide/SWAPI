---
title: "Get File Variable Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_File_Variable_Data_Example_VBNET.htm"
---

# Get File Variable Data Example (VB.NET)

This example shows how to get the card variable data for the latest version of a selected file.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
   '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 ' 2. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms App.
 ' 4. For Location, click ... and navigate to the folder where to create the project.
 ' 5. Click Next.
 ' 6. Select Framework.
 ' 7. Click Create.
 ' 8. Click Show All Files in the Solution Explorer toolbar and expand
 '    Form1.vb in the Solution Explorer.
 ' 9.  Add dependencies and safely pass arrays of structures.
 '10. Replace the code in Form1.vb with this code.
 '11. To create the form, replace the code in Form1.Designer.vb with
 '    this code.
 '12. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the File variable data dialog box.
 ' 2. Select a vault view.
 ' 3. Click Select file.
 '    a. In the Select File dialog:
 '       1. Click a vault file.
 '       2. Click Open.
 ' 4. Click Get variable data.
 ' 5. Click OK in the message box.
 ' 6. Close the File variable data dialog box.
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

     Private vault1 As IEdmVault5
     Dim aFile As IEdmFile7
     Dim aFolder As IEdmFolder5
     Dim enumVar As IEdmEnumeratorVariable7

     Public Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
         Try
             vault1 = New EdmVault5()
             Dim vault As IEdmVault10 = DirectCast(vault1, IEdmVault10)
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

     Public Sub SelectFile_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles SelectFile.Click
         Try
             File1List.Items.Clear()

             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             'Set the initial directory in the Select File dialog
             OpenFileDialog1.InitialDirectory = vault1.RootFolderPath

             'Show the Select File dialog
             Dim DialogResult As System.Windows.Forms.DialogResult = Nothing
             DialogResult = OpenFileDialog1.ShowDialog()

             If Not (DialogResult = System.Windows.Forms.DialogResult.OK) Then
                 ' do nothing
             Else
                 For Each FileName As String In OpenFileDialog1.FileNames
                     File1List.Items.Add(FileName)
                     aFile = vault1.GetFileFromPath(FileName, aFolder)
                 Next
             End If

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub GetVarData_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GetVarData.Click
         Try

             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim ppoRetVars() As Object = Nothing
             Dim ppoRetConfs() As String = Nothing
             Dim poRetDat As EdmGetVarData = Nothing

             enumVar = aFile.GetEnumeratorVariable()
             enumVar.GetVersionVars(0, aFolder.ID, ppoRetVars, ppoRetConfs, poRetDat)

             Dim str As String
             str = "File variable data for " & aFile.Name & vbLf
             str = str & "Version: " & poRetDat.mlVersion & vbLf
             str = str & "Latest version: " & poRetDat.mlLatestVersion & vbLf
             str = str & "Revision: " & poRetDat.mbsRevision & vbLf
             str = str & "State: " & poRetDat.mbsState & vbLf
             str = str & "Workflow: " & poRetDat.mbsWorkflow & vbLf
             str = str & "Category: " & poRetDat.mbsCategory & vbLf
             str = str & "SQL Server date format code: " & poRetDat.mlDateFmt & vbLf
             str = str & "EdmGetVarDataFlags: " & poRetDat.mlEdmGetVarDataFlags

             MsgBox(str)

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
         Me.SelectFile = New System.Windows.Forms.Button()
         Me.File1List = New System.Windows.Forms.ListBox()
         Me.GetVarData = New System.Windows.Forms.Button()
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
         'SelectFile
         '
         Me.SelectFile.Location = New System.Drawing.Point(39, 85)
         Me.SelectFile.Name = "SelectFile"
         Me.SelectFile.Size = New System.Drawing.Size(157, 23)
         Me.SelectFile.TabIndex = 2
         Me.SelectFile.Text = "Select file..."
         Me.SelectFile.UseVisualStyleBackColor = True
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
         'GetVarData
         '
         Me.GetVarData.Location = New System.Drawing.Point(40, 176)
         Me.GetVarData.Name = "GetVarData"
         Me.GetVarData.Size = New System.Drawing.Size(107, 23)
         Me.GetVarData.TabIndex = 6
         Me.GetVarData.Text = "Get variable data"
         Me.GetVarData.UseVisualStyleBackColor = True
         '
         'OpenFileDialog1
         '
         Me.OpenFileDialog1.FileName = "OpenFileDialog1"
         Me.OpenFileDialog1.Title = "Select File"
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(284, 227)
         Me.Controls.Add(Me.GetVarData)
         Me.Controls.Add(Me.File1List)
         Me.Controls.Add(Me.SelectFile)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "File variable data"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents SelectFile As System.Windows.Forms.Button
     Friend WithEvents File1List As System.Windows.Forms.ListBox
     Friend WithEvents GetVarData As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog

 End Class
```

[Back to top](#top)
