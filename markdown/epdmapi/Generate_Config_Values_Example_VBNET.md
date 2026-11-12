---
title: "Generate Configuration Values Example (VB.NET"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Generate_Config_Values_Example_VBNET.htm"
---

# Generate Configuration Values Example (VB.NET

## Generate Configuration Values Example (VB.NET)

This example shows how to copy card control variable values from one configuration to another.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 ' 2. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms App.
 ' 3. Type Files in Project name.
 ' 4. For Location, click ... and navigate to the folder where to create the project.
 ' 5. Click Next.
' 6. Select Framework.
' 7. Click Create.
' 8. Click Show All Files in the Solution Explorer toolbar and expand
'     Form1.vb in the Solution Explorer.
 ' 9. Replace the code in Form1.vb with this code.
 '10. To create the form, replace the code in Form1.Designer.vb with this code.
 '11. Add dependencies and safely pass arrays of structures.
 '12. Check out a file that has a data card with two or more configurations.
 '13. Modify a control variable in the @ configuration.
 '14. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Copy Control Values to Configurations dialog box.
 '    a. Select a vault view.
 '       Folder is set to the root folder.
 '    b. Select a file that has a data card with two or more configurations.
 '    c. Displays the data card.
 '    d. Click Copy Control Values.
 '       Copies the value set in Preconditions step 5 to all configurations.
  ' 2. Close the dialog box.
 ' 3. Inspect the control values in all of the configurations of the data card.
  '----------------------------------------------------------------------------

 'Form1.vb

 Imports System
 Imports System.Collections.Generic
 Imports System.ComponentModel
 Imports System.Data
 Imports System.Drawing
 Imports System.Linq
 Imports System.Text
 Imports System.Threading.Tasks
 Imports System.Windows.Forms
 Imports EPDM.Interop.epdm

 Partial Public Class MainForm
 Inherits Form

 Private oFoldersArray As Dictionary(Of Integer,IEdmFolder5) = New Dictionary(Of Integer, IEdmFolder5)()
 Private oFileArray As New Dictionary(Of Integer, IEdmFile5)()
 Private edmCardView As IEdmCardView63

 Public Sub New()
 InitializeComponent()
 End Sub

 Private Sub MainForm_Load(ByVal sender As Object, ByVal e As EventArgs) Handles Me.Load
 Try
  'Declare and create an instance of IEdmVault5
 Dim vault1 As IEdmVault5 = New EdmVault5()

 'Cast IEdmVault5 to IEdmVault8
 Dim vault As IEdmVault8 = DirectCast(vault1, IEdmVault8)

 Dim Views() As EdmViewInfo = Nothing

 'Populate the form with the names of
 'the vaults on the computer
 vault.GetVaultViews(Views, False)
 VaultsComboBox.Items.Clear()
 For Each View As EdmViewInfo In Views
 VaultsComboBox.Items.Add(View.mbsVaultName)
 Next View

 Catch ex As System.Runtime.InteropServices.COMException
 MessageBox.Show("HRESULT = 0x" & ex.ErrorCode.ToString("X") & ex.Message)
 Catch ex As Exception
 MessageBox.Show(ex.Message)
 End Try

 End Sub

 Private Sub VaultsComboBox_SelectedIndexChanged(ByVal sender As Object, ByVal e As EventArgs) Handles VaultsComboBox.SelectedIndexChanged
 Try
  'Declare and create an instance of IEdmVault5
 Dim vault As IEdmVault5 = New EdmVault5()

  'Log into selected vault as the current user
 vault.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())

 Dim folderPos As IEdmPos5 = vault.RootFolder.GetFirstSubFolderPosition()

 FoldersComboBox.Items.Clear()
 oFoldersArray.Clear()

 Dim i As Integer = FoldersComboBox.Items.Add("\")
 oFoldersArray(i) = vault.RootFolder

 Do While Not folderPos.IsNull
 Dim edmFolder As IEdmFolder5 = vault.RootFolder.GetNextSubFolder(folderPos)

 i = FoldersComboBox.Items.Add(edmFolder.Name)
 oFoldersArray(i) = edmFolder
 Loop

 FoldersComboBox.Text = CStr(FoldersComboBox.Items(0))
 Catch e1 As Exception
 FoldersComboBox.Items.Clear()
 oFoldersArray.Clear()
 FoldersComboBox.Text = "Error"
 End Try
 End Sub

 Private Sub FoldersComboBox_SelectedIndexChanged(ByVal sender As Object, ByVal e As EventArgs) Handles FoldersComboBox.SelectedIndexChanged
 Try
 Dim i As Integer = FoldersComboBox.SelectedIndex
 Dim edmFolder As IEdmFolder5 = oFoldersArray(i)

 Dim filePos As IEdmPos5 = edmFolder.GetFirstFilePosition()

 FilesComboBox.Items.Clear()
 oFileArray.Clear()

 Do While Not filePos.IsNull
 Dim edmFile As IEdmFile5 = edmFolder.GetNextFile(filePos)

 i = FilesComboBox.Items.Add(edmFile.Name)
 oFileArray(i) = edmFile
 Loop

 FilesComboBox.Text = CStr(FilesComboBox.Items(0))
 Catch ex As Exception
 FilesComboBox.Items.Clear()
 oFileArray.Clear()
 FilesComboBox.Text = "Error"
 End Try

 End Sub

 Private Sub ShowDataCard()
 If edmCardView IsNot Nothing Then
 edmCardView.ShowWindow(False)
 End If

 Dim i As Integer = FoldersComboBox.SelectedIndex
 Dim edmFolder As IEdmFolder5 = oFoldersArray(i)

 i = FilesComboBox.SelectedIndex
 Dim edmFile As IEdmFile5 = oFileArray(i)

 Dim vault1 As IEdmVault10 = DirectCast(edmFolder.Vault, IEdmVault10)

 Dim params As EdmCardViewParams = Nothing
 params.mlFileID = edmFile.ID
 params.mlFolderID = edmFolder.ID
 params.mlCardID = 0
 params.mlX = 10
 params.mlY = 15
 params.mhParentWindow = CardPanel.Handle.ToInt32()
 params.mlEdmCardViewFlags = CInt(EdmCardViewFlag.EdmCvf_Normal)

 edmCardView = vault1.CreateCardViewEx2(params, Me)
 If edmCardView Is Nothing Then
 MessageBox.Show("The file does not have a card.")
 Return
 End If

 edmCardView.SetFocus(0)

 Dim width_Renamed As Integer = 0
 Dim height_Renamed As Integer = 0
 edmCardView.GetCardSize(width_Renamed, height_Renamed)
 CardPanel.Width = width_Renamed+20
 CardPanel.Height = height_Renamed+20
 edmCardView.ShowWindow(True)
 End Sub

 Private Sub FilesComboBox_SelectedIndexChanged(ByVal sender As Object, ByVal e As EventArgs) Handles FilesComboBox.SelectedIndexChanged
 ShowDataCard()
 End Sub

 Private Sub DoBtn_Click(ByVal sender As Object, ByVal e As EventArgs) Handles DoBtn.Click
 Dim i As Integer = FoldersComboBox.SelectedIndex
 Dim edmFolder As IEdmFolder5 = oFoldersArray(i)

 i = FilesComboBox.SelectedIndex
 Dim edmFile As IEdmFile14 = DirectCast(oFileArray(i), IEdmFile14)

 Dim cfgList As New List(Of String)()
 Dim configLst As EdmStrLst5 = edmFile.GetConfigurations()
 Dim cfgPos As IEdmPos5 = configLst.GetHeadPosition()
 Do While Not cfgPos.IsNull
 Dim configName As String = configLst.GetNext(cfgPos)
 cfgList.Add(configName)
 Loop

 For Each configName As String In cfgList
 ' Move variable values from "@" to configName
 edmFile.GenerateDefaultConfigValues(edmFile.ID, "@", configName, "", False)
 Next configName

 ShowDataCard()
 End Sub
 End Class

 Back to top
 'Form1.Designer.vb

 Partial Public Class MainForm
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
 Me.DoBtn = New System.Windows.Forms.Button()
 Me.CardPanel = New System.Windows.Forms.Panel()
 Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
 Me.FoldersComboBox = New System.Windows.Forms.ComboBox()
 Me.FilesComboBox = New System.Windows.Forms.ComboBox()
 Me.label1 = New System.Windows.Forms.Label()
 Me.label2 = New System.Windows.Forms.Label()
 Me.label3 = New System.Windows.Forms.Label()
 Me.label4 = New System.Windows.Forms.Label()
 Me.SuspendLayout()
 '
 ' DoBtn
 '
 Me.DoBtn.Location = New System.Drawing.Point(223, 108)
 Me.DoBtn.Name = "DoBtn"
 Me.DoBtn.Size = New System.Drawing.Size(271, 23)
 Me.DoBtn.TabIndex = 0
 Me.DoBtn.Text = "Copy Control Values"
 Me.DoBtn.UseVisualStyleBackColor = True

 '
 ' CardPanel
 '
 Me.CardPanel.AutoScroll = True
 Me.CardPanel.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
 Me.CardPanel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
 Me.CardPanel.Location = New System.Drawing.Point(12, 162)
 Me.CardPanel.Name = "CardPanel"
 Me.CardPanel.Size = New System.Drawing.Size(841, 479)
 Me.CardPanel.TabIndex = 1
 '
 ' VaultsComboBox
 '
 Me.VaultsComboBox.FormattingEnabled = True
 Me.VaultsComboBox.Location = New System.Drawing.Point(108, 25)
 Me.VaultsComboBox.Name = "VaultsComboBox"
 Me.VaultsComboBox.Size = New System.Drawing.Size(273, 21)
 Me.VaultsComboBox.TabIndex = 2

 '
 ' FoldersComboBox
 '
 Me.FoldersComboBox.FormattingEnabled = True
 Me.FoldersComboBox.Location = New System.Drawing.Point(108, 52)
 Me.FoldersComboBox.Name = "FoldersComboBox"
 Me.FoldersComboBox.Size = New System.Drawing.Size(434, 21)
 Me.FoldersComboBox.TabIndex = 3

 '
 ' FilesComboBox
 '
 Me.FilesComboBox.FormattingEnabled = True
 Me.FilesComboBox.Location = New System.Drawing.Point(108, 79)
 Me.FilesComboBox.Name = "FilesComboBox"
 Me.FilesComboBox.Size = New System.Drawing.Size(434, 21)
 Me.FilesComboBox.TabIndex = 4

 '
 ' label1
 '
 Me.label1.AutoSize = True
 Me.label1.Location = New System.Drawing.Point(9, 25)
 Me.label1.Name = "label1"
 Me.label1.Size = New System.Drawing.Size(31, 13)
 Me.label1.TabIndex = 5
 Me.label1.Text = "Vault"
 '
 ' label2
 '
 Me.label2.AutoSize = True
 Me.label2.Location = New System.Drawing.Point(9, 52)
 Me.label2.Name = "label2"
 Me.label2.Size = New System.Drawing.Size(36, 13)
 Me.label2.TabIndex = 6
 Me.label2.Text = "Folder"
 '
 ' label3
 '
 Me.label3.AutoSize = True
 Me.label3.Location = New System.Drawing.Point(9, 79)
 Me.label3.Name = "label3"
 Me.label3.Size = New System.Drawing.Size(23, 13)
 Me.label3.TabIndex = 7
 Me.label3.Text = "File"
 '
 ' label4
 '
 Me.label4.AutoSize = True
 Me.label4.Location = New System.Drawing.Point(12, 143)
 Me.label4.Name = "label4"
 Me.label4.Size = New System.Drawing.Size(57, 13)
 Me.label4.TabIndex = 8
 Me.label4.Text = "Data card:"
 '
 ' MainForm
 '
 Me.AutoScaleDimensions = New System.Drawing.SizeF(6F, 13F)
 Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
 Me.ClientSize = New System.Drawing.Size(913, 670)
 Me.Controls.Add(Me.label4)
 Me.Controls.Add(Me.label3)
 Me.Controls.Add(Me.label2)
 Me.Controls.Add(Me.label1)
 Me.Controls.Add(Me.FilesComboBox)
 Me.Controls.Add(Me.FoldersComboBox)
 Me.Controls.Add(Me.VaultsComboBox)
 Me.Controls.Add(Me.CardPanel)
 Me.Controls.Add(Me.DoBtn)
 Me.Name = "MainForm"
 Me.Text = "Copy Control Values to Configurations"

 Me.ResumeLayout(False)
 Me.PerformLayout()

 End Sub

 #End Region

 Private WithEvents DoBtn As System.Windows.Forms.Button
 Private CardPanel As System.Windows.Forms.Panel
 Private WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
 Private WithEvents FoldersComboBox As System.Windows.Forms.ComboBox
 Private WithEvents FilesComboBox As System.Windows.Forms.ComboBox
 Private label1 As System.Windows.Forms.Label
 Private label2 As System.Windows.Forms.Label
 Private label3 As System.Windows.Forms.Label
 Private label4 As System.Windows.Forms.Label
 End Class
```

[Back to top](#top)
