---
title: "Make Line Infinite Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Make_Line_Infinite_Example_VB.htm"
---

# Make Line Infinite Example (VBA)

This example shows how to make the selected finite line an infinite line.

```
'---------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part.
' 2. Sketches a finite line and sets its angle.
' 3. Changes the finite line to an infinite line and
'    changes the angle of the infinite line.
' 4. Examine the graphics area and Immediate window.
'---------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchMgr As SldWorks.SketchManager
Dim swSketchLine As SldWorks.SketchLine
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
```

```
    'Sketch a finite line and change its angle
    boolstatus = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSketchMgr = swModel.SketchManager
    swSketchMgr.InsertSketch True
    Set swSketchLine = swSketchMgr.CreateLine(-0.064203, -0.00825, 0#, -0.009545, 0.029422, 0#)
    swSketchLine.Angle = 0.785
    swModel.ClearSelection2 True
```

```
    boolstatus = swSketchLine.Infinite
    Debug.Print "Infinite line? " & boolstatus
    Debug.Print "Angle? " & swSketchLine.Angle
```

```
    'Change finite line to infinite line
    'and change its angle
    boolstatus = swSketchLine.MakeInfinite
    boolstatus = swSketchLine.Infinite
    Debug.Print "Infinite line? " & boolstatus
    swSketchLine.Angle = 1#
    Debug.Print "Angle? " & swSketchLine.Angle
```

```
   swSketchMgr.InsertSketch True
```

```
End Sub
```
