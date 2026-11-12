---
title: "Insert and Use Plane with Manipulator Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swpublishedapi/Insert_and_Use_Plane_with_Manipulator_Example_VB.htm"
---

# Insert and Use Plane with Manipulator Example (VBA)

This example shows how to insert a plane that has a manipulator.

* [Module](#Module)

* [Class module](#Class)

```vb
' Module
```

```
'--------------------------------------------------------------
' Preconditions:
' 1. In the IDE:
'    a. Click Tools > References > SOLIDWORKS <version>
'       exposed type libraries for add-in.
'    b. Open the Immediate window.
' 2. Ensure that the specified part document exists.
'
' Postconditions:
' 1. Part document opens.
' 2. Plane with manipulator is displayed.
' 3. Distance, angles, height, and width of the plane are
'    printed to the Immediate window.
' 4. Click and hold the right-mouse button and drag the
'    plane up and down using the manipulator that calls the
'    the handler. The handle index is printed to
'    the Immediate window at each drag.
' 5. Click and hold the right-mouse button and rotate the plane,
'    which calls the handler. The handle index
'    is printed to the Immediate window at each rotation.
'
' NOTE: Because the part document is used elsewhere, do not
' save any changes when closing it.
'---------------------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModelDoc As SldWorks.ModelDoc2
Dim swModelViewMgr As SldWorks.ModelViewManager
Dim swHdlr As Class1
Dim swManipulator As SldWorks.Manipulator
Dim swPlaneManipulator As SldWorks.PlaneManipulator
Dim fileName As String
Dim errors As Long
Dim warnings As Long
Dim PiVal As Double
```

```
Sub main()
```

```
    Set swHdlr = New Class1
```

```
    Set swApp = Application.SldWorks
```

```
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
    Set swModelDoc = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
```

```
    ' Create a plane with a manipulator
    Set swModelViewMgr = swModelDoc.ModelViewManager
    Set swManipulator = swModelViewMgr.CreateManipulator(swManipulatorType_e.swPlaneManipulator, swHdlr)
    Set swPlaneManipulator = swManipulator.GetSpecificManipulator
```

```
    ' Set PI
    PiVal = 4 * Atn(1)
```

```
    ' Set the distance of the plane
    swPlaneManipulator.Distance = 0.04
    Debug.Print "Distance = " & swPlaneManipulator.Distance
```

```
    'Set the angles of the plane
    swPlaneManipulator.XAngle = 2 * PiVal / 180
    Debug.Print "X = " & swPlaneManipulator.XAngle
```

```
    swPlaneManipulator.YAngle = 10 * PiVal / 180
    Debug.Print "Y = " & swPlaneManipulator.YAngle
```

```
    ' Set the height and width of the plane
    swPlaneManipulator.Height = 0.1
    Debug.Print ("Height = " & swPlaneManipulator.Height)
```

```
    swPlaneManipulator.Width = 0.075
    Debug.Print ("Width = " & swPlaneManipulator.Width)

    ' Set the color of plane manipulator
    swPlaneManipulator.Color = RGB(255, 0, 0)
    ' Update the plane's properties
    swPlaneManipulator.Update
    ' Show plane manipulator
    swManipulator.Show swModelDoc
End Sub
Back to top

' Class module
Option Explicit
Implements SwManipulatorHandler2
Private Sub SwManipulatorHandler2_OnUpdateDrag(ByVal pManipulator As Object, ByVal handleIndex As Long, ByVal newPosMathPt As Object)
    Debug.Print "SwManipulatorHandler2_OnUpdateDrag"
    Debug.Print "  HandleIndex      = " & handleIndex
    Dim swRetManip As SldWorks.PlaneManipulator
    Set swRetManip = pManipulator

    If (handleIndex = 8) Then
        Dim retDist As Double
        retDist = swRetManip.Distance
    Else
        Dim angleX As Double
        Dim angleY As Double
        angleX = swRetManip.XAngle
        angleY = swRetManip.YAngle
    End If

End Sub
Private Function SwManipulatorHandler2_OnDelete(ByVal pManipulator As Object) As Boolean
End Function
Private Sub SwManipulatorHandler2_OnDirectionFlipped(ByVal pManipulator As Object)
End Sub
Private Function SwManipulatorHandler2_OnDoubleValueChanged(ByVal pManipulator As Object, ByVal Id As Long, Value As Double) As Boolean
End Function
Private Sub SwManipulatorHandler2_OnEndNoDrag(ByVal pManipulator As Object, ByVal handleIndex As Long)
End Sub
Private Sub SwManipulatorHandler2_OnHandleRmbSelected(ByVal pManipulator As Object, ByVal handleIndex As Long)
End Sub
Private Function SwManipulatorHandler2_OnHandleLmbSelected(ByVal pManipulator As Object) As Boolean
End Function
Private Sub SwManipulatorHandler2_OnHandleSelected(ByVal pManipulator As Object, ByVal handleIndex As Long)
End Sub
Private Sub SwManipulatorHandler2_OnItemSetFocus(ByVal pManipulator As Object, ByVal Id As Long)
End Sub
Private Function SwManipulatorHandler2_OnLmbSelected(ByVal pManipulator As Object) As Boolean
End Function
Private Function SwManipulatorHandler2_OnStringValueChanged(ByVal pManipulator As Object, ByVal Id As Long, Value As String) As Boolean
End Function
Private Sub SwManipulatorHandler2_OnEndDrag(ByVal pMani As Object, ByVal index As Long)
End Sub
Back to top
```
