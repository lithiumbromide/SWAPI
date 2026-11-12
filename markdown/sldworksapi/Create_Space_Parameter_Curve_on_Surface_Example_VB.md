---
title: "Create Space Parameter Curve on Surface Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Space_Parameter_Curve_on_Surface_Example_VB.htm"
---

# Create Space Parameter Curve on Surface Example (VBA)

This example shows how to create a space parameter (SP) curve on a surface. This example also shows how to pack integers into doubles.

```
'----------------------------------------------
' Preconditions:
' 1. Open a part or assembly.
' 2. Select a face.
'
' Postconditions:
' 1. Creates a 3D sketch that contains a curve lying
'    on selected face.
' 2. Examine the graphics area.
'
' NOTES:
' * Sketch contains a tessellated approximation of
'   the curve lying on the selected face
' * Control points are a random selection of U-V-W
'   values.
'----------------------------------------------
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
Type Int2Rec
    iLower As Long ' C int has 4 bytes
    iUpper As Long
End Type
```

```
Sub CreateTessCurve(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swTrimCurve As SldWorks.Curve)
```

```
    Const nChordTol             As Double = 0.001
    Const nLengthTol            As Double = 0.001
    Dim nStartParam             As Double
    Dim nEndParam               As Double
    Dim bIsClosed               As Boolean
    Dim bIsPeriodic             As Boolean
    Dim vStartPt                As Variant
    Dim vEndPt                  As Variant
    Dim vTessPts                As Variant
    Dim swSketchSeg             As SldWorks.SketchSegment
    Dim bRet                    As Boolean
    Dim i                       As Long
```

```
    ' Not really needed because curve is a trimmed curve,
    ' so could pass in trim points as parameters
    bRet = swTrimCurve.GetEndParams(nStartParam, nEndParam, bIsClosed, bIsPeriodic): Debug.Assert bRet
```

```
    vStartPt = swTrimCurve.Evaluate(nStartParam)
    vEndPt = swTrimCurve.Evaluate(nEndParam)
```

```
    vTessPts = swTrimCurve.GetTessPts(nChordTol, nLengthTol, (vStartPt), (vEndPt))
```

```
    swModel.Insert3DSketch2 False
```

```
    swModel.SetAddToDB True
```

```
    swModel.SetDisplayWhenAdded False
```

```
    ' Disable Visual Basic range checking because tessellation points
    ' may not be a multiple of 6
    On Error Resume Next
    For i = 0 To UBound(vTessPts) Step 3
        Set swSketchSeg = swModel.CreateLine2(vTessPts(i + 0), vTessPts(i + 1), vTessPts(i + 2), vTessPts(i + 3), vTessPts(i + 4), vTessPts(i + 5))
    Next i
```

```
    On Error GoTo 0
```

```
    swModel.SetDisplayWhenAdded True
    swModel.SetAddToDB False
```

```
    swModel.Insert3DSketch2 True
```

```
    bRet = swModel.EditRebuild3: Debug.Assert bRet
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp                           As SldWorks.SldWorks
    Dim swModeler                       As SldWorks.Modeler
    Dim swModel                         As SldWorks.ModelDoc2
    Dim swSelMgr                        As SldWorks.SelectionMgr
    Dim swFace                          As SldWorks.Face2
    Dim swSurf                          As SldWorks.Surface
    Dim vProps                          As Variant
    Dim nProp(1)                        As Double
    Dim i2rDim_Order                    As Int2Rec
    Dim i2rNumCtrlPt_Period             As Int2Rec
    Dim nDummy1                         As DoubleRec
    Dim nDummy2                         As DoubleRec
    Dim swCurve                         As SldWorks.Curve
    Dim nKnot(9)                        As Double
    Dim vKnot                           As Variant
    Dim nCtrlPt(8)                      As Double
    Dim vCtrlPt                         As Variant
```

```
    Set swApp = Application.SldWorks
    Set swModeler = swApp.GetModeler
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
    Set swSurf = swFace.GetSurface
```

```
    ' Dimension of control points 'dim':
    '   * For rational curves 'dim' = 3
    '   * For non-rational curves 'dim' = 2
    i2rDim_Order.iLower = 3
```

```
    ' Order of the curve 'order':
    '   * The order of the curve = degree + 1
    '   * The minimum order is 2
    i2rDim_Order.iUpper = 3
```

```
    ' Number of control points 'nctrl': 'nctrl' >= 'order'
    i2rNumCtrlPt_Period.iLower = 3
```

```
    ' Periodic flag 'period':
    '   * For periodic curve = 1
    '   * For non-periodic curve = 0
    i2rNumCtrlPt_Period.iUpper = 0
    LSet nDummy1 = i2rDim_Order
    LSet nDummy2 = i2rNumCtrlPt_Period
    nProp(0) = nDummy1.dValue
    nProp(1) = nDummy2.dValue
```

```
    vProps = nProp
```

```
    ' Knot vector 'knots': The knot values must form a non-decreasing sequence
    nKnot(0) = 0.09
    nKnot(1) = 0.1
    nKnot(2) = 0.2
    nKnot(3) = 0.3
    nKnot(4) = 0.4
    nKnot(5) = 0.5
    nKnot(6) = 0.6
    nKnot(7) = 0.7
    nKnot(8) = 0.8
    nKnot(9) = 0.9
    vKnot = nKnot
```

```
    ' Control points 'ctrl':
    '   * For non-rational curves, the control
    '     points are points in the parameter space of 'surf';
    '     they must be supplied as [u0,v0,u1,v1...]
    '   * For rational curves each vector contains a point in parameter space
    '     followed by a weight for the point; the points are supplied
    '[u0,v0,w0,u1,v1,w1...]; the weights must be positive
    nCtrlPt(0) = 168.441616909048 / 1000#:  nCtrlPt(1) = 150.079444300104 / 1000#:  nCtrlPt(2) = 361.067614130377 / 1000#
    nCtrlPt(3) = 200.587021030302 / 1000#:  nCtrlPt(4) = 133.788963935729 / 1000#:  nCtrlPt(5) = 15.7123672133821 / 1000#
    nCtrlPt(6) = 454.553312070037 / 1000#:  nCtrlPt(7) = 78.0558561766611 / 1000#:  nCtrlPt(8) = 1.00713763464455 / 1000#
    vCtrlPt = nCtrlPt
```

```
    ' Eventually goes down to CRSPCU, which is equivalent to:
    '   * PK_CURVE_embed_in_surf
    '   * PK_SPCURVE_create
    Set swCurve = swModeler.CreatePCurve(swSurf, (vProps), (vKnot), (vCtrlPt))
    Debug.Assert Not swCurve Is Nothing
    Debug.Assert swCurve.IsTrimmedCurve
```

```
    CreateTessCurve swApp, swModel, swCurve
```

```
End Sub
```
