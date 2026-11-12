---
title: "Start, Update, and Stop Progress Indicator Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Start,_Update,_and_Stop_User_Progress_Indicator_Example_VB.htm"
---

# Start, Update, and Stop Progress Indicator Example (VBA)

This example shows how to create, start, update, and stop a progress indicator on the status bar.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VBA macro in SOLIDWORKS Design.
 ' 2. Right-click the macro project name in the Project Explorer and click
 '    Insert > UserForm.
 ' 3. Modify UserForm1 (UserForm) to look like this:

' 4. Copy Forms - UserForm1  into UserForm1 (Code).
 ' 5. Modify control_name in each control_name_Click subroutine to
 '    match your form.
 ' 6. Right-click the macro project name and click Insert > Module.
 ' 7. Copy Modules into the new module.
 ' 8. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Shows a dialog box.
 ' 2. Click Start.
 '    * Displays a progress indicator on the SOLIDWORKS Design status bar.
 '    * Increments the progress indicator to 100% completion.
 ' 3. Click Update repeatedly to increment the progress indicator in steps of
 '    10.
 ' 4. Inspect the Immediate window to see the return code after each update.
 ' 5. Type a new title and click Update Title to change the progress indicator
 '    title.
 ' 6. Click Stop to remove the progress indicator from the SOLIDWORKS Design status bar.
 ' 7. Click Exit to close the dialog box.
 ' ---------------------------------------------------------------------------
```

#### Forms - UserForm1

```vb
Dim swApp As SldWorks.SldWorks
 Dim pb As SldWorks.UserProgressBar
 Dim Position As Long
 Dim lRet As Long
 Dim retVal As Boolean
 Dim boolstatus As Boolean

Public Sub cmdExit_Click()
    Unload Me
End Sub

Public Sub cmdPBTitle_Click()
    retVal = pb.UpdateTitle(TextBox1.Text)
End Sub

Public Sub cmdStartPB_Click()
    boolstatus = pb.Start(0, 160, "Status")
     Do While Not (Position = 160)
         Position = Position + 10
         lRet = pb.UpdateProgress(Position)
     Loop
    Position = 0
 End Sub

Public Sub cmdStopPB_Click()
    pb.End
End Sub

Public Sub UserForm_Initialize()
    Set swApp = Application.SldWorks
    retVal = swApp.GetUserProgressBar(pb)
End Sub

Public Sub cmdUpdatePB_Click()
    Position = Position + 10
    If (Position = 160) Then Position = 0
    lRet = pb.UpdateProgress(Position)
    If lRet <> 2 Then
        Debug.Print " Result " & lRet
    Else
        MsgBox " User pressed Esc to cancel ", vbInformation, " API"
        pb.End
        End
    End If
End Sub
```

[Back to top](#Top)

#### Modules

```vb
Dim swApp As SldWorks.SldWorks
 Sub main()
     UserForm1.Show vbModeless
 End Sub
```

[Back to top](#Top)
