---
title: "Execute Template Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Execute_Template_Example_VBNET.htm"
---

# Execute Template Example (VB.NET)

This example shows how to execute a template to create a folder structure in a vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
'  1. Start Microsoft Visual Studio.
'     a. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms App.
'     b. Type TemplateVBNET in Project name.
'     c. For Location, click ... and navigate to the folder where to
create the project.
'       d. Click Next.
'     e. Select Framework.
'     f. Click Create.
'  2. Click Show All Files in the Solution Explorer toolbar and expand
'     Form1.vb in the Solution Explorer.
'  3. Replace the code in Form1.vb with this code.
'  4. To create the form, replace the code in Form1.Designer.vb with
'     this code.
'  5. Add dependencies and safely pass arrays of structures.
'  6. Ensure that a template exists in the vault that you plan to
'     select and that a template card is assigned to that template.
'     NOTE: This example assumes that the template in your selected vault
'     creates a folder structure and that folder structure does not already
'     exist in the selected vault.
'  7. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays the Execute Template dialog box.
'     a. Select a vault.
'     b. Click Execute Template.
'     c. Displays a message box showing the name of the template to execute.
'     d. Click OK to close the message box.
'     e. Creates the folder structure defined for the template at the selected
'        vault's root folder and prompts for variable values, if any
'        exist for the template card and template.
'  2. Displays a message box informing you that a new folder structure
'     was created in the selected vault.
'     - or -
'     Displays a message box informing you that a folder structure
'     was not created.
'  3. Click OK to close the message box.
'  4. Close the Execute Template dialog box.
'  5. Examine the selected vault to verify that a new folder
'     structure based on the template was, or was not, created.
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
            Dim template As IEdmTemplate5 = Nothing

            Dim message As String = ""
            message = "Installed template in vault, " + vault.Name + ", to use:" + vbLf + vbLf

            While Not pos.IsNull

                template = templateMgr.GetNextTemplate(pos)

                message = message + template.GetMenuString + vbLf
                'Display message box with name of template
                'to use in the selected vault
                MessageBox.Show(message)

                'Create template folders in the selected vault
                'using this template
                Dim refreshFlag As EdmRefreshFlag
                Dim retData() As Object = Nothing
                refreshFlag = template.Run(Me.Handle.ToInt32(), vault1.RootFolderID)
```

```
                'Make sure folder structure is created
                'Exit application if it is not
                If refreshFlag = EdmRefreshFlag.EdmRefresh_Nothing Then
                    MessageBox.Show("Folder structure not created.")
                    Exit Sub
                Else
                    'Folder structure created
                    If refreshFlag = EdmRefreshFlag.EdmRefresh_FileList Then
                        vault1.RefreshFolder(vault1.RootFolderPath)
                        MessageBox.Show("The new folder structure based on the template was created in the selected vault.")
                    End If
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
