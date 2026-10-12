---
title: "Create Custom Card View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Create_Custom_Card_View_Example_VBNET.htm"
---

# Create Custom Card View Example (VB.NET)

This example shows how to create a custom file card view.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
   '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio 2010.
 '    a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '    b. Type CustomCardView_VBNET in Name.
 '    c. Click Browse and navigate to the folder where to create the project.
 '    d. Click OK.
 '    e. Click Show All Files in the Solution Explorer toolbar and expand
 '       Form1.vb in the Solution Explorer.
 '    f. Replace the code in Form1.vb with this code.
 '    g. To create the form, replace the code in Form1.Designer.vb with
 '       this code.
 ' 2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 '    name in the Solution Explorer, click Add Reference, click
 '    Assemblies > Framework in the left-side panel, browse to the top folder of
 '    your SOLIDWORKS PDM Professional installation, locate and click
 '    EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
 ' 3. Right-click EPDM.Interop.epdm in References, click Properties, and set
 '    Embed Interop Types to False to handle methods that pass arrays of
 '    structures.
 ' 4. Check out a file that has a data card with a Comment tab and a
 '    Comment variable.
 ' 5. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Custom Card View dialog box.
 ' 2. Select a vault view.
 ' 3. Click Select file.
 '    a. In the Select File dialog:
 '       1. Click the text file checked out in Preconditions step 4.
 '       2. Click Open.
 '    b. In the file data card, click the Comment tab.
 '    c. Type something in Comments.
 ' 4. Click Save data card.
 ' 5. Click OK in the message box.
 ' 6. Close the Custom Card View dialog box.
 ' 7. Check in the file and inspect the comment in the file data card.
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
     Implements IEdmCardViewCallback6

     Private vault1 As IEdmVault5
     Dim view As IEdmCardView63
     Dim aFile As IEdmFile7
     Dim aFolder As IEdmFolder5

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
                     ShowCard(aFolder, aFile.ID)
                 Next
             End If

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub SaveCard_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles SaveCard.Click
         Try

             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If

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

     'Display the card of the selected file
     Private Sub ShowCard(ByVal folder As IEdmFolder5, ByVal fileID As Integer)
         Try
```

```vb
         If vault1 Is Nothing Then
             vault1 = New EdmVault5()
         End If

         If Not vault1.IsLoggedIn Then
             vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
         End If
         Dim vault As IEdmVault10 = vault1

         Dim params As EdmCardViewParams
         params.mlFileID = fileID
         params.mlFolderID = folder.ID
         params.mlCardID = 0
         params.mlX = 40
         params.mlY = 300
         params.mhParentWindow = Me.Handle.ToInt32()
         params.mlEdmCardViewFlags = EdmCardViewFlag.EdmCvf_Normal

         'Create the card view interface
         view = vault.CreateCardViewEx2(params, Me)

         If view Is Nothing Then
             MsgBox("The file does not have a card.")
             Exit Sub
         End If

         'Set input focus to the first control in the card
         view.SetFocus(0)

         'Enable all controls in the card
         view.Update(EdmCardViewUpdateType.EdmCvut_EnableCtrl)

         'Get the size needed to display the card
         Dim width As Integer
         Dim height As Integer
         view.GetCardSize(width, height)

         'Resize the form window to make room for the card
         Me.Width = (width + 100)
         Me.Height = (height + 400)
         view.ShowWindow(True)

         SaveCard.Enabled = False
```

```vb
         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub EdmCardViewCallback6_SetModifiedFlag() Implements IEdmCardViewCallback6.SetModifiedFlag
         SaveCard.Enabled = True
     End Sub

     Private Sub EdmCardViewCallback6_OnAddInInput(ByVal lFlags As Integer) Implements IEdmCardViewCallback6.OnAddInInput
     End Sub

     Private Sub EdmCardViewCallback6_SetCtrlData(ByVal lCardWnd As Integer, ByVal lCardID As Integer, ByVal lControlID As Integer, ByVal lVariableID As Integer, ByVal bsVariableName As String, ByVal poView As IEdmCardView5, ByRef poValue As Object) Implements IEdmCardViewCallback6.SetCtrlData
         Try
             If bsVariableName = "Comment" Then
                 MsgBox(lCardWnd & " " & lCardID & " " & lControlID & " " & lVariableID & " " & bsVariableName & " " & poValue.ToString)

                 Dim enumvar As IEdmEnumeratorVariable8
                 enumvar = aFile.GetEnumeratorVariable()

                 enumvar.SetVar(bsVariableName, "", poValue, True)
                 enumvar.CloseFile(True)
             End If
         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Function EdmCardViewCallback6_GetCtrlData(ByVal lCardWnd As Integer, ByVal lCardID As Integer, ByVal lControlID As Integer, ByVal lVariableID As Integer, ByVal bsVariableName As String, ByVal poView As IEdmCardView5) As Object Implements IEdmCardViewCallback6.GetCtrlData

        Dim poValue As Object = Nothing
         Try
              Dim enumVar As IEdmEnumeratorVariable5 = aFile.GetEnumeratorVariable()
              enumVar.GetVar(bsVariableName, "", poValue)
           Catch ex As System.Runtime.InteropServices.COMException
               MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
           Catch ex As Exception
               MessageBox.Show(ex.Message)
         End Try
         Return  poValue

     End Function

     Private Function EdmCardViewCallback6_GetDefaultValueComponent(ByVal eValue As EdmDefValComp) As Object Implements IEdmCardViewCallback6.GetDefaultValueComponent
         Return Nothing
     End Function

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
         Me.SaveCard.Location = New System.Drawing.Point(40, 176)
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
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(284, 227)
         Me.Controls.Add(Me.SaveCard)
         Me.Controls.Add(Me.File1List)
         Me.Controls.Add(Me.SelectFile)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Custom Card View"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents SelectFile As System.Windows.Forms.Button
     Friend WithEvents File1List As System.Windows.Forms.ListBox
     Friend WithEvents SaveCard As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog

 End Class
```

[Back to top](#top)
