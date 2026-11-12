---
title: "Create Drag Arrow Manipulator Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Drag_Arrow_Manipulator_Example_VB.htm"
---

# Create Drag Arrow Manipulator Example (VBA)

This example shows how to create a drag arrow manipulator, which is called a handle in the user interface.

- [Main Module](#Modules)
- [Handler Module](#Class)

#### Main module

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part or assembly and select a face.
 ' 2. Select:
 '    Tools > References > SOLIDWORKS <version> exposed type libraries for add-in
 ' 3. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. A unidirectional drag arrow manipulator or handle is created on the selected face.
 ' 2. Drag the handle to another location. The first time you drag the handle,
 '    IDragArrowManipulator::FixedLength is set to true,
 '    and the origin is moved in the direction of the drag. For second and
 '    subsequent drags, IDragArrowManipulator::FixedLength is set to false,
 '    and the origin is not changed.
 ' 3. When you drag the handle a ruler displays.
 '    IDragArrowManipulator::ShowRuler is true.
 ' 4. When you drag the handle past length = 0, the handle flips direction.
 '    IDragArrowManipulator::AllowFlip is true.
 ' 5. Inspect the Immediate window.
 '--------------------------------------------------------------------------
Option Explicit
    Dim swManip                     As SldWorks.Manipulator
     Public swDrag                   As SldWorks.DragArrowManipulator
     Dim swDragHdlr                  As swDragManipHdlr
     Public swFace                   As SldWorks.Face2
Sub main()
    Dim swApp                       As SldWorks.SldWorks
     Dim swMathUtil                  As SldWorks.MathUtility
     Dim swModel                     As SldWorks.ModelDoc2
     Dim swModViewMgr                As SldWorks.ModelViewManager
     Dim swSelMgr                    As SldWorks.SelectionMgr
     Dim vPickPt                     As Variant
     Dim swPickPt                    As SldWorks.MathPoint
     Dim boolstatus As Boolean
    Set swDragHdlr = New swDragManipHdlr
     Set swApp = Application.SldWorks
     Set swMathUtil = swApp.GetMathUtility
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFace = swSelMgr.GetSelectedObject6(1, 0)
    Dim nVector(2)              As Double
     Dim vVector                 As Variant
     nVector(0) = 0:     nVector(1) = 1:     nVector(2) = 0
     vVector = nVector
    Dim swN                     As SldWorks.MathVector
     Set swN = swMathUtil.CreateVector((vVector))
    vPickPt = swSelMgr.GetSelectionPoint2(1, -1)
     Set swPickPt = swMathUtil.CreatePoint((vPickPt))
     Set swModViewMgr = swModel.ModelViewManager
    Set swManip = swModViewMgr.CreateManipulator(SwConst.swManipulatorType_e.swDragArrowManipulator, swDragHdlr)
     Set swDrag = swManip.GetSpecificManipulator
    swDrag.ShowRuler = True
     swDrag.AllowFlip = True
     swDrag.ShowOppositeDirection = False
     swDrag.Length = 0.02
     swDrag.Direction = swN
     swDrag.LengthOppositeDirection = 0.01
     swDrag.origin = swPickPt
     swManip.Show swModel
     swDrag.Update
    Dim origin As SldWorks.MathPoint
     Set origin = swDrag.origin
    Dim pt As Variant
     pt = origin.ArrayData
End Sub
```

#### Handler module

```vb
Dim Doneonce As Long
 '-----------------------------------------------------------------------------
 Const lenFact = 1
 Option Explicit
 Implements SwManipulatorHandler2
Public Function SwManipulatorHandler2_OnHandleLmbSelected(ByVal pManipulator As Object) As Boolean
    Debug.Print "SwManipulatorHandler2_OnHandleLmbSelected"
End Function
Public Function SwManipulatorHandler2_OnDelete(ByVal pManipulator As Object) As Boolean
    Debug.Print "SwManipulatorHandler2_OnDelete"
End Function

Public Sub SwManipulatorHandler2_OnDirectionFlipped(ByVal pManipulator As Object)
    Debug.Print "SwManipulatorHandler2_OnDirectionFlipped"
End Sub
Public Function SwManipulatorHandler2_OnDoubleValueChanged(ByVal pManipulator As Object, ByVal Id As Long, Value As Double) As Boolean
    Doneonce = Doneonce + 1
     Debug.Print "SwManipulatorHandler2_OnDoubleValueChanged"
    Debug.Print "  ID               = " & Id
    Debug.Print "  Value            = " & Value
     Dim swTmpManipulator As SldWorks.DragArrowManipulator
     Set swTmpManipulator = pManipulator
     'Update origin
     Dim swMathPoint As SldWorks.MathPoint
     Set swMathPoint = swTmpManipulator.origin
     Dim varMathPt As Variant
     varMathPt = swMathPoint.ArrayData
     varMathPt(1) = varMathPt(1) + lenFact / 1000
     swMathPoint.ArrayData = varMathPt
     If (Doneonce = 1) Then
         swTmpManipulator.FixedLength = True
     End If
     swTmpManipulator.origin = swMathPoint

    swTmpManipulator.Update
 End Function
Public Sub SwManipulatorHandler2_OnEndDrag(ByVal pManipulator As Object, ByVal handleIndex As Long)
    Dim swTmpManipulator As SldWorks.DragArrowManipulator
     Set swTmpManipulator = pManipulator
     swTmpManipulator.FixedLength = False
     Doneonce = Doneonce + 1
     Debug.Print "SwManipulatorHandler2_OnEndDrag"
    Debug.Print "  HandleIndex      = " & handleIndex

    If (handleIndex = swDragArrowManipulatorOptions_e.swDragArrowManipulatorDirection2) Then
        Debug.Print " Direction1"
    Else
        Debug.Print " Direction2"
    End If
End Sub
 Public Sub SwManipulatorHandler2_OnEndNoDrag(ByVal pManipulator As Object, ByVal handleIndex As Long)

    Debug.Print "SwManipulatorHandler2_OnEndNoDrag"

 End Sub
Public Sub SwManipulatorHandler2_OnHandleRmbSelected(ByVal pManipulator As Object, ByVal handleIndex As Long)
    Debug.Print "SwManipulatorHandler2_OnHandleRmbSelected"
    Debug.Print "  handleIndex      = " + handleIndex
End Sub
Public Sub SwManipulatorHandler2_OnHandleSelected(ByVal pManipulator As Object, ByVal handleIndex As Long)
    Debug.Print "SwManipulatorHandler2_OnHandleSelected"
    Debug.Print "  HandleIndex      = " + handleIndex
End Sub
Public Sub SwManipulatorHandler2_OnItemSetFocus(ByVal pManipulator As Object, ByVal Id As Long)
    Debug.Print "SwManipulatorHandler2_OnItemSetFocus"
    Debug.Print "  ID               = " & Id
End Sub
Public Function SwManipulatorHandler2_OnLmbSelected(ByVal pManipulator As Object) As Boolean
    Debug.Print "SwManipulatorHandler2_OnLmbSelected"
End Function
Public Function SwManipulatorHandler2_OnStringValueChanged(ByVal pManipulator As Object, ByVal Id As Long, Value As String) As Boolean
    Debug.Print "SwManipulatorHandler2_OnStringValueChanged"
    Debug.Print "  ID               = " & Id
    Debug.Print "  Value            = " & Value
End Function
Public Sub SwManipulatorHandler2_OnUpdateDrag(ByVal pManipulator As Object, ByVal handleIndex As Long, ByVal newPosMathPt As Object)
    Debug.Print "SwManipulatorHandler2_OnUpdateDrag"
    Debug.Print "  HandleIndex      = " & handleIndex
End Sub
```
