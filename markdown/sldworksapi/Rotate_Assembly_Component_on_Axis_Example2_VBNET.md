---
title: "Rotate Assembly Component on Axis Using IDragOperator::DragAsUI Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Assembly_Component_on_Axis_Example2_VBNET.htm"
---

# Rotate Assembly Component on Axis Using IDragOperator::DragAsUI Example (VB.NET)

This example shows how to rotate an assembly component about an assembly axis using IDragOperator::DragAsUI.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Assembly document is open.
 ' 2. Component in the assembly document is selected.
 '
 ' Postconditions: Transform matrix is set.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Const PI As Double = 3.14159
     Const RadPerDeg As Double = PI / 180.0#

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

         Dim swModel As ModelDoc2
         Dim swAssy As AssemblyDoc
         Dim swDragOp As DragOperator
         Dim swSelMgr As SelectionMgr
         Dim swComp(1) As Component2
         Dim vComp As Object
         Dim swXform As MathTransform
         Dim swMathUtil As MathUtility
         Dim swOriginPt As MathPoint
         Dim swX_Axis As MathVector
         Dim nPts(2) As Double
         Dim vData As Object
         Dim i As  Integer
         Dim bRet As Boolean

         swModel = swApp.ActiveDoc
         swAssy = swModel
         swDragOp = swAssy.GetDragOperator
         swSelMgr = swModel.SelectionManager
         swComp(0) = swSelMgr.GetSelectedObjectsComponent(1)
         swComp(1) = swSelMgr.GetSelectedObjectsComponent(2)
         swMathUtil = swApp.GetMathUtility

         vComp = swComp

         nPts(0) = 0.0#
         nPts(1) = 0.0#
         nPts(2) = 0.0#

         vData = nPts

         swOriginPt = swMathUtil.CreatePoint(vData)

         nPts(0) = 1.0#
         nPts(1) = 0.0#
         nPts(2) = 0.0#
         vData = nPts

         swX_Axis = swMathUtil.CreateVector(vData)

         ' This is an incremental rotation,
         ' so angle is always the same.
         swXform = swMathUtil.CreateTransformRotateAxis(swOriginPt, swX_Axis, 1.0# * RadPerDeg)

         bRet = swDragOp.AddComponent(swComp(0),  False)
         Debug.Assert(bRet)

         swDragOp.DynamicClearanceEnabled =  False

         ' Axial rotation
         swDragOp.TransformType = 1

         ' Solve by relaxation
         swDragOp.DragMode = 2

         bRet = swDragOp.BeginDrag
         Debug.Assert(bRet)

         For i = 0 To 500
             bRet = swDragOp.DragAsUI(swXform)
         Next i

         bRet = swDragOp.EndDrag
         Debug.Assert(bRet)

     End Sub

     Public swApp As SldWorks

 End  Class
```
