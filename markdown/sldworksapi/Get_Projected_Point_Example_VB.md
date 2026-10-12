---
title: "Get Projected Point Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Projected_Point_Example_VB.htm"
---

# Get Projected Point Example (VBA)

This example shows how to get the point where an input point is projected on to a face and surface in the specified direction.

```
'-----------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Select a face on the part.
'
' Postconditions:
' 1. Returns the point where the input point
'    is projected onto a face or surface, if
'    the input point is projected.
' 2. Examine the Immediate window.
'------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim myModel As SldWorks.ModelDoc2
    Dim mathUtils As SldWorks.MathUtility
```

```
    Set swApp = Application.SldWorks
    Set myModel = swApp.ActiveDoc
    Set mathUtils = swApp.GetMathUtility()
```

```
   ' Preselect the face with which to work
    Dim mySelMgr As SldWorks.SelectionMgr
    Dim selObj As Object
    Dim faceToUse As SldWorks.Face2
    Dim surfaceToUse As SldWorks.Surface
    Dim selCount As Long
    Dim selType As Long
```

```
    Set mySelMgr = myModel.SelectionManager
    selCount = mySelMgr.GetSelectedObjectCount2(0)
    If (selCount > 0) Then
        selType = mySelMgr.GetSelectedObjectType3(1, 0)
        Set selObj = mySelMgr.GetSelectedObject6(1, 0)
        If (selType = SwConst.swSelFACES) Then
            Set faceToUse = selObj
        End If
    End If
```

```
   ' Do the ray intersection operation
    Dim basePoint(0 To 2) As Double, rayDir(0 To 2) As Double
    Dim vBasePoint As Variant, vVector As Variant
    Dim rayPoint As SldWorks.MathPoint, rayVector As SldWorks.MathVector
    Dim intersectPt As SldWorks.MathPoint
    Dim vPoint As Variant, vPoint2 As Variant
    Dim xPt As Double, yPt As Double, zPt As Double
```

```
   ' First try the face
    If Not faceToUse Is Nothing Then
        basePoint(0) = 0.04 '0.013
        basePoint(1) = 0.04 '0.056
        basePoint(2) = 1#
        vBasePoint = basePoint
        Set rayPoint = mathUtils.CreatePoint(vBasePoint)
        rayDir(0) = 0#
        rayDir(1) = 0#
        rayDir(2) = -1#
        vVector = rayDir
        Set rayVector = mathUtils.CreateVector(vVector)
        Set intersectPt = faceToUse.GetProjectedPointOn(rayPoint, rayVector)
        Debug.Print "Ray point = " & Format(basePoint(0), "##0.0#####") & " , " & Format(basePoint(1), "##0.0#####") & " , " & Format(basePoint(2), "##0.0#####")
        Debug.Print "Ray direction = " & Format(rayDir(0), "##0.0#####") & " , " & Format(rayDir(1), "##0.0#####") & " , " & Format(rayDir(2), "##0.0#####")
        If Not intersectPt Is Nothing Then
            vPoint = intersectPt.ArrayData
            xPt = vPoint(0)
            yPt = vPoint(1)
            zPt = vPoint(2)
            Debug.Print "    Face hit point = " & Format(xPt, "##0.0#####") & " , " & Format(yPt, "##0.0#####") & " , " & Format(zPt, "##0.0#####")
        Else
            Debug.Print "    No face hit point."
        End If
```

```
        ' Now try the surface, gotten from the face
        Set surfaceToUse = faceToUse.GetSurface()
        If Not surfaceToUse Is Nothing Then
            Set intersectPt = surfaceToUse.GetProjectedPointOn(rayPoint, rayVector)
            If Not intersectPt Is Nothing Then
                vPoint2 = intersectPt.ArrayData
                xPt = vPoint2(0)
                yPt = vPoint2(1)
                zPt = vPoint2(2)
                Debug.Print "    Surface hit point = " & Format(xPt, "##0.0#####") & " , " & Format(yPt, "##0.0#####") & " , " & Format(zPt, "##0.0#####")
            Else
                Debug.Print "    No surface hit point."
            End If
        End If
    End If
```

```
End Sub
```
