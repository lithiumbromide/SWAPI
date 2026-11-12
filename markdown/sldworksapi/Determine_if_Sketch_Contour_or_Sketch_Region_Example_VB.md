---
title: "Determine if Sketch Contour or Sketch Region Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Determine_if_Sketch_Contour_or_Sketch_Region_Example_VB.htm"
---

# Determine if Sketch Contour or Sketch Region Example (VBA)

This example shows how to determine if the object is a sketch contour or sketch region. It also shows how to use the TypeOf keyword to determine the type of object in the first element in the array.

```
'--------------------------------------------------------
' Preconditions:
' 1. Open a part that contains a Boss-Extrude1 feature
'    with sketch contours and sketch regions.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens Boss-Extrude1's sketch and selects
'    the sketch contours and sketch regions.
' 2. Gets whether the first selection in the sketch
'    is a sketch contour or sketch region.
' 3. Examine the Immediate window.
'--------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.PartDoc
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set Part = swApp.ActiveDoc
    boolstatus = Part.Extension.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
```

```
    'Boss-Extrude1 has sketch contours and sketch regions
    Dim Extrudefeature As SldWorks.Feature
    Dim Extrudefeature_DEF As SldWorks.ExtrudeFeatureData2
    Dim SelMgr As SldWorks.SelectionMgr
    Dim ContourArray As Variant
```

```
    Set SelMgr = Part.SelectionManager
    Set Extrudefeature = SelMgr.GetSelectedObject5(1)
    Set Extrudefeature_DEF = Extrudefeature.GetDefinition
    Extrudefeature_DEF.AccessSelections Part, Nothing
        ContourArray = Extrudefeature_DEF.Contours
    Extrudefeature_DEF.ReleaseSelectionAccess
```

```
    Dim SR As SketchRegion
    Dim SC As SketchContour
```

```
    ContourArray(0).Select False, 0
    Debug.Print TypeName(ContourArray(0))
    If TypeOf ContourArray(0) Is SketchRegion Then
        Debug.Print "Object is SketchRegion"
        Set SR = ContourArray(0)
    Else
        Debug.Print "Object is SketchContour"
        Set SC = ContourArray(0)
    End If
```

```
End Sub
```
