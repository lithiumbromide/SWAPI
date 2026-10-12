---
title: "Get All Sketch Segments in Drawing Template Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_All_Sketch_Segments_in_Drawing_Template_Example_VB.htm"
---

# Get All Sketch Segments in Drawing Template Example (VBA)

This example shows how to get all of the sketch segments in a drawing template.

```
'--------------------------------------------------------
' Preconditions:
' 1. Open a drawing.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets all of the sketch segments in the drawing
'    template and their type and length.
' 2. Examine the Immediate window.
'--------------------------------------------------------
Option Explicit
```

```
Public Enum swSketchSegments_e
    swSketchLINE = 0
    swSketchARC = 1
    swSketchELLIPSE = 2
    swSketchSPLINE = 3
    swSketchTEXT = 4
    swSketchPARABOLA = 5
End Enum
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swView As SldWorks.View
    Dim swSketch As SldWorks.Sketch
    Dim swSketchSeg As SldWorks.SketchSegment
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelData As SldWorks.SelectData
    Dim vSketchSeg As Variant
    Dim vSketchSegID As Variant
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    Set swDraw = swModel
```

```
    swDraw.EditTemplate
```

```
    ' This is the drawing template
    Set swSketch = swModel.GetActiveSketch2
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    swModel.ClearSelection2 (True)
```

```
    vSketchSeg = swSketch.GetSketchSegments
    For i = 0 To UBound(vSketchSeg)
        Set swSketchSeg = vSketchSeg(i)
        vSketchSegID = swSketchSeg.GetID
```

```
        Debug.Print "    SketchSegID(" & i & ") = [" & vSketchSegID(0) & ", " & vSketchSegID(1) & "]"
        Debug.Print "      Type       = " & swSketchSeg.GetType
        Debug.Print "      Length     = " & swSketchSeg.GetLength
```

```
        bRet = swSketchSeg.Select4(True, swSelData)
```

```
    Next
```

```
End Sub
```
