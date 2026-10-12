---
title: "Get Length of Edge Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Length_of_Edge_Example_VB.htm"
---

# Get Length of Edge Example (VBA)

This example shows how to get the length of an edge directly from the underlying curve and also from the display tessellation. The effect of the tolerance, when getting the curve tessellation, can be seen in the differences in the calculated lengths. This example exists primarily to show how to use ICurve::GetTessPts.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a part or fully resolved assembly.
' 2. Select an edge.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the length of the selected edge.
' 2. Examine the Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Public Const LINE_TYPE As Integer = 3001
Public Const CIRCLE_TYPE As Integer = 3002
Public Const ELLIPSE_TYPE As Integer = 3003
Public Const INTERSECTION_TYPE As Integer = 3004
Public Const BCURVE_TYPE As Integer = 3005
Public Const SPCURVE_TYPE As Integer = 3006
Public Const CONSTPARAM_TYPE As Integer = 3008
Public Const TRIMMED_TYPE As Integer = 3009
```

```
Function TessLength(vTessPts As Variant) As Double
    Dim i As Long
```

```
    For i = 0 To ((UBound(vTessPts) + 1) / 3 - 2)
        TessLength = TessLength + Sqr((vTessPts(3 * i + 0) - vTessPts(3 * i + 3)) ^ 2# + (vTessPts(3 * i + 1) - vTessPts(3 * i + 4)) ^ 2# + (vTessPts(3 * i + 2) - vTessPts(3 * i + 5)) ^ 2#)
    Next i
End Function
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swEdge As SldWorks.Edge
    Dim swCurve As SldWorks.Curve
    Dim bRet As Boolean
    Dim vCurveParam As Variant
    Dim StartPt(2) As Double
    Dim EndPt(2) As Double
    Dim vStartPt As Variant
    Dim vEndPt As Variant
    Dim vTessPts As Variant
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swEdge = swSelMgr.GetSelectedObject6(1, -1)
    Set swCurve = swEdge.GetCurve
    vCurveParam = swEdge.GetCurveParams2
    StartPt(0) = vCurveParam(0)
    StartPt(1) = vCurveParam(1)
    StartPt(2) = vCurveParam(2)
    EndPt(0) = vCurveParam(3)
    EndPt(1) = vCurveParam(4)
    EndPt(2) = vCurveParam(5)
    vStartPt = StartPt
    vEndPt = EndPt
```

```
    Debug.Print "CurveType   = " & swCurve.Identity
    Debug.Print "CurveLength = " & swCurve.GetLength2(vCurveParam(6), vCurveParam(7)) * 1000# & " mm"
    Debug.Print ""
```

```
    vTessPts = swCurve.GetTessPts(0.000001, 0.000001, (vStartPt), (vEndPt))
    Debug.Print "TessLength(" & UBound(vTessPts) & ")  = " & TessLength(vTessPts) * 1000# & " mm"
```

```
    vTessPts = swCurve.GetTessPts(0.00001, 0.00001, (vStartPt), (vEndPt))
    Debug.Print "TessLength(" & UBound(vTessPts) & ")  = " & TessLength(vTessPts) * 1000# & " mm"
```

```
    vTessPts = swCurve.GetTessPts(0.0001, 0.0001, (vStartPt), (vEndPt))
    Debug.Print "TessLength(" & UBound(vTessPts) & ")  = " & TessLength(vTessPts) * 1000# & " mm"
```

```
    vTessPts = swCurve.GetTessPts(0.001, 0.001, (vStartPt), (vEndPt))
    Debug.Print "TessLength(" & UBound(vTessPts) & ")  = " & TessLength(vTessPts) * 1000# & " mm"
```

```
    vTessPts = swCurve.GetTessPts(0.01, 0.01, (vStartPt), (vEndPt))
    Debug.Print "TessLength(" & UBound(vTessPts) & ")  = " & TessLength(vTessPts) * 1000# & " mm"
```

```
End Sub
```
