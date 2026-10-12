---
title: "Get and Set Model Break View Display Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Model_Break_View_Display_Example_VB.htm"
---

# Get and Set Model Break View Display Example (VBA)

This example shows how to get and set whether to display an assembly's Model Break View in a drawing.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing that has:
 '    * assembly with Model Break View1.
 '    * Drawing View1.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Displays Model Break View1.
 ' 2. Inspect the Immediate window and graphics area.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim swView As SldWorks.View
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim boolstatus As Boolean
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
     Set swSelMgr = Part.SelectionManager
    boolstatus = Part.ActivateView("Drawing View1")
     boolstatus = Part.Extension.SelectByID2("Drawing View1", "DRAWINGVIEW", 0.395146689428525, 0.746414551874767, 0, False, 0, Nothing, 0)
    Set swView = swSelMgr.GetSelectedObject6(1, -1)
     boolstatus = swView.ShowModelBreakState(True, "Model Break View1")
    Debug.Print "Displaying Model Break View? " & swView.IsModelBreakState
    Part.ForceRebuild3 True
End Sub
```
