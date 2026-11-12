---
title: "Check Out and Copy File Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Check_Out_and_Copy_File_Example_VBNET.htm"
---

# Check Out and Copy File Example (VB.NET)

This example shows how to find a vault from a file path, check out the file from the vault, and copy the file to another location.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio 2010.
 '    a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '    b. Type GetVaultFromFilePath in Name.
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
 ' 4. Ensure that c:\temp exists.
 ' 5. Ensure that at least one file is checked into a vault.
 ' 6. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Check out and copy a file dialog box.
 ' 2. Click Check out and copy a file.
 ' 3. In the Open dialog, navigate to and click a file checked into a vault.
 ' 4. Click Open.
  '    a. Gets the vault from the selected file's path.
 '    b. Logs into the vault.
 '    c. Checks out the file.
 '    d. Displays a message box confirming the check-out.
 '    e. Click OK.
 '    f. Copies the selected file to c:\temp.
 '    g. Displays a message box confirming the copy.
 '    h. Click OK.
  ' 5. Close the Check out and copy a file dialog box.
  '----------------------------------------------------------------------------

 'Form1.vb

 Imports System.Collections.Generic
 Imports System.Data
 Imports System.Diagnostics
 Imports System.Windows.Forms
 Imports System.ComponentModel
 Imports EPDM.Interop.epdm

 Public Class Form1

     Public Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
     End Sub

     Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
         Try
             Dim vault As EdmVault5
             vault = New EdmVault5

             Dim strList As IEdmStrLst5
             strList = vault.BrowseForFile(Me.Handle.ToInt32())

             Dim pos As IEdmPos5
             pos = strList.GetHeadPosition()
             Dim filePath As String = strList.GetNext(pos)

             'Get name of the vault in which the file is located
             Dim VaultName As String
             VaultName = vault.GetVaultNameFromPath(filePath)

             'Log into the vault
             vault.LoginAuto(VaultName, Me.Handle.ToInt32())

             'Get the interface to the file and its parent folder
             Dim file As IEdmFile5
             Dim folder As IEdmFolder5 = Nothing
             file = vault.GetFileFromPath(filePath, folder)

             If file Is Nothing Then
                 MessageBox.Show("The file is not in the vault " + VaultName + ".")
             Else
                 'Check out the file
                 file.LockFile(folder.ID, Me.Handle.ToInt32())
                 MessageBox.Show("Checked out " & file.Name & " in vault " + VaultName + ".")

                 'Copy the file
                 Dim verEnum As IEdmEnumeratorVersion5
                 verEnum = file
                 Dim Version As Integer
                 Version = file.GetLocalVersionNo(folder.ID)
                 Dim ver As IEdmVersion5
                 ver = verEnum.GetVersion(Version)
                 ver.GetFileCopy(Me.Handle.ToInt32(), "c:\temp\")
                 MessageBox.Show("Copied " & file.Name & " to c:\temp.")
             End If

         Catch ex As System.Runtime.InteropServices.COMException
             If ex.ErrorCode = &H8004022B Then
                 MessageBox.Show("The selected file is not located in a file vault.")
             Else
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
             End If
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

     Private components As System.ComponentModel.IContainer = Nothing

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
         Me.Button1 = New System.Windows.Forms.Button()
         Me.SuspendLayout()
         '
         'Button1
         '
         Me.Button1.Location = New System.Drawing.Point(31, 26)
         Me.Button1.Name = "Button1"
         Me.Button1.Size = New System.Drawing.Size(150, 23)
         Me.Button1.TabIndex = 6
         Me.Button1.Text = "Check out and copy a file"
         Me.Button1.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(263, 87)
         Me.Controls.Add(Me.Button1)
         Me.Name = "Form1"
         Me.Text = "Check out and copy a file"
         Me.ResumeLayout(False)

     End Sub

 #End Region

     Friend WithEvents Button1 As System.Windows.Forms.Button

 End Class
```

[Back to top](#top)
