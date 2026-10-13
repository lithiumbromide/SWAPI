---
title: "Get Assembly Bounding Box using Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Assembly_Bounding_Box_using_Assembly_Example_VB.htm"
---

# Get Assembly Bounding Box using Assembly Example (VBA)

This example shows how to get the box bounding an assembly using the assembly.

```
'--------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. Open the Immediate window.
' 3. Run the macro.
'
' Postconditions:
' 1. Adds a 3D sketch to the assembly showing the bounding box.
' 2. Examine the graphics area and Immediate window to verify.
'
' NOTE: The bounding box is approximated and oriented
' with the assembly coordinate system.
'----------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swAssy                  As SldWorks.AssemblyDoc
    Dim vBox                    As Variant
    Dim X_max                   As Double
    Dim X_min                   As Double
    Dim Y_max                   As Double
    Dim Y_min                   As Double
    Dim Z_max                   As Double
    Dim Z_min                   As Double
    Dim swSketchMgr             As SldWorks.SketchManager
    Dim swSketchPt(8)           As SldWorks.SketchPoint
    Dim swSketchSeg(12)         As SldWorks.SketchSegment
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
```

```
    vBox = swAssy.GetBox(swBoundingBoxIncludeRefPlanes)
```

```
    ' Initialize values
    X_max = vBox(3)
    X_min = vBox(0)
    Y_max = vBox(4)
    Y_min = vBox(1)
    Z_max = vBox(5)
    Z_min = vBox(2)
```

```
    Debug.Print "Assembly Bounding Box (" + swModel.GetPathName + ") = "
    Debug.Print "  (" + Str(X_min * 1000#) + "," + Str(Y_min * 1000#) + "," + Str(Z_min * 1000#) + ") mm"
    Debug.Print "  (" + Str(X_max * 1000#) + "," + Str(Y_max * 1000#) + "," + Str(Z_max * 1000#) + ") mm"
```

```
    Set swSketchMgr = swModel.SketchManager
    swSketchMgr.Insert3DSketch True
    swSketchMgr.AddToDB = True
```

```
    ' Draw points at each corner of bounding box
    Set swSketchPt(0) = swSketchMgr.CreatePoint(X_min, Y_min, Z_min)
    Set swSketchPt(1) = swSketchMgr.CreatePoint(X_min, Y_min, Z_max)
    Set swSketchPt(2) = swSketchMgr.CreatePoint(X_min, Y_max, Z_min)
    Set swSketchPt(3) = swSketchMgr.CreatePoint(X_min, Y_max, Z_max)
    Set swSketchPt(4) = swSketchMgr.CreatePoint(X_max, Y_min, Z_min)
    Set swSketchPt(5) = swSketchMgr.CreatePoint(X_max, Y_min, Z_max)
    Set swSketchPt(6) = swSketchMgr.CreatePoint(X_max, Y_max, Z_min)
    Set swSketchPt(7) = swSketchMgr.CreatePoint(X_max, Y_max, Z_max)

    ' Draw bounding box
    Set swSketchSeg(0) = swSketchMgr.CreateLine(X_min, Y_min, Z_min, X_max, Y_min, Z_min)
    Set swSketchSeg(1) = swSketchMgr.CreateLine(X_max, Y_min, Z_min, X_max, Y_min, Z_max)
    Set swSketchSeg(2) = swSketchMgr.CreateLine(X_max, Y_min, Z_max, X_min, Y_min, Z_max)
    Set swSketchSeg(3) = swSketchMgr.CreateLine(X_min, Y_min, Z_max, X_min, Y_min, Z_min)
    Set swSketchSeg(4) = swSketchMgr.CreateLine(X_min, Y_min, Z_min, X_min, Y_max, Z_min)
    Set swSketchSeg(5) = swSketchMgr.CreateLine(X_min, Y_min, Z_max, X_min, Y_max, Z_max)
    Set swSketchSeg(6) = swSketchMgr.CreateLine(X_max, Y_min, Z_min, X_max, Y_max, Z_min)
    Set swSketchSeg(7) = swSketchMgr.CreateLine(X_max, Y_min, Z_max, X_max, Y_max, Z_max)
    Set swSketchSeg(8) = swSketchMgr.CreateLine(X_min, Y_max, Z_min, X_max, Y_max, Z_min)
    Set swSketchSeg(9) = swSketchMgr.CreateLine(X_max, Y_max, Z_min, X_max, Y_max, Z_max)
    Set swSketchSeg(10) = swSketchMgr.CreateLine(X_max, Y_max, Z_max, X_min, Y_max, Z_max)
    Set swSketchSeg(11) = swSketchMgr.CreateLine(X_min, Y_max, Z_max, X_min, Y_max, Z_min)
```

```
    swSketchMgr.AddToDB = False
    swSketchMgr.Insert3DSketch True
```

```
End Sub
```
