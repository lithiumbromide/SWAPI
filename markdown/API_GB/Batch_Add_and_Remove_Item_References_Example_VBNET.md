---
title: "Batch Add Item References Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Batch_Add_and_Remove_Item_References_Example_VBNET.htm"
---

# Batch Add Item References Example (VB.NET)

This example shows how to add item references in one batch.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 '  1. Start Microsoft Visual Studio 2010.
 '     a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '     b. Type BatchGetFiles in Name.
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
 '  4.  Open Start > All Programs > SOLIDWORKS PDM Professional >
 '     Item Explorer.
 '     a. Click the vault to which to add new items.
 '     b. Click New Item on the toolbar to add   00000004 and 00000005.
 '     c. Keep the Item Explorer open.
 '  5. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 '  1. The Add Item Reference dialog box displays.
 '     a. Select a vault view.
 '     b. Click Add item reference.
 '  2. Click OK in the BatchAddItemRefs dialog box.
 '  3. In the Item Explorer:
 '     a. Click 00000004 under New Item Folder.
 '     b. Observe that item 00000005 is linked to item 00000004.
 '  4. Close the Add Item Reference dialog box and the Item Explorer.
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

     Public Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

         Try
             vault1 = New EdmVault5()
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

     Public Sub AddItemRefs_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles AddItemRefs.Click
         Try

             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             AddItemReference(vault1)

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub AddItemReference(ByVal vault As IEdmVault11)

         'Set up the search interface to find items
         Dim res As IEdmSearchResult5
         Dim search As IEdmSearch7
         search = vault.CreateUtility(EdmUtility.EdmUtil_Search)
         search.StartFolderID = vault.ItemRootFolderID
         search.SetToken(EdmSearchToken.Edmstok_FindFolders, False)
         search.SetToken(EdmSearchToken.Edmstok_FindFiles, True)
         search.SetToken(EdmSearchToken.Edmstok_FindItems, True)
         search.SetToken(EdmSearchToken.Edmstok_Recursive, True)

         'Get the database ID of item number 00000004
         search.FileName = "00000004.<item>"
         res = search.GetFirstResult
         If res Is Nothing Then Exit Sub
         Dim item4ID As Integer
         item4ID = res.ID

         'Get the database ID of item number 00000005
         search.FileName = "00000005.<item>"
         res = search.GetFirstResult
         If res Is Nothing Then Exit Sub
         Dim item5ID As Integer
         item5ID = res.ID

         'Add item number 00000005 as a reference to item number 00000004
         Dim addRefs(0) As EdmItemRef
         addRefs(0).moParentNamePathOrItemID = item4ID
         addRefs(0).moNamePathOrID = item5ID
         addRefs(0).mlEdmRefFlags = EdmRefFlags.EdmRef_Item

         'No item references to remove
         Dim removeRefs() As EdmItemRef
         removeRefs = Nothing

         Dim batch As IEdmBatchItemReferenceUpdate
         batch = vault.CreateUtility(EdmUtility.EdmUtil_BatchItemReferenceUpdate)
         batch.UpdateReferences(addRefs, removeRefs)
         MsgBox("Result of operation: " + vbLf + vault.GetErrorMessage(addRefs(0).mhResult))

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
         Me.AddItemRefs = New System.Windows.Forms.Button()
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
         'AddItemRefs
         '
         Me.AddItemRefs.Location = New System.Drawing.Point(39, 84)
         Me.AddItemRefs.Name = "AddItemRefs"
         Me.AddItemRefs.Size = New System.Drawing.Size(157, 23)
         Me.AddItemRefs.TabIndex = 6
         Me.AddItemRefs.Text = "Add item reference"
         Me.AddItemRefs.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(284, 147)
         Me.Controls.Add(Me.AddItemRefs)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Add Item Reference"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents AddItemRefs As System.Windows.Forms.Button

 End Class
```

[Back to top](#top)
