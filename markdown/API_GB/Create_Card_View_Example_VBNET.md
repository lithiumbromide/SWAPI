---
title: "Create Card View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Create_Card_View_Example_VBNET.htm"
---

# Create Card View Example (VB.NET)

This example shows how to create a file or folder card view.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio 2015.
 '    a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '    b. Type CreateCardView in Name.
 '    c. Click Browse and navigate to the folder where to create the project.
 '    d. Click OK.
 '    e. Click Show All Files in the Solution Explorer toolbar and expand
 '       Form1.vb in the Solution Explorer.
 '    f. Replace the code in Form1.vb with this code.
 '    g. To create the form, replace the code in Form1.Designer.vb with
 '       this code.
 ' 2. Add references to:
 '    a. EPDM.Interop.epdm.dll (right-click the project
 '       name in the Solution Explorer, click Add > Reference >
 '       Assemblies > Framework > Browse and browse to the top folder of  your
 '       SOLIDWORKS PDM Professional installation, click
 '       EPDM.Interop.epdm.dll > Add).
 '    b.  EPDM.interop.EPDMResultCode.dll (click  Browse >
 '       EPDM.interop.EPDMResultCode.dll > Add > OK).
 ' 3. Right-click EPDM.Interop.epdm in References, click Properties, and set
 '    Embed Interop Types to False to handle methods that pass arrays of
 '    structures.
 ' 4. Create a folder in the vault.
 ' 5. Check out a file from the vault in which you created the folder.
 ' 6. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Create Card View dialog box.
 ' 2. Select the vault in which you created a folder and
 '    checked out a file.
 ' 3. Click either:
 '    a. Select file.
 '    b. In the Select File dialog:
 '       1. Click the file checked out in Preconditions step 5.
 '       2. Click Open.
 '       3. Inspect the message box, then click  OK.
 '    c. In the file data card, modify a field.
 '    d. Click Save data card.
 '    e. Check in the file and inspect its data card.
 '       - or -
 '    a. Select folder.
 '    b. In the Select Folder dialog, select the vault folder created in
 '       Preconditions step 4 and click OK.
 '    c. Inspect the message box, then click OK.
 '    d. In the folder data card, click the Edit Values tab.
 '    e. Modify a field.
 '    f. Click Save data card.
 '    g. Inspect the folder card in the vault.
 ' 4. Close the Create Card View dialog box.
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
     Implements EdmCallback

     Private vault1 As IEdmVault5 = Nothing
     Dim view As IEdmCardView64
     Dim aFile As IEdmFile7
     Dim aFolder As IEdmFolder5

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

     Public Sub SelectFile_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles SelectFile.Click
         Try
             File1List.Items.Clear()

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             SelectFolder.Enabled = False

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
                     aFile = CType(vault1.GetFileFromPath(FileName, aFolder), IEdmFile7)
                     ShowCard(aFolder, aFile.ID)
                 Next
             End If

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub SelectFolder_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles SelectFolder.Click
         Try
             Folder1List.Items.Clear()

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             SelectFile.Enabled = False
             aFolder = vault1.BrowseForFolder(Me.Handle.ToInt32(), "Select folder:")
             If Folder1List Is Nothing Then Exit Sub
             Folder1List.Items.Add(aFolder.Name)
             ShowCard(aFolder, 0)

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub SaveCard_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles SaveCard.Click
         Try
             Folder1List.Items.Clear()

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             view.SaveData()
             SaveCard.Enabled = False

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     'Display the card of the selected file or folder
     Private Sub ShowCard(ByVal folder As IEdmFolder5, ByVal fileID As Integer)

         ' Create the card view interface
         Dim folder10 As IEdmFolder10 = Nothing
         folder10 = DirectCast(folder, IEdmFolder10)
         view = CType(folder10.CreateCardView2(fileID, Me.Handle.ToInt32(), 40, 300, Me, EdmCardViewFlag.EdmCvf_Normal), IEdmCardView64)

         If view Is Nothing Then
             MsgBox("The file does not have a card.")
             Exit Sub
         End If

         view.SetFlagIsFocusOnDataCard(True)

        ' Set input focus to the first control in the card
         view.SetFocus(0)

         ' Enable all controls in the card
         view.Update(EdmCardViewUpdateType.EdmCvut_EnableCtrl)

         ' Get the size needed to display the card
         Dim width As Integer
         Dim height As Integer
         view.GetCardSize(width, height)

         ' Resize the form window to make room for the card
         Me.Width = (width + 100)
         Me.Height = (height + 400)
         view.ShowWindow(True)
         Dim ID As Integer
         Dim folderName As String
         Dim vaultName As String
         Dim vaultObject As IEdmVault5

         ' Get some folder information
         ID = folder10.ID
         folderName = folder10.Name
         vaultObject = folder10.Vault
         vaultName = vaultObject.Name
         MessageBox.Show("Database ID: " + ID.ToString() + "; Vault name: " + vaultName + "; Folder name: " + folderName)

         folder10.Refresh()

         SaveCard.Enabled = False
     End Sub

     Private Sub Cancel_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Cancel.Click
         view.OnCancel()
         SaveCard.Enabled = False
         SelectFile.Enabled = True
         SelectFolder.Enabled = True
         view.ShowWindow(False)
     End Sub

     Private Sub EdmCallback_SetModifiedFlag() Implements EdmCallback.SetModifiedFlag
         SaveCard.Enabled = True
     End Sub

     Private Sub EdmCallback_SetProgressPos(ByVal lPos As Integer) Implements EdmCallback.SetProgressPos
     End Sub

     Private Sub EdmCallback_SetProgressRange(ByVal lMin As Integer, ByVal lMax As Integer) Implements EdmCallback.SetProgressRange
     End Sub

     Private Sub EdmCallback_SetStatusMessage(ByVal bsMessage As String) Implements EdmCallback.SetStatusMessage
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
         Me.SaveCard = New System.Windows.Forms.Button()
         Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
         Me.SelectFolder = New System.Windows.Forms.Button()
         Me.Folder1List = New System.Windows.Forms.ListBox()
         Me.Cancel = New System.Windows.Forms.Button()
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
         'SaveCard
         '
         Me.SaveCard.Location = New System.Drawing.Point(40, 255)
         Me.SaveCard.Name = "SaveCard"
         Me.SaveCard.Size = New System.Drawing.Size(107, 23)
         Me.SaveCard.TabIndex = 6
         Me.SaveCard.Text = "Save data card"
         Me.SaveCard.UseVisualStyleBackColor = True
         '
         'OpenFileDialog1
         '
         Me.OpenFileDialog1.FileName = "OpenFileDialog1"
         Me.OpenFileDialog1.Title = "Select File"
         '
         'SelectFolder
         '
         Me.SelectFolder.Location = New System.Drawing.Point(40, 163)
         Me.SelectFolder.Name = "SelectFolder"
         Me.SelectFolder.Size = New System.Drawing.Size(157, 23)
         Me.SelectFolder.TabIndex = 7
         Me.SelectFolder.Text = "Select folder..."
         Me.SelectFolder.UseVisualStyleBackColor = True
         '
         'Folder1List
         '
         Me.Folder1List.FormattingEnabled = True
         Me.Folder1List.Location = New System.Drawing.Point(39, 192)
         Me.Folder1List.Name = "Folder1List"
         Me.Folder1List.Size = New System.Drawing.Size(220, 43)
         Me.Folder1List.TabIndex = 8
         '
         'Cancel
         '
         Me.Cancel.Location = New System.Drawing.Point(163, 255)
         Me.Cancel.Name = "Cancel"
         Me.Cancel.Size = New System.Drawing.Size(96, 23)
         Me.Cancel.TabIndex = 9
         Me.Cancel.Text = "Cancel"
         Me.Cancel.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(284, 327)
         Me.Controls.Add(Me.Cancel)
         Me.Controls.Add(Me.Folder1List)
         Me.Controls.Add(Me.SelectFolder)
         Me.Controls.Add(Me.SaveCard)
         Me.Controls.Add(Me.File1List)
         Me.Controls.Add(Me.SelectFile)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Create Card View"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents SelectFile As System.Windows.Forms.Button
     Friend WithEvents File1List As System.Windows.Forms.ListBox
     Friend WithEvents SaveCard As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog
     Friend WithEvents SelectFolder As System.Windows.Forms.Button
     Friend WithEvents Folder1List As System.Windows.Forms.ListBox
     Friend WithEvents Cancel As System.Windows.Forms.Button

 End Class
```

[Back to top](#top)
