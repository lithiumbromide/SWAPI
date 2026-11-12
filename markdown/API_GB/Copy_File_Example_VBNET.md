---
title: "Copy File Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Copy_File_Example_VBNET.htm"
---

# Copy File Example (VB.NET)

This example shows how to copy a file in the vault to a different folder in the vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Start Microsoft Visual Studio 2010.
'    a. Click File > New > Project > Visual Basic > Windows Forms Application.
'    b. Type VaultUtilities in Name.
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
'    EPDM.Interop.epdm.dll, click Open, and click Add).
' 3. Add EPDM.Interop.EPDMResultCode.dll as a reference (click Browse, locate and
'    click EPDM.Interop.EPDMResultCode.dll, click Open, click Add, and click Close).
' 4. Right-click EPDM.Interop.epdm in References, click Properties, and set
'    Embed Interop Types to False to handle methods that pass arrays of
'    structures.
' 5. Run the Administration tool, log in as admin, expand the vault,
'    right-click File Types, click Duplicate file name settings, and
'    click Do not allow duplicate files names in this file vault.
' 6. Ensure that multiple folders exist in the vault.
' 7. Click Debug > Start Debugging or press F5.
'
' Postconditions:
' 1. Displays the Copy file dialog box.
'    a. Select a vault view.
'    b. Click Copy file.
'       1. In the Open dialog, click a vault file.
'       2. Click Open.
'       3. In the Select Folder dialog, click a different folder to which to
'          copy the selected file.
'       4. Click OK.
'       5. Displays a message with the file copy status.
'       6. Click OK.
' 2. Close the Copy file dialog box.
'----------------------------------------------------------------------------
```

```
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
Imports EPDM.Interop.EPDMResultCode

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

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        'Copy file
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

            Dim pathList As EdmStrLst5
            pathList = vault2.BrowseForFile(Me.Handle.ToInt32(), EdmBrowseFlag.EdmBws_ForOpen + EdmBrowseFlag.EdmBws_PermitVaultFiles)
            If pathList Is Nothing Then Exit Sub

            Dim file As IEdmFile5
            Dim srcFolder As IEdmFolder5 = Nothing
            file = vault2.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition), srcFolder)

            Dim destFolder1 As IEdmFolder5 = Nothing
            Dim destFolder As IEdmFolder8 = DirectCast(destFolder1, IEdmFolder5)
            destFolder = vault2.BrowseForFolder(Me.Handle.ToInt32(), "Select destination folder:")
            If destFolder Is Nothing Then Exit Sub
            Dim fileID As Integer
            Dim copyFileStatus As Integer
            fileID = destFolder.CopyFile2(file.ID, srcFolder.ID, Me.Handle.ToInt32(), copyFileStatus, "", EdmCopyFlag.EdmCpy_Simple)
            Select Case copyFileStatus
                Case EdmResultSuccessCodes_e.S_EDM_FILES_NOT_UNIQUE_GLOBALLY
                    MessageBox.Show("WARNING: File is not unique in the vault, but the file was copied to a new file with a file ID of " & fileID & ".")
                Case Else
                    MessageBox.Show("SUCCESS: File copied to a new file with a file ID of " & fileID & ".")
            End Select

        Catch ex As System.Runtime.InteropServices.COMException
            MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
        Catch ex As Exception
            MessageBox.Show(ex.Message)
        End Try
    End Sub

End Class
```

```
Form1.Designer.vb
```

```
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
        Me.Button1 = New System.Windows.Forms.Button()
        Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
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
        'Button1
        '
        Me.Button1.Location = New System.Drawing.Point(16, 84)
        Me.Button1.Name = "Button1"
        Me.Button1.Size = New System.Drawing.Size(62, 23)
        Me.Button1.TabIndex = 6
        Me.Button1.Text = "Copy file"
        Me.Button1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.Button1.UseVisualStyleBackColor = True
        '
        'OpenFileDialog1
        '
        Me.OpenFileDialog1.FileName = "OpenFileDialog1"
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(213, 132)
        Me.Controls.Add(Me.Button1)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Controls.Add(Me.VaultsLabel)
        Me.Name = "Form1"
        Me.Text = "Copy file"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

#End Region

    Friend WithEvents VaultsLabel As System.Windows.Forms.Label
    Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents Button1 As System.Windows.Forms.Button
    Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog
End Class
```
