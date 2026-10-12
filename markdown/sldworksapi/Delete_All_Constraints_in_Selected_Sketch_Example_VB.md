---
title: "Delete All Constraints in Selected Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_All_Constraints_in_Selected_Sketch_Example_VB.htm"
---

# Delete All Constraints in Selected Sketch Example (VBA)

This example shows how to delete all of the constraints in the selected sketch.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\surfaces\nozzle.sldprt.
' 2. Select Sketch14 in the FeatureManager design tree.
' 3. Examine the graphics area.
'
' Postconditions:
' 1. Deletes all constraints in Sketch14.
' 2. Examine the graphics area.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
```

```
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swSketch As SldWorks.Sketch
    Dim vSketchSeg As Variant
    Dim swSketchSeg As SldWorks.SketchSegment
    Dim vSketchPt As Variant
    Dim swSketchPt As SldWorks.SketchPoint
    Dim swSelData As SldWorks.SelectData
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    Set swFeat = swSelMgr.GetSelectedObject6(1, 0)
    Set swSketch = swFeat.GetSpecificFeature2
```

```
    ' Edit sketch
    swModel.EditSketch
```

```
    vSketchSeg = swSketch.GetSketchSegments
    For i = 0 To UBound(vSketchSeg)
        Set swSketchSeg = vSketchSeg(i)
        bRet = swSketchSeg.Select4(False, swSelData): Debug.Assert bRet
        swModel.SketchConstraintsDelAll
    Next i
```

```
    vSketchPt = swSketch.GetSketchPoints2
    For i = 0 To UBound(vSketchPt)
        Set swSketchPt = vSketchPt(i)
        bRet = swSketchPt.Select4(False, swSelData): Debug.Assert bRet
        swModel.SketchConstraintsDelAll
    Next i
```

```
    ' Exit sketch
    swModel.InsertSketch2 True
```

```
End Sub
```
