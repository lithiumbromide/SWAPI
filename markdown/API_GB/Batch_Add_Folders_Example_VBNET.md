---
title: "Batch Add Folders Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Batch_Add_Folders_Example_VBNET.htm"
---

# Batch Add Folders Example (VB.NET)

This example shows how to create several folders in the vault at once.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio 2010.
 '    a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '    b. Type AddFolder in Name.
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
 ' 1. Displays the Add folders dialog box.
 '    a. Select a vault view.
 '    b. Type the name of a new folder to create in the root folder
 '       of the vault.
 '    c. Click Add folder to the batch.
 '       1. Displays a message that the folder is added to the batch.
 '       2. Click OK.
 ' 2. Repeat steps 1b-c repeatedly to add more folders to the batch.
 ' 3. Click Create folders.
 '    a. Displays a message that the folder is created.
 '    b. Click OK in each message box.
 ' 4. Close the Add folders dialog box.
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
     Dim batchAddFolders As IEdmBatchAddFolders
     Dim ppoRetFolders() As EdmFolderInfo = Nothing
     Dim i As Integer

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

     Private Sub AddFolders_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles AddFolders.Click

         Try
             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             If batchAddFolders Is Nothing Then
                 batchAddFolders = vault1.CreateUtility(EdmUtility.EdmUtil_BatchAddFolders)
             End If

             batchAddFolders.AddFolder(vault2.RootFolderID, TextBox1.Text, i, EdmBatchAddFolderFlag.Ebaff_GetInterface, Nothing, 0)
             i = i + 1

             MsgBox(TextBox1.Text & " added to the batch.")
             TextBox1.Clear()

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try

     End Sub

     Public Sub CreateFolders_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles CreateFolders.Click
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             batchAddFolders.Create(Me.Handle.ToInt32, ppoRetFolders, EdmBatchCreateFolderFlag.Ebcf_Nothing)

             For Each FoldName As EdmFolderInfo In ppoRetFolders
                 MsgBox("Created " & FoldName.mbsPath & " successfully" & " in " + vault2.RootFolder.Name)
             Next

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
         Me.AddFolders = New System.Windows.Forms.Button()
         Me.CreateFolders = New System.Windows.Forms.Button()
         Me.TextBox1 = New System.Windows.Forms.TextBox()
         Me.Label1 = New System.Windows.Forms.Label()
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
         'AddFolders
         '
         Me.AddFolders.Location = New System.Drawing.Point(16, 112)
         Me.AddFolders.Name = "AddFolders"
         Me.AddFolders.Size = New System.Drawing.Size(145, 23)
         Me.AddFolders.TabIndex = 3
         Me.AddFolders.Text = "Add folder to the batch..."
         Me.AddFolders.UseVisualStyleBackColor = True
         '
         'CreateFolders
         '
         Me.CreateFolders.Location = New System.Drawing.Point(111, 156)
         Me.CreateFolders.Name = "CreateFolders"
         Me.CreateFolders.Size = New System.Drawing.Size(98, 23)
         Me.CreateFolders.TabIndex = 5
         Me.CreateFolders.Text = "Create folders"
         Me.CreateFolders.UseVisualStyleBackColor = True
         '
         'TextBox1
         '
         Me.TextBox1.Location = New System.Drawing.Point(16, 88)
         Me.TextBox1.Name = "TextBox1"
         Me.TextBox1.Size = New System.Drawing.Size(289, 20)
         Me.TextBox1.TabIndex = 6
         '
         'Label1
         '
         Me.Label1.AutoSize = True
         Me.Label1.Location = New System.Drawing.Point(13, 72)
         Me.Label1.Name = "Label1"
         Me.Label1.Size = New System.Drawing.Size(237, 13)
         Me.Label1.TabIndex = 7
         Me.Label1.Text = "Type name of new folder to add to the vault root:"
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(317, 208)
         Me.Controls.Add(Me.Label1)
         Me.Controls.Add(Me.TextBox1)
         Me.Controls.Add(Me.CreateFolders)
         Me.Controls.Add(Me.AddFolders)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Add folders"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents AddFolders As System.Windows.Forms.Button
     Friend WithEvents CreateFolders As System.Windows.Forms.Button
     Friend WithEvents TextBox1 As System.Windows.Forms.TextBox
     Friend WithEvents Label1 As System.Windows.Forms.Label
 End Class
```

[Back to top](#top)
