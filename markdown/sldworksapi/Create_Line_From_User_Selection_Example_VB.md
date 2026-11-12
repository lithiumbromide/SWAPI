---
title: "Create Line From User Selection Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Line_From_User_Selection_Example_VB.htm"
---

# Create Line From User Selection Example (VBA)

This example shows how to create geometry in a sketch or drawing, including how to retrieve the coordinates of a user's selection.

```
'---------------------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Click anywhere on the model.
'
' Postconditions:
' 1. Creates a line starting at the selected point in model
'    space coordinates from the currently selected object
'    and ending at the specified coordinates.
' 2. Examine the graphics area.
'--------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim PickPt As Variant
Dim x1, y1, x2, y2 As Double
```

```
Sub main()
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
```

```
    ' Get the selection point coordinates in model space
    ' from the currently selected object
    PickPt = swSelMgr.GetSelectionPointInSketchSpace2(1, -1)
```

```
    ' If no selection was made, then return an error message
    If (swSelMgr.GetSelectedObjectCount = 0) Or (IsEmpty(PickPt)) Then
        swApp.SendMsgToUser ("Click anywhere on the model, then rerun the macro.")
    ' Otherwise, create a line
    Else
        ' Set line start point
        x1 = PickPt(0)
        y1 = PickPt(1)
        ' Set line end point
        x2 = PickPt(0) + 0.5
        y2 = PickPt(1) + 0.5
        ' Create the line
        swModel.CreateLineVB x1, y1, 0#, x2, y2, 0#
    End If
```

```
End Sub
```
