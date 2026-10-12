---
title: "Rotate Assembly Component on Axis Using IDragOperator::DragAsUI Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Assembly_Component_on_Axis_Example2_VB.htm"
---

# Rotate Assembly Component on Axis Using IDragOperator::DragAsUI Example (VBA)

This example shows how to rotate an assembly component about an assembly axis using IDragOperator::DragAsUI.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Assembly document is open.
 ' 2. Component in the assembly document is selected.
 '
 ' Postconditions: Transform matrix is set.
 '----------------------------------------------------------------------------
Option Explicit
 Const PI                As Double = 3.14159
 Const RadPerDeg         As Double = PI / 180#
'   DragOperator::TransformType
 '       Translation     0
 '       Transform is translation-only.
 '
 '       Axial rotation  1
 '       Transform is rotation-only.
 '
 '       General         2
 '       Transform can be translation, rotation, or both.
 '
 '   DragOperator::DragMode
 '       Minimum Move    0
 '       Move smallest number of geometries.
 '
 '       Maximum Move    1
 '       Move geometries rigidly if possible.
 '
 '       Relaxation      2
 '       Solve geometries using relaxation.
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swAssy                  As SldWorks.AssemblyDoc
     Dim swDragOp                As SldWorks.DragOperator
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swComp(1)               As SldWorks.Component2
     Dim vComp                   As Variant
     Dim swXform                 As SldWorks.MathTransform
     Dim swMathUtil              As SldWorks.MathUtility
     Dim swOriginPt              As SldWorks.MathPoint
     Dim swX_Axis                As SldWorks.MathVector
     Dim nPts(2)                 As Double
     Dim vData                   As Variant
     Dim i                       As Long
     Dim bRet                    As Boolean
    Set swApp = CreateObject("SldWorks.Application")
     Set swModel = swApp.ActiveDoc
     Set swAssy = swModel
     Set swDragOp = swAssy.GetDragOperator
     Set swSelMgr = swModel.SelectionManager
     Set swComp(0) = swSelMgr.GetSelectedObjectsComponent(1)
     Set swComp(1) = swSelMgr.GetSelectedObjectsComponent(2)
     Set swMathUtil = swApp.GetMathUtility
    vComp = swComp
    nPts(0) = 0#
     nPts(1) = 0#
     nPts(2) = 0#
    vData = nPts
    Set swOriginPt = swMathUtil.CreatePoint(vData)
    nPts(0) = 1#
     nPts(1) = 0#
     nPts(2) = 0#
     vData = nPts
    Set swX_Axis = swMathUtil.CreateVector(vData)
    ' This is an incremental rotation,
     ' so angle is always the same.
     Set swXform = swMathUtil.CreateTransformRotateAxis(swOriginPt, swX_Axis, 1# * RadPerDeg)
    bRet = swDragOp.AddComponent(swComp(0), False)
     Debug.Assert bRet
    swDragOp.DynamicClearanceEnabled = False
    ' Axial rotation
     swDragOp.TransformType = 1
    ' Solve by relaxation
     swDragOp.DragMode = 2
    bRet = swDragOp.BeginDrag
     Debug.Assert bRet
    For i = 0 To 500
         bRet = swDragOp.DragAsUI(swXform)
     Next i
    bRet = swDragOp.EndDrag
     Debug.Assert bRet
End Sub
```
