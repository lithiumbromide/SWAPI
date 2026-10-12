---
title: "Get Edge Curve Parameterization Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Edge_Curve_Parameterization_Example_VBNET.htm"
---

# Get Edge Curve Parameterization Example (VB.NET)

This example shows how to get curve parameterization data for a selected edge.

```vb
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()
         Dim swApp As SldWorks
         Dim Part As ModelDoc2

         swApp = CreateObject("SldWorks.Application")
         Part = swApp.ActiveDoc

         Dim swSelectMgr As SelectionMgr
         swSelectMgr = Part.SelectionManager

         Dim swEdge As Edge
         swEdge = swSelectMgr.GetSelectedObject5(1)

         Dim swCurve As Curve
         Dim swCurveParaData As CurveParamData
         swCurve = swEdge.GetCurve
         swCurveParaData = swEdge.GetCurveParams3

         Debug.Print("The curve tag is: " & swCurveParaData.CurveTag)
         Debug.Print("The curve type as defined in swCurveType_e is: " & swCurveParaData.CurveType)

         Dim vEndPoint As Object
         vEndPoint = swCurveParaData.EndPoint
         Dim EndPoint(2) As Double

         Dim i As  Long

         For i = 0 To UBound(vEndPoint)
             EndPoint(i) = vEndPoint(i)
         Next i

         Debug.Print("The end point x,y,z coordinates are: " & EndPoint(0)   "," & EndPoint(1) & "," & EndPoint(2))

         Dim vStartPoint As Object
         Dim StartPoint(2) As Double
         vStartPoint = swCurveParaData.StartPoint
         For i = 0 To UBound(vStartPoint)
             StartPoint(i) = vStartPoint(i)
         Next i

         Debug.Print("The start point x,y,z coordinates are: " & StartPoint(0) & "," & StartPoint(1) & "," & StartPoint(2))

         Debug.Print("The curve and edge are in the same direction: " & swCurveParaData.Sense)
         Debug.Print("The maximum U parameter value is: " & swCurveParaData.UMaxValue)
         Debug.Print("The minimum U parameter value is: " & swCurveParaData.UMinValue)

     End Sub

     Public swApp As SldWorks

 End  Class
```
