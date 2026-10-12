---
title: "Get and Set Dictionary Key-Value Pairs Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Get_and_Set_Key_Value_Pairs_Example_VBNET.htm"
---

# Get and Set Dictionary Key-Value Pairs Example (VB.NET)

This example shows how to access key-value pairs in a vault dictionary.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Start Microsoft Visual Studio 2010.
'    a. Click File > New > Project > Visual Basic > Windows Forms Application.
'    b. Type TestDictionary in Name.
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
' 4. Click Debug > Start Debugging or press F5.
'
' Postconditions:
'  1. Displays a dialog.
'  2. Select a vault view.
'  3. Click Substring in key.
'  4. Click Get key-value pairs.
'     a. Displays a message box with all key-value pairs in the dictionary where
'        string key contains "at".
'     b. Click OK.
'  5. Click Integer key range.
'  6. Click Get key-value pairs.
'     a. Displays a message box with all key-value pairs in the dictionary where
'        integer keys are in the range, 13-88.
'     b. Click OK.
'  7. Click Substring in values of all integer keys.
'  8. Click Get key-value pairs.
'     a. Displays a message box with all key-value pairs in the dictionary where
'        value contains "three".
'     b. Click OK.
'  9. Click Specific integer key.
' 10. Click Get key-value pairs.
'     a. Displays a message box with the value for key, 77.
'     b. Click OK.
' 11. Click Enumeration of all integer keys.
' 12. Click Get key-value pairs.
'     a. Displays a message box with all integer key-value pairs in the dictionary.
'     b. Click OK.
' 13. Click Delete a key-value pair.
'     a. Displays a message box notifying that key, 2, is removed.
'     b. Click OK.
' 14. Click Create a key-value pair.
'     a. Displays a message box notifying that key, 2, is created.
'     b. Click OK.
' 15. Close the dialog.
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
     Dim dic As IEdmDictionary5
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

     Private Sub Button5_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button5.Click
         'Delete key-value pair clicked
         Try
             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             dic = vault.GetDictionary("MyDictionary", True)
             'Add some values
             dic.LongSetAt(2, "two")
             dic.LongSetAt(15, "fifteen")
             dic.LongSetAt(300, "three hundred")
             dic.LongSetAt(77, "seventy-seven")

             dic.LongRemoveAt(2)
             MessageBox.Show("Key 2 removed.")
             dic.RemoveDictionary()

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
         'Get key-value pairs clicked
         Try
             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             If Me.RadioButton1.Checked Then
                 'Get key-value pairs by substring in key

                 dic = vault.GetDictionary("MyDictionary", True)

                 'Add some values
                 dic.StringSetAt("Cat", "Socks")
                 dic.StringSetAt("Dog", "Milou")
                 dic.StringSetAt("Human", "Attila")
                 dic.StringSetAt("At last", "Last value")

                 'Find all keys containing the text, "at"
                 Dim key As String = ""
                 Dim value As String = ""
                 Dim message As String
                 message = "Keys with 'at' in them:" + vbLf
                 Dim pos As IEdmPos5
                 pos = dic.StringFindKeys("at")
                 While Not pos.IsNull
                     dic.StringGetNextAssoc(pos, key, value)
                     message = message + "<" + key + "> = <" + value + ">" + vbLf
                 End While

                 'Show a message and delete the dictionary
                 MsgBox(message)
                 dic.RemoveDictionary()

             ElseIf Me.RadioButton2.Checked Then
                 'Get key-value pairs by integer key range

                 dic = vault.GetDictionary("MyDictionary", True)

                 'Add some values
                 dic.LongSetAt(2, "two")
                 dic.LongSetAt(15, "fifteen")
                 dic.LongSetAt(300, "three hundred")
                 dic.LongSetAt(77, "seventy-seven")

                 'Find all keys in the range, 13-88
                 Dim key As Long
                 Dim value As String = ""
                 Dim message As String
                 message = "Keys in the range 13-88:" + vbLf
                 Dim pos As IEdmPos5
                 pos = dic.LongFindKeys(13, 88)
                 While Not pos.IsNull
                     dic.LongGetNextAssoc(pos, key, value)
                     message = message + "<" + Str(key) + "> = <" + value + ">" + vbLf
                 End While

                 'Show a message and delete the dictionary
                 MsgBox(message)
                 dic.RemoveDictionary()

             ElseIf Me.RadioButton3.Checked Then
                 'Get key-value pairs by substring in values of integer keys

                 dic = vault.GetDictionary("MyDictionary", True)
                 'Add some values
                 dic.LongSetAt(2, "two")
                 dic.LongSetAt(15, "fifteen")
                 dic.LongSetAt(300, "three hundred")
                 dic.LongSetAt(77, "seventy-seven")

                 Dim bsValueSubString As String = "three"
                 Dim aPos As IEdmPos5
                 Dim plRetKey As Integer
                 Dim pbsRetValue As String = ""
                 aPos = dic.LongFindValues(bsValueSubString)
                 While Not aPos.IsNull
                     dic.LongGetNextAssoc(aPos, plRetKey, pbsRetValue)
                     MessageBox.Show("Key-value pair with " & """" & bsValueSubString & """" & " in value: " & vbLf & "<" & plRetKey & "> = <" & pbsRetValue & ">")
                 End While
                 dic.RemoveDictionary()

             ElseIf Me.RadioButton4.Checked Then
                 'Get key-value pairs by specific integer key

                 dic = vault.GetDictionary("MyDictionary", True)
                 'Add some values
                 dic.LongSetAt(2, "two")
                 dic.LongSetAt(15, "fifteen")
                 dic.LongSetAt(300, "three hundred")
                 dic.LongSetAt(77, "seventy-seven")

                 Dim pbsRetValue As String = ""
                 dic.LongGetAt(77, pbsRetValue)
                 MessageBox.Show("Value for key 77: " & pbsRetValue)
                 dic.RemoveDictionary()

             ElseIf Me.RadioButton5.Checked Then
                 'Get key-value pairs by enumeration of all integer keys

                 dic = vault.GetDictionary("MyDictionary", True)
                 'Add some values
                 dic.LongSetAt(2, "two")
                 dic.LongSetAt(15, "fifteen")
                 dic.LongSetAt(300, "three hundred")
                 dic.LongSetAt(77, "seventy-seven")

                 Dim msg As String
                 Dim key As Long
                 Dim value As String = ""

                 msg = "Integer keys in dictionary:" + vbLf

                 Dim pos As IEdmPos5
                 pos = dic.LongGetFirstPosition
                 While Not pos.IsNull
                     dic.LongGetNextAssoc(pos, key, value)
                     msg = msg + "<" + Str(key) + "> = <" + value + ">" + vbLf
                 End While
                 MsgBox(msg)
                 dic.RemoveDictionary()

             Else
                 MessageBox.Show("Select how to get key-value pairs.")

             End If

         Catch ex As System.Runtime.InteropServices.COMException
             MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MessageBox.Show(ex.Message)
         End Try
     End Sub

     Private Sub Button7_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button7.Click
         'Create key-value pair clicked
         Try
             Dim vault2 As IEdmVault7 = Nothing
             If vault1 Is Nothing Then
                 vault1 = New EdmVault5()
             End If
             vault2 = DirectCast(vault1, IEdmVault7)

             If Not vault1.IsLoggedIn Then
                 vault1.LoginAuto(VaultsComboBox.Text, Me.Handle.ToInt32())
             End If

             Dim pbsRetValue As String = ""

             dic = vault.GetDictionary("MyDictionary", True)
             dic.LongTestAndSetAt(2, "Two")
             dic.LongGetAt(2, pbsRetValue)
             MessageBox.Show("Created:" & vbLf & "<2> = <" & pbsRetValue & ">")
             dic.RemoveDictionary()
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
         Me.VaultsComboBox = New System.Windows.Forms.ComboBox()
         Me.Label1 = New System.Windows.Forms.Label()
         Me.Button5 = New System.Windows.Forms.Button()
         Me.Button7 = New System.Windows.Forms.Button()
         Me.RadioButton1 = New System.Windows.Forms.RadioButton()
         Me.RadioButton2 = New System.Windows.Forms.RadioButton()
         Me.RadioButton3 = New System.Windows.Forms.RadioButton()
         Me.RadioButton4 = New System.Windows.Forms.RadioButton()
         Me.RadioButton5 = New System.Windows.Forms.RadioButton()
         Me.Button1 = New System.Windows.Forms.Button()
         Me.GroupBox1 = New System.Windows.Forms.GroupBox()
         Me.GroupBox1.SuspendLayout()
         Me.SuspendLayout()
         '
         'VaultsComboBox
         '
         Me.VaultsComboBox.FormattingEnabled = True
         Me.VaultsComboBox.Location = New System.Drawing.Point(20, 39)
         Me.VaultsComboBox.Name = "VaultsComboBox"
         Me.VaultsComboBox.Size = New System.Drawing.Size(169, 21)
         Me.VaultsComboBox.TabIndex = 1
         '
         'Label1
         '
         Me.Label1.AutoSize = True
         Me.Label1.Location = New System.Drawing.Point(19, 23)
         Me.Label1.Name = "Label1"
         Me.Label1.Size = New System.Drawing.Size(91, 13)
         Me.Label1.TabIndex = 2
         Me.Label1.Text = "Select vault view:"
         '
         'Button5
         '
         Me.Button5.Location = New System.Drawing.Point(40, 272)
         Me.Button5.Name = "Button5"
         Me.Button5.Size = New System.Drawing.Size(132, 23)
         Me.Button5.TabIndex = 7
         Me.Button5.Text = "Delete a key-value pair"
         Me.Button5.UseVisualStyleBackColor = True
         '
         'Button7
         '
         Me.Button7.Location = New System.Drawing.Point(39, 312)
         Me.Button7.Name = "Button7"
         Me.Button7.Size = New System.Drawing.Size(132, 23)
         Me.Button7.TabIndex = 9
         Me.Button7.Text = "Create a key-value pair"
         Me.Button7.UseVisualStyleBackColor = True
         '
         'RadioButton1
         '
         Me.RadioButton1.AutoSize = True
         Me.RadioButton1.Location = New System.Drawing.Point(30, 19)
         Me.RadioButton1.Name = "RadioButton1"
         Me.RadioButton1.Size = New System.Drawing.Size(100, 17)
         Me.RadioButton1.TabIndex = 11
         Me.RadioButton1.Text = "Substring in key"
         Me.RadioButton1.UseVisualStyleBackColor = True
         '
         'RadioButton2
         '
         Me.RadioButton2.AutoSize = True
         Me.RadioButton2.Location = New System.Drawing.Point(30, 42)
         Me.RadioButton2.Name = "RadioButton2"
         Me.RadioButton2.Size = New System.Drawing.Size(108, 17)
         Me.RadioButton2.TabIndex = 12
         Me.RadioButton2.TabStop = True
         Me.RadioButton2.Text = "Integer key range"
         Me.RadioButton2.UseVisualStyleBackColor = True
         '
         'RadioButton3
         '
         Me.RadioButton3.AutoSize = True
         Me.RadioButton3.Location = New System.Drawing.Point(29, 65)
         Me.RadioButton3.Name = "RadioButton3"
         Me.RadioButton3.Size = New System.Drawing.Size(199, 17)
         Me.RadioButton3.TabIndex = 13
         Me.RadioButton3.TabStop = True
         Me.RadioButton3.Text = "Substring in values of all integer keys"
         Me.RadioButton3.UseVisualStyleBackColor = True
         '
         'RadioButton4
         '
         Me.RadioButton4.AutoSize = True
         Me.RadioButton4.Location = New System.Drawing.Point(30, 88)
         Me.RadioButton4.Name = "RadioButton4"
         Me.RadioButton4.Size = New System.Drawing.Size(118, 17)
         Me.RadioButton4.TabIndex = 14
         Me.RadioButton4.TabStop = True
         Me.RadioButton4.Text = "Specific integer key"
         Me.RadioButton4.UseVisualStyleBackColor = True
         '
         'RadioButton5
         '
         Me.RadioButton5.AutoSize = True
         Me.RadioButton5.Location = New System.Drawing.Point(30, 111)
         Me.RadioButton5.Name = "RadioButton5"
         Me.RadioButton5.Size = New System.Drawing.Size(169, 17)
         Me.RadioButton5.TabIndex = 15
         Me.RadioButton5.TabStop = True
         Me.RadioButton5.Text = "Enumeration of all integer keys"
         Me.RadioButton5.UseVisualStyleBackColor = True
         '
         'Button1
         '
         Me.Button1.Location = New System.Drawing.Point(30, 143)
         Me.Button1.Name = "Button1"
         Me.Button1.Size = New System.Drawing.Size(132, 23)
         Me.Button1.TabIndex = 16
         Me.Button1.Text = "Get key-value pairs"
         Me.Button1.UseVisualStyleBackColor = True
         '
         'GroupBox1
         '
         Me.GroupBox1.Controls.Add(Me.Button1)
         Me.GroupBox1.Controls.Add(Me.RadioButton5)
         Me.GroupBox1.Controls.Add(Me.RadioButton4)
         Me.GroupBox1.Controls.Add(Me.RadioButton3)
         Me.GroupBox1.Controls.Add(Me.RadioButton2)
         Me.GroupBox1.Controls.Add(Me.RadioButton1)
         Me.GroupBox1.Location = New System.Drawing.Point(10, 69)
         Me.GroupBox1.Name = "GroupBox1"
         Me.GroupBox1.Size = New System.Drawing.Size(249, 181)
         Me.GroupBox1.TabIndex = 17
         Me.GroupBox1.TabStop = False
         Me.GroupBox1.Text = "Get key-value pairs by:"
         '
         'Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(271, 366)
         Me.Controls.Add(Me.GroupBox1)
         Me.Controls.Add(Me.Button7)
         Me.Controls.Add(Me.Button5)
         Me.Controls.Add(Me.Label1)
         Me.Controls.Add(Me.VaultsComboBox)
         Me.Name = "Form1"
         Me.Text = "Dictionary Test"
         Me.GroupBox1.ResumeLayout(False)
         Me.GroupBox1.PerformLayout()
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub
     Friend WithEvents VaultsComboBox As System.Windows.Forms.ComboBox
     Friend WithEvents Label1 As System.Windows.Forms.Label
     Friend WithEvents Button5 As System.Windows.Forms.Button
     Friend WithEvents Button7 As System.Windows.Forms.Button
     Friend WithEvents RadioButton1 As System.Windows.Forms.RadioButton
     Friend WithEvents RadioButton2 As System.Windows.Forms.RadioButton
     Friend WithEvents RadioButton3 As System.Windows.Forms.RadioButton
     Friend WithEvents RadioButton4 As System.Windows.Forms.RadioButton
     Friend WithEvents RadioButton5 As System.Windows.Forms.RadioButton
     Friend WithEvents Button1 As System.Windows.Forms.Button
     Friend WithEvents GroupBox1 As System.Windows.Forms.GroupBox

 End Class
```

```
Back to top
```
