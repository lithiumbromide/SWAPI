---
title: "Destroy Deleted Files in Vault Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Destroy_Deleted_Files_in_Vault_Example_VBNET.htm"
---

# Destroy Deleted Files in Vault Example (VB.NET)

This example shows how to create an application that displays a form in which a user can select the vault in whose root folder and subfolders all deleted files will be permanently destroyed. The user must have permission to delete files.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

**IMPORTANT:** Do not recreate and run this example if you do not want to destroy all deleted files in the root folder and subfolders in the selected vault. Instead, SOLIDWORKS PDM Professional suggests that you review the code to understand how you can programmatically destroy deleted files in the root folder and subfolders of a vault.

```vb
'----------------------------------------------------------------------------
' Preconditions:
'  1. Start Microsoft Visual Studio.
'  2. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms App.
'  3. Type the name of your project in  Project name.
'  4. For Location, click ... and navigate to the folder where to create the project.
  '  5. Click Next.
 '  6. Select Framework.
'  7. Click Create.
 '  8. Click Show All Files in the Solution Explorer toolbar and expand
 '     Form1.vb in the Solution Explorer.
'  9. Replace the code in Form1.vb with this code.
 ' 10. Replace the code in Form1.Designer.vb with  this code.
' 11.      Add dependencies and safely pass arrays of structures.
' 12. Delete one or more checked-in files in the root folder of your vault.
' 13. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 '  1. Displays the Destroy Deleted Files dialog.
 '  2. Select a vault.
 '  3. Optionally select the Include all subfolders check box.
 '  4. Click the Destroy deleted files button.
 '     A message box pops up informing you that:
 '     * No deleted files were found to destroy.
 '       - or -
 '     * The deleted files were destroyed.
 '  5. Click OK in the message box.
 '  6. Close the Destroy Deleted Files dialog.
 '----------------------------------------------------------------------------
'Form1.vb

 Imports EPDM.Interop.epdm

 Public Class Form1

     Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

         Try
             'Declare and create an instance of IEdmVault5
             'Cast IEdmVault5 to IEdmVault8
             Dim vault As IEdmVault8 = New EdmVault5
             Dim Views() As EdmViewInfo = Nothing

             'Populate the form with the names of
             'the vaults on the computer
             vault.GetVaultViews(Views, False)
             VaultsComboBox.Items.Clear()
             For Each View As EdmViewInfo In Views
                 VaultsComboBox.Items.Add(View.mbsVaultName)
             Next
             If VaultsComboBox.Items.Count > 0 Then
                 VaultsComboBox.Text = VaultsComboBox.Items(0)
             End If

         Catch ex As Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + vbCrLf + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub DestroyDeletedItemsButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles DestroyDeletedItemsButton.Click

         Try
             'Declare and create an instance of IEdmVault5
             Dim vault As IEdmVault5 = New EdmVault5()

             'Log into selected vault as the current user
             vault.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())

             'Check to see if deleted files should be
             'destroyed in all subfolders
             Dim aRecursive As Boolean = False
             If CheckBox_Recursive.Checked Then
                 aRecursive = True
             End If

            Dim poDeletedItems() As EdmDeletedItems  = Nothing
             Dim ppoDestroyedItems() As EdmFileInfo = Nothing
             Dim poErrors() As EdmBatchDelErrInfo = Nothing
             Dim DeletedFolder As IEdmFolder13

             'Get the root folder of the vault
             DeletedFolder = vault.RootFolder

             DeletedFolder.GetDeletedItems(poDeletedItems, aRecursive)
             DeletedFolder.DestroyDeletedItems2(poDeletedItems, ppoDestroyedItems, poErrors)

             'Destroy all deleted files in the root folder and
             'subfolders, if the check box is selected on the form
             Dim idx As Integer
             idx = LBound(ppoDestroyedItems)
             Dim msg As String = Nothing

             'If any deleted files found, display their names in a message box
             While idx <= UBound(ppoDestroyedItems)
                 Dim row As String
                 row = "DocumentID: " + CStr(ppoDestroyedItems(idx).mlFileID) + ", FolderID: " + _
                     CStr(ppoDestroyedItems(idx).mlFolderID) + ", File path: " + ppoDestroyedItems(idx).mbsPath + vbCrLf
                 If ppoDestroyedItems(idx).mhResult = 0 Then
                     row = row + "Status: OK" + vbCrLf
                 Else
                     row = row + " status: Failed=" + "HRESULT = 0x" + CStr(poErrors(idx).mlErrorCode)
                 End If
                 idx = idx + 1
                 msg = msg + row + vbCrLf
             End While

             If msg Is Nothing Then
                 MessageBox.Show("No deleted files were found in the selected vault's root folder or subfolders.")
             Else
                 MessageBox.Show("The status for each destroyed file is: " + vbCrLf + vbCrLf + msg)
             End If

         Catch ex As Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + vbCrLf + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Label1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs)

     End Sub

     Private Sub VaultsLabel_Click(ByVal sender As System.Object, ByVal e As System.EventArgs)

     End Sub

     Private Sub CheckBox_Recursive_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles CheckBox_Recursive.CheckedChanged

     End Sub

 End Class
Back to top
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
        Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
        Me.CheckBox_Recursive = New System.Windows.Forms.CheckBox()
        Me.DestroyDeletedItemsButton = New System.Windows.Forms.Button()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.VaultsLabel = New System.Windows.Forms.Label()
        Me.SuspendLayout()
        '
        'VaultsComboBox
        '
        Me.VaultsComboBox.FormattingEnabled = True
        Me.VaultsComboBox.Location = New System.Drawing.Point(69, 133)
        Me.VaultsComboBox.Name = "VaultsComboBox"
        Me.VaultsComboBox.Size = New System.Drawing.Size(139, 21)
        Me.VaultsComboBox.TabIndex = 1
        '
        'CheckBox_Recursive
        '
        Me.CheckBox_Recursive.AutoSize = True
        Me.CheckBox_Recursive.Location = New System.Drawing.Point(69, 181)
        Me.CheckBox_Recursive.Name = "CheckBox_Recursive"
        Me.CheckBox_Recursive.Size = New System.Drawing.Size(125, 17)
        Me.CheckBox_Recursive.TabIndex = 3
        Me.CheckBox_Recursive.Text = "Include all subfolders"
        Me.CheckBox_Recursive.UseVisualStyleBackColor = True
        '
        'DestroyDeletedItemsButton
        '
        Me.DestroyDeletedItemsButton.Location = New System.Drawing.Point(69, 218)
        Me.DestroyDeletedItemsButton.Name = "DestroyDeletedItemsButton"
        Me.DestroyDeletedItemsButton.Size = New System.Drawing.Size(139, 23)
        Me.DestroyDeletedItemsButton.TabIndex = 4
        Me.DestroyDeletedItemsButton.Text = "Destroy deleted files"
        Me.DestroyDeletedItemsButton.UseVisualStyleBackColor = True
        '
        'Label1
        '
        Me.Label1.Location = New System.Drawing.Point(66, 20)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(171, 68)
        Me.Label1.TabIndex = 5
        Me.Label1.Text = "This application destroys all deleted files in the root folder of the selected va" & _
            "ult and also allows you to destroy all deleted files in all of the selected vaul" & _
            "t's subfolders."
        '
        'VaultsLabel
        '
        Me.VaultsLabel.AutoSize = True
        Me.VaultsLabel.Location = New System.Drawing.Point(66, 108)
        Me.VaultsLabel.Name = "VaultsLabel"
        Me.VaultsLabel.Size = New System.Drawing.Size(75, 13)
        Me.VaultsLabel.TabIndex = 6
        Me.VaultsLabel.Text = "Select a vault:"
        '
        'DestroyDeletedItems
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(284, 262)
        Me.Controls.Add(Me.VaultsLabel)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.DestroyDeletedItemsButton)
        Me.Controls.Add(Me.CheckBox_Recursive)
        Me.Controls.Add(Me.VaultsComboBox)
        Me.Name = "DestroyDeletedItems"
        Me.Text = "Destroy Deleted Files"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents CheckBox_Recursive As System.Windows.Forms.CheckBox
    Friend WithEvents DestroyDeletedItemsButton As System.Windows.Forms.Button
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents VaultsLabel As System.Windows.Forms.Label

End Class
```

```vb
Back to top
```
