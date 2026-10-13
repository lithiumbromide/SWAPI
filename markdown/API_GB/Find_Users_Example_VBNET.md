---
title: "Find Users Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Find_Users_Example_VBNET.htm"
---

# Find Users Example (VB.NET)

This example shows how to find users in the vault.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
'  1. Start Microsoft Visual Studio 2010.
'     a. Click File > New > Project > Visual Basic > Windows Forms Application.
'     b. Type FindUser in Name.
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
'  4. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays the Find Users dialog box.
'     a. Select a vault view.
'     b. In Full name contains, type a substring of the full name of a
'        user that exists in the vault.
'     c. Click Find Users.
'        A message box confirms the substring typed in Postconditions
'        step 1b.
'     d. Click OK.
'        Displays a Search for users dialog.
'     e. Click Find.
'        Displays a Search for users dialog with results.
'     f. Click the first row.
'     g. Click Select.
'        * Displays a message box with the updated user information.
'        * The selected user's phone and website information are updated.
'     h. Click OK.
'  2. Updates the Find Users dialog box with the full name and picture, if
'     it exists, of the last user found whose full name contains the substring
'     typed in Postconditions step 1b.
'  3. Close the Find Users dialog box.
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

     Private Sub FindUsers_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles FindUsers.Click

         Try
             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             'Get the user search interface
             Dim poFind As IEdmFindUser
             poFind = vault2.CreateUtility(EdmUtility.EdmUtil_FindUser)

             'Search for a user with specified text in the full user name
             poFind.SetPropt(EdmFindUserProp.Edmfup_FullName, Me.TextBox1.Text)
             Dim val As String
             val = poFind.GetPropt(EdmFindUserProp.Edmfup_FullName)
             MessageBox.Show("Find users whose full names contain " & """" & val & """")

             poFind.ShowFindUI(Me.Handle.ToInt32(), True, "Search for users")

             Dim poResult As IEdmEnum
             poResult = poFind.Result
             Dim str As String = "Found " & poResult.Count.ToString & " users with full names containing, " & """" & Me.TextBox1.Text & """" & ":"

             Dim oImg As System.Drawing.Image
             Dim poUser As IEdmUser10
             Dim UserInfo As EdmUserDataEx = New EdmUserDataEx()
             UserInfo.mlEdmUserDataExFlags = EdmUserDataExFlag.Edmudex_All

             For Each element In poResult
                 poUser = element

                 'Get user's information
                 poUser.GetUserDataEx(UserInfo)

                 'Update user's information
                 UserInfo.mbsPhone = "123456789"
                 UserInfo.mbsWebSite1 = "http://www.solidworks.com"
                 UserInfo.mbsWebSite2 = "https://www.facebook.com/solidworks"
                 poUser.SetUserDataEx(UserInfo)

                 str = str & vbLf & "Full name: " & UserInfo.mbsCompleteName & ", Phone: " & UserInfo.mbsPhone & ", WebSite1: " & UserInfo.mbsWebSite1 & ", Website2: " & UserInfo.mbsWebSite2
             Next

             MessageBox.Show(str)

             'Display the picture, if available, of the last user found
             If Not UserInfo.mbsPicturePath = Nothing Then
                 Me.TextBox2.Text = UserInfo.mbsCompleteName
                 oImg = System.Drawing.Bitmap.FromFile(UserInfo.mbsPicturePath)
                 Me.CreateGraphics().DrawImage(oImg, 40, 220)
             End If

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

```vb
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
         Me.FindUsers = New System.Windows.Forms.Button()
         Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
         Me.Label1 = New System.Windows.Forms.Label()
         Me.Label2 = New System.Windows.Forms.Label()
         Me.TextBox1 = New System.Windows.Forms.TextBox()
         Me.Label3 = New System.Windows.Forms.Label()
         Me.TextBox2 = New System.Windows.Forms.TextBox()
         Me.SuspendLayout()
         '
         'FindUsers
         '
         Me.FindUsers.Location = New System.Drawing.Point(72, 136)
         Me.FindUsers.Name = "FindUsers"
         Me.FindUsers.Size = New System.Drawing.Size(66, 23)
         Me.FindUsers.TabIndex = 0
         Me.FindUsers.Text = "Find Users"
         Me.FindUsers.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
         Me.FindUsers.UseVisualStyleBackColor = True
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
         'Label2
         '
         Me.Label2.AutoSize = True
         Me.Label2.Location = New System.Drawing.Point(27, 77)
         Me.Label2.Name = "Label2"
         Me.Label2.Size = New System.Drawing.Size(104, 13)
         Me.Label2.TabIndex = 3
         Me.Label2.Text = "Full name contains:"
         '
         'TextBox1
         '
         Me.TextBox1.Location = New System.Drawing.Point(32, 93)
         Me.TextBox1.Name = "TextBox1"
         Me.TextBox1.Size = New System.Drawing.Size(167, 20)
         Me.TextBox1.TabIndex = 4
         '
         'Label3
         '
         Me.Label3.AutoSize = True
         Me.Label3.Location = New System.Drawing.Point(29, 172)
         Me.Label3.Name = "Label3"
         Me.Label3.Size = New System.Drawing.Size(83, 13)
         Me.Label3.TabIndex = 6
         Me.Label3.Text = "Last user found:"
         '
         'TextBox2
         '
         Me.TextBox2.Location = New System.Drawing.Point(30, 188)
         Me.TextBox2.Name = "TextBox2"
         Me.TextBox2.Size = New System.Drawing.Size(169, 20)
         Me.TextBox2.TabIndex = 7
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(406, 447)
         Me.Controls.Add(Me.TextBox2)
         Me.Controls.Add(Me.Label3)
         Me.Controls.Add(Me.TextBox1)
         Me.Controls.Add(Me.Label2)
         Me.Controls.Add(Me.Label1)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.FindUsers)
         Me.Name = "Form1"
         Me.Text = "Find Users"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents FindUsers As System.Windows.Forms.Button
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents Label1 As System.Windows.Forms.Label
     Friend WithEvents Label2 As System.Windows.Forms.Label
     Friend WithEvents TextBox1 As System.Windows.Forms.TextBox
     Friend WithEvents Label3 As System.Windows.Forms.Label
     Friend WithEvents TextBox2 As System.Windows.Forms.TextBox

 End Class
```

```
Back to top
```
