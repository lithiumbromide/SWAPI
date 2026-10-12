---
title: "Get Parameters and Spline Points for Curve Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Parameters_and_Spline_Points_for_Curve_Example_VB.htm"
---

# Get Parameters and Spline Points for Curve Example (VBA)

This example shows how to get the parameters and spline points for the selected spline.

```
'----------------------------------------
' Preconditions:
' 1. Verify that the specified part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Selects a spline in a sketch.
' 3. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'-----------------------------------------
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
    iLower As Long ' Assuming that a C integer has 4 bytes
    iUpper As Long
End Type
```

```
' Extract two integer values out of a single double value
' by assigning a DoubleRec to the double value,
' copying the value over an Long2Rec, and
' extracting the integer values
Function ExtractFields(ByVal dValue As Double, iLower As Integer, iUpper As Integer)
    Dim dr As DoubleRec
    Dim i2r As Long2Rec
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
End Function
```

```
Sub DumpModelerSettings(swModeler As SldWorks.Modeler)
```

```
    ' Dump modeler settings
    Debug.Print "Modeler Settings:"
    Debug.Print "  BSCurveOutputTol                 = " & swModeler.GetToleranceValue(swBSCurveOutputTol)
    Debug.Print "  BSCurveNonRationalOutputTol      = " & swModeler.GetToleranceValue(swBSCurveNonRationalOutputTol)
    Debug.Print "  UVCurveOutputTol                 = " & swModeler.GetToleranceValue(swUVCurveOutputTol)
    Debug.Print "  SurfChordTessellationTol         = " & swModeler.GetToleranceValue(swSurfChordTessellationTol)
    Debug.Print "  SurfAngularTessellationTol       = " & swModeler.GetToleranceValue(swSurfAngularTessellationTol)
    Debug.Print "  CurveChordTessellationTol        = " & swModeler.GetToleranceValue(swCurveChordTessellationTol)
    Debug.Print ""
End Sub
```

```
Sub DumpBCurveInfo(vBCurveParam As Variant)
```

```
    Dim nDim As Integer
    Dim nOrder As Integer
    Dim nCtrlPoints As Integer
    Dim nPeriodicity As Integer
    Dim nNumKnots As Integer
    Dim i As Integer
```

```
    ExtractFields vBCurveParam(0), nDim, nOrder
    ExtractFields vBCurveParam(1), nCtrlPoints, nPeriodicity
```

```
    nNumKnots = nOrder + nCtrlPoints
```

```
    Debug.Print "  Dimension                 = " & nDim
    Debug.Print "  Order                     = " & nOrder
    Debug.Print "  Number Control Points     = " & nCtrlPoints
    Debug.Print "  Periodicity               = " & nPeriodicity
    Debug.Print "  Num Knots                 = " & nNumKnots
```

```
    Debug.Print ""
```

```
    For i = 0 To nNumKnots - 1
        ' Knot weights should be increasing monotonically
        Debug.Print "  Knot(" & i & ")          = " & vBCurveParam(2 + i)
    Next i
```

```
    Debug.Print ""
```

```
    If 3 = nDim Then
        For i = 2 + nNumKnots To UBound(vBCurveParam) - 1 Step 3
            Debug.Print "  Ctrl(" & (i - 2 - nNumKnots) / 3 & ")          = (" & vBCurveParam(i + 0) * 1000# & ", " & vBCurveParam(i + 1) * 1000# & ", " & vBCurveParam(i + 2) * 1000# & ") mm"
        Next i
    Else
        For i = 2 + nNumKnots To UBound(vBCurveParam) - 1 Step 4
            Debug.Print "  Ctrl(" & (i - 2 - nNumKnots) / 4 & ")          = (" & vBCurveParam(i + 0) * 1000# & ", " & vBCurveParam(i + 1) * 1000# & ", " & vBCurveParam(i + 2) * 1000# & ") mm [" & vBCurveParam(i + 3) & "]"
        Next i
    End If
End Sub
```

```
Sub DumpSplineInfo(vSplinePts As Variant)
    Dim i As Long
```

```
    For i = 0 To UBound(vSplinePts) Step 3
        Debug.Print "  SplinePt(" & i / 3 & ")     = (" & vSplinePts(i + 0) * 1000# & ", " & vSplinePts(i + 1) * 1000# & ", " & vSplinePts(i + 2) * 1000# & ") mm"
    Next i
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModeler As SldWorks.Modeler
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSketch As SldWorks.Sketch
    Dim swSketchSegment As SldWorks.SketchSegment
    Dim swCurve As SldWorks.Curve
    Dim vBCurveParam As Variant
    Dim vSplinePts As Variant
    Dim i As Long
    Dim bRet As Boolean
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
```

```
    Set swApp = Application.SldWorks
    Set swModeler = swApp.GetModeler
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\molds\telephone.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    bRet = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    swModel.EditSketch
    swModel.ClearSelection2 True
    bRet = swModelDocExt.SelectByID2("Spline2", "SKETCHSEGMENT", 6.21547510219904E-02, 0.111861721213803, 5.89464775348876E-02, False, 0, Nothing, 0)
    Set swSketchSegment = swSelMgr.GetSelectedObject6(1, -1)
    Set swCurve = swSketchSegment.GetCurve
```

```
    DumpModelerSettings swModeler
```

```
    vBCurveParam = swCurve.GetBCurveParams(False)
    vSplinePts = swCurve.GetSplinePts(vBCurveParam)
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    DumpBCurveInfo vBCurveParam
```

```
    Debug.Print "  -------------------------------------------"
```

```
    Debug.Assert Not IsNull(vSplinePts)
```

```
    DumpSplineInfo vSplinePts
```

```
    Debug.Print "  -------------------------------------------"
```

```
End Sub
```
