---
title: "Add Custom File Reference Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Add_Custom_File_Reference_Example_VBNET.htm"
---

# Add Custom File Reference Example (VB.NET)

This example shows how to add a custom file reference to a file in the vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 '    a. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms Application.
 '    b. Type CustRef in Project name.
 '    c. For Location, click ... and navigate to the folder where to create the project.
'      d. Click Next.
'    e. Select Framework.
'    f. Click Create.
'    g. Click Show All Files in the Solution Explorer toolbar and expand
'        Form1.vb in the Solution Explorer.
 '    h. Replace the code in Form1.vb with this code.
 '    i. Replace the code in Form1.Designer.vb with this code.
 ' 2. Add dependencies and safely pass arrays of structures.
 ' 3. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. The Add custom references dialog displays.
 ' 2. Select a vault.
 ' 3. Click Browse for file to which to add custom reference,
  '    locate and click a file in the vault, and click Open.
 '    The file is checked out.
 ' 4. In a view of the selected vault, right-click a file and click Copy.
 ' 5. In the Add custom references dialog, click Add custom file reference.
  '    The file that was copied to the clipboard is added as a custom
 '    reference to the checked-out file.
 ' 6. In the Create File References dialog, click OK.
 '    The file is checked in.
  ' 7. In the Edit User-Defined File References dialog, click OK.
  ' 8. Close the Add custom references dialog.
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
             CustRefListBox.Items.Clear()

             'Only create a new vault object
             'if one hasn't been created yet
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             If Not vault1.IsLoggedIn Then
                 'Log into selected vault as the current user
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             'Set the initial directory in the File Open dialog
             CustRefOpenFileDialog.InitialDirectory = vault1.RootFolderPath
             'Show the File Open dialog
             Dim DialogResult As System.Windows.Forms.DialogResult = Nothing
             DialogResult = CustRefOpenFileDialog.ShowDialog()
             'If the user didn't click Open, exit the sub
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
             'Only create a new vault object
             'if one hasn't been created yet
             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 'Log into selected vault as the current user
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim addCustRefs As IEdmAddCustomRefs = DirectCast(vault2.CreateUtility(EdmUtility.EdmUtil_AddCustomRefs), IEdmAddCustomRefs)
             Dim ppoFileIdArray As Int32() = New Int32(CustRefListBox.Items.Count - 1) {}
             Dim file As IEdmFile5 = Nothing
             Dim parentFolder As IEdmFolder5 = Nothing
             Dim i As Integer = 0
             For Each FileName As String In CustRefListBox.Items
                 file = vault2.GetFileFromPath(FileName, parentFolder)
                 If Not file.IsLocked Then
                     file.LockFile(parentFolder.ID, Me.Handle.ToInt32(), CInt(EdmLockFlag.EdmLock_Simple))
                 End If
                 ppoFileIdArray(i) = file.ID
                 i += 1
             Next
             Dim retCode As [Boolean] = False

             'Add the file that is copied to the clipboard as a custom reference to the selected file
             For Each ID As Integer In ppoFileIdArray
                 addCustRefs.AddReferencesClipboard(ID)
                 addCustRefs.CreateTree(CInt(EdmCreateReferenceFlags.Ecrf_Nothing))
                 addCustRefs.ShowDlg(Me.Handle.ToInt32())
                 retCode = addCustRefs.CreateReferences()
             Next

             ' Check in the file
             file.UnlockFile(Me.Handle.ToInt32(), "Custom reference added")

             'Display current custom file references

             retCode = addCustRefs.ShowEditReferencesDlg(ppoFileIdArray, Me.Handle.ToInt32())
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
         Me.VaultsLabel.Size = New System.Drawing.Size(244, 13)
         Me.VaultsLabel.TabIndex = 0
         Me.VaultsLabel.Text = "Copy a file to the clipboard, then select vault view:"
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(16, 59)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(121, 21)
         Me.VaultsComboBox.TabIndex = 1
         '
         'BrowseButton
         '
         Me.BrowseButton.Location = New System.Drawing.Point(16, 98)
         Me.BrowseButton.Name = "BrowseButton"
         Me.BrowseButton.Size = New System.Drawing.Size(271, 23)
         Me.BrowseButton.TabIndex = 3
         Me.BrowseButton.Text = "Browse for file to which to add a custom reference..."
         Me.BrowseButton.UseVisualStyleBackColor = True
         '
         'CustRefListBox
         '
         Me.CustRefListBox.FormattingEnabled = True
         Me.CustRefListBox.Location = New System.Drawing.Point(16, 150)
         Me.CustRefListBox.Name = "CustRefListBox"
         Me.CustRefListBox.Size = New System.Drawing.Size(259, 95)
         Me.CustRefListBox.TabIndex = 4
         '
         'AddCustomFileReference
         '
         Me.AddCustomFileReference.Location = New System.Drawing.Point(16, 273)
         Me.AddCustomFileReference.Name = "AddCustomFileReference"
         Me.AddCustomFileReference.Size = New System.Drawing.Size(259, 23)
         Me.AddCustomFileReference.TabIndex = 5
         Me.AddCustomFileReference.Text = "Add custom file reference"
         Me.AddCustomFileReference.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(317, 308)
         Me.Controls.Add(Me.AddCustomFileReference)
         Me.Controls.Add(Me.CustRefListBox)
         Me.Controls.Add(Me.BrowseButton)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Add custom file references"
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
