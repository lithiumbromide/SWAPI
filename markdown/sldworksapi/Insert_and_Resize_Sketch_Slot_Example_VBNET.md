---
title: "Insert and Resize Sketch Slot Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Resize_Sketch_Slot_Example_VBNET.htm"
---

# Insert and Resize Sketch Slot Example (VB.NET)

This example shows how to insert a sketch slot and resize it.

```
'--------------------------------------------------------
' Preconditions:
' 1. Open a new part document.
' 2. Open the Immediate window..
'
' Postconditions:
' 1. Creates a sketch and inserts a sketch slot.
' 2. Press F5 after examining the graphics area.
' 3. Resizes the slot.
' 4. Examine the graphics area and Immediate window.
'-------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swExt As ModelDocExtension
    Dim swSelMgr As SelectionMgr
    Dim boolstatus As Boolean
    Dim swPart As PartDoc
    Dim skManager As SketchManager

    Public Sub main()
```

```vb
         swModel = swApp.ActiveDoc
         swExt = swModel.Extension
         swSelMgr = swModel.SelectionManager
         skManager = swModel.SketchManager
         swPart = swModel

         boolstatus = swExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)

         skManager.InsertSketch(True)

         Dim swSketchSlot As SketchSlot
         swSketchSlot = skManager.CreateSketchSlot(swSketchSlotCreationType_e.swSketchSlotCreationType_line, swSketchSlotLengthType_e.swSketchSlotLengthType_CenterCenter, 0.05, -0.05, 0, 0, 0.05, 0, 0, 0, 0, 0, 1, False)

         Dim lengthType As swSketchSlotLengthType_e
         lengthType = swSketchSlot.LengthType

         Debug.Print("Length: " & swSketchSlot.Length)
         Debug.Print("Length Type: " & lengthType.ToString())
         Debug.Print("Width: " & swSketchSlot.Width)

         Stop

         ' Edit the original slot
         swSketchSlot.Width = swSketchSlot.Width * 2.0#
         Debug.Print "Modified width: " & swSketchSlot.Width
         skManager.InsertSketch(True)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks
 End Class
```
