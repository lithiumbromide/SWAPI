---
title: "Rotate Assembly Component on Axis Using IDragOperator::Drag Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Assembly_Component_on_Axis_Example_VBNET.htm"
---

# Rotate Assembly Component on Axis Using IDragOperator::Drag Example (VB.NET)

This example shows how to rotate an assembly component about an assembly axis using IDragOperator::Drag.

**NOTE:** The code shows how to use a MathUtility object to directly create a transformation matrix (object) that represents rotation about a point and an axis, without having to know details of the OpenGL transformations.

```
'------------------------------------------------------------------
' Preconditions: Verify that the specified assembly document exists.
'
' Postconditions:
' 1. Opens the specified assembly document, which is fully resolved.
' 2. Selects a floating component.
' 3. Watch the selected component in the graphics area rotate 90°
'    about the assembly's x axis.
'
' NOTE: Because this assembly is used elsewhere, do not save any changes.
'------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics
Imports System.Windows.Forms.Application

Partial Class SolidWorksMacro

    Const PI As Double = 3.14159
    Const RadPerDeg As Double = PI / 180.0#

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swAssy As AssemblyDoc
        Dim swDragOp As DragOperator
        Dim swSelMgr As SelectionMgr
        Dim swComp As Component2
        Dim swXform As MathTransform
        Dim swMathUtil As MathUtility
        Dim swOriginPt As MathPoint
        Dim swX_Axis As MathVector
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim status As Boolean
        Dim nPts(2) As Double
        Dim vData As Object
        Dim nNow As Single
        Dim i As Integer
        Dim bRet As Boolean

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem2.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Part3^Assem2-1@assem2", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swAssy = swModel

        swDragOp = swAssy.GetDragOperator
        swSelMgr = swModel.SelectionManager
        swComp = swSelMgr.GetSelectedObjectsComponent2(1)
        swMathUtil = swApp.GetMathUtility

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
        ' so angle is always the same
        swXform = swMathUtil.CreateTransformRotateAxis(swOriginPt, swX_Axis, 1.0# * RadPerDeg)

        bRet = swDragOp.AddComponent(swComp, False)

        swDragOp.CollisionDetectionEnabled = False
        swDragOp.DynamicClearanceEnabled = False

        ' Axial rotation
        swDragOp.TransformType = 1

        ' Solve by relaxation
        swDragOp.DragMode = 2

        bRet = swDragOp.BeginDrag

        For i = 0 To 90
            ' Returns false if drag fails
            bRet = swDragOp.Drag(swXform)
            ' Wait for 0.1 secs
            nNow = Timer
            While Timer < nNow + 0.1
                ' Process event loop
                DoEvents()
            End While
        Next i

        bRet = swDragOp.EndDrag

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
