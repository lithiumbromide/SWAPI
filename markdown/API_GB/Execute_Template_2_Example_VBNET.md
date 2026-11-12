---
title: "Execute Template and Return Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Execute_Template_2_Example_VBNET.htm"
---

# Execute Template and Return Data Example (VB.NET)

This example shows how to execute a template to create a folder structure in a vault and return information.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
'  1. Start Microsoft Visual Studio 2010.
'     a. Click File > New > Project > Visual Basic > Windows Forms Application.
'     b. Type TemplateVBNET in Name.
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
'  4. Ensure that a template exists in the vault that you plan to
'     select and that a template card is assigned to that template.
'     NOTE: This example assumes that the template in your selected vault
'     creates a folder structure and that folder structure does not already
'     exist in the selected vault.
'  5. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays the Execute Template dialog box.
'     a. Select a vault view.
'     b. Click Execute Template.
'     c. Displays a message box showing the name of the template to execute.
'     d. Click OK to close the message box.
'     e. A template card dialog may appear to prompt for values.
'        1. Type values.
'        2. Click OK.
'  2. Displays a message box informing you that a new folder structure
'     is, or is not, created in the selected vault.
'  3. Click OK.
'  4. If a folder structure is created, displays a message box with
'     information about the folder structure.
'  5. Click OK.
'  6. Close the Execute Template dialog box.
'  7. Examine the selected vault to verify that a new folder
'     structure based on the template is, or is not, created.
'----------------------------------------------------------------------------
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
     Dim vault1 As IEdmVault5 = New EdmVault5()
     Dim vault As IEdmVault8 = DirectCast(vault1, IEdmVault8)
     Dim Views As EdmViewInfo() = Nothing
     Public Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

         Try
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

     Private Sub ExecuteTemplateButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ExecuteTemplateButton.Click

         Try
             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             'Access template in the selected vault
             Dim templateMgr As IEdmTemplateMgr5
             templateMgr = vault1.CreateUtility(EdmUtility.EdmUtil_TemplateMgr)
             Dim pos As IEdmPos5
             pos = templateMgr.GetFirstTemplatePosition
             Dim template As IEdmTemplate53 = Nothing

             Dim message As String = ""
             message = "Installed template in vault, " + vault.Name + ", to use:" + vbLf + vbLf

             While Not pos.IsNull

                 template = templateMgr.GetNextTemplate(pos)

                 message = message + template.GetMenuString + vbLf
                 'Display message box with name of template to execute
                 MessageBox.Show(message)

                 'Create template folders in the selected vault
                 'using this template
                 Dim refreshFlag As EdmRefreshFlag
                 Dim retData() As Object
                 refreshFlag = template.RunEx(Me.Handle.ToInt32(), vault1.RootFolderID, retData)

                 If retData.Length <= 0 Then
                     MessageBox.Show("No folder structure created.")
                 Else
                     MessageBox.Show("The new folder structure based on the template is created in the selected vault.")
                     If refreshFlag = EdmRefreshFlag.EdmRefresh_FileList Then
                         vault1.RefreshFolder(vault1.RootFolderPath)
                     End If

                     'Show a message box with information about the folder structure created by the template
                     Dim idx As Long
                     idx = LBound(retData)
                     Dim upper As Long
                     upper = UBound(retData)

                     Dim data As EdmData
                     message = "Template generated:" + vbLf
                     Dim row As String

                     While idx <= upper
                         data = retData(idx)
                         Select Case data.Type
                             Case EdmDataType.EdmData_File
                                 row = "Type=File, Path=" + data.Get(EdmDataPropertyType.EdmProp_Path)
                             Case EdmDataType.EdmData_Folder
                                 row = "Type=Folder, path=" + data.Get(EdmDataPropertyType.EdmProp_Path)
                             Case EdmDataType.EdmData_Variable
                                 row = "Type=Variable, Name=" + data.Get(EdmDataPropertyType.EdmProp_Name) + ", Value=" + data.Get(EdmDataPropertyType.EdmProp_Value)
                             Case EdmDataType.EdmData_Link
                                 row = "Type=Link, Name=" + data.Get(EdmDataPropertyType.EdmProp_LinkPath)
                             Case Else
                                 row = "No data"
                         End Select

                         idx = idx + 1
                         message = message + row + vbLf
                     End While

                     MessageBox.Show(message)
                 End If

             End While

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

```
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
        Me.ExecuteTemplateButton = New System.Windows.Forms.Button()
        Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.SuspendLayout()
        '
        'ExecuteTemplateButton
        '
        Me.ExecuteTemplateButton.Location = New System.Drawing.Point(30, 75)
        Me.ExecuteTemplateButton.Name = "ExecuteTemplateButton"
        Me.ExecuteTemplateButton.Size = New System.Drawing.Size(102, 23)
        Me.ExecuteTemplateButton.TabIndex = 0
        Me.ExecuteTemplateButton.Text = "Execute Template"
        Me.ExecuteTemplateButton.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        Me.ExecuteTemplateButton.UseVisualStyleBackColor = True
        '
        'VaultsComboBox
        '
        Me.VaultsComboBox.FormattingEnabled = True
        Me.VaultsComboBox.Location = New System.Drawing.Point(30, 39)
        Me.VaultsComboBox.Name = "VaultsComboBox"
        Me.VaultsComboBox.Size = New System.Drawing.Size(169, 21)
        Me.VaultsComboBox.TabIndex = 1
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(27, 23)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(91, 13)
        Me.Label1.TabIndex = 2
        Me.Label1.Text = "Select vault view:"
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(246, 123)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Controls.Add(Me.ExecuteTemplateButton)
        Me.Name = "Form1"
        Me.Text = "Execute Template"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents ExecuteTemplateButton As System.Windows.Forms.Button
    Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents Label1 As System.Windows.Forms.Label

End Class
```

```
Back to top
```
