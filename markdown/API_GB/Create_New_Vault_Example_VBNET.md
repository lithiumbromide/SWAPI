---
title: "Create New Vault Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Create_New_Vault_Example_VBNET.htm"
---

# Create New Vault Example (VB.NET)

This example shows how to:

- Create a new vault.
- Create a new vault view.
- Log into the new vault.
- Get all of the users currently logged into vault views on this machine.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio 2010.
 '    a. Click File > New > Project > Visual Basic > Windows Forms Application.
 '    b. Type CreateNewVault in Name.
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
 ' 4. In the code, substitute the following parameters in IEdmVault11::CreateNewVault
 '    to create MyNewVault on your machine:
 '    * database_server
 '    * sql_sa_password
 ' 5. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Create new vault dialog box.
 '    a. Click Create and log in to MyNewVault.
 '    b. After a few seconds, displays a login dialog.
 '    c. Type Admin's password in Password.
 '    d. Click Log in.
 '       1. MyNewVault is created using the Default configuration in the root
 '          folder of the archive server.
 '       2. A view of MyNewVault, accessible to all users, is created in c:\temp.
 '       3. Admin is logged into MyNewVault.
 '    e. Click Get users logged into all vaults.
  '    f. Displays a dialog with all of the users currently logged into
 '       vault views on this machine.
 '    g. Click OK.
  ' 2. Close the Create new vault dialog box.
  '----------------------------------------------------------------------------

 'Form1.vb

 Imports System.Collections.Generic
 Imports System.Data
 Imports System.Diagnostics
 Imports System.Windows.Forms
 Imports System.ComponentModel
 Imports EPDM.Interop.epdm

 Public Class Form1

     Dim vault1 As IEdmVault5 = New EdmVault5()
     Dim vault2 As IEdmVault13 = DirectCast(vault1, IEdmVault13)
     Dim vaults As String = ""
     Public Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
     End Sub

     Public Sub GetLoggedIn_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GetLoggedIn.Click
         'Get all of the users currently logged into vault views on this machine
         Try
             If vault1 Is Nothing Then
                 MessageBox.Show("Click Log in")
                 Exit Sub
             End If

             Dim userMgr As IEdmUserMgr5
             userMgr = vault2.CreateUtility(EdmUtility.EdmUtil_UserMgr)
             Dim pos As IEdmPos5
             pos = userMgr.GetFirstLoggedInUserPosition(vaults)

             Dim userName As String = ""
             Dim computerName As String = ""
             Dim vaultName As String = ""
             Dim loginTime As Object = Nothing

             Dim message As String
             message = "The following users are logged into vault views:" & vbLf & vbLf

             While Not pos.IsNull
                 userMgr.GetNextLoggedInUser(pos, userName, computerName, vaultName, loginTime)
                 message = message & userName & " (" & computerName & ")" & " logged in to " & vaultName & " at " & loginTime.ToString & vbLf
             End While

             MsgBox(message)

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
         ' Create a new vault and vault view
         Try
             vault1 = New EdmVault5()
             vault2 = DirectCast(vault1, IEdmVault13)

             vault2.CreateNewVault("", "", "", "MyNewVault", "This is my new vault", "", "database_server", "sa", "sql_sa_password", "MyNewVault", 110, "", EdmCreateVaultFlag.EdmCreateVault_UseDefaultAdminPassword, Nothing, "Default")
             vault2.CreateNewVaultView("", "", "", "MyNewVault", "c:\temp", EdmCreateVaultViewFlag.EdmCreateVaultView_SharedView)

             Dim Views As EdmViewInfo() = Nothing
             vault2.GetVaultViews(Views, False)

             For Each View As EdmViewInfo In Views
                 vaults = vaults & View.mbsVaultName & vbLf
             Next

             'Log into the new vault view
             vault2.LoginAuto("MyNewVault", Me.Handle.ToInt32())

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
         Me.GetLoggedIn = New System.Windows.Forms.Button()
         Me.Button1 = New System.Windows.Forms.Button()
         Me.SuspendLayout()
         '
         'GetLoggedIn
         '
         Me.GetLoggedIn.Location = New System.Drawing.Point(31, 71)
         Me.GetLoggedIn.Name = "GetLoggedIn"
         Me.GetLoggedIn.Size = New System.Drawing.Size(167, 23)
         Me.GetLoggedIn.TabIndex = 5
         Me.GetLoggedIn.Text = "Get users logged into all vaults"
         Me.GetLoggedIn.UseVisualStyleBackColor = True
         '
         'Button1
         '
         Me.Button1.Location = New System.Drawing.Point(31, 26)
         Me.Button1.Name = "Button1"
         Me.Button1.Size = New System.Drawing.Size(178, 23)
         Me.Button1.TabIndex = 6
         Me.Button1.Text = "Create and log in to MyNewVault"
         Me.Button1.UseVisualStyleBackColor = True
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(287, 136)
         Me.Controls.Add(Me.Button1)
         Me.Controls.Add(Me.GetLoggedIn)
         Me.Name = "Form1"
         Me.Text = "Create new vault"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Friend WithEvents GetLoggedIn As System.Windows.Forms.Button
     Friend WithEvents Button1 As System.Windows.Forms.Button

 End Class
```

[Back to top](#top)
