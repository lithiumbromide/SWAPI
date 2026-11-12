---
title: "Zoom to Region Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Zoom_to_Region_Example_VB.htm"
---

# Zoom to Region Example (VBA)

This example shows how to zoom to a specific region.

```vb
'------------------------------------------------------------------
' Problem:
'       This sample code shows how to use:
'
'           IModelDoc2::ViewZoomTo2
'
'       The input parameters may not be obvious, but
'       they are related to the current view orientation.
'       The code shows how to transform points
'       from model space so that the resulting view is
'       zoomed to points selected in model space.
'
' Preconditions:
'       (1) Part or assembly is open.
'       (2) Two points are picked in the graphics window.
'
' Postconditions:
'       Graphics area is zoomed to minimally include
'       the two selection points.
'
'------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swModView               As SldWorks.ModelView
    Dim swViewOrient            As SldWorks.MathTransform
    Dim swSelMgr                As SldWorks.SelectionMgr
    Dim swMathUtil              As SldWorks.MathUtility
    Dim vSelPt1                 As Variant
    Dim vSelPt2                 As Variant
    Dim swSelPt1                As SldWorks.MathPoint
    Dim swSelPt2                As SldWorks.MathPoint
    Dim i                       As Long
    Dim bRet                    As Boolean
    Set swApp = CreateObject("SldWorks.Application")
    Set swMathUtil = swApp.GetMathUtility
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swModView = swModel.ActiveView
    Set swViewOrient = swModView.Orientation3

    vSelPt1 = swSelMgr.GetSelectionPoint(1)
    vSelPt2 = swSelMgr.GetSelectionPoint(2)

    Set swSelPt1 = swMathUtil.CreatePoint((vSelPt1))
    Set swSelPt2 = swMathUtil.CreatePoint((vSelPt2))
    Set swSelPt1 = swSelPt1.MultiplyTransform(swViewOrient)
    Set swSelPt2 = swSelPt2.MultiplyTransform(swViewOrient)

    swModel.ViewZoomTo2 _
        swSelPt1.ArrayData(0), swSelPt1.ArrayData(1), swSelPt1.ArrayData(2), _
        swSelPt2.ArrayData(0), swSelPt2.ArrayData(1), swSelPt2.ArrayData(2)
End Sub
'-------------------------------------------
```
