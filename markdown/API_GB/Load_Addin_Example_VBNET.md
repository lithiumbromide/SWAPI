---
title: "Install Add-in Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Load_Addin_Example_VBNET.htm"
---

# Install Add-in Example (VB.NET)

This example shows how to install an add-in, obtain information about it, and uninstall it.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 '  1. Start Microsoft Visual Studio 2010.
 '     a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '     b. Type AddinMgr in Name.
 '     c. Click Browse and navigate to the folder where to create the project.
 '     d. Click OK.
 '     e. Click Show All Files in the Solution Explorer toolbar and expand
 '        Form1.vb in the Solution Explorer.
  '     f. Create a form similar to the form shown above and change:
 '        1. Top label to VaultsLabel.
 '        2. Combo box to VaultsComboBox.
 '        3. Browse for add-in button to BrowseButton.
 '        4. List box to AddinListBox.
 '        5. Install add-in button to LoadAddin.
 '     g. Replace the code in Form1.vb with this code.
 '     h. Replace the code in Form1.Designer.vb with this code.
 '  2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 '     name in the Solution Explorer, click Add Reference, click
 '     Assemblies > Framework in the left-side panel, browse to the top folder of
 '     your SOLIDWORKS PDM Professional installation, locate and click
 '     EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
 '  3. Right-click EPDM.Interop.epdm in References, click Properties, and set
 '     Embed Interop Types to False to handle methods that pass arrays of
 '     structures.
 '  4. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 '  1. The Install add-in dialog box displays.
 '     a. Select a vault view.
 '     b. Click Browse for add-in.
 '     c. In the Browse for add-ins dialog:
 '        1. Navigate to your add-in directory and click addin_name.dll
 '           and EPDM.Interop.epdm.dll.
 '        2. Click Open.
 '     d. Click Install add-in.
 '        A message box containing information about each add-in installed in
 '        the selected vault displays.
 '     e. Click OK to close each message box.
 '     f. Click Remove add-in.
 '  2. Close the Install add-in dialog box.
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
     Dim addinName As String  = ""

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
             AddinListBox.Items.Clear()

             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             'Set the initial directory in the Browse for add-ins dialog
             AddinOpenFileDialog.InitialDirectory = vault1.RootFolderPath

             'Show the Browse for add-ins dialog
             Dim DialogResult As System.Windows.Forms.DialogResult = Nothing
             DialogResult = AddinOpenFileDialog.ShowDialog()

             'If the user did not click Open, exit this subroutine
             If Not (DialogResult = System.Windows.Forms.DialogResult.OK) Then
                 Return
             End If

             For Each FileName As String In AddinOpenFileDialog.FileNames
                 AddinListBox.Items.Add(FileName)
             Next

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub LoadAddin_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles LoadAddin.Click
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim AddinMgr As IEdmAddInMgr8
             AddinMgr = vault1

             Dim ppoFiles() As EdmAddInFileInfo = Nothing
             Dim fileList As String
             fileList = ""
             Dim fileidx As Integer = 1

             ' Save the path and name of the add-in just installed
             Dim justInstalledPathName As String = ""

             For Each FileName As String In AddinListBox.Items
                 If Not (FileName.Contains("Interop")) Then
                     justInstalledPathName = FileName
                 End If

                 If fileidx = 1 Then
                     fileList = FileName

                 Else
                     fileList = fileList & vbLf & FileName
                 End If
                 fileidx = fileidx + 1
             Next

             AddinMgr.AddAddIns(fileList, EdmAddAddInFlags.EdmAddin_AddAllFilesToOneAddIn, Nothing)

             ' Get information about each of the installed add-ins
             Dim addIns() As EdmAddInInfo2 = Nothing
             AddinMgr.GetInstalledAddIns(addIns)

             Dim addinPath As String = ""
             Dim s As String = ""
             Dim idx As Integer
             idx = LBound(addIns)

             While idx <= UBound(addIns)

                 s = "Add-in: " + addIns(idx).mbsAddInName + vbLf + "Class: " + addIns(idx).mbsClassID + vbLf
                 s = s + "Company: " + addIns(idx).mbsCompany + vbLf + "Description: " + addIns(idx).mbsDescription + vbLf
                 s = s + "Path: " + addIns(idx).mbsModulePath + vbLf + "Version: " + CStr(addIns(idx).mlAddInVersion) + vbLf
                 s = s + "Req ver: " + CStr(addIns(idx).mlRequiredVersionMajor) + "." + CStr(addIns(idx).mlRequiredVersionMinor)

                 MsgBox(s)
                 addinName = addIns(idx).mbsAddInName ' Save the name of the add-in just installed
                 idx = idx + 1
             End While

             ' Get information about each add-in installed for debugging
             Dim debugAddIns() As EdmAddInInfo2 = Nothing
             AddinMgr.GetDebugAddIns(debugAddIns)

             idx = LBound(debugAddIns)
             While idx <= UBound(debugAddIns)

                 s = "Debug add-in: " + debugAddIns(idx).mbsAddInName + vbLf + "Class: " + debugAddIns(idx).mbsClassID + vbLf
                 s = s + "Company: " + debugAddIns(idx).mbsCompany + vbLf + "Description: " + debugAddIns(idx).mbsDescription + vbLf
                 s = s + "Path: " + debugAddIns(idx).mbsModulePath + vbLf + "Version: " + CStr(debugAddIns(idx).mlAddInVersion) + vbLf
                 s = s + "Req ver: " + CStr(debugAddIns(idx).mlRequiredVersionMajor) + "." + CStr(debugAddIns(idx).mlRequiredVersionMinor)

                 MsgBox(s)
                 idx = idx + 1
             End While

             ' Get information about the add-in just installed
             Dim poInfo As EdmAddInInfo2 = Nothing
             AddinMgr.GetAddInInfo2(justInstalledPathName, Nothing, poInfo)

             s = "Getting info for add-in: " + poInfo.mbsAddInName + vbLf + "Class: " + poInfo.mbsClassID + vbLf
             s = s + "Company: " + poInfo.mbsCompany + vbLf + "Description: " + poInfo.mbsDescription + vbLf
             s = s + "Path: " + poInfo.mbsModulePath + vbLf + "Version: " + CStr(poInfo.mlAddInVersion) + vbLf
             s = s + "Req ver: " + CStr(poInfo.mlRequiredVersionMajor) + "." + CStr(poInfo.mlRequiredVersionMinor)

             MsgBox(s)

             ' Extract information about the add-in just installed
             Dim ppoCmds() As EdmAddInMenuInfo = Nothing
             AddinMgr.GetInstalledAddIn(addinName, "c:\temp", poInfo, ppoFiles, ppoCmds)

             Dim msg As String
             msg = "Extracting info for add-in: " + poInfo.mbsAddInName + vbLf
             msg = msg + "CLSID=" + poInfo.mbsClassID + vbLf
             msg = msg + "Company=" + poInfo.mbsCompany + vbLf
             msg = msg + "Module=" + poInfo.mbsModulePath + vbLf
             msg = msg + "Version=" + CStr(poInfo.mlAddInVersion) + vbLf
             msg = msg + "Requires version=" + CStr(poInfo.mlRequiredVersionMajor) + "." + CStr(poInfo.mlRequiredVersionMinor)
             msg = msg + vbLf + "Files:" + vbLf

             idx = LBound(ppoFiles)
             While idx <= UBound(ppoFiles)
                 msg = msg + ppoFiles(idx).mbsFileName + " Flags=" + CStr(ppoFiles(idx).mlEdmAddInFileInfoFlags) + vbLf
                 idx = idx + 1
             End While

             msg = msg + vbLf + "Commands:" + vbLf

             idx = LBound(ppoCmds)
             While idx <= UBound(ppoCmds)
                 msg = msg + "'" + ppoCmds(idx).mbsMenuStr + "' Flags=" + CStr(ppoCmds(idx).mlEdmMenuFlags) + vbLf
                 idx = idx + 1
             End While

             vault1.MsgBox(Me.Handle.ToInt32, msg)

             ' Get CAF information about the add-in just installed
             AddinMgr.GetCAFInfo(poInfo.mbsModulePath, "c:\temp", poInfo, ppoFiles, ppoCmds)
             msg = "Getting CAF info for add-in: " + poInfo.mbsAddInName + vbLf
             msg = msg + "CLSID=" + poInfo.mbsClassID + vbLf
             msg = msg + "Company=" + poInfo.mbsCompany + vbLf
             msg = msg + "Module=" + poInfo.mbsModulePath + vbLf
             msg = msg + "Version=" + CStr(poInfo.mlAddInVersion) + vbLf
             msg = msg + "Requires version=" + CStr(poInfo.mlRequiredVersionMajor) + "." + CStr(poInfo.mlRequiredVersionMinor)
             msg = msg + vbLf + "Files:" + vbLf

             idx = LBound(ppoFiles)
             While idx <= UBound(ppoFiles)
                 msg = msg + ppoFiles(idx).mbsFileName + " Flags=" + CStr(ppoFiles(idx).mlEdmAddInFileInfoFlags) + vbLf
                 idx = idx + 1
             End While

             msg = msg + vbLf + "Commands:" + vbLf

             idx = LBound(ppoCmds)
             While idx <= UBound(ppoCmds)
                 msg = msg + "'" + ppoCmds(idx).mbsMenuStr + "' flags=" + CStr(ppoCmds(idx).mlEdmMenuFlags) + vbLf
                 idx = idx + 1
             End While

             vault1.MsgBox(Me.Handle.ToInt32, msg)

             Me.Button1.Enabled = True

             Exit Sub

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try

     End Sub

     Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
         Try

             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim AddinMgr As IEdmAddInMgr9
             AddinMgr = vault1

             AddinMgr.RemoveAddIn(addinName)
             Me.Button1.Enabled = False

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
         Me.BrowseButton = New System.Windows.Forms.Button()
         Me.AddinListBox = New System.Windows.Forms.ListBox()
         Me.LoadAddin = New System.Windows.Forms.Button()
         Me.AddinOpenFileDialog = New System.Windows.Forms.OpenFileDialog()
         Me.Button1 = New System.Windows.Forms.Button()
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
         Me.BrowseButton.Text = "Browse for add-in..."
         Me.BrowseButton.UseVisualStyleBackColor = True
         '
         'AddinListBox
         '
         Me.AddinListBox.FormattingEnabled = True
         Me.AddinListBox.HorizontalScrollbar = True
         Me.AddinListBox.Location = New System.Drawing.Point(16, 151)
         Me.AddinListBox.Name = "AddinListBox"
         Me.AddinListBox.SelectionMode = System.Windows.Forms.SelectionMode.MultiSimple
         Me.AddinListBox.Size = New System.Drawing.Size(259, 56)
         Me.AddinListBox.TabIndex = 4
         '
         'Load add-in
         '
         Me.LoadAddin.Location = New System.Drawing.Point(16, 230)
         Me.LoadAddin.Name = "LoadAddin"
         Me.LoadAddin.Size = New System.Drawing.Size(259, 23)
         Me.LoadAddin.TabIndex = 5
         Me.LoadAddin.Text = "Install add-in"
         Me.LoadAddin.UseVisualStyleBackColor = True
         '
         'AddinOpenFileDialog
         '
         Me.AddinOpenFileDialog.Multiselect = True
         Me.AddinOpenFileDialog.Title = "Browse for add-ins"
         '
         'Remove add-in
         '
         Me.Button1.Location = New System.Drawing.Point(16, 273)
         Me.Button1.Name = "Button1"
         Me.Button1.Size = New System.Drawing.Size(259, 23)
         Me.Button1.TabIndex = 6
         Me.Button1.Text = "Remove add-in"
         Me.Button1.UseVisualStyleBackColor = True
         Me.Button1.Enabled = False
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(317, 314)
         Me.Controls.Add(Me.Button1)
         Me.Controls.Add(Me.LoadAddin)
         Me.Controls.Add(Me.AddinListBox)
         Me.Controls.Add(Me.BrowseButton)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Install add-in"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents BrowseButton As System.Windows.Forms.Button
     Friend WithEvents AddinListBox As System.Windows.Forms.ListBox
     Friend WithEvents LoadAddin As System.Windows.Forms.Button
     Friend WithEvents AddinOpenFileDialog As System.Windows.Forms.OpenFileDialog
     Friend WithEvents Button1 As System.Windows.Forms.Button
 End Class
```

[Back to top](#top)
