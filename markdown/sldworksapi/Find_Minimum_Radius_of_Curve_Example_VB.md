---
title: "Find Minimum Radius of Curve (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Find_Minimum_Radius_of_Curve_Example_VB.htm"
---

# Find Minimum Radius of Curve (VBA)

This example shows how to get the minimum radius of the selected curve.

```vb
'----------------------------------
' Preconditions: Model  document is open and a curve
'                on a part is selected.
'
' Postconditions: None
'----------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swDoc As SldWorks.ModelDoc2
Dim selMgr As SldWorks.SelectionMgr
Dim swEdge As SldWorks.Edge
Dim swCurve As SldWorks.Curve
Dim param(1) As Double
Dim isClose As Boolean
Dim isPeriodic As Boolean
Dim retPar As Boolean
Dim test As Double
Dim status As Boolean
Dim BoundSuf As Variant
Dim numOfRadius As Long
Dim radius As Variant
Dim location As Variant
Dim uvparameter As Variant
Dim locationDisp1 As SldWorks.MathPoint
Dim arrayData1 As Variant

Sub main()

Set swApp = Application.SldWorks
Set swDoc = swApp.ActiveDoc
Set selMgr = swDoc.SelectionManager
Set swEdge = selMgr.GetSelectedObject6(1, -1)
' Get the selected curve
Set swCurve = swEdge.GetCurve

retPar = swCurve.GetEndParams(param(0), param(1), isClose, isPeriodic)
BoundSuf = param
status = swCurve.FindMinimumRadius(BoundSuf, numOfRadius, radius, location, uvparameter)

'Assume that numOfRadius output is 1

Debug.Print ("Radius")
Debug.Print (radius(0))

Set locationDisp1 = location(0)
arrayData1 = locationDisp1.ArrayData

Debug.Print ("Location")
Debug.Print (arrayData1(0))
Debug.Print (arrayData1(1))
Debug.Print (arrayData1(2))

Debug.Print ("Parameter")
Debug.Print (uvparameter(0))

End Sub
```
