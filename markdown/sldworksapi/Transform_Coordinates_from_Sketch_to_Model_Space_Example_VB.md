---
title: "Transform Coordinates from Sketch to Model Space Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Transform_Coordinates_from_Sketch_to_Model_Space_Example_VB.htm"
---

# Transform Coordinates from Sketch to Model Space Example (VBA)

When an entity is selected while editing a sketch, for example a sketch point, the coordinates of the point are shown in the space of the sketch. Sometimes it is desirable to know the coordinates of this point in the space of the model.

This example shows how to use various transforms and math utilities to transform a point in sketch space to model space.

```vb
'------------------------------------------------------------------
'
' Preconditions:
'       (1) Part, assembly or drawing is open.
'       (2) If a part or assembly, then a sketch is being edited.
'       (3) If a part or assembly, then an entity is selected in
'           the sketch.
'       (4) If a drawing, then an entity is selected.
'
' Postconditions: None
'
' NOTES:
'       (1) If the sketch is a 3D sketch, then the selected sketch
'           point is automatically in model coordinates.
'       (2) If the sketch is a 3D sketch, then its transform is the
'           unit transform.
'
'------------------------------------------------------------------
Option Explicit
Public Function GetModelCoordinates _
( _
    swApp As SldWorks.SldWorks, _
    swSketch As SldWorks.sketch, _
    vPtArr As Variant _
) As Variant
    Dim swMathPt                    As SldWorks.MathPoint
    Dim swMathUtil                  As SldWorks.MathUtility
    Dim swMathTrans                 As SldWorks.MathTransform
    Set swMathUtil = swApp.GetMathUtility
    Set swMathPt = swMathUtil.CreatePoint(vPtArr)
    ' Is a unit transform if 3D sketch; for example, selected sketch
    ' point is automatically in model space
    Set swMathTrans = swSketch.ModelToSketchTransform
    Set swMathTrans = swMathTrans.Inverse
    Set swMathPt = swMathPt.MultiplyTransform(swMathTrans)
    GetModelCoordinates = swMathPt.ArrayData
End Function
Sub main()
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swSelMgr                    As SldWorks.SelectionMgr
    Dim swSketch                    As SldWorks.sketch
    Dim vSketchSelPt                As Variant
    Dim vModelSelPt                 As Variant
    Dim i                           As Long

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swSketch = swModel.GetActiveSketch2

    vSketchSelPt = swSelMgr.GetSelectionPointInSketchSpace(1)
    vModelSelPt = GetModelCoordinates(swApp, swSketch, vSketchSelPt)

    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Is3D sketch          = " & swSketch.Is3D
    Debug.Print "  SelPt (sketch space) = (" & vSketchSelPt(0) * 1000# & ", " & vSketchSelPt(1) * 1000# & ", " & vSketchSelPt(2) * 1000# & ") mm"
    Debug.Print "  SelPt (model  space) = (" & vModelSelPt(0) * 1000# & ", " & vModelSelPt(1) * 1000# & ", " & vModelSelPt(2) * 1000# & ") mm"
End Sub
'------------------------------------------
```
