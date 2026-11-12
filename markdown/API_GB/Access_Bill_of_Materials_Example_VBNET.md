---
title: "Access Bill of Materials Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Access_Bill_of_Materials_Example_VBNET.htm"
---

# Access Bill of Materials Example (VB.NET)

This example shows how to access the Bill of Materials (BOM) of a file in the vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 '    a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '    b. Type EdmBOM in Name.
 '    c. Click Browse and navigate to the folder where to create the project.
 '    d. Click OK.
 '    e. Click Show All Files in the Solution Explorer toolbar and expand
 '       Form1.vb in the Solution Explorer.
 '    f. Replace the code in Form1.vb with this code.
 '    g. To create the form, replace the code in Form1.Designer.vb with
 '       this code.
 ' 2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 '    name in the Solution Explorer, click Add Reference, click
 '    Assemblies > Framework in the left-side panel, browse to the top folder
 '    of your SOLIDWORKS PDM Professional installation, locate and click
 '    EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
 ' 3. Right-click EPDM.Interop.epdm in References, click Properties, and set
 '    Embed Interop Types to False to handle methods that pass arrays of
 '    structures.
 ' 4. Ensure that the vault contains the BOM layout.
 '    To inspect the existing layouts:
 '    a. Open the SOLIDWORKS PDM Professional Administration tool.
 '    b. Log into vault_name.
 '    c. Expand vault_name > Bills of Materials.
 '    d. Verify that layout, BOM, exists.
 ' 5. Ensure that an assembly and its parts exist in the root folder of
 '    the vault in default configuration, @.
 ' 6. Ensure that one or more named Bills of Materials exist for the assembly.
 '    a. Open File Explorer on a vault_name view.
 '    b. Click the assembly.
 '    c. Click the Bill of Materials tab.
 '    d. Click BOM.
 '    e. If a named Bill of Materials does not exist in the BOM list:
 '       1. Click Save > Save As in the tab toolbar.
 '       2. In the Save As dialog, click  Save.
 ' 7. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Opens the Bill of Materials dialog box.
 '    a. Select a vault_name view.
 '    b. Click Select file.
 '    c. In the Select File dialog:
 '       1. Click the assembly specified in Preconditions step 5.
 '       2. Click Open.
 '    d. Click Get BOM Info.
 '       Displays message boxes containing:
 '       * Information about all named BOMs of the assembly.
 '       * Version information for the named BOMs.
 '       * Information about all BOM layouts in the vault.
 '       * Row and column information about a BOM view in the BOM layout
 '         for the selected assembly in its @ configuration.
 '    e. Click OK in each message box.
 '    f. Click Save BOM to CSV.
 '       Saves the BOM to c:\temp\SavedBOM.csv.
 ' 2. Close the Bill of Materials dialog box.
 ' 3. Verify that c:\temp\SavedBOM.csv is created.
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
     Dim bom As IEdmBom
     Dim bomMgr As IEdmBomMgr2
     Dim bomView As IEdmBomView3

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
                 Next
             End If

             GetBOM.Enabled = True
             SaveBOM.Enabled = False

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
             vault2 = DirectCast(vault1, IEdmVault11)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             If Not IsNothing(aFile) Then

                ' Get named BOMs and their versions for the selected file
                Dim derivedBOMs() As EdmBomInfo = Nothing
                aFile.GetDerivedBOMs(derivedBOMs)

                Dim arrSize As Integer
                Dim ppoVersions() As EdmBomVersion = Nothing
                Dim i As Integer = 0
                Dim j As Integer = 0
                Dim id As Integer
                Dim str As String = ""
                Dim verstr As String = ""
                Dim verArrSize As Integer
               Dim canSeeLayout As Boolean
               Dim userID As Integer
                userID = vault2.GetLoggedInWindowsUserID(vault2.Name)
                arrSize = derivedBOMs.Length

                While i < arrSize
                 id = derivedBOMs(i).mlBomID
                 bom = vault2.GetObject(EdmObjectType.EdmObject_BOM, id)
                 str = "Named BOM: " & derivedBOMs(i).mbsBomName & vbLf & "Type of BOM as defined in EdmBomType: " & vbLf & derivedBOMs(i).meType & vbLf & "Check-out user: " & bom.CheckOutUserID & vbLf & "Current state: " & bom.CurrentState.Name & vbLf & "Current version: " & bom.CurrentVersion & vbLf & "ID: " & bom.FileID & vbLf & "Is checked out: " & bom.IsCheckedOut
                 MessageBox.Show(str)
                 bom.GetVersions(ppoVersions)
                 verArrSize = ppoVersions.Length
                 While j < verArrSize
                     verstr = "BOM version: " & vbLf & "Type as defined in EdmBomVersionType: " & ppoVersions(j).meType & vbLf & "Version number: " & ppoVersions(j).mlVersion & vbLf & "Date: " & ppoVersions(j).moDate & vbLf & "Label: " & ppoVersions(j).mbsTag & vbLf & "Comment: " & ppoVersions(j).mbsComment
                     MessageBox.Show(verstr)
                     j = j + 1
                 End While
                 i = i + 1
                End While

                ' Get a BOM view with the specified layout
                bomMgr = vault2.CreateUtility(EdmUtility.EdmUtil_BomMgr)
                Dim ppoRetLayouts() As EdmBomLayout2 = Nothing
                Dim ppoRetLayout As EdmBomLayout2
                bomMgr.GetBomLayouts2(ppoRetLayouts)

                i = 0
                arrSize = ppoRetLayouts.Length
                str = ""
                While i < arrSize
                 ppoRetLayout = ppoRetLayouts(i)
                  canSeeLayout = bomMgr.CanSeeBomLayout(userID, ppoRetLayout.mlLayoutID)
                 str = "BOM Layout " & i & ": " & vbLf & ppoRetLayout.mbsLayoutName & vbLf & "ID: " & ppoRetLayout.mlLayoutID
                 str = str & " Logged-in user can see this layout? " & canSeeLayout
                 If ppoRetLayout.mbsLayoutName = "BOM" Then
                     bomView = aFile.GetComputedBOM(ppoRetLayout.mbsLayoutName, 0, "@", EdmBomFlag.EdmBf_AsBuilt + EdmBomFlag.EdmBf_ShowSelected)
                 End If
                 MessageBox.Show(str)
                 i = i + 1
                End While

                ' Display BOM view row and column information
                Dim ppoRows() As Object = Nothing
                Dim ppoRow As IEdmBomCell
                bomView.GetRows(ppoRows)
                i = 0
                arrSize = ppoRows.Length
                str = ""
                While i < arrSize
                 ppoRow = ppoRows(i)
                 str = "BOM Row " & i & ": " & vbLf & "Item ID: " & ppoRow.GetItemID & vbLf & "Path name: " & ppoRow.GetPathName & vbLf & "Tree level: " & ppoRow.GetTreeLevel & vbLf & " Is locked? " & ppoRow.IsLocked
                 MessageBox.Show(str)
                 i = i + 1
                End While

                Dim ppoColumns() As EdmBomColumn = Nothing
                bomView.GetColumns(ppoColumns)
                i = 0
                arrSize = ppoColumns.Length
                str = ""
                While i < arrSize
                 str = "BOM Column " & i & ": " & vbLf & "Header: " & ppoColumns(i).mbsCaption & vbLf & "Column type as defined in EdmBomColumnType: " & ppoColumns(i).meType & vbLf & "ID: " & ppoColumns(i).mlColumnID & vbLf & "Flags: " & ppoColumns(i).mlFlags & vbLf & "Variable ID: " & ppoColumns(i).mlVariableID & vbLf & "Variable type as defined in EdmVariableType: " & ppoColumns(i).mlVariableType & vbLf & "Column width: " & ppoColumns(i).mlWidth
                 MessageBox.Show(str)
                 i = i + 1
                End While

                SaveBOM.Enabled = True

          End If
         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try

     End Sub

     Public Sub SaveBOM_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles SaveBOM.Click
         Try

             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault9)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             If Not IsNothing(aFile) And Not IsNothing(bomView) Then
                 bomView.SaveToCSV("c:\temp\SavedBOM.csv", False)
             End If

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
         Me.SaveBOM = New System.Windows.Forms.Button()
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
         'GetBOM
         '
         Me.GetBOM.Enabled = False
         Me.GetBOM.Location = New System.Drawing.Point(40, 183)
         Me.GetBOM.Name = "GetBOM"
         Me.GetBOM.Size = New System.Drawing.Size(157, 23)
         Me.GetBOM.TabIndex = 6
         Me.GetBOM.Text = "Get BOM Info"
         Me.GetBOM.UseVisualStyleBackColor = True
         '
         'OpenFileDialog1
         '
         Me.OpenFileDialog1.FileName = "OpenFileDialog1"
         Me.OpenFileDialog1.Title = "Select File"
         '
         'SaveBOM
         '
         Me.SaveBOM.Enabled = False
         Me.SaveBOM.Location = New System.Drawing.Point(40, 234)
         Me.SaveBOM.Name = "SaveBOM"
         Me.SaveBOM.Size = New System.Drawing.Size(157, 23)
         Me.SaveBOM.TabIndex = 7
         Me.SaveBOM.Text = "Save BOM to CSV"
         Me.SaveBOM.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(284, 305)
         Me.Controls.Add(Me.SaveBOM)
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
     Friend WithEvents SaveBOM As Button
 End Class
```

[Back to top](#top)
