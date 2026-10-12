---
title: "Get Card Control Information Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Get_Card_Control_Info_Example_VBNET.htm"
---

# Get Card Control Information Example (VB.NET)

This example shows how to get information about the list and edit box controls in a selected file's data card.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 '  1. Start Microsoft Visual Studio 2010.
 '  2. Click File > New > Project > Visual Basic > Windows Forms Application.
 '  3. Type CardControlInfo in Name.
 '  4. Click Browse to navigate to the folder where to create the project.
 '  5. Click OK.
 '  6. Click Show All Files in the Solution Explorer toolbar and expand
 '     Form1.vb in the Solution Explorer.
 '  7. Replace the code in Form1.vb with this code.
 '  8. To create the form, replace the code in Form1.Designer.vb with this code.
 '  9. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 '     name in the Solution Explorer, click Add Reference, click
 '     Framework in the left-side panel, browse to the top folder of your
 '     SOLIDWORKS PDM Professional installation, locate and click
 '     EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
 ' 10. Right-click EPDM.Interop.epdm in References, select Properties, and set
 '     Embed Interop Types to False to handle methods that pass arrays of
 '     structures.
 ' 11. Ensure that there is a file in the vault whose extension has a
 '     file data card in the vault, and the file data card has a droplist
 '     control.
 ' 12. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 '  1. Displays a dialog.
 '  2. Select a vault.
 '  3. Click Select file.
 '  4. In the Select File dialog:
 '     a. Click a file whose extension has a file data card in the vault.
 '     b. Click Open.
 '  5. Click Get card information.
 '  6. A message box displays information about the selected file's data card.
 '  7. Click OK in the message box.
 '  8. A message box displays the list items of any drop list controls.
 '  9. Click OK in the message box.
 ' 10. A message box displays information about each edit box control in the
 '     data card.
 ' 11. Click OK in the message box.
 ' 12. Close the dialog.
 '----------------------------------------------------------------------------
```

```
'Form1.vb
```

```vb
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
     Dim aFile As IEdmFile5
     Dim aFolder As IEdmFolder5
     Dim aCard As IEdmCard6
     Dim aControl As IEdmCardControl7
     Dim aPos As IEdmPos5
     Dim plWidth As Integer
     Dim plHeight As Integer
     Dim plX As Integer
     Dim plY As Integer
     Dim plParentCtrlID As Integer
     Dim plPageNo As Integer
     Dim poMin As Object = Nothing
     Dim poMax As Object = Nothing
     Dim varType As EdmVariableType
     Dim contType As EdmCardControlType
     Dim fileExt As String
     Dim cardID As Integer
     Dim str As String
     Dim k As Integer

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

     Public Sub SelectFiles_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles SelectFiles.Click
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
                     aFile = vault1.GetFileFromPath(FileName)
                     k = FileName.LastIndexOf(".")
                     fileExt = FileName.Substring(k + 1, (FileName.Length) - k - 1)
                     aPos = aFile.GetFirstFolderPosition()
                     aFolder = aFile.GetNextFolder(aPos)
                 Next
             End If

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub GetCardControls_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GetCardControls.Click
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault9)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             If Not IsNothing(aFile) Then

                 ' Get the selected file's data card
                 aCard = aFolder.GetCard(fileExt)
                 cardID = aFolder.GetCardID(fileExt)

                 aCard.GetSize(plWidth, plHeight)
                 str = "Card ID: " & cardID & ", EdmCardType: " & aCard.CardType & ", Width: " & plWidth & ", Height: " & plHeight
                 MessageBox.Show(str)

                 aPos = aCard.GetFirstControlPosition()
                 While Not (aPos.IsNull)
                     aControl = aCard.GetNextControl(aPos)
                     contType = aControl.ControlType

                     Dim ret As Boolean
                     Dim variableItemsList As String() = Nothing
                     If ((contType = 7) Or (contType = 8) Or (contType = 9) Or (contType = 10)) Then
                         str = "List values associated with drop-down card control: " & aControl.VariableID.ToString

                         ret = aControl.GetControlVariableList(aFile.ID, variableItemsList)

                         For Each listValue As String In variableItemsList
                             str = str & vbLf & listValue
                         Next
                         MessageBox.Show(str)
                     End If

                     ' Get the edit box controls in the card
                     If (contType = 4) Then
                         str = ""
                         aControl.GetParentInfo(plParentCtrlID, plPageNo)
                         aControl.GetPosition(plX, plY, plWidth, plHeight)
                         varType = aControl.GetValidation(poMin, poMax)

                         str = "Card control: " & aControl.Name
                         str = str & vbLf & "Variable ID: " & aControl.VariableID & vbLf & "EdmCardControlType: " & contType & vbLf & "Is multi-line? " & aControl.IsMultiLine & vbLf & "Is read-only? " & aControl.IsReadOnly & vbLf & "Show in preview? " & aControl.ShowInPreview
                         str = str & vbLf & "Location on card: [" & plX & ", " & plY & "], Width: " & plWidth & ", Height: " & plHeight
                         str = str & vbLf & "Parent control ID (0, if none): " & plParentCtrlID
                         str = str & vbLf & "Tab index: " & plPageNo
                         str = str & vbLf & "EdmVariableType: " & varType
                         str = str & vbLf & "Updates all configurations? " & aControl.UpdatesAllConfigurations.ToString

                         MessageBox.Show(str)
                     End If
                 End While
             End If
         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try

     End Sub

 End Class
```

```
Back to top
```

```
'Form1.Designer.vb
```

```vb
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
         Me.SelectFiles = New System.Windows.Forms.Button()
         Me.File1List = New System.Windows.Forms.ListBox()
         Me.GetCardControls = New System.Windows.Forms.Button()
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
         'SelectFiles
         '
         Me.SelectFiles.Location = New System.Drawing.Point(39, 85)
         Me.SelectFiles.Name = "SelectFiles"
         Me.SelectFiles.Size = New System.Drawing.Size(191, 23)
         Me.SelectFiles.TabIndex = 2
         Me.SelectFiles.Text = "Select file..."
         Me.SelectFiles.UseVisualStyleBackColor = True
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
         'GetCardControls
         '
         Me.GetCardControls.Location = New System.Drawing.Point(40, 183)
         Me.GetCardControls.Name = "GetCardControls"
         Me.GetCardControls.Size = New System.Drawing.Size(157, 23)
         Me.GetCardControls.TabIndex = 6
         Me.GetCardControls.Text = "Get card  information"
         Me.GetCardControls.UseVisualStyleBackColor = True
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
         Me.ClientSize = New System.Drawing.Size(284, 235)
         Me.Controls.Add(Me.GetCardControls)
         Me.Controls.Add(Me.File1List)
         Me.Controls.Add(Me.SelectFiles)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Card controls"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents SelectFiles As System.Windows.Forms.Button
     Friend WithEvents File1List As System.Windows.Forms.ListBox
     Friend WithEvents GetCardControls As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog

 End Class
```

```
Back to top
```
