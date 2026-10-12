---
title: "Get Lines in Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Lines_in_Sketch_Example_VB.htm"
---

# Get Lines in Sketch Example (VBA)

This example shows how to get the number of lines in a selected sketch and their start and end point coordinates.

```
'------------------------------------------------
' Preconditions:
' 1. Open a part and select a sketch.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the  number of lines in the selected
'    sketch and their start and end point
'    coordinates.
' 2. Examine the Immediate window.
'-------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swSketch As SldWorks.Sketch
    Dim NumLines As Long
    Dim vLines As Variant
    Dim i As Variant
    Dim bRet As Boolean
    Dim TrueFalse As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    Set swSelMgr = swModel.SelectionManager
```

```
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Debug.Print "Feature = " & swFeat.GetTypeName
    Set swSketch = swFeat.GetSpecificFeature2
    NumLines = swSketch.GetLineCount2(1) ' Exclude crosshatch lines
    Debug.Print "  Number of lines = " & NumLines
    vLines = swSketch.GetLines2(1) 'Exclude crosshatch lines
    For i = 0 To NumLines - 1
        Debug.Print "  Line(" & i & ")"
        Debug.Print "    Start = (" & vLines(12 * i + 6) * 1000# & "," & vLines(12 * i + 7) * 1000# & "," & vLines(12 * i + 8) * 1000# & ") mm"
        Debug.Print "    End   = (" & vLines(12 * i + 9) * 1000# & "," & vLines(12 * i + 10) * 1000# & "," & vLines(12 * i + 11) * 1000# & ") mm"
    Next i
```

```
End Sub
```
