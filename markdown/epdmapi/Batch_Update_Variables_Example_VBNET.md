---
title: "Batch Update Card Variables Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Batch_Update_Variables_Example_VBNET.htm"
---

# Batch Update Card Variables Example (VB.NET)

This example shows how to update file and folder card variables in one batch.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 '  1. Start Microsoft Visual Studio.
 '     a. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms App.
 '     b. Type BatchUpdateCardVars in Project name.
 '     c. For Location, click ... and navigate to the folder where to create the project.
'       d. Click Next.
'     e. Select Framework.
'     f. Click Create.
'     g. Click Show All Files in the Solution Explorer toolbar and expand
'        Form1.vb in the Solution Explorer.
 '     h. Replace the code in Form1.vb with this code.
 '     i. To create the form, replace the code in Form1.Designer.vb with
 '        this code.
 '  2. Add dependencies and safely pass arrays of structures.
 '  3. Ensure that at least one text file is checked out, and at least one folder
 '     with the word Folder in its name exists in the vault.
 '  4. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 '  1. Displays the Batch Update dialog box.
 '     a. Select a vault.
 '     b. Click Batch Update Variables.
 '        * Updates the Title and Comment variables in the data cards
 '          only of checked-out text files.
 '        * Updates the Description variable of the data cards of all folders
 '          with the word Folder in their names.
 '        * Displays a message box saying  Card variables updated.
 '     c. Click OK to close the message box.
 '  2. Close the Batch Update dialog box.
 '  3. Inspect the data cards of any checked-out text files and folders with
 '     the word Folder in their names in the selected vault.
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

     Private Sub BatchUpdateButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BatchUpdateButton.Click

         Try
             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             'Create a batch update utility
             Dim Update As IEdmBatchUpdate2
             Update = vault2.CreateUtility(EdmUtility.EdmUtil_BatchUpdate)

             'Get the IDs of the file and folder card variables to update
             Dim TitleID As Integer
             Dim CommentID As Integer
             Dim DescriptionID As Integer
             Dim VariableMgr As IEdmVariableMgr5

             VariableMgr = vault1
             TitleID = VariableMgr.GetVariable("Title").ID
             DescriptionID = VariableMgr.GetVariable("Description").ID
             CommentID = VariableMgr.GetVariable("Comment").ID

             'Search for all text files in the vault
             Dim Search As IEdmSearch5
             Search = vault1.CreateUtility(EdmUtility.EdmUtil_Search)

             Search.FileName = "%.txt"

             Dim Result As IEdmSearchResult5
             Result = Search.GetFirstResult

             While Not Result Is Nothing
                 Update.SetVar(Result.ID, TitleID, "My Title", "", EdmBatchFlags.EdmBatch_Nothing)
                 Update.SetVar(Result.ID, CommentID, "My Comment", "", EdmBatchFlags.EdmBatch_Nothing)
                 Result = Search.GetNextResult
             End While

             'Search for all folders whose names contain the word Folder in the vault
             Search.FileName = "%Folder%"

             Result = Search.GetFirstResult

             While Not Result Is Nothing
                 Update.SetFolderVar(Result.ID, DescriptionID, "My Description", EdmBatchFlags.EdmBatch_Nothing)
                 Result = Search.GetNextResult
             End While

             'Write all the card variable values to the database
             Dim Errors() As EdmBatchError2 = Nothing
             Dim errorSize As Integer
             errorSize = Update.CommitUpdate(Errors, Nothing)

             'Display any errors
             Dim Msg As String
             Msg = "Card variables updated."

             Dim ErrName As String = Nothing
             Dim ErrDesc As String = Nothing
             Dim FileName As String = Nothing

             Dim Lo As Integer
             Lo = LBound(Errors)

             Dim Hi As Integer
             Hi = UBound(Errors)
```

```
            Dim vault9 As IEdmVault9
            vault9 = DirectCast(vault1, IEdmVault9)
            Dim ppoObjects(Hi) As EdmObjectInfo
            While Lo <= Hi
                ppoObjects(Lo).meType = EdmObjectType.EdmObject_File
                Lo = Lo + 1
            End While

            vault9.GetObjects(ppoObjects)

            While Lo <= Hi
                If (Errors(Lo).mlFileID > 0) Then
                    Dim File As IEdmFile6 = Nothing
                    Dim ID As Integer
                    ID = DirectCast(ppoObjects(Lo).moObjectID, Integer)
                    If (ppoObjects(Lo).meType = EdmObjectType.EdmObject_File) _
                       And (ID = Errors(Lo).mlFileID) Then
                        File = DirectCast(ppoObjects(Lo).mpoObject, IEdmFile6)
                        FileName = File.Name
                    End If
                End If

                vault1.GetErrorString(Errors(Lo).mlErrorCode, ErrName, ErrDesc)

                Msg = Msg + vbLf + ErrName + " " + FileName

                Lo = Lo + 1

            End While

            MsgBox(Msg)

        Catch ex As System.Runtime.InteropServices.COMException

            MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)

        Catch ex As Exception

            MessageBox.Show(ex.Message)

        End Try

    End Sub

End Class
```

```vb
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
         Me.BatchUpdateButton = New System.Windows.Forms.Button()
         Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
         Me.Label1 = New System.Windows.Forms.Label()
         Me.SuspendLayout()
         '
         'BatchUpdateButton
         '
         Me.BatchUpdateButton.Location = New System.Drawing.Point(30, 100)
         Me.BatchUpdateButton.Name = "BatchUpdateButton"
         Me.BatchUpdateButton.Size = New System.Drawing.Size(215, 23)
         Me.BatchUpdateButton.TabIndex = 0
         Me.BatchUpdateButton.Text = "Batch Update Variables"
         Me.BatchUpdateButton.UseVisualStyleBackColor = True
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(30, 56)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(121, 21)
         Me.VaultsComboBox.TabIndex = 1
         '
         'Label1
         '
         Me.Label1.AutoSize = True
         Me.Label1.Location = New System.Drawing.Point(27, 23)
         Me.Label1.Name = "Label1"
         Me.Label1.Size = New System.Drawing.Size(75, 13)
         Me.Label1.TabIndex = 2
         Me.Label1.Text = "Select vault view:"
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(284, 153)
         Me.Controls.Add(Me.Label1)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.BatchUpdateButton)
         Me.Name = "Form1"
         Me.Text = "Batch Update"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents BatchUpdateButton As System.Windows.Forms.Button
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents Label1 As System.Windows.Forms.Label

 End Class
```

[Back to top](#top)
