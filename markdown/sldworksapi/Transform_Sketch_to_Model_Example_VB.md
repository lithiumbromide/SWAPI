---
title: "Transform Sketch to Model Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Transform_Sketch_to_Model_Example_VB.htm"
---

# Transform Sketch to Model Example (VBA)

When a sketch point is created, its x, y, and z location values are in relation to the sketch origin. This example shows how to get the sketch point’s coordinates in relation to the model origin using a MathUtility object.

```
'-----------------------------------------------------------------------
' Preconditions:
'  1. Open a part.
'  2. Select a sketch.
'
' Postconditions:
'  1. Gets a MathUtility object from the current model document.
'  2. Gets the selected sketch that contains the points whose
'     coordinates to modify.
'  3. Fills array with all of the points in the sketch.
'  4. Creates a coordinate array with the x, y, and z value sof a sketch point
'     from the sketch-point array.
'  5. Creates a new MathPoint object from the MathUtility object, providing
'     the coordinate array for the location of the MathPoint.
'  6. Gets and displays the model-to-sketch transform for this sketch.
'  7. Click OK to close the message box.
'  8. Calls IMathTransform::Inverse, which provides a MathTransform
'     object from the sketch coordinates to the model coordinates.
'  9. Calls IMathPoint::MulitplyTransform(MathTransform) to move
'     the MathPoint object into the model.
' 10. Displays the point coordinates in relation to the model origin.
' 11. Click OK to close the message box.
'--------------------------------------------------------------------------
Option Explicit
```

```
    Dim swApp As SldWorks.SldWorks
    Dim selMgr As SldWorks.SelectionMgr
    Dim Model As SldWorks.ModelDoc2
    Dim SketchPoints As Variant
    Dim SketchFeature As SldWorks.Feature
    Dim PointCoords(2) As Double
    Dim MathUtil As SldWorks.MathUtility
    Dim MathTrans As SldWorks.MathTransform
    Dim MathP As SldWorks.MathPoint
    Dim ModelSketchTransform As Variant
```

```
Sub main()
```

```
    'Connect to SOLIDWORKS Design
    Set swApp = CreateObject("SldWorks.Application")
    Set Model = swApp.ActiveDoc
```

```
    'Prepare the MathUtility
    Set MathUtil = swApp.GetMathUtility
```

```
    'Get the SelectionMgr
    Set selMgr = Model.SelectionManager
```

```
    'Get the sketch from the SelectionMgr
    Set SketchFeature = selMgr.GetSelectedObject6(1, 0)
    Set SketchFeature = SketchFeature.GetSpecificFeature2
```

```
    'Get the sketch points
    SketchPoints = SketchFeature.GetSketchPoints2
```

```
    'Build a coordinate array from the first point in the sketch
    PointCoords(0) = SketchPoints(0).X
    PointCoords(1) = SketchPoints(0).Y
    PointCoords(2) = SketchPoints(0).Z
```

```
    'Create the new MathPoint from the sketch point data
    'MathP refers to the point location in the sketch coordinates
    Set MathP = MathUtil.CreatePoint(PointCoords)
```

```
    'Display the point coordinates in relation to the sketch origin
    SketchPoints = MathP.ArrayData
    MsgBox "Point coordinates in relation to the sketch origin: " & SketchPoints(0) & ", " & SketchPoints(1) & ", " & SketchPoints(2)
```

```
    'Get the model-to-sketch transform for this sketch
    Set MathTrans = SketchFeature.ModelToSketchTransform
```

```
    'Get the inversion of the transform
    Set MathTrans = MathTrans.Inverse
```

```
    'Multiply the point by the inverse transform
    'MathP now refers to the point location in the model coordinates
    Set MathP = MathP.MultiplyTransform(MathTrans)
```

```
    'Display the point coordinates in relation to the model origin
    SketchPoints = MathP.ArrayData
    MsgBox "Point coordinates in relation to the model origin: " & SketchPoints(0) & ", " & SketchPoints(1) & ", " & SketchPoints(2)
```

```
End Sub
```
