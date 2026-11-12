---
title: "Rotate Assembly Component on Axis Using IDragOperator::Drag Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Assembly_Component_on_Axis_Example_VB.htm"
---

# Rotate Assembly Component on Axis Using IDragOperator::Drag Example (VBA)

This example shows how to rotate an assembly component about an assembly axis using IDragOperator::Drag.

**NOTE:** The code shows how to use a MathUtility object to directly create a transformation matrix (object) that represents rotation about a point and an axis, without having to know details of the OpenGL transformations.

```
'------------------------------------------------------------------
' Preconditions: Verify that the specified assembly document exists.
'
' Postconditions:
' 1. Opens the specified assembly document, which is fully resolved.
' 2. Selects a floating component.
' 3. Watch the selected component in the graphics area rotate
'    90° about the assembly's x axis.
'
' NOTE: Because this assembly is used elsewhere, do not save any changes.
'------------------------------------------------------------------
Option Explicit
```

```
Const PI                As Double = 3.14159
Const RadPerDeg         As Double = PI / 180#
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swDragOp As SldWorks.DragOperator
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swComp As SldWorks.Component2
    Dim swXform As SldWorks.MathTransform
    Dim swMathUtil As SldWorks.MathUtility
    Dim swOriginPt As SldWorks.MathPoint
    Dim swX_Axis As SldWorks.MathVector
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
    Dim status As Boolean
    Dim nPts(2) As Double
    Dim vData As Variant
    Dim nNow As Single
    Dim i  As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem2.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Part3^Assem2-1@assem2", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swAssy = swModel

    Set swDragOp = swAssy.GetDragOperator
    Set swSelMgr = swModel.SelectionManager
    Set swComp = swSelMgr.GetSelectedObjectsComponent2(1)
    Set swMathUtil = swApp.GetMathUtility
```

```
    nPts(0) = 0#
    nPts(1) = 0#
    nPts(2) = 0#
    vData = nPts
    Set swOriginPt = swMathUtil.CreatePoint(vData)
```

```
    nPts(0) = 1#
    nPts(1) = 0#
    nPts(2) = 0#
    vData = nPts
    Set swX_Axis = swMathUtil.CreateVector(vData)

    ' This is an incremental rotation,
    ' so angle is always the same
    Set swXform = swMathUtil.CreateTransformRotateAxis(swOriginPt, swX_Axis, 1# * RadPerDeg)
```

```
    bRet = swDragOp.AddComponent(swComp, False)
```

```
    swDragOp.CollisionDetectionEnabled = False
    swDragOp.DynamicClearanceEnabled = False
```

```
    ' Axial rotation
    swDragOp.TransformType = 1
```

```
    ' Solve by relaxation
    swDragOp.DragMode = 2
```

```
    bRet = swDragOp.BeginDrag
```

```
    For i = 0 To 90
        ' Returns false if drag fails
        bRet = swDragOp.Drag(swXform)
        ' Wait for 0.1 secs
        nNow = Timer
        While Timer < nNow + 0.1
            ' Process event loop
            DoEvents
        Wend
    Next i
```

```
    bRet = swDragOp.EndDrag
```

```
End Sub
```
