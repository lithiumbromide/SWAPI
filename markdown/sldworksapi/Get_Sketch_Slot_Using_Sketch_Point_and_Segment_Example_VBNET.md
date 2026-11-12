---
title: "Get Sketch Slot Using Sketch Point and Segment Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_VBNET.htm"
---

# Get Sketch Slot Using Sketch Point and Segment Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
```

```vb
 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swExt As ModelDocExtension
     Dim swSelMgr As SelectionMgr
     Dim boolstatus As Boolean
     Dim swSketchManager As SketchManager
     Dim swSketchSlot As SketchSlot
     Dim swSketchPoint As SketchPoint
     Dim swSketchSegment As SketchSegment
    Public Sub main()
        swModel = swApp.ActiveDoc
         swExt = swModel.Extension
         swSelMgr = swModel.SelectionManager
         swSketchManager = swModel.SketchManager

         ' Select a plane and open a sketch
        boolstatus = swExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
         swModel.InsertSketch()

         ' Insert a sketch of sketch slot
         swSketchSlot = swSketchManager.CreateSketchSlot(swSketchSlotCreationType_e.swSketchSlotCreationType_line, swSketchSlotLengthType_e.swSketchSlotLengthType_CenterCenter, 0.05, -0.05, 0, 0, 0.05, 0, 0, 0, 0, 0, 1, False)
         Debug.Print("Length: " & swSketchSlot.Length)
         Debug.Print(" ")
         swModel.InsertSketch()

         ' Get a sketch point on the sketch slot
         boolstatus = swExt.SelectByID2("Point1@Sketch1", "EXTSKETCHPOINT", 0.05, 0.025, 0, False, 0, Nothing, 0)
         swSketchPoint = swSelMgr.GetSelectedObject6(1, -1)
         ' Get sketch slot
         swSketchSlot = swSketchPoint.GetSketchSlot
         Debug.Print("Length: " & swSketchSlot.Length)
         Debug.Print(" ")

         ' Get a sketch segment on the sketch slot
         boolstatus = swExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.03969355327396, -0.025, 0, False, 0, Nothing, 0)
         swSketchSegment = swSelMgr.GetSelectedObject6(1, -1)
         ' Get sketch slot
         swSketchSlot = swSketchSegment.GetSketchSlot
         Debug.Print("Length: " & swSketchSlot.Length)
         Debug.Print(" ")
    End Sub
    ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
