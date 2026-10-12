---
title: "Get Intersecting Faces Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Intersecting_Faces_Example_VB.htm"
---

# Get Intersecting Faces Example (VBA)

This example shows how to get the intersection of two faces.

**NOTE:** This example uses some geometry- and topology-related methods and properties; e.g., ISurface::IntersectSurface, to get intersecting surfaces.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\cstick.sldprt.
' 2. Select the face of the finger holder that intersects
'    the curved face at the base of the candlestick
'    and the curved face at the base of the candlestick holder.
'
' Postconditions:
' 1. Inserts a 3D sketch with a series of line segments
'    approximating the intersection for each intersection curve.
' 2. Examine the graphics area and FeatureManager design tree.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-------------------------------------------------------------
```

```
Option Explicit
```

```
Sub CreateTessCurve(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swTrimCurve As SldWorks.Curve)
    Dim nChordTol As Double
    Dim nLengthTol As Double
    Dim nStartParam As Double
    Dim nEndParam As Double
    Dim bIsClosed As Boolean
    Dim bIsPeriodic As Boolean
    Dim vStartPt As Variant
    Dim vEndPt As Variant
    Dim vTessPts As Variant
    Dim swSketchSeg As SldWorks.SketchSegment
    Dim bRet As Boolean
    Dim i As Long
```

```
    ' Not needed because curve is a trimmed curve
    ' Could pass in trim points as parameters
    bRet = swTrimCurve.GetEndParams(nStartParam, nEndParam, bIsClosed, bIsPeriodic)
```

```
    vStartPt = swTrimCurve.Evaluate(nStartParam)
    vEndPt = swTrimCurve.Evaluate(nEndParam)
```

```
    nChordTol = 0.001
    nLengthTol = 0.001
    vTessPts = swTrimCurve.GetTessPts(nChordTol, nLengthTol, (vStartPt), (vEndPt))
```

```
    swModel.SetAddToDB True
    swModel.Insert3DSketch2 False
```

```
    ' Disable Visual Basic range checking because tessellation points
    ' might not be a multiple of 6
    On Error Resume Next
    For i = 0 To UBound(vTessPts) Step 6
        Set swSketchSeg = swModel.CreateLine2(vTessPts(i + 0), vTessPts(i + 1), vTessPts(i + 2), vTessPts(i + 3), vTessPts(i + 4), vTessPts(i + 5))
    Next i
    On Error GoTo 0
```

```
    swModel.SetAddToDB False
    swModel.Insert3DSketch2 True
```

```
End Sub
```

```
Function CreateTrimmedCurve(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSurf As SldWorks.Surface, swCurve As SldWorks.Curve) As SldWorks.Curve
    Dim nStartParam As Double
    Dim nEndParam As Double
    Dim bIsClosed As Boolean
    Dim bIsPeriodic As Boolean
    Dim vStartPt As Variant
    Dim vEndPt As Variant
    Dim nCurveBounds(0 To 5) As Double
    Dim vCurveBounds As Variant
    Dim vPointArray As Variant
    Dim vTArray As Variant
    Dim vUVArray As Variant
    Dim bRet As Boolean
```

```
    bRet = swCurve.GetEndParams(nStartParam, nEndParam, bIsClosed, bIsPeriodic)
```

```
    vStartPt = swCurve.Evaluate(nStartParam)
    vEndPt = swCurve.Evaluate(nEndParam)
    nCurveBounds(0) = vStartPt(0)
    nCurveBounds(1) = vStartPt(1)
    nCurveBounds(2) = vStartPt(2)
    nCurveBounds(3) = vEndPt(0)
    nCurveBounds(4) = vEndPt(1)
    nCurveBounds(5) = vEndPt(2)
    vCurveBounds = nCurveBounds
    bRet = swSurf.IntersectCurve(swCurve, (vCurveBounds), vPointArray, vTArray, vUVArray)
```

```
    Set CreateTrimmedCurve = swCurve.CreateTrimmedCurve(vPointArray(0), vPointArray(1), vPointArray(2), vPointArray(3), vPointArray(4), vPointArray(5))
End Function
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFace1 As SldWorks.Face2
    Dim swFace2 As SldWorks.Face2
    Dim swSurf1 As SldWorks.Surface
    Dim swSurf2 As SldWorks.Surface
    Dim swCurve1 As SldWorks.Curve
    Dim swCurve2 As SldWorks.Curve
    Dim vCurveArray As Variant
    Dim vBoundArray As Variant
    Dim swIntCurve As SldWorks.Curve
    Dim swTrimCurve As SldWorks.Curve
    Dim nLength As Double
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace1 = swSelMgr.GetSelectedObject6(1, -1)
    Set swFace2 = swSelMgr.GetSelectedObject6(2, -1)
    Set swSurf1 = swFace1.GetSurface
    Set swSurf2 = swFace2.GetSurface
```

```
    bRet = swSurf1.IntersectSurface(swSurf2, vCurveArray, vBoundArray)
```

```
    For i = 0 To UBound(vCurveArray)
        Set swIntCurve = vCurveArray(i)
        ' Curve could be infinite (that is, a straight line)
        If swIntCurve.IsTrimmedCurve Then
            nLength = swIntCurve.GetLength2(vBoundArray(2 * i), vBoundArray(2 * i + 1))
            Debug.Print "Curve(" & i & ") = " & nLength * 1000# & " mm"
            Set swTrimCurve = swIntCurve
        Else
            ' Create a trimmed curve by re-intersecting
            ' intersection curve with surface
            Set swTrimCurve = CreateTrimmedCurve(swApp, swModel, swSurf1, swIntCurve)
        End If
        CreateTessCurve swApp, swModel, swTrimCurve
    Next i
```

```
    bRet = swModel.EditRebuild3
```

```
End Sub
```
