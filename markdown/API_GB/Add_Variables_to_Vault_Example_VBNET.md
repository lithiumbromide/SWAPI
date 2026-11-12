---
title: "Add Card Variables to Vault Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Add_Variables_to_Vault_Example_VBNET.htm"
---

# Add Card Variables to Vault Example (VB.NET)

This example shows how to add card variables to a vault and edit them.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio 2010.
 '    a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '    b. Type AddEditVars in Name.
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
 ' 1. Displays the Add variables to vault dialog box.
 ' 2. Select a vault view.
 ' 3. Click Add card variables.
  '    a. Adds two card variables, MyNewVar and MySecondVar, to the vault.
 '    b. Displays a message box with the IDs of the new variables.
 '    c. Click OK.
 ' 4. Click Edit card variables.
 '    a. Displays the Edit Variables dialog box.
 '    b. Click OK.
 '    c. Displays a message box.
 '    d. Click OK.
  ' 5. Close the Add variables to vault dialog box.
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
     Dim item As IEdmItem
     Dim fileInt As IEdmFile8

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

             Button1.Enabled = False

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub AddVaultVars_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles AddVaultVars.Click
         'Add card variables to vault
         Try
             Dim vault2 As IEdmVault11 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault11)
             If Not vault1.IsLoggedIn Then
                 'Log into selected vault as the current user
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim poVarMgr As IEdmVariableMgr6
             poVarMgr = vault2.CreateUtility(EdmUtility.EdmUtil_VariableMgr)

             Dim aoNewVars(1) As EdmVariableData 'Array with 2 variables

             'Set some properties for the first variable
             aoNewVars(0).mbsVariableName = "MyNewVar"
             aoNewVars(0).meType = EdmVariableType.EdmVarType_Text
             aoNewVars(0).mlEdmVariableFlags = EdmVariableFlags.EdmVar_Mandatory
             Dim aoAttributes(0) As EdmAttributeData
             aoAttributes(0).mbsBlockName = "DrawingBorder"
             aoAttributes(0).mbsAttribName = "PartNumber"
             aoAttributes(0).mbsExtensions = "DWG,DXF"
             aoNewVars(0).mpoAttributes = aoAttributes

             'Set some properties for the second variable
             aoNewVars(1).mbsVariableName = "MySecondVar"
             aoNewVars(1).meType = EdmVariableType.EdmVarType_Date

             'Add the variables
             poVarMgr.AddVariables(aoNewVars)

             'Show the IDs of the new variables
             Dim sMsg As String
             sMsg = ""

             Dim iIdx As Integer
             iIdx = LBound(aoNewVars)

             While iIdx <= UBound(aoNewVars)
                 sMsg = sMsg + aoNewVars(iIdx).mbsVariableName + " has ID " + CStr(aoNewVars(iIdx).mlVariableID) + vbLf
                 iIdx = iIdx + 1
             End While

             MessageBox.Show(sMsg)

             Button1.Enabled = True

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
         'Edit card variables
         Try
             Dim vault2 As IEdmVault11 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault11)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim varMgr As IEdmVariableMgr5
             varMgr = vault2
             If varMgr.EditVariables(Me.Handle.ToInt32()) Then
                 MessageBox.Show("An update was made!")
             Else
                 MessageBox.Show("No changes were made.")
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
         Me.AddVaultVars = New System.Windows.Forms.Button()
         Me.OpenFileDialog = New System.Windows.Forms.OpenFileDialog()
         Me.Button1 = New System.Windows.Forms.Button()
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
         'AddVaultVars
         '
         Me.AddVaultVars.Location = New System.Drawing.Point(16, 86)
         Me.AddVaultVars.Name = "AddVaultVars"
         Me.AddVaultVars.Size = New System.Drawing.Size(139, 23)
         Me.AddVaultVars.TabIndex = 5
         Me.AddVaultVars.Text = "Add card variables"
         Me.AddVaultVars.UseVisualStyleBackColor = True
         '
         'OpenFileDialog
         '
         Me.OpenFileDialog.Title = "Open"
         '
         'Button1
         '
         Me.Button1.Location = New System.Drawing.Point(16, 127)
         Me.Button1.Name = "Button1"
         Me.Button1.Size = New System.Drawing.Size(139, 23)
         Me.Button1.TabIndex = 6
         Me.Button1.Text = "Edit card variables"
         Me.Button1.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(243, 185)
         Me.Controls.Add(Me.Button1)
         Me.Controls.Add(Me.AddVaultVars)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Add variables to vault"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents AddVaultVars As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog As System.Windows.Forms.OpenFileDialog
     Friend WithEvents Button1 As System.Windows.Forms.Button
 End Class
```

[Back to top](#top)
