---
title: "Implement Manipulator Handler Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swpublishedapi/Implement_Manipulator_Handler_Example_VB.htm"
---

# Implement Manipulator Handler Example (VBA)

This example shows how to implement a manipulator handler.

```vb
'-----------------------------------------------------------------------------
Option Explicit
Implements SwManipulatorHandler2
______________________________________________________________________________
Private Function SwManipulatorHandler2_OnDelete(ByVal pManipulator As Object) As Boolean
    Debug.Print "SwManipulatorHandler2_OnDelete"
End Function
______________________________________________________________________________
Private Sub SwManipulatorHandler2_OnDirectionFlipped(ByVal pManipulator As Object)
    Debug.Assert False
    Debug.Print "SwManipulatorHandler2_OnDirectionFlipped"
End Sub
______________________________________________________________________________
Private Function SwManipulatorHandler2_OnDoubleValueChanged(ByVal pManipulator As Object, ByVal Id As Long, Value As Double) As Boolean
    'Debug.Assert False
    Debug.Print "SwManipulatorHandler2_OnDoubleValueChanged"
    Debug.Print "  ID               = " & Id
    Debug.Print "  Value            = " & Value
End Function
______________________________________________________________________________
Private Sub SwManipulatorHandler2_OnEndDrag(ByVal pManipulator As Object)
    Debug.Print "SwManipulatorHandler2_OnEndDrag"
End Sub
______________________________________________________________________________
Private Sub SwManipulatorHandler2_OnEndDrag(ByVal pManipulator As Object, ByVal handleIndex As Long)
    Debug.Print "SwManipulatorHandler2_OnEndDrag"
    Debug.Print "  HandleIndex      = " & handleIndex

    If (handleIndex = swDragArrowManipulatorOptions_e.swDragArrowManipulatorDirection2) Then
        Debug.Print " Direction1"
    Else
        Debug.Print " Direction2"
    End If
End Sub
______________________________________________________________________________
Private Sub SwManipulatorHandler2_OnHandleRmbSelected(ByVal pManipulator As Object, ByVal handleIndex As Long)
    Debug.Print "SwManipulatorHandler2_OnHandleRmbSelected"
    Debug.Print "  handleIndex      = " + handleIndex
End Sub
______________________________________________________________________________
Private Sub SwManipulatorHandler2_OnHandleSelected(ByVal pManipulator As Object, ByVal handleIndex As Long)
    Debug.Print "SwManipulatorHandler2_OnHandleSelected"
    Debug.Print "  HandleIndex      = " + handleIndex
End Sub
______________________________________________________________________________
Private Sub SwManipulatorHandler2_OnItemSetFocus(ByVal pManipulator As Object, ByVal Id As Long)
    Debug.Assert False
    Debug.Print "SwManipulatorHandler2_OnItemSetFocus"
    Debug.Print "  ID               = " & Id
End Sub
______________________________________________________________________________
Private Function SwManipulatorHandler2_OnLmbSelected(ByVal pManipulator As Object) As Boolean
    Debug.Assert False
    Debug.Print "SwManipulatorHandler2_OnLmbSelected"
End Function
______________________________________________________________________________
Private Function SwManipulatorHandler2_OnStringValueChanged(ByVal pManipulator As Object, ByVal Id As Long, Value As String) As Boolean
    Debug.Assert False
    Debug.Print "SwManipulatorHandler2_OnStringValueChanged"
    Debug.Print "  ID               = " & Id
    Debug.Print "  Value            = " & Value
End Function
______________________________________________________________________________
Private Sub SwManipulatorHandler2_OnUpdateDrag(ByVal pManipulator As Object, ByVal handleIndex As Long, ByVal newPosMathPt As Object)
    Debug.Print "SwManipulatorHandler2_OnUpdateDrag"
    Debug.Print "  HandleIndex      = " & handleIndex

End Sub
```
