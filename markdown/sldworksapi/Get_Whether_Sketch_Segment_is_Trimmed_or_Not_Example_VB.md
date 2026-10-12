---
title: "Get Whether Sketch Segment is Trimmed or Not Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Whether_Sketch_Segment_is_Trimmed_or_Not_Example_VB.htm"
---

# Get Whether Sketch Segment is Trimmed or Not Example (VBA)

This example shows how to determine if a sketch segment is trimmed or not.

```
'---------------------------------------------
' Preconditions:
' 1. Open a part that contains a 3D sketch containing
'    a sketch segment (i.e., line, arc, ellipse,
'    spline, or parabola).
' 2. Select the 3D sketch.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the sketch segment and its ID and type
'    and whether the sketch segment is construction
'    geometry and trimmed.
' 2. Examine the Immediate window.
'---------------------------------------------
Option Explicit
```

```
Public Enum swSkSegments_e
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
    Dim sSkSegmentsName(5) As String
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSkSeg As SldWorks.SketchSegment
    Dim swCurve As SldWorks.Curve
    Dim swSkFeat As SldWorks.Feature
    Dim swSketch As SldWorks.Sketch
    Dim vID As Variant
    Dim bRet As Boolean
```

```
    sSkSegmentsName(swSketchLINE) = "swSketchLINE"
    sSkSegmentsName(swSketchARC) = "swSketchARC"
    sSkSegmentsName(swSketchELLIPSE) = "swSketchELLIPSE"
    sSkSegmentsName(swSketchSPLINE) = "swSketchSPLINE"
    sSkSegmentsName(swSketchTEXT) = "swSketchTEXT"
    sSkSegmentsName(swSketchPARABOLA) = "swSketchPARABOLA"
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swSkSeg = swSelMgr.GetSelectedObject5(1)
    Set swCurve = swSkSeg.GetCurve
    Set swSkFeat = swSkSeg.GetSketch
    Set swSketch = swSkFeat.GetSpecificFeature
```

```
    vID = swSkSeg.GetID
```

```
    Debug.Print "Feature = " & swSkFeat.Name & " [" & swSketch.Is3D & "]"
    Debug.Print "  Sketch Segment"
    Debug.Print "    ID = [" & vID(0) & "," & vID(1) & "]"
    Debug.Print "      Type                  = " & sSkSegmentsName(swSkSeg.GetType)
    Debug.Print "      Construction geometry = " & swSkSeg.ConstructionGeometry
    Debug.Print "      Is trimmed            = " & swCurve.IsTrimmedCurve
```

```
End Sub
```
