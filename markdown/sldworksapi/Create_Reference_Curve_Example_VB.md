---
title: "Create Reference Curve Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Reference_Curve_Example_VB.htm"
---

# Create Reference Curve Example (VBA)

This example shows how to create a reference curve by first creating a temporary spline curve.

```
'----------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Adds a reference curve to the part document.
' 3. Selects an endpoint on the reference curve
'    and prints to the Immediate window the
'    endpoint's position and coordinates.
' 4. Examine the graphics area and Immediate window.
'----------------------------------------------------------
```

```
Option Explicit
```

```
'Type definitions
Type DoubleRec
    dValue As Double
End Type
```

```
Type Int2Rec
    iLower As Long      '1 Integer is 4 bytes
    iUpper As Long
End Type
```

```
'Pack 2 integers to 1 Double
Function ImportFields(iLower As Integer, iUpper As Integer, dValue As Double)
    Dim dr As DoubleRec
    Dim i2r As Int2Rec
```

```
    i2r.iLower = iLower
    i2r.iUpper = iUpper
    LSet dr = i2r
    dValue = dr.dValue
```

```
End Function
```

```
Sub main()

    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swPart As SldWorks.PartDoc
    Dim swBody As SldWorks.Body2
    Dim swCurve(0) As SldWorks.Curve
    Dim vCurve As Variant
    Dim swRefCurve As SldWorks.ReferenceCurve
    Dim swSelObj As Object
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swEdgePoint As SldWorks.EdgePoint
    Dim bRet As Boolean
    Dim nRetVal As Long
    Dim iDim As Integer
    Dim iOrd As Integer
    Dim incp As Integer
    Dim iper As Integer
    Dim dprops(1) As Double
    Dim knots(9) As Double
    Dim cPoints(17) As Double
    Dim vprops As Variant
    Dim vknots As Variant
    Dim vcPoints As Variant
    Dim selType As Long
    Dim x As Double
    Dim y As Double
    Dim z As Double
```

```
    'Open new part document and create a body
    Set swApp = Application.SldWorks
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
    Set swPart = swModel
    Set swBody = swPart.CreateNewBody
```

```
    'Create a curve
    'Set properties
    iDim = 3: iOrd = 4: incp = 6: iper = 0
    ImportFields iDim, iOrd, dprops(0)
    ImportFields incp, iper, dprops(1)
    vprops = dprops
```

```
    'Set knots
    knots(0) = 0: knots(1) = 0: knots(2) = 0: knots(3) = 0
    knots(4) = 0.33096: knots(5) = 0.72
    knots(6) = 1: knots(7) = 1: knots(8) = 1: knots(9) = 1
    vknots = knots
```

```
    'Set control points
    cPoints(0) = 0: cPoints(1) = 0: cPoints(2) = 0
    cPoints(3) = 0.008703: cPoints(4) = 0.016501: cPoints(5) = 0
    cPoints(6) = 0.027636: cPoints(7) = 0.052399: cPoints(8) = 0
    cPoints(9) = 0.069472: cPoints(10) = -0.011297: cPoints(11) = 0
    cPoints(12) = 0.090421: cPoints(13) = 0.017622: cPoints(14) = 0
    cPoints(15) = 0.099188: cPoints(16) = 0.029725: cPoints(17) = 0
    vcPoints = cPoints
```

```
    'Create a spline curve
    Set swCurve(0) = swBody.AddProfileBspline((vprops), (vknots), (vcPoints))
    vCurve = swCurve
```

```
    'Create a reference curve
    Set swRefCurve = swModel.FeatureReferenceCurve(1, (vCurve), True, "", nRetVal)
```

```
    'Rebuild to display curve
    swModel.EditRebuild3
```

```
    'Get endpoint on reference curve
    Set swModelDocExt = swModel.Extension
    bRet = swModelDocExt.SelectByID2("Unknown", "POINTREF", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    selType = swSelMgr.GetSelectedObjectType3(1, -1)
    Debug.Print "Type of selection: " & selType
    If swSelectType_e.swSelPOINTREFS = selType Then
            Set swSelObj = swSelMgr.GetSelectedObject6(1, -1)
            Set swEdgePoint = swSelObj
            Debug.Print " Position of the endpoint: " & swEdgePoint.Position
            swEdgePoint.GetPointCoordinates x, y, z
            Debug.Print " Endpoint coordinates: " & x & ", " & y & ", and " & z
    End If
```

```
End Sub
```
