---
title: "Get Curve Spline Points Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Curve_Spline_Points_Example_VB.htm"
---

# Get Curve Spline Points Example (VBA)

Given a spline curve, this example shows how to get the set of interpolation points.

```
'------------------------------------------------------------
' Preconditions:
' 1. Open a part containing a sketch of a spline.
' 2. Select the spline.
' 3. Open the Immediate window.
' 4. Run the Curve_GetSplinePts1() subroutine.
'
' Postconditions:
' 1. Gets the parameters and spline points for the selected spline.
' 2. Examine the Immediate window.
' 3. Run Curve_GetSplinePts2() subroutine.
' 4. Gets the parameters and spline points for the selected spline.
' 5. Examine the Immediate window.
'------------------------------------------------------------
Option Explicit
```

```
' Extract two integer values out of a single
' double value, assuming that a C int has 4 bytes
Type DoubleRec
    dValue As Double
End Type
```

```
Type Int2Rec
    iLower As Long
    iUpper As Long
End Type
```

```
' Extract two integer values out of a single
' double value, by assigning a DoubleRec to the
' double value then copying the value over an
' Int2Rec and extracting the integer values
Function ExtractFields(dValue As Double, iLower As Integer, iUpper As Integer)
    Dim dr As DoubleRec
    Dim i2r As Int2Rec
```

```
    ' Set the double value
    dr.dValue = dValue
    ' Copy the values
    LSet i2r = dr
    ' Extract the values
    iLower = i2r.iLower
    iUpper = i2r.iUpper
End Function
```

```
Sub DumpSplineInfo(varSplinePts As Variant)
    Dim i As Long
    For i = 0 To UBound(varSplinePts) Step 3
        Debug.Print "  SplinePt(" & i / 3 & ")     = (" & varSplinePts(i + 0) * 1000# & ", " & varSplinePts(i + 1) * 1000# & ", " & varSplinePts(i + 2) * 1000# & ") mm"
    Next i
End Sub
```

```
Sub Curve_GetSplinePts1()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim Part As SldWorks.ModelDoc2
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set Part = swApp.ActiveDoc
    Dim swSelectMgr As SldWorks.SelectionMgr
    Set swSelectMgr = Part.SelectionManager
    Dim swSketchSeg As SldWorks.SketchSegment
    Set swSketchSeg = swSelectMgr.GetSelectedObject5(1)
    Dim swCurveIn As SldWorks.Curve
    Set swCurveIn = swSketchSeg.GetCurve
    Dim varSplineParams As Variant
```

```
    ' False - do not want a cubic spline
    varSplineParams = swCurveIn.GetBCurveParams(False)
```

```
    Dim iNumKnots As Integer
    Dim iNumCtrlPts As Integer
    Dim iDimension As Integer
    Dim iOrder As Integer
    Dim iPeriodicity As Integer
    Dim iSplineArraySize As Integer
    Dim dTmpValue1 As Double
    Dim dTmpValue2 As Double
    Dim iSplineIndex As Integer
    Dim iVarIndex As Integer
```

```
    dTmpValue1 = varSplineParams(0)
    ExtractFields dTmpValue1, iDimension, iOrder
    dTmpValue2 = varSplineParams(1)
    ExtractFields dTmpValue2, iNumCtrlPts, iPeriodicity
    iNumKnots = iOrder + iNumCtrlPts
    iSplineArraySize = 2 + iNumKnots + (iDimension * iNumCtrlPts)
    Dim dSplineParams() As Double
    ReDim dSplineParams(iSplineArraySize - 1)
```

```
    ' Set Property Array
    dSplineParams(0) = dTmpValue1
    dSplineParams(1) = dTmpValue2
```

```
    ' Set Knot Vector
    iSplineIndex = 2
    iVarIndex = 2
    Dim i As Long
    For i = 0 To (iNumKnots - 1)
        dSplineParams(iSplineIndex) = varSplineParams(iVarIndex)
        iSplineIndex = iSplineIndex + 1
        iVarIndex = iVarIndex + 1
    Next i
```

```
    ' Set Control Point Vector
    For i = 0 To (iNumCtrlPts - 1)
        Dim j As Long
        For j = 1 To iDimension
            dSplineParams(iSplineIndex) = varSplineParams(iVarIndex)
            iSplineIndex = iSplineIndex + 1
            iVarIndex = iVarIndex + 1
        Next j
    Next i
```

```
    Dim varSplinePtParams As Variant
    varSplinePtParams = dSplineParams
    Dim varSplinePts As Variant
    varSplinePts = swCurveIn.GetSplinePts((varSplinePtParams))
```

```
    DumpSplineInfo varSplinePts
```

```
End Sub
```

```
Sub Curve_GetSplinePts2()
    Dim swApp As SldWorks.SldWorks
    Dim Part As SldWorks.ModelDoc2
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set Part = swApp.ActiveDoc
    Dim swSelectMgr As SldWorks.SelectionMgr
    Set swSelectMgr = Part.SelectionManager
    Dim swSketchSeg As SldWorks.SketchSegment
    Set swSketchSeg = swSelectMgr.GetSelectedObject3(1)
    Dim swCurveIn As SldWorks.Curve
    Set swCurveIn = swSketchSeg.GetCurve
    Dim varSplineParams As Variant
```

```
    ' False - do not want a cubic spline
    varSplineParams = swCurveIn.GetBCurveParams(False)
    Dim varSplinePts As Variant
    varSplinePts = swCurveIn.GetSplinePts((varSplineParams))
```

```
    DumpSplineInfo varSplinePts
```

```
End Sub
```
