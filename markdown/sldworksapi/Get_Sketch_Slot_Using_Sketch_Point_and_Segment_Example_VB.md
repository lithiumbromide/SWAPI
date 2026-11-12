---
title: "Get Sketch Slot Using Sketch Point and Segment Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_VB.htm"
---

# Get Sketch Slot Using Sketch Point and Segment Example (VBA)

This example shows you how to get a sketch slot using a sketch point and a sketch segment.

```
'--------------------------------------------------------
' Preconditions:
' 1. Open a new part document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a sketch slot.
' 2. Gets the length of the sketch slot.
' 3. Selects a sketch point on the sketch slot
'    and accesses the sketch slot using that
'    sketch point.
' 4. Gets the length of the sketch slot.
' 5. Selects a sketch segment on the sketch slot
'    and accesses the sketch slot using that
'    sketch segment.
' 6. Gets the length of the sketch slot.
' 7. Examine the Immediate window.
'-------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim boolstatus As Boolean
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSlot As SldWorks.SketchSlot
Dim swSketchPoint As SldWorks.SketchPoint
Dim swSketchSegment As SldWorks.SketchSegment
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    Set swSketchManager = swModel.SketchManager
```

```
    ' Select a plane and open a sketch
    boolstatus = swExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swModel.InsertSketch

    ' Create a sketch slot
    Set swSketchSlot = swSketchManager.CreateSketchSlot(swSketchSlotCreationType_e.swSketchSlotCreationType_line, swSketchSlotLengthType_e.swSketchSlotLengthType_CenterCenter, 0.05, -0.05, 0, 0, 0.05, 0, 0, 0, 0, 0, 1, False)
    Debug.Print "Length: " & swSketchSlot.Length
    Debug.Print " "
    swModel.InsertSketch
```

```
    ' Get a sketch point on the sketch slot
    boolstatus = swExt.SelectByID2("Point1@Sketch1", "EXTSKETCHPOINT", 0.05, 0.025, 0, False, 0, Nothing, 0)
    Set swSketchPoint = swSelMgr.GetSelectedObject6(1, -1)
```

```
    ' Get sketch slot
    Set swSketchSlot = swSketchPoint.GetSketchSlot
    Debug.Print "Length: " & swSketchSlot.Length
    Debug.Print " "
```

```
    ' Get a sketch segment on the sketch slot
    boolstatus = swExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0, -0, 0, False, 0, Nothing, 0)
    Set swSketchSegment = swSelMgr.GetSelectedObject6(1, -1)
```

```
    ' Get sketch slot
    Set swSketchSlot = swSketchSegment.GetSketchSlot
    Debug.Print "Length: " & swSketchSlot.Length
```

```
End Sub
```
