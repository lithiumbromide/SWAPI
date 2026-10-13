---
title: "Batch Get and Set Reference Variables Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Batch_Get_and_Set_Reference_Variables_Example_VBNET.htm"
---

# Batch Get and Set Reference Variables Example (VB.NET)

This example shows how to get and set reference variables in one batch.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 '  1. Start Microsoft Visual Studio 2010.
 '     a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '     b. Type BatchGetSetRefVariables in Name.
 '     c. Click Browse and navigate to the folder where to create the project.
 '     d. Click OK.
 '     e. Click Show All Files in the Solution Explorer toolbar and expand
 '        Form1.vb in the Solution Explorer.
 '     f. Replace the code in Form1.vb with this code.
 '     g. To create the form, replace the code in Form1.Designer.vb with
 '        this code.
 '  2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 '     name in the Solution Explorer, click Add Reference, click
 '     Assemblies > Framework in the left-side panel, browse to the top folder of
 '     your SOLIDWORKS PDM Professional installation, locate and click
 '     EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
 '  3. Right-click EPDM.Interop.epdm in References, click Properties, and set
 '     Embed Interop Types to False to handle methods that pass arrays of
 '     structures.
 '  4. Open the Administration tool.
 '     a. Log into a vault.
 '     b. Double-click Bill of Materials > BOM.
 '     c. Click Description in the Columns list.
 '     d. Select Look for variable in reference specific values.
 '     e. Click OK.
 '  5. Open File Explorer on a vault view.
 '  6. Ensure that an assembly and its referenced parts reside in the vault.
 '  7. Check out the assembly.
 '  8. Click the Bill of Materials tab in the vault view.
 '  9. Select Latest in the Reference Version dropdown.
 ' 10. Select @ in the Configuration dropdown.
 ' 11. Type a description in Description for each part in the assembly.
 ' 12. Click Save on the Bill of Materials toolbar and close the vault view.
 ' 13. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 '  1. The Batch Reference Variables dialog box displays.
 '     a. Select a vault view.
 '     b. Click Show all reference variables.
 '        1. In the Select Parent File dialog, select the assembly file identified
 '           in Preconditions step 5 and click Open.
 '        2. In the Select Child File dialog, select a part file referenced by the
 '           assembly file and click Open.
 '           Displays all of the reference variables for all configurations.
 '        3. Click OK in the dialog box.
 '     c. Click Get Description reference variable.
 '        1.  In the Select Parent File dialog, select the assembly file identified
 '           in Preconditions step 5 and click Open.
 '        2.  In the Select Child File dialog, select a part file referenced by the
 '           assembly file and click Open.
 '           Displays the current value of reference variable, Description.
 '        3. Click OK in the dialog box.
 '     d. Click Update Description reference variable.
 '        1.  In the Select Parent File dialog, select the assembly file identified
 '           in Preconditions step 5 and click Open.
 '        2.  In the Select Child File dialog, select a part file referenced by the
 '           assembly file and click Open.
 '        3. Type a new description and click OK.
 '        4. Click OK in the dialog box.
 '  2. Close the Batch Reference Variables dialog box.
 '  3. Open the vault view and click the assembly.
 '  4. Click the Bill of Materials tab.
 '  5. Select @ in the Configuration dropdown.
 '  6. Observe the text in the Description column for the updated part.
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

     Private vault As IEdmVault5 = Nothing

     Public Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

         Try
             vault = New EdmVault5()
             Dim vault1 As IEdmVault8 = DirectCast(vault, IEdmVault8)
             Dim Views As EdmViewInfo() = Nothing

             vault1.GetVaultViews(Views, False)
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

     Public Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
         ShowRefVars(vault)
     End Sub

     Public Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
         ShowRefDescription(vault)
     End Sub

     Public Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
         UpdateRefDescription(vault)
     End Sub

     Private Sub ShowRefVars(ByVal vault As IEdmVault11)

         If vault Is Nothing Then
             vault = New EdmVault5()
         End If

         If Not vault.IsLoggedIn Then
             vault.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
         End If

         'Let the user select the parent file
         Dim pathList As IEdmStrLst5
         pathList = vault.BrowseForFile(Me.Handle.ToInt32, EdmBrowseFlag.EdmBws_ForOpen + EdmBrowseFlag.EdmBws_PermitVaultFiles, "All Files (*.*)|*.*||", "", "", "", "Select Parent File:")
         If pathList Is Nothing Then Exit Sub

         Dim parent As IEdmFile8
         parent = vault.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition))

         'Let the user select the child file
         pathList = vault.BrowseForFile(Me.Handle.ToInt32, EdmBrowseFlag.EdmBws_ForOpen + EdmBrowseFlag.EdmBws_PermitVaultFiles, "All Files (*.*)|*.*||", "", "", "", "Select Child File:")
         If pathList Is Nothing Then Exit Sub

         Dim child As IEdmFile8
         child = vault.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition))

         'Get reference variables in the latest version
         Dim batch As IEdmBatchRefVars
         batch = vault.CreateUtility(EdmUtility.EdmUtil_BatchRefVars)
         Dim vars() As EdmRefVar
         vars = Nothing
         batch.GetAllRefVars(vars, parent.ID, 0, child.ID)

         'Show the result
         Dim msg As String
         msg = "Reference variables:" + vbLf + vbLf
         Dim idx As Integer
         idx = LBound(vars)
         While idx <= UBound(vars)
             msg = msg + "Parent ID: " + CStr(vars(idx).mlParentFileID) + vbLf
             msg = msg + "Parent cfg: " + vars(idx).mbsParentCfgName + vbLf
             msg = msg + "Child ID: " + CStr(vars(idx).mlChildFileID) + vbLf
             msg = msg + "Child cfg: " + vars(idx).mbsChildCfgName + vbLf
             msg = msg + "Status: " + vault.GetErrorMessage(vars(idx).mhResult) + vbLf
             msg = msg + "Variable ID: " + CStr(vars(idx).mlVarID) + vbLf
             msg = msg + "Value: " + CStr(vars(idx).moValue) + vbLf
             msg = msg + vbLf
             idx = idx + 1
         End While

         MsgBox(msg)
     End Sub

     Private Sub ShowRefDescription(ByVal vault As IEdmVault11)

         If vault Is Nothing Then
             vault = New EdmVault5()
         End If

         If Not vault.IsLoggedIn Then
             vault.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
         End If

         'Let the user select the parent file
         Dim pathList As IEdmStrLst5
         pathList = vault.BrowseForFile(Me.Handle.ToInt32, EdmBrowseFlag.EdmBws_ForOpen + EdmBrowseFlag.EdmBws_PermitVaultFiles, "All Files (*.*)|*.*||", "", "", "", "Select Parent File:")
         If pathList Is Nothing Then Exit Sub

         Dim parent As IEdmFile8
         parent = vault.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition))

         'Let the user select the child file
         pathList = vault.BrowseForFile(Me.Handle.ToInt32, EdmBrowseFlag.EdmBws_ForOpen + EdmBrowseFlag.EdmBws_PermitVaultFiles, "All Files (*.*)|*.*||", "", "", "", "Select Child File:")
         If pathList Is Nothing Then Exit Sub

         Dim child As IEdmFile8
         child = vault.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition))

         'Get the Description variable
         Dim varMgr As IEdmVariableMgr6
         varMgr = vault.CreateUtility(EdmUtility.EdmUtil_VariableMgr)
         Dim desc As IEdmVariable5
         desc = varMgr.GetVariable("Description")
         If desc Is Nothing Then Exit Sub

         'Get reference variables in the latest version
         Dim batch As IEdmBatchRefVars
         batch = vault.CreateUtility(EdmUtility.EdmUtil_BatchRefVars)
         Dim vars(0) As EdmRefVar
         vars(0).mlParentFileID = parent.ID
         vars(0).mlChildFileID = child.ID
         vars(0).mbsChildCfgName = "@"
         vars(0).mbsParentCfgName = "@"
         vars(0).mlParentVersion = 0
         vars(0).mlVarID = desc.ID
         batch.GetRefVars(vars)

         'Show the result to the caller
         Dim msg As String
         msg = "Reference variable: " + "Description" + vbLf + vbLf
         msg = msg + "Status: " + vault.GetErrorMessage(vars(0).mhResult) + vbLf
         msg = msg + "Value: " + CStr(vars(0).moValue)
         MsgBox(msg)

     End Sub

     Private Sub UpdateRefDescription(ByVal vault As IEdmVault11)

         If vault Is Nothing Then
             vault = New EdmVault5()
         End If

         If Not vault.IsLoggedIn Then
             vault.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
         End If

         'Let the user select the parent file
         Dim pathList As IEdmStrLst5
         pathList = vault.BrowseForFile(Me.Handle.ToInt32, EdmBrowseFlag.EdmBws_ForOpen + EdmBrowseFlag.EdmBws_PermitVaultFiles, "All Files (*.*)|*.*||", "", "", "", "Select Parent File:")
         If pathList Is Nothing Then Exit Sub

         Dim parent As IEdmFile8
         parent = vault.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition))

         'Let the user select the child file
         pathList = vault.BrowseForFile(Me.Handle.ToInt32, EdmBrowseFlag.EdmBws_ForOpen + EdmBrowseFlag.EdmBws_PermitVaultFiles, "All Files (*.*)|*.*||", "", "", "", "Select Child File:")
         If pathList Is Nothing Then Exit Sub

         Dim child As IEdmFile8
         child = vault.GetFileFromPath(pathList.GetNext(pathList.GetHeadPosition))

         'Get the Description variable
         Dim varMgr As IEdmVariableMgr6
         varMgr = vault.CreateUtility(EdmUtility.EdmUtil_VariableMgr)
         Dim desc As IEdmVariable5
         desc = varMgr.GetVariable("Description")
         If desc Is Nothing Then Exit Sub

         'Get reference variables in the latest version
         Dim batch As IEdmBatchRefVars
         batch = vault.CreateUtility(EdmUtility.EdmUtil_BatchRefVars)
         Dim vars(0) As EdmRefVar
         vars(0).mlParentFileID = parent.ID
         vars(0).mlChildFileID = child.ID
         vars(0).mbsChildCfgName = "@"
         vars(0).mbsParentCfgName = "@"
         vars(0).mlParentVersion = 0
         vars(0).mlVarID = desc.ID
         batch.GetRefVars(vars)

         'Let the user edit the Description variable
         vars(0).moValue = InputBox("Enter new description:", "Update Reference Variable", vars(0).moValue)

         'Store the value back in the reference
         batch.SetRefVars(vars)
         MsgBox(vault.GetErrorMessage(vars(0).mhResult))
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
         Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
         Me.VaultsLabel = New System.Windows.Forms.Label()
         Me.Button1 = New System.Windows.Forms.Button()
         Me.Button2 = New System.Windows.Forms.Button()
         Me.Button3 = New System.Windows.Forms.Button()
         Me.SuspendLayout()
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(33, 43)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(121, 21)
         Me.VaultsComboBox.TabIndex = 0
         '
         'VaultsLabel
         '
         Me.VaultsLabel.AutoSize = True
         Me.VaultsLabel.Location = New System.Drawing.Point(30, 18)
         Me.VaultsLabel.Name = "VaultsLabel"
         Me.VaultsLabel.Size = New System.Drawing.Size(100, 13)
         Me.VaultsLabel.TabIndex = 1
         Me.VaultsLabel.Text = "Select a vault view:"
         '
         'Button1
         '
         Me.Button1.Location = New System.Drawing.Point(33, 84)
         Me.Button1.Name = "Button1"
         Me.Button1.Size = New System.Drawing.Size(187, 23)
         Me.Button1.TabIndex = 2
         Me.Button1.Text = "Show all reference variables..."
         Me.Button1.UseVisualStyleBackColor = True
         '
         'Button2
         '
         Me.Button2.Location = New System.Drawing.Point(33, 138)
         Me.Button2.Name = "Button2"
         Me.Button2.Size = New System.Drawing.Size(187, 24)
         Me.Button2.TabIndex = 3
         Me.Button2.Text = "Get Description reference variable..."
         Me.Button2.UseVisualStyleBackColor = True
         '
         'Button3
         '
         Me.Button3.Location = New System.Drawing.Point(33, 190)
         Me.Button3.Name = "Button3"
         Me.Button3.Size = New System.Drawing.Size(208, 23)
         Me.Button3.TabIndex = 4
         Me.Button3.Text = "Update Description reference variable..."
         Me.Button3.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(284, 262)
         Me.Controls.Add(Me.Button3)
         Me.Controls.Add(Me.Button2)
         Me.Controls.Add(Me.Button1)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Name = "Form1"
         Me.Text = "Batch Reference Variables"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents Button1 As System.Windows.Forms.Button
     Friend WithEvents Button2 As System.Windows.Forms.Button
     Friend WithEvents Button3 As System.Windows.Forms.Button

 End Class
```

[Back to top](#top)
