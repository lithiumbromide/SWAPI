---
title: "Traverse Folders and Files in Vault Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Traverse_Folders_and_Files_in_Vault_Example_VBNET.htm"
---

# Traverse Folders and Files in Vault Example (VB.NET)

This example shows how to recursively traverse all of the folders and files in a vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 '  1. Start Microsoft Visual Studio.
 '  2. Click File > New > Project > Dropdowns: Visual Basic, Windows, Desktop > Windows Forms App. Click Next.
 '  3. Type TraverseFilesFolders in Project name.
 '  4. In Location click ... and navigate to the folder where to create the project. Click Next.
 '  5. Select a supported .NET Framework installed on your computer. Click Create.
 '  6. Replace the code in Form1.vb with this code.
 '  7. Replace the code in Form1.Designer.vb with this code.
 '  8. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 '     name in the Solution Explorer, click Add > Project Reference, click Browse,
 '     navigate to the top folder of your SOLIDWORKS PDM Professional installation,
 '     locate and select EPDM.Interop.epdm.dll). Click OK.
 '  9. Click Show All Files in the tool bar. Right-click Dependencies > Assemblies >
'     EPDM.Interop.epdm, click Properties, and set
 '     Embed Interop Types to No to handle methods that pass arrays of
 '     structures.
 ' 10. Ensure that the vault contains one or more checked-out files.
 ' 11. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays a Traverse Folders and Files dialog.
 ' 2. Select a vault.
 ' 3. Click Log in, get client log, get checked-out files in vault.
 ' 4. Displays a message box with the vault type.
 ' 5. Click OK.
 ' 6. Populates Client log and Checked-out files.
 ' 7. Close the dialog.
 '----------------------------------------------------------------------------

'Form1.vb

 Imports EPDM.Interop.epdm

 Public Class TraverseFilesFolders

     Dim vault As IEdmVault20
     Public Sub TraverseFilesFolders_Load(
 ByVal sender As System.Object,
 ByVal e As System.EventArgs) _
       Handles MyBase.Load

         Try

             Dim Views() As EdmViewInfo = Nothing
             Dim vault5 As IEdmVault5 = New EdmVault5()
             vault = DirectCast(vault5, IEdmVault20)

             vault.GetVaultViews(Views, False)

             VaultsComboBox.Items.Clear()
             For Each View As EdmViewInfo In Views
                 VaultsComboBox.Items.Add(View.mbsVaultName)
             Next
             If VaultsComboBox.Items.Count > 0 Then
                 VaultsComboBox.Text = VaultsComboBox.Items(0)
             End If

         Catch ex As Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" +
 ex.ErrorCode.ToString("X") + vbCrLf +
 ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub TraverseFoldersButton_Click(
 ByVal sender As System.Object,
 ByVal e As System.EventArgs) _
       Handles TraverseFoldersButton.Click

         Try

             'Log into selected vault as the current user
             vault.LoginAuto(VaultsComboBox.Text,
 Me.Handle.ToInt32())

             MessageBox.Show(vault.GetVaultType().ToString(), "Vault type")

             Dim log As String = Nothing
             vault.GetClientLog(log)
             TextBox1.Text = log

             TraverseFolder(vault.RootFolder)

         Catch ex As Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" +
 ex.ErrorCode.ToString("X") + vbCrLf +
 ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Public Sub TraverseFolder(
 ByVal CurFolder As IEdmFolder5)

         Try

             'Enumerate the files in the folder
             Dim FilePos As IEdmPos5
             FilePos = CurFolder.GetFirstFilePosition
             Dim file As IEdmFile5
             While Not FilePos.IsNull
                 file = CurFolder.GetNextFile(FilePos)
                 'Get its checked out status
                 If file.IsLocked Then
                     ListBox2.Items.Add(file.LockPath)
                 End If
             End While

             'Enumerate the subfolders in the folder
             Dim FolderPos As IEdmPos5
             FolderPos = CurFolder.GetFirstSubFolderPosition
             While Not FolderPos.IsNull
                 Dim SubFolder As IEdmFolder5
                 SubFolder = CurFolder.GetNextSubFolder _
                   (FolderPos)
                 TraverseFolder(SubFolder)
             End While

         Catch ex As Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" +
 ex.ErrorCode.ToString("X") + vbCrLf +
 ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

 End Class
```

```vb
Back to top
```

```vb
'Form1.Designer.vb
```

```vb
 <Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
 Partial Class TraverseFilesFolders
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
         Me.Label1 = New System.Windows.Forms.Label()
         Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
         Me.TraverseFoldersButton = New System.Windows.Forms.Button()
         Me.Label2 = New System.Windows.Forms.Label()
         Me.Label3 = New System.Windows.Forms.Label()
         Me.ListBox2 = New System.Windows.Forms.ListBox()
         Me.TextBox1 = New System.Windows.Forms.TextBox()
         Me.SuspendLayout()
         '
         'Label1
         '
         Me.Label1.AutoSize = True
         Me.Label1.Location = New System.Drawing.Point(22, 34)
         Me.Label1.Name = "Label1"
         Me.Label1.Size = New System.Drawing.Size(91, 13)
         Me.Label1.TabIndex = 0
         Me.Label1.Text = "Select vault view:"
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(25, 50)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(121, 21)
         Me.VaultsComboBox.TabIndex = 1
         '
         'TraverseFoldersButton
         '
         Me.TraverseFoldersButton.Location = New System.Drawing.Point(25, 89)
         Me.TraverseFoldersButton.Name = "TraverseFoldersButton"
         Me.TraverseFoldersButton.Size = New System.Drawing.Size(212, 34)
         Me.TraverseFoldersButton.TabIndex = 2
         Me.TraverseFoldersButton.Text = "Log in, get client log, get checked-out files in vault"
         Me.TraverseFoldersButton.UseVisualStyleBackColor = True
         '
         'Label2
         '
         Me.Label2.AutoSize = True
         Me.Label2.Location = New System.Drawing.Point(22, 144)
         Me.Label2.Name = "Label2"
         Me.Label2.Size = New System.Drawing.Size(53, 13)
         Me.Label2.TabIndex = 4
         Me.Label2.Text = "Client log:"
         '
         'Label3
         '
         Me.Label3.AutoSize = True
         Me.Label3.Location = New System.Drawing.Point(24, 310)
         Me.Label3.Name = "Label3"
         Me.Label3.Size = New System.Drawing.Size(89, 13)
         Me.Label3.TabIndex = 5
         Me.Label3.Text = "Checked-out files:"
         '
         'ListBox2
         '
         Me.ListBox2.FormattingEnabled = True
         Me.ListBox2.HorizontalScrollbar = True
         Me.ListBox2.Location = New System.Drawing.Point(27, 326)
         Me.ListBox2.Name = "ListBox2"
         Me.ListBox2.ScrollAlwaysVisible = True
         Me.ListBox2.SelectionMode = System.Windows.Forms.SelectionMode.None
         Me.ListBox2.Size = New System.Drawing.Size(210, 160)
         Me.ListBox2.TabIndex = 6
         '
         'TextBox1
         '
         Me.TextBox1.Location = New System.Drawing.Point(25, 160)
         Me.TextBox1.Multiline = True
         Me.TextBox1.Name = "TextBox1"
         Me.TextBox1.ScrollBars = System.Windows.Forms.ScrollBars.Both
         Me.TextBox1.Size = New System.Drawing.Size(212, 147)
         Me.TextBox1.TabIndex = 7
         '
         'TraverseFilesFolders
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(258, 509)
         Me.Controls.Add(Me.TextBox1)
         Me.Controls.Add(Me.ListBox2)
         Me.Controls.Add(Me.Label3)
         Me.Controls.Add(Me.Label2)
         Me.Controls.Add(Me.TraverseFoldersButton)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.Label1)
         Me.Name = "TraverseFilesFolders"
         Me.Text = "Traverse Folders and Files"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents Label1 As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents TraverseFoldersButton As System.Windows.Forms.Button
     Friend WithEvents Label2 As Label
     Friend WithEvents Label3 As Label
     Friend WithEvents ListBox2 As ListBox
     Friend WithEvents TextBox1 As TextBox
 End Class
```

```
Back to top
```
