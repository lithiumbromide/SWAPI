---
title: "Evaluate Curves Defined in Sketch Space Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Evaluate_Curves_Defined_in_Sketch_Space_Example_VB.htm"
---

# Evaluate Curves Defined in Sketch Space Example (VBA)

This example shows how to evaluate curves that were defined in the space of a sketch.

```
'---------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Selects a sketch, opens the sketch, and selects a curve
'    in that sketch.
' 3. Evaluates the curve.
' 4. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-----------------------------------------------------------
```

```
Option Explicit
```

```
' Define two types
Type DoubleRec
    dValue As Double
End Type
```

```
Type Long2Rec
    iLower As Long
    iUpper As Long
End Type
```

```
' Extract two integer values from a single double value
' by assigning a DoubleRec to the double value and then
' copying the value to Long2Rec and
' extracting the integer values
Function ExtractFields(ByVal dValue As Double, iLower As Long, iUpper As Long)
```

```
    Dim dr                  As DoubleRec
    Dim i2r                 As Long2Rec
```

```
    ' Set the double value
    dr.dValue = dValue
```

```
    ' Copy the values
    LSet i2r = dr
```

```
    ' Extract the values
    iLower = i2r.iLower
    iUpper = i2r.iUpper
```

```
End Function
```

```
Sub ProcessCurve(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swCurve As SldWorks.Curve)
```

```
    Dim swMathUtil          As SldWorks.MathUtility
    Dim swXform             As SldWorks.MathTransform
    Dim nStartParam         As Double
    Dim nEndParam           As Double
    Dim bIsClosed           As Boolean
    Dim bIsPeriodic         As Boolean
    Dim vStartEval          As Variant
    Dim vEndEval            As Variant
    Dim nSuccessStart       As Long
    Dim nEndStart           As Long
    Dim nDummy              As Long
    Dim nStartPt(2)         As Double
    Dim vStartPt            As Variant
    Dim swStartPt           As SldWorks.MathPoint
    Dim nStartTanPt(2)      As Double
    Dim vStartTanPt         As Variant
    Dim swStartTanPt        As SldWorks.MathPoint
    Dim nEndPt(2)           As Double
    Dim vEndPt              As Variant
    Dim swEndPt             As SldWorks.MathPoint
    Dim nEndTanPt(2)        As Double
    Dim vEndTanPt           As Variant
    Dim swEndTanPt          As SldWorks.MathPoint
    Dim bRet                As Boolean
```

```
    Set swMathUtil = swApp.GetMathUtility
    Set swXform = swSketch.ModelToSketchTransform
    Set swXform = swXform.Inverse
    bRet = swCurve.GetEndParams(nStartParam, nEndParam, bIsClosed, bIsPeriodic): Debug.Assert bRet
    vStartEval = swCurve.Evaluate(nStartParam)
    vEndEval = swCurve.Evaluate(nEndParam)
```

```
    ExtractFields vStartEval(6), nSuccessStart, nDummy
    ExtractFields vEndEval(6), nEndStart, nDummy
    nStartPt(0) = vStartEval(0):        nStartPt(1) = vStartEval(1):        nStartPt(2) = vStartEval(2)
    vStartPt = nStartPt
    Set swStartPt = swMathUtil.CreatePoint((vStartPt))
    Set swStartPt = swStartPt.MultiplyTransform(swXform)
```

```
    nStartTanPt(0) = vStartEval(3):     nStartTanPt(1) = vStartEval(4):     nStartTanPt(2) = vStartEval(5)
    vStartTanPt = nStartTanPt
    Set swStartTanPt = swMathUtil.CreatePoint((vStartTanPt))
    Set swStartTanPt = swStartPt.MultiplyTransform(swXform)
```

```
    nEndPt(0) = vEndEval(0):            nEndPt(1) = vEndEval(1):            nEndPt(2) = vEndEval(2)
    vEndPt = nEndPt
    Set swEndPt = swMathUtil.CreatePoint((vEndPt))
    Set swEndPt = swEndPt.MultiplyTransform(swXform)
```

```
    nEndTanPt(0) = vEndEval(3):         nEndTanPt(1) = vEndEval(4):         nEndTanPt(2) = vEndEval(5)
    vEndTanPt = nEndTanPt
    Set swEndTanPt = swMathUtil.CreatePoint((vEndTanPt))
    Set swEndTanPt = swEndPt.MultiplyTransform(swXform)
```

```
    Debug.Print "IsClosed       = " & bIsClosed
    Debug.Print "IsPeriodic     = " & bIsPeriodic
    Debug.Print ""
```

```
    Debug.Print "Start (sketch)"
    Debug.Print "  Point        = (" & vStartEval(0) * 1000# & ", " & vStartEval(1) * 1000# & ", " & vStartEval(2) * 1000# & ") mm"
    Debug.Print "  Tangent      = (" & vStartEval(3) & ", " & vStartEval(4) & ", " & vStartEval(5) & ")"
    Debug.Print "  Success      = " & nSuccessStart
```

```
    Debug.Print "Finish (sketch)"
```

```
    Debug.Print "  Point        = (" & vEndEval(0) * 1000# & ", " & vEndEval(1) * 1000# & ", " & vEndEval(2) * 1000# & ") mm"
    Debug.Print "  Tangent      = (" & vEndEval(3) & ", " & vEndEval(4) & ", " & vEndEval(5) & ")"
    Debug.Print "  Success      = " & nEndStart
```

```
    Debug.Print "Start (model)"
```

```
    Debug.Print "  Point        = (" & swStartPt.ArrayData(0) * 1000# & ", " & swStartPt.ArrayData(1) * 1000# & ", " & swStartPt.ArrayData(2) * 1000# & ") mm"
    Debug.Print "  Tangent      = (" & swStartTanPt.ArrayData(0) & ", " & swStartTanPt.ArrayData(1) & ", " & swStartTanPt.ArrayData(2) & ")"
    Debug.Print "Finish (model)"
```

```
    Debug.Print "  Point        = (" & swEndPt.ArrayData(0) * 1000# & ", " & swEndPt.ArrayData(1) * 1000# & ", " & swEndPt.ArrayData(2) * 1000# & ") mm"
    Debug.Print "  Tangent      = (" & swEndTanPt.ArrayData(0) & ", " & swEndTanPt.ArrayData(1) & ", " & swEndTanPt.ArrayData(2) & ")"
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp               As SldWorks.SldWorks
    Dim swModel             As SldWorks.ModelDoc2
    Dim swModelDocExt       As SldWorks.ModelDocExtension
    Dim swSelMgr            As SldWorks.SelectionMgr
    Dim swSkSeg             As SldWorks.SketchSegment
    Dim swSketch            As SldWorks.Sketch
    Dim swCurve             As SldWorks.Curve
    Dim errors              As Long
    Dim warnings            As Long
    Dim fileName            As String
    Dim status              As Boolean
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cstick.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    swModel.EditSketch
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0.142211893757474, 3.33699273467745E-02, -1.57877105588811E-02, False, 0, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    Set swSkSeg = swSelMgr.GetSelectedObject6(1, -1)
    Set swSketch = swSkSeg.GetSketch
    Set swCurve = swSkSeg.GetCurve
```

```
    ProcessCurve swApp, swModel, swSketch, swCurve
```

```
End Sub
```
