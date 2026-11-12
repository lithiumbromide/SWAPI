---
title: "Convert Drawing Views to Sketch Blocks Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Convert_Drawing_Views_to_Sketches_Example_VB.htm"
---

# Convert Drawing Views to Sketch Blocks Example (VBA)

This example shows how to convert drawing views to sketches and sketch blocks.

```
'----------------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\api\ReplaceView.slddrw
'
' Postconditions:
' 1. Converts Drawing View1 to a sketch.
' 2. Converts Drawing View2 to a sketch block
' 3. Converts Drawing View3 to a sketch block at a new position in the drawing.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim boolstatus As Boolean
Dim drawDoc As SldWorks.DrawingDoc
Dim selMan As SldWorks.SelectionMgr
Dim drview As SldWorks.View
Dim nPt(2) As Double
Dim vPt As Variant
Dim swMathUtil As SldWorks.MathUtility
Dim insertionPt As SldWorks.MathPoint
Dim position As SldWorks.MathPoint
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    Set Part = swApp.ActiveDoc
    Set drawDoc = Part
    Set swMathUtil = swApp.GetMathUtility
    Set selMan = Part.SelectionManager
```

```
    boolstatus = Part.Extension.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
    Set drview = selMan.GetSelectedObject6(1, 0)
    boolstatus = drview.ReplaceViewWithSketch
```

```
    Part.ClearSelection2 True
    boolstatus = Part.Extension.SelectByID2("Drawing View2", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
    Set drview = selMan.GetSelectedObject6(1, 0)
```

```
    nPt(0) = 1.41
    nPt(1) = 3.88
    nPt(2) = 0
    vPt = nPt
    Set insertionPt = swMathUtil.CreatePoint(vPt)
    boolstatus = drview.ReplaceViewWithBlock(insertionPt)
```

```
    Part.ClearSelection2 True
    boolstatus = Part.Extension.SelectByID2("Drawing View3", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
    Set drview = selMan.GetSelectedObject6(1, 0)
```

```
    nPt(0) = 5.48
    nPt(1) = 5.22
    nPt(2) = 0
    vPt = nPt
    Set position = swMathUtil.CreatePoint(vPt)
    boolstatus = drview.InsertViewAsBlock(insertionPt, position)
```

```
End Sub
```
