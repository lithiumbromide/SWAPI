---
title: "Get Points of Repeating Elements in Table-driven Pattern (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VB.htm"
---

# Get Points of Repeating Elements in Table-driven Pattern (VBA)

This example shows that the points that describe the locations of the repeating elements in a table-driven pattern are based on the table-driven pattern's coordinate system.

```
'---------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the coordinates of the
'    points for the two repeating elements in the
'    table-driven pattern.
' 2. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'---------------------------------------------
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
Dim swCoordinateData As SldWorks.CoordinateSystemFeatureData
Dim swTablePatternFeatData As SldWorks.TablePatternFeatureData
Dim swMathTransform As SldWorks.MathTransform
Dim swMathUtility As SldWorks.MathUtility
Dim swMathPoint As SldWorks.MathPoint
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim filename As String
Dim points As Variant
Dim point As String
Dim pointsArray(2) As Double
Dim i As Integer
```

```
Sub main()
```

```
filename = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\tablepattern.sldprt"
Set swApp = Application.SldWorks
```

```
Set swModel = swApp.OpenDoc6(filename, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
Set swModelDocExt = swModel.Extension
Set swSelMgr = swModel.SelectionManager
```

```
' Select the table-driven pattern
status = swModelDocExt.SelectByID2("TPattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
```

```
Set swTablePatternFeatData = swFeat.GetDefinition
swTablePatternFeatData.AccessSelections swModel, Nothing
```

```
' Get the points of the repeating elements in a table-driven pattern
' and transform them to coordinates
Set swCoordinateData = swTablePatternFeatData.CoordinateSystem.GetDefinition
swCoordinateData.AccessSelections swModel, Nothing
Set swMathTransform = swCoordinateData.Transform
swCoordinateData.ReleaseSelectionAccess
```

```
Set swMathUtility = swApp.GetMathUtility
```

```
points = swTablePatternFeatData.PointArray
```

```
Debug.Print "Number of points: " & swTablePatternFeatData.GetPointCount
```

```
For i = 0 To UBound(points) Step 3
    pointsArray(0) = points(i): pointsArray(1) = points(i + 1): pointsArray(2) = points(i + 2)
    Set swMathPoint = swMathUtility.CreatePoint(pointsArray)
```

```
    Set swMathPoint = swMathPoint.MultiplyTransform(swMathTransform.Inverse)
```

```
    ' Print the coordinates for the two repeating elements in the table-driven pattern
    point = "x: " & swMathPoint.ArrayData(0) & "   y: " & swMathPoint.ArrayData(1) & "   z: " & swMathPoint.ArrayData(2)
```

```
    Debug.Print point
Next
```

```
swTablePatternFeatData.ReleaseSelectionAccess
```

```
End Sub
```
