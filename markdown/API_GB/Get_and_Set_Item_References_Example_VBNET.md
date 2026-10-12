---
title: "Get and Set Item References Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Get_and_Set_Item_References_Example_VBNET.htm"
---

# Get and Set Item References Example (VB.NET)

This example shows how to get and set item references.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio 2010.
 '    a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '    b. Type ItemRefs in Name.
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
 ' 4. Ensure that an item folder with at least one item is checked into the vault.
 ' 5. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Get and set item references dialog box.
 ' 2. Select a vault view.
 ' 3. Click Get item references.
  '    a. Click an item folder in the vault.
 '    b. Click OK.
 '    c. Displays a message box confirming your folder selection.
 '    d. Click OK.
 '    e. Displays a message box with item references for the first item found
 '       in the selected folder.
 '    f. Click OK.
 ' 4. Click Set item references.
 '    a. Click one or more files to add as references to the item.
 '    b. Click Open.
 '    c. Displays a message box with the updated references.
 '       - or -
 '       Displays a message box with errors.
 '    d. Click OK.
  ' 5. Close the Get and set item references dialog box.
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

     Public Sub GetItemRefs_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GetItemRefs.Click
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

             Dim folder As IEdmFolder6
             folder = vault2.BrowseForFolder2(Me.Handle.ToInt32, "Select a folder", vault2.RootFolder, EdmBrowseForFolderFlag.EdmBwsFld_None)
             If Not folder Is Nothing Then
                 If folder.ObjectType = EdmObjectType.EdmObject_Folder Then
                     MsgBox("You selected the file folder: " + vbLf + folder.LocalPath)
                 Else
                     MsgBox("You selected the item folder: " + vbLf + folder.LocalPath)
                 End If
             End If

             'Get the first item in the selected folder
             Dim pos As IEdmPos5
             Dim msg As String

             pos = folder.GetFirstFilePosition
             fileInt = folder.GetNextFile(pos)

             'Search for item by name to get its ID
             Dim search As IEdmSearch7
             search = vault2.CreateUtility(EdmUtility.EdmUtil_Search)
             search.FindFiles = True
             search.FindFolders = False
             search.Recursive = True
             search.SetToken(EdmSearchToken.Edmstok_FindItems, True)
             search.StartFolderID = vault2.ItemRootFolderID
             search.FileName = fileInt.Name

             Dim result As IEdmSearchResult5
             result = search.GetFirstResult

             If result Is Nothing Then
                 MessageBox.Show("The item '" + fileInt.Name + "' was not found.")
             End If

             While Not result Is Nothing
                 If (result.IsKindOf(EdmObjectType.EdmObject_Item)) Then
                     fileInt = result
                     item = fileInt

                     'Create a message about the item and its references
                     msg = "Name=" & item.Name & vbLf
                     msg = msg & "ID = " & item.ID.ToString & vbLf
                     msg = msg & "Descriptive name = " & item.ItemDescriptiveName & vbLf
                     msg = msg & "Check-out path = " & fileInt.LockPath & vbLf
                     msg = msg & "Workflow state = " & fileInt.CurrentState.Name & vbLf
                     msg = msg & vbLf & "Referenced files:" & vbLf

                     Dim refs() As EdmItemRef = Nothing
                     item.GetReferences(EdmRefFlags.EdmRef_Dynamic + EdmRefFlags.EdmRef_Static + EdmRefFlags.EdmRef_Item + EdmRefFlags.EdmRef_File, refs)

                     Dim idx As Integer
                     idx = LBound(refs)

                     While (idx <= UBound(refs))

                         msg = msg + "File ID=(" + CStr(refs(idx).moNamePathOrID) + ") "
                         msg = msg + "Parent Item ID=(" + CStr(refs(idx).moParentNamePathOrItemID) + ") "
                         msg = msg + "Configuration='" + refs(idx).mbsConfiguration + "' "

                         If (refs(idx).mlEdmRefFlags And EdmRefFlags.EdmRef_Dynamic) = EdmRefFlags.EdmRef_Dynamic Then
                             msg = msg + " (auto-update reference)"
                         Else
                             If (refs(idx).mlEdmRefFlags And EdmRefFlags.EdmRef_Static) = EdmRefFlags.EdmRef_Static Then
                                 msg = msg + " (static reference)"
                             End If
                         End If
                         idx = idx + 1
                         msg = msg + vbLf
                     End While

                     MessageBox.Show(msg)
                     Button1.Enabled = True

                 End If
                 Exit Sub
             End While

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
         'Set item references
         Try

             Dim vault2 As IEdmVault11 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault11)
             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             'Get the current item references
             Dim oldRefs() As EdmItemRef = Nothing
             item.GetReferences(EdmRefFlags.EdmRef_Dynamic + EdmRefFlags.EdmRef_Static + EdmRefFlags.EdmRef_Item + EdmRefFlags.EdmRef_File, oldRefs)

             'Let the user browse for new file references
             Dim pathList As IEdmStrLst5 = vault2.BrowseForFile(Me.Handle.ToInt32, EdmBrowseFlag.EdmBws_ForOpen + EdmBrowseFlag.EdmBws_PermitVaultFiles + EdmBrowseFlag.EdmBws_PermitMultipleSel, "All Files|*.*||")

             If pathList Is Nothing Then Return

             'Create an array of new item references
             Dim newRefs(pathList.Count - 1) As EdmItemRef
             Dim idx As Integer = 0
             Dim pos As IEdmPos5
             pos = pathList.GetHeadPosition

             While Not pos.IsNull
                 Dim path As String
                 path = pathList.GetNext(pos)
                 newRefs(idx).moNamePathOrID = path
                 newRefs(idx).mlEdmRefFlags = EdmRefFlags.EdmRef_Static + EdmRefFlags.EdmRef_File
                 newRefs(idx).moParentNamePathOrItemID = item.ID
                 idx = idx + 1
             End While

             'Check out the item
             fileInt.LockFile(vault2.ItemRootFolderID, Me.Handle.ToInt32())

             'Update the item references
             item.UpdateReferences(newRefs, oldRefs)

             'Collect all errors
             Dim msg As String = ""
             Dim errstr As String = ""
             idx = LBound(newRefs)

             While (idx <= UBound(newRefs))
                 If newRefs(idx).mhResult <> 0 Then
                     errstr = vault2.GetErrorName(newRefs(idx).mhResult)
                     msg = msg + "Failed to save ref: '" + CStr(newRefs(idx).moNamePathOrID) + "' (" + errstr + ")" + vbLf
                 End If
                 idx = idx + 1
             End While

             idx = LBound(oldRefs)

             While (idx <= UBound(oldRefs))
                 If oldRefs(idx).mhResult <> 0 Then
                     errstr = vault2.GetErrorName(oldRefs(idx).mhResult)
                     msg = msg + "Failed to delete ref: '" + CStr(oldRefs(idx).moNamePathOrID) + "' (" + errstr + ")" + vbLf
                 End If
                 idx = idx + 1
             End While

             'Display a status message
             If msg = "" Then
                 msg = "Updated references successfully!" & vbLf

                 Dim refs() As EdmItemRef = Nothing
                 item.GetReferences(EdmRefFlags.EdmRef_Dynamic + EdmRefFlags.EdmRef_Static + EdmRefFlags.EdmRef_Item + EdmRefFlags.EdmRef_File, refs)
                 idx = LBound(refs)

                 'Construct a message about the reference updates
                 While (idx <= UBound(refs))

                     msg = msg + "File ID=(" + CStr(refs(idx).moNamePathOrID) + ") "
                     msg = msg + "Parent Item ID=(" + CStr(refs(idx).moParentNamePathOrItemID) + ") "
                     msg = msg + "Configuration='" + refs(idx).mbsConfiguration + "' "

                     If (refs(idx).mlEdmRefFlags And EdmRefFlags.EdmRef_Dynamic) = EdmRefFlags.EdmRef_Dynamic Then
                         msg = msg + " (auto-update reference)"
                     Else
                         If (refs(idx).mlEdmRefFlags And EdmRefFlags.EdmRef_Static) = EdmRefFlags.EdmRef_Static Then
                             msg = msg + " (static reference)"
                         End If
                     End If
                     idx = idx + 1
                     msg = msg + vbLf
                 End While

                 MessageBox.Show(msg)
             Else
                 MessageBox.Show("Errors detected: " + vbLf + msg)
             End If

             'Check in the item
             fileInt.UnlockFile(Me.Handle.ToInt32(), "Updated item references", EdmUnlockFlag.EdmUnlock_IgnoreRefsNotLockedByCaller)

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
         Me.GetItemRefs = New System.Windows.Forms.Button()
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
         'GetItemRefs
         '
         Me.GetItemRefs.Location = New System.Drawing.Point(16, 86)
         Me.GetItemRefs.Name = "GetItemRefs"
         Me.GetItemRefs.Size = New System.Drawing.Size(139, 23)
         Me.GetItemRefs.TabIndex = 5
         Me.GetItemRefs.Text = "Get item references..."
         Me.GetItemRefs.UseVisualStyleBackColor = True
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
         Me.Button1.Text = "Set item references..."
         Me.Button1.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(317, 185)
         Me.Controls.Add(Me.Button1)
         Me.Controls.Add(Me.GetItemRefs)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Name = "Form1"
         Me.Text = "Get and set item references"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents GetItemRefs As System.Windows.Forms.Button
     Friend WithEvents OpenFileDialog As System.Windows.Forms.OpenFileDialog
     Friend WithEvents Button1 As System.Windows.Forms.Button
 End Class
```

[Back to top](#top)
