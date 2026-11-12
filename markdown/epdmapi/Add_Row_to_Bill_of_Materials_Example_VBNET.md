---
title: "Add Row to Bill of Materials Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Add_Row_to_Bill_of_Materials_Example_VBNET.htm"
---

# Add Row to Bill of Materials Example (VB.NET)

This example shows how to add a row to the named Bill of Materials (BOM) of a file in the vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 '    a. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms Application.
 '    b. Type EdmBOM in Project name.
 '    c. For Location, click ... and navigate to the folder where to create the project.
'      d. Click Next.
'    e. Select Framework.
'    f. Click Create.
'    g. Click Show All Files in the Solution Explorer toolbar and expand
'       Form1.vb in the Solution Explorer.
 '    h. Replace the code in Form1.vb with this code.
 '    i. To create the form, replace the code in Form1.Designer.vb with
 '       this code.
 ' 2. Add dependencies and safely pass arrays of structures.
 ' 3. Ensure that the vault contains the BOM layout.
 '    To inspect the existing layouts:
 '    a. Open the SOLIDWORKS PDM Professional Administration tool.
 '    b. Log into vault_name.
 '    c. Expand vault_name > Bills of Materials.
 '    d. Verify that layout, BOM, exists.
 ' 4. Ensure that an assembly and its parts exist in a folder of
 '    the vault.
 ' 5. Check in a text file named "temp" in the assembly directory.
 ' 6. Modify the path to "temp" in the code.
 ' 7. Ensure that a named Bill of Materials exists for the assembly.
 '    a. Open File Explorer on a vault_name view.
 '    b. Click the assembly.
 '    c. Click the Bill of Materials tab.
 '    d. Click BOM.
 '    e. If a named Bill of Materials does not exist in the BOM list:
 '       1. Click Save > Save As in the tab toolbar.
 '       2. In the Save As dialog, click  Save.
 ' 8. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. The Bill of Materials dialog box displays.
 '    a. Select a vault_name view.
 '    b. Click Select file.
 '    c. In the Select File dialog:
 '       1. Click the assembly specified in Preconditions step 5.
 '       2. Click Open.
 '    d. Click Get BOM.
 '       Displays message boxes containing:
 '       * Version information for the named BOM.
 '       * Row and column information about a BOM view in the BOM layout
 '         for the selected assembly.
 '    e. Click OK in each message box.
 ' 2. Inserts a row for "temp" after the first row in the BOM.
 ' 3. Close the Bill of Materials dialog box.
 ' 4. Verify the new row in the named BOM of the assembly in vault_name view.
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
     Dim aFile As IEdmFile7
     Dim aFolder As IEdmFolder5
     Dim aPos As IEdmPos5
     Dim bom As IEdmBom
     Dim bomCell As IEdmBomCell
     Dim bomMgr As IEdmBomMgr
     Dim bomView As IEdmBomView2
     Dim retVal As Boolean
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
                     aPos = aFile.GetFirstFolderPosition
                     aFolder = aFile.GetNextFolder(aPos)
                 Next
             End If

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub GetBOM_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GetBOM.Click
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault9)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             bomMgr = vault2.CreateUtility(EdmUtility.EdmUtil_BomMgr)
             Dim ppoRetLayouts() As EdmBomLayout
             bomMgr.GetBomLayouts(ppoRetLayouts)

             Dim derivedBOMs() As EdmBomInfo
             aFile.GetDerivedBOMs(derivedBOMs)

             Dim arrSize As Integer
             Dim i As Integer = 0
             Dim id As Integer
             Dim str As String = ""
             arrSize = derivedBOMs.Length

             While i < arrSize
                 id = derivedBOMs(i).mlBomID
                 bom = vault2.GetObject(EdmObjectType.EdmObject_BOM, id)
                 str = "Derived BOM: " + derivedBOMs(i).mbsBomName & " " & bom.CheckOutUserID & " " & bom.CurrentState.Name & " " & bom.CurrentVersion & " " & bom.FileID & " " & bom.IsCheckedOut
                 MessageBox.Show(str)
                 i = i + 1
             End While

             bomView = bom.GetView(0)

             Dim ppoRows() As Object
             Dim ppoRow As IEdmBomCell
             bomView.GetRows(ppoRows)
             i = 0
             arrSize = ppoRows.Length
             str = ""
             While i < arrSize
                 ppoRow = ppoRows(i)
                 str = "Row " & i & ": " & ppoRow.GetItemID & " " & ppoRow.GetPathName & " " & ppoRow.GetTreeLevel & " " & ppoRow.IsLocked
                 MessageBox.Show(str)
                 i = i + 1
             End While

             Dim ppoColumns() As EdmBomColumn
             bomView.GetColumns(ppoColumns)
             i = 0
             arrSize = ppoColumns.Length
             str = ""
             While i < arrSize
                 str = "Column " & i & ": " & ppoColumns(i).mbsCaption & " " & ppoColumns(i).meType & " " & ppoColumns(i).mlColumnID & " " & ppoColumns(i).mlFlags & " " & ppoColumns(i).mlVariableID & " " & ppoColumns(i).mlVariableType & " " & ppoColumns(i).mlWidth
                 MessageBox.Show(str)
                 i = i + 1
             End While

             Dim ppoNewRow As IEdmBomCell
             Dim errMsg As String = ""
             'Dim poValue As Object = Nothing
             'Dim poComputedValue As Object = Nothing
             'Dim pbsConfiguration As String = ""
             'Dim pbReadOnly As Boolean
             Dim plFocusNode As Integer
             bomView.InsertRow(ppoRows(0), EdmBomInsertRowOption.EdmBomInsertRowOption_BelowRow, ppoNewRow)
             ppoNewRow.SetVar(ppoColumns(0).mlVariableID, ppoColumns(0).meType, "vault_name\temp", "", EdmBomSetVarOption.EdmBomSetVarOption_Both, errMsg)
             'ppoNewRow.GetVar(ppoColumns(0).mlVariableID, ppoColumns(0).meType, poValue, poComputedValue, pbsConfiguration, pbReadOnly)
             'MessageBox.Show(poValue.ToString)
             'MessageBox.Show(poComputedValue.ToString)
             'MessageBox.Show(pbsConfiguration)
             'MessageBox.Show(pbReadOnly.ToString)

             bomView.Commit("", errMsg, plFocusNode)

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
         Me.SelectFiles = New System.Windows.Forms.Button()
         Me.File1List = New System.Windows.Forms.ListBox()
         Me.GetBOM = New System.Windows.Forms.Button()
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
         Me.SelectFiles.Text = "Select file for which to get a BOM..."
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
         'GetBOM
         '
         Me.GetBOM.Location = New System.Drawing.Point(40, 183)
         Me.GetBOM.Name = "GetBOM"
         Me.GetBOM.Size = New System.Drawing.Size(157, 23)
         Me.GetBOM.TabIndex = 6
         Me.GetBOM.Text = "Get BOM"
         Me.GetBOM.UseVisualStyleBackColor = True
         '
         'OpenFileDialog1
         '
         Me.OpenFileDialog1.FileName = "OpenFileDialog1"
         Me.OpenFileDialog1.Multiselect = False
         Me.OpenFileDialog1.Title = "Select File"
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(284, 235)
         Me.Controls.Add(Me.GetBOM)
         Me.Controls.Add(Me.File1List)
         Me.Controls.Add(Me.SelectFiles)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Bill of Materials"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents SelectFiles As System.Windows.Forms.Button
     Friend WithEvents File1List As System.Windows.Forms.ListBox
     Friend WithEvents GetBOM As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog1 As System.Windows.Forms.OpenFileDialog

 End Class
Back to top
```
