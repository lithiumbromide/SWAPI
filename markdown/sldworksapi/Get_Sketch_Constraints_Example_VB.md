---
title: "Get Sketch Constraints Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Constraints_Example_VB.htm"
---

# Get Sketch Constraints Example (VBA)

This examples shows how to:

- determine whether a sketch is under-constrained or over-constrained.
- iterate over all the segments in the sketch and get their constraints.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\surfaces\nozzle.sldprt.
' 2. Select Sketch14 in the FeatureManager design tree.
' 3. Examine the graphics area.
'
' Postconditions:
' 1. Iterates all constraints in Sketch14 and prints
'    to the Immediate window its constraint status and constraints.
' 2. Examine the Immediate window.
'------------------------------------------------------------------
Option Explicit
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
    Dim vSketchSeg As Variant
    Dim vConstraint As Variant
    Dim i As Long
    Dim j As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swSketch = swFeat.GetSpecificFeature2
```

```
    Debug.Print "Sketch = " & swFeat.Name
    Debug.Print ""
    Debug.Print "  SketchConstraintStatus (3 = fully constrained) = " & swSketch.GetConstrainedStatus
    Debug.Print ""
```

```
    ' Put sketch into edit mode to get access
    ' to constraint information for each segment
    ' in the sketch
    swModel.EditSketch
```

```
    vSketchSeg = swSketch.GetSketchSegments
    For i = 0 To UBound(vSketchSeg)
        vConstraint = vSketchSeg(i).GetConstraints
        For j = 0 To UBound(vConstraint)
            Debug.Print "  SketchSegConstraint[" & i & "] = " & vConstraint(j)
        Next j
    Next i
```

```
    ' Exit edit mode and do not rebuild the model
    swModel.InsertSketch2 False
```

```
End Sub
```
