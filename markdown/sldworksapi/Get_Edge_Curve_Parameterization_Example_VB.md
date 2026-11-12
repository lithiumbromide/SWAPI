---
title: "Get Edge Curve Parameterization Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Edge_Curve_Parameterization_Example_VB.htm"
---

# Get Edge Curve Parameterization Example (VBA)

This example shows how to get curve parameterization data for a selected edge.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a part or assembly.
' 2. If you opened an assembly, ensure that it is
'    fully resolved.
' 3. Select an edge.
' 4. Open the Immediate window.
'
' Postconditions: Inspect the Immediate window.
'-----------------------------------------------
```

```vb
 Option Explicit
Sub main()

     Dim swApp As SldWorks.SldWorks
     Dim Part As SldWorks.ModelDoc2

    Set swApp = CreateObject("SldWorks.Application")
     Set Part = swApp.ActiveDoc
    Dim swSelectMgr As SldWorks.SelectionMgr
     Set swSelectMgr = Part.SelectionManager
    Dim swEdge As SldWorks.Edge
     Set swEdge = swSelectMgr.GetSelectedObject5(1)

    Dim swCurve As SldWorks.Curve
     Dim swCurveParaData As SldWorks.CurveParamData
     Set swCurve = swEdge.GetCurve
     Set swCurveParaData = swEdge.GetCurveParams3

    Debug.Print "The curve tag is: " & swCurveParaData.CurveTag
     Debug.Print "The curve type as defined in swCurveType_e is: " & swCurveParaData.CurveType

    Dim vEndPoint As Variant
     vEndPoint = swCurveParaData.EndPoint
     Dim EndPoint(2) As Double

    Dim i As Long

    For i = 0 To UBound(vEndPoint)
         EndPoint(i) = vEndPoint(i)
     Next i

    Debug.Print "The end point x,y,z coordinates are: " & EndPoint(0) & "," & EndPoint(1) & "," & EndPoint(2)

    Dim vStartPoint As Variant
     Dim StartPoint(2) As Double
     vStartPoint = swCurveParaData.StartPoint
     For i = 0 To UBound(vStartPoint)
         StartPoint(i) = vStartPoint(i)
     Next i

    Debug.Print "The start point x,y,z coordinates are: " & StartPoint(0) & "," & StartPoint(1) & "," & StartPoint(2)

    Debug.Print "The curve and edge are in the same direction: " & swCurveParaData.Sense
     Debug.Print "The maximum U parameter value is: " & swCurveParaData.UMaxValue
     Debug.Print "The minimum U parameter value is: " & swCurveParaData.UMinValue

 End Sub
```
