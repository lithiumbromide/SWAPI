---
title: "Create User Picture Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Create_User_Picture_Example_VBNET.htm"
---

# Create User Picture Example (VB.NET)

This example shows how to display a user's picture in a form and pop up user information when hovering over a form label.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 '    a. Click File > New > Project > Visual Basic, Windows, Desktop > Windows Forms App.
 '    b. Type CreateUserPicture in Project name.
 '    c. For Location, click ... and navigate to the folder where to create the project.
'      d. Click Next.
'    e. Select Framework.
'    f. Click Create.
'    g. Click Show All Files in the Solution Explorer toolbar and expand
'       Form1.vb in the Solution Explorer.
 '    f. Replace the code in Form1.vb with this code.
 '    g. To create the form, replace the code in Form1.Designer.vb with this code.
 ' 2. Add dependencies and safely pass arrays of structures.
 ' 3. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the Get Admin's picture dialog box.
 ' 2. Select a vault view.
 ' 3. Click Get picture.
  ' 4. Displays a picture of the Admin of the selected vault.
 ' 5. Hover over System Administrator.
 ' 6. Pops up a window with the Admin's information.
  ' 7. Close the Get Admin's picture dialog box.
  '----------------------------------------------------------------------------

 'Form1.vb

 Imports System.Collections.Generic
 Imports System.Data
 Imports System.Diagnostics
 Imports System.Windows.Forms
 Imports System.ComponentModel
 Imports EPDM.Interop.epdm

 Public Class Form1

     Dim mpoImage As IEdmImage

     Public Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
         Dim vault As IEdmVault8 = New EdmVault5
         Dim Views() As EdmViewInfo = {}

         vault.GetVaultViews(Views, False)
         VaultsComboBox.Items.Clear()
         For Each View As EdmViewInfo In Views
             VaultsComboBox.Items.Add(View.mbsVaultName)
         Next
         If VaultsComboBox.Items.Count > 0 Then
             VaultsComboBox.Text = VaultsComboBox.Items(0)
         End If
     End Sub

     Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
         Try

             Dim vault As IEdmVault5
             Dim vault2 As IEdmVault12
             vault = New EdmVault5
             vault2 = vault

             vault.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())

             Dim poUserMgr As IEdmUserMgr8
             poUserMgr = vault2.CreateUtility(EdmUtility.EdmUtil_UserMgr)

             'Create a bounding rectangle for the picture
             Dim oRect As EdmRect
             oRect.mlTop = 10
             oRect.mlLeft = 10
             oRect.mlRight = oRect.mlLeft + 80
             oRect.mlBottom = oRect.mlTop + 100

             'Create the Admin user's image
             Dim poAdmin As IEdmUser10
             poAdmin = poUserMgr.GetUser("Admin")
             mpoImage = poUserMgr.CreateUserPicture(Me.Handle.ToInt32, oRect, poAdmin.ID)

             Label1.Text = poAdmin.FullName

             'Invalidate the window to trigger a call to OnPaintPic
             Me.Invalidate()

         Catch ex As System.Runtime.InteropServices.COMException
                 MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     'Displays the Admin user's picture when the form is repainted
     Private Sub OnPaintPic(ByVal sender As System.Object, ByVal e As System.Windows.Forms.PaintEventArgs) Handles MyBase.Paint
         If Not mpoImage Is Nothing Then
             mpoImage.Paint(e.Graphics.GetHdc())
         End If
     End Sub

     'Called when the user hovers over the form label, Label1
     Private Sub OnMouseHoverName(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Label1.MouseHover

         Dim poVault As IEdmVault12
         poVault = New EdmVault5
         poVault.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())

         Dim poUserMgr As IEdmUserMgr8
         poUserMgr = poVault.CreateUtility(EdmUtility.EdmUtil_UserMgr)

         'Get the screen coordinates of the label that displays the user name
         Dim pnt As System.Drawing.Point
         pnt.X = Label1.Left
         pnt.Y = Label1.Top
         pnt = Me.PointToScreen(pnt)

         'Create the bounding rectangle
         Dim oTrackRect As EdmRect
         oTrackRect.mlTop = pnt.Y
         oTrackRect.mlLeft = pnt.X
         oTrackRect.mlRight = oTrackRect.mlLeft + Label1.Width
         oTrackRect.mlBottom = oTrackRect.mlTop + Label1.Height

         'Display a popup window with the Admin user's information
         poUserMgr.ShowUserPopup(Me.Handle.ToInt32, oTrackRect, Label1.Text)
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
         Me.Button1 = New System.Windows.Forms.Button()
         Me.Label1 = New System.Windows.Forms.Label()
         Me.SuspendLayout()
         '
         'VaultsLabel
         '
         Me.VaultsLabel.AutoSize = True
         Me.VaultsLabel.Location = New System.Drawing.Point(22, 164)
         Me.VaultsLabel.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
         Me.VaultsLabel.Name = "VaultsLabel"
         Me.VaultsLabel.Size = New System.Drawing.Size(91, 13)
         Me.VaultsLabel.TabIndex = 10
         Me.VaultsLabel.Text = "Select vault view:"
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(25, 179)
         Me.VaultsComboBox.Margin = New System.Windows.Forms.Padding(2)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(132, 21)
         Me.VaultsComboBox.TabIndex = 11
         '
         'Button1
         '
         Me.Button1.Location = New System.Drawing.Point(48, 214)
         Me.Button1.Margin = New System.Windows.Forms.Padding(2)
         Me.Button1.Name = "Button1"
         Me.Button1.Size = New System.Drawing.Size(101, 31)
         Me.Button1.TabIndex = 14
         Me.Button1.Text = "Get picture"
         Me.Button1.UseVisualStyleBackColor = True
         '
         'Label1
         '
         Me.Label1.AutoSize = True
         Me.Label1.Location = New System.Drawing.Point(22, 128)
         Me.Label1.Name = "Label1"
         Me.Label1.Size = New System.Drawing.Size(0, 13)
         Me.Label1.TabIndex = 15
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(235, 256)
         Me.Controls.Add(Me.Label1)
         Me.Controls.Add(Me.Button1)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Controls.Add(Me.VaultsLabel)
         Me.Margin = New System.Windows.Forms.Padding(2)
         Me.Name = "Form1"
         Me.Text = "Get Admin's picture"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsLabel As System.Windows.Forms.Label
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents Button1 As System.Windows.Forms.Button
     Friend WithEvents Label1 As System.Windows.Forms.Label

 End Class
```

[Back to top](#top)
