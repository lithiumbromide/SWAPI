---
title: "Add Folder Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Add_Folder_Example_VBNET.htm"
---

# Add Folder Example (VB.NET)

This example shows how to create a folder and set its data card and permissions.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 '    a. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms Application.
 '    b. Type AddFolder in Project name.
 '    c. For Location, click ... and navigate to the folder where to create the project.
'      d. Click Next.
'    e. Select Framework.
'    f. Click Create.
'    g. Click Show All Files in the Solution Explorer toolbar and expand
'       Form1.vb in the Solution Explorer.
 '    h. Replace the code in Form1.vb with this code.
 '    i. To create the form, replace the code in Form1.Designer.vb with this code.
 ' 2. Add dependencies and safely pass arrays of structures.
 ' 3. Ensure that the vault has user, Engineer1, and group,
 '    Administrators.
 ' 4. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Add folder dialog box.
 '    a. Select a vault view.
 '    b. Click Browse for parent folder.
  '       1. Locate and click a folder in the vault.
 '       2. Click OK.
 '    c. Click Add folder.
 '       1.  Creates an IEdmFolderData5 object with:
 '           * Folder user permissions for user, Engineer1.
 '           * Folder group permissions for group, Administrators.
 '           * File data card for .doc files.
   '       2. Displays a message that folder, Temp, is added as a subfolder to
 '          the folder clicked in Postconditions 1b1.
 '       3. Click OK.
  ' 2. Close the Add folder dialog box.
 ' 3. Open File Explorer on a vault view and observe the new sub-folder,
 '    Temp.
 ' 4. Open the Administration tool.
 '    a. Log in to the vault selected in step 1a.
 '    b. Expand Groups and double-click Administrators.
 '    c. Click Folder Permissions.
 '    d. Inspect the folder permissions for Temp and click OK.
 '    e. Expand Users and double-click Engineer1.
 '    f. Repeat steps 4c and 4d.
 ' 5. Exit the Administration tool.
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

     Public Sub AddFolder_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles AddFolder.Click
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

             Dim folderName = "Temp"
             Dim usrMgr As IEdmUserMgr5
             usrMgr = parentFolder.vault

             Dim data As EdmFolderData
             data = New EdmFolderData

             data.SetUserRights(usrMgr.GetUser("Engineer1").ID, EdmRightFlags.EdmRight_Read Or EdmRightFlags.EdmRight_Lock)
             data.SetGroupRights(usrMgr.GetUserGroup("Administrators").ID, EdmRightFlags.EdmRight_All)

             Dim card As IEdmCard5
             card = parentFolder.Vault.RootFolder.GetCard("doc")
             data.SetCardSource(card.ID, "doc;xls")

             Dim folder As IEdmFolder5
             folder = parentFolder.AddFolder(Me.Handle.ToInt32(), folderName, data)
             MsgBox("Created " + folderName + " successfully with ID, " + Str(folder.ID) + ", in " + parentFolder.Name)

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
         Me.AddFolder = New System.Windows.Forms.Button()
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
         'AddFolder
         '
         Me.AddFolder.Location = New System.Drawing.Point(84, 178)
         Me.AddFolder.Name = "AddFolder"
         Me.AddFolder.Size = New System.Drawing.Size(98, 23)
         Me.AddFolder.TabIndex = 5
         Me.AddFolder.Text = "Add folder"
         Me.AddFolder.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(317, 215)
         Me.Controls.Add(Me.AddFolder)
         Me.Controls.Add(Me.ListBox)
         Me.Controls.Add(Me.BrowseButton)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Add folder"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents BrowseButton As System.Windows.Forms.Button
     Friend WithEvents ListBox As System.Windows.Forms.ListBox
     Friend WithEvents AddFolder As System.Windows.Forms.Button
     Friend WithEvents FolderBrowserDialog1 As System.Windows.Forms.FolderBrowserDialog
 End Class
```

[Back to top](#top)
