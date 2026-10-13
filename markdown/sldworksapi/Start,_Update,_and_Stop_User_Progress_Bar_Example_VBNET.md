---
title: "Start, Update, and Stop Progress Indicator Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Start,_Update,_and_Stop_User_Progress_Bar_Example_VBNET.htm"
---

# Start, Update, and Stop Progress Indicator Example (VB.NET)

This example shows how to create, start, update, and stop a progress indicator on the system task bar.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VB.NET macro in SOLIDWORKS Design .
 ' 2. Right-click the macro project name in the Project Explorer and click
 '    Add > Windows Form.
 ' 3. Click Add.
 ' 4. Modify Form1.vb [Design] to look like this:

' 5. Copy  Forms - Form1  into Form1.vb.
 ' 6. Modify control_name in each control_name_Click subroutine to
 '    match your form.
 ' 7. Copy SolidWorksMacro into SolidWorksMacro.vb.
 ' 8. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Shows a dialog box.
 ' 2. Click Start.
 '    * Displays a progress indicator on the SOLIDWORKS Design icon on the
 '      system taskbar.
 '    * Increments the progress indicator to 100% completion.
 ' 3. Click Update repeatedly to increment the progress indicator in steps of
 '    10.
 ' 4. Inspect the Immediate window to see the return code after each update.
 ' 5. Type a new title and click Update Title to change the progress indicator
 '    title.
 ' 6. Click Stop to remove the progress indicator from SOLIDWORKS Design.
 ' 7. Click Exit to close the dialog box.
 ' ---------------------------------------------------------------------------
```

#### Forms - Form1

```vb
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Public Class Form1
     Dim pb As UserProgressBar
     Dim Position As Integer
     Dim lRet As Integer
     Dim retVal As Boolean
     Dim boolstatus As Boolean
     Public swApp As SldWorks

     Public Sub cmdExit_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cmdExit.Click
         Me.Close()
     End Sub

     Public Sub cmdPBTitle_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cmdPBTitle.Click
         retVal = pb.UpdateTitle(TextBox1.Text)
     End Sub

     Public Sub cmdStartPB_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cmdStartPB.Click
         boolstatus = pb.Start(0, 160, "Status")
         Do While Not (Position = 160)
             Position = Position + 10
             lRet = pb.UpdateProgress(Position)
         Loop
         Position = 0
     End Sub

     Public Sub cmdStopPB_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cmdStopPB.Click
         pb.End()
     End Sub

     Public Sub Form1_Initialize(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Me.Load
         swApp = CType(System.Runtime.InteropServices.Marshal.GetActiveObject("SldWorks.Application"), SldWorks)
         retVal = swApp.GetUserProgressBar(pb)
     End Sub

     Public Sub cmdUpdatePB_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cmdUpdatePB.Click
         Position = Position + 10
         If (Position = 160) Then Position = 0
         lRet = pb.UpdateProgress(Position)
         If lRet <> 2 Then
             Debug.Print(" Result " & lRet)
         Else
             MsgBox(" User pressed Esc to cancel ", vbInformation, " API")
             pb.End()
         End If
     End Sub

     Private Sub TextBox1_TextChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles TextBox1.TextChanged
     End Sub

 End Class
```

[Back to top](#Top)

#### SolidWorksMacro

```vb
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro
     Dim aForm As Windows.Forms.Form
     Public Sub main()
         aForm = New Form1
         aForm.ShowDialog()
     End Sub

     Public swApp As SldWorks

 End Class
```

[Back to top](#Top)
