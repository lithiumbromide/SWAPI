---
title: "Create On-surface Spline Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_On-surface_Spline_Example_VB.htm"
---

# Create On-surface Spline Example (VBA)

This example shows how to create a spline constrained to a surface.

'----------------------------------------------------------------------------
' Preconditions: Open `public_documents`**\samples\tutorial\api\cstick.sldprt.**
'
' Postconditions:
' 1. Creates a 3D sketch of a spline on a surface.
' 2. Inspect the graphics area.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'----------------------------------------------------------------------------

```vb
Dim swApp As SldWorks.SldWorks
 Dim swCurFace As SldWorks.Face2
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim Part As SldWorks.ModelDoc2
 Dim skSegment As SldWorks.SketchSegment
 Dim pointArray As Variant
 Dim points() As Double
 Dim surfs As Variant
 Dim dirs As Variant
 Dim surfaceArr() As SldWorks.Surface
 Dim selType As Long
 Dim surfaceArrUbound As Long
 Dim statuses As Variant
 Dim boolstatus as Boolean
Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc

    ReDim points(0 To 11) As Double
     points(0) = -3.34270787209949E-02
     points(1) = 2.23913424029847E-02
     points(2) = 0.053671471463652
     points(3) = 1.53063989576147E-02
     points(4) = 4.78899892864157E-02
     points(5) = 2.50019220828396E-02
     points(6) = 5.11644715447442E-02
     points(7) = 2.72060072570875E-02
     points(8) = 5.78476387745854E-03
     points(9) = 2.59263831071606E-03
     points(10) = 2.62831648993199E-02
     points(11) = -0.053206707614433
     pointArray = points

    boolstatus = Part.Extension.SelectByRay(0.030303902514845, 2.86262382667246E-02, 3.85109058888133E-02, -0.577381545199981, -0.577287712085548, -0.577381545199979, 1.78932209693826E-03, 2, False, 0, 0)

    Set swSelMgr = Part.SelectionManager

    selType = swSelMgr.GetSelectedObjectType3(1, -1)
     surfaceArrUbound = -1
     If selType = swSelFACES Then
       Set swCurFace = swSelMgr.GetSelectedObject6(1, -1)
       surfaceArrUbound = surfaceArrUbound + 1
       ReDim Preserve surfaceArr(0 To surfaceArrUbound) As Surface
       Set surfaceArr(surfaceArrUbound) = swCurFace.GetSurface()
     End If
    surfs = surfaceArr

     'Set Direction parameter to Nothing to use the view vector of the current view
     'to project the points in the pointArray onto the surface in the surfs array
     Set skSegment = Part.SketchManager.CreateSpline3((pointArray), surfs, Nothing, True, statuses)
     Part.SketchManager.InsertSketch True
End Sub
```
