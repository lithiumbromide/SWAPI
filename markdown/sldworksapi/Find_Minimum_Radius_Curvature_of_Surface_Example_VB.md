---
title: "Find Minimum Radius Curvature of Surface (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Find_Minimum_Radius_Curvature_of_Surface_Example_VB.htm"
---

# Find Minimum Radius Curvature of Surface (VBA)

This example shows how to find the minimum radius of curvature for the selected surface.

```vb
'---------------------------------------------
' Preconditions: Model document is open and a surface is selected.
'
' Postconditions: None
' --------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swDoc As SldWorks.ModelDoc2
Dim selMgr As SldWorks.SelectionMgr
Dim swface As SldWorks.Face2
Dim swSurface As SldWorks.Surface
Dim paraVar As Variant
Dim uBoundArray(1) As Double
Dim vBoundArray(1) As Double
Dim test As Double
Dim status As Boolean
Dim uBoundSuf As Variant
Dim vBoundSuf As Variant
Dim vFaceUV As Variant
Dim numOfRadius As Long
Dim radius As Variant
Dim location As Variant
Dim uvparameter As Variant
Dim locationDisp1 As SldWorks.MathPoint
Dim arrayDataLoc1 As Variant
Dim locationDisp2 As SldWorks.MathPoint
Dim arrayDataLoc2 As Variant
Dim uvParamDisp1 As SldWorks.MathPoint
Dim arrayDataUV1 As Variant
Dim uvParamDisp2 As SldWorks.MathPoint
Dim arrayDataUV2 As Variant
Dim arrayData1 As Variant
Dim arrayData2 As Variant
Dim I As Long

Sub main()

Set swApp = Application.SldWorks
Set swDoc = swApp.ActiveDoc
Set selMgr = swDoc.SelectionManager
Set swface = selMgr.GetSelectedObject6(1, -1)
Set swSurface = swface.GetSurface
vFaceUV = swface.GetUVBounds
paraVar = swSurface.Parameterization

uBoundArray(0) = vFaceUV(0)
uBoundArray(1) = vFaceUV(1)
vBoundArray(0) = vFaceUV(2)
vBoundArray(1) = vFaceUV(3)
uBoundSuf = uBoundArray
vBoundSuf = vBoundArray
status = swSurface.FindMinimumRadius(uBoundSuf, vBoundSuf, numOfRadius, radius, location, uvparameter)

'Assume that numOfRadius output is 2

Set locationDisp1 = location(0)
arrayData1 = locationDisp1.ArrayData
Set locationDisp2 = location(1)
arrayData2 = locationDisp2.ArrayData

Set uvParamDisp1 = uvparameter(0)
arrayData1 = uvParamDisp1.ArrayData
Set uvParamDisp2 = uvparameter(1)
arrayData2 = uvParamDisp2.ArrayData

Debug.Print ("Printing radius:-")
For I = 0 To (numOfRadius - 1)
    Debug.Print (radius(I))
Next I

Debug.Print ("Location")
Debug.Print (arrayData1(0))
Debug.Print (arrayData1(1))
Debug.Print (arrayData1(2))
Debug.Print (arrayData2(0))
Debug.Print (arrayData2(1))
Debug.Print (arrayData2(2))

Debug.Print ("UVParameter")
Debug.Print (arrayData1(0))
Debug.Print (arrayData1(1))
Debug.Print (arrayData1(2))
Debug.Print (arrayData2(0))
Debug.Print (arrayData2(1))
Debug.Print (arrayData2(2))

End Sub
```
