---
title: "Add Buttons to Task Pane Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Buttons_to_Task_Pane_Example_VB.htm"
---

# Add Buttons to Task Pane Example (VBA)

This example shows how to add standard SOLIDWORKS and custom buttons to the Task Pane.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Copy Main to the main module.
' 2. Click Insert > Class Module and copy Class to that module.
' 3. Copy save.png from public_documents\samples\tutorial\api to
'    this macro 's folder.
'
' Postconditions:
' 1. Opens the Task Pane and loads the My Calendar control with
'    the specified standard and custom buttons at the
'    top of the pane.
' 2. Click each button from left to right.
' 3. Displays a message box confirming each button click.
' 4. Click OK to close each message box.
'    a. Clicking the Close button prompts you to remove the
'       control from the Task Pane.
'    b. Click OK.
'-----------------------------------------------------------------
'Main
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swTaskPane As SldWorks.TaskpaneView
Dim result As Boolean
Dim folder As String
Dim bitmap As String
Dim toolTip As String
Dim ctrlName As String
Dim ctrlLicKey As String
Public buttonIdx As Integer
Dim swTaskpaneEvents As New Class1
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    folder = swApp.GetCurrentMacroPathFolder + "\"

    ' Use default image for Task Pane tab
    bitmap = ""
    toolTip = "My Calendar"
    ctrlName = "My.Calendar"
    ctrlLicKey = ""
    Set swTaskPane = swApp.CreateTaskpaneView2(bitmap, toolTip)
```

```
    ' Add standard and custom buttons to Task Pane
    result = swTaskPane.AddCustomButton(folder & "save.png", "Save (custom png)")
    result = swTaskPane.AddStandardButton(swTaskPaneBitmapsOptions_Next, "Next (standard)")
    result = swTaskPane.AddStandardButton(swTaskPaneBitmapsOptions_Back, "Back (standard)")
    result = swTaskPane.AddStandardButton(swTaskPaneBitmapsOptions_Ok, "OK (standard)")
    result = swTaskPane.AddStandardButton(swTaskPaneBitmapsOptions_Close, "Close (standard)")
```

```
    ' Add control to Task Pane for the buttons
    swTaskPane.AddControl ctrlName, ctrlLicKey
```

```
    ' Set up events
    Set swTaskpaneEvents.swTaskPane = swTaskPane
```

```
End Sub
```

```
Back to top
```

'Class

```
Option Explicit
```

```
Public WithEvents swTaskPane As SldWorks.TaskpaneView
```

```
Private Function swTaskPane_TaskPaneActivateNotify() As Long
    If (swTaskPane.GetButtonState(0) = False) Then
        For buttonIdx = 0 To 20
            swTaskPane.SetButtonState buttonIdx, True
            Next
    Else
        For buttonIdx = 0 To 20
            swTaskPane.SetButtonState buttonIdx, False
        Next
    End If
End Function
```

```
Private Function swTaskPane_TaskPaneDestroyNotify() As Long
    MsgBox ("Remove control from Task Pane?")
End Function
```

```
Private Function swTaskPane_TaskPaneToolbarButtonClicked(ByVal ButtonIndex As Long) As Long
    Select Case (ButtonIndex + 1)
        Case 1
            MsgBox "Save (custom png) button clicked."
        Case 2
            MsgBox "Next button clicked."
        Case 3
            MsgBox "Back button clicked."
        Case 4
            MsgBox "Okay button clicked."
        Case 5
            MsgBox "Close button clicked."
            swTaskPane.DeleteView
    End Select
```

```
End Function
```

```
Back to top
```
