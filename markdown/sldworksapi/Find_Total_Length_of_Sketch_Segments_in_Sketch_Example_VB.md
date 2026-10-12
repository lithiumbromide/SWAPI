---
title: "Find Total Length of Sketch Segments in Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Find_Total_Length_of_Sketch_Segments_in_Sketch_Example_VB.htm"
---

# Find Total Length of Sketch Segments in Sketch Example (VBA)

This example shows how to find the total length of all sketch segments in a sketch.

```
'----------------------------------------------------
' Preconditions:
' 1. Open a part and select a sketch.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the total length of the segments in the
'    selected sketch.
' 2. Examine the Immediate window.
'----------------------------------------------------
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
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swSketch As SldWorks.Sketch
    Dim i As Long
    Dim bRet As Boolean
    Dim vSketchSeg As Variant
    Dim swSketchSeg As SldWorks.SketchSegment
    Dim nLength As Double
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swSketch = swFeat.GetSpecificFeature2
    vSketchSeg = swSketch.GetSketchSegments
    For i = 0 To UBound(vSketchSeg)
        Set swSketchSeg = vSketchSeg(i)
        ' Ignore construction lines
        If swSketchSeg.ConstructionGeometry = False Then
            ' Ignore text
            If swSketchTEXT <> swSketchSeg.GetType Then
                nLength = nLength + swSketchSeg.GetLength
            End If
        End If
    Next i
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Sketch = " & swFeat.Name
    Debug.Print "    Total length = " & nLength * 1000# & " mm"
```

```
End Sub
```
