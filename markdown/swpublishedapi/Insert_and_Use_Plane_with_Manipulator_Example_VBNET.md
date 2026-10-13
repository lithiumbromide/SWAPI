---
title: "Insert and Use Plane with Manipulator Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swpublishedapi/Insert_and_Use_Plane_with_Manipulator_Example_VBNET.htm"
---

# Insert and Use Plane with Manipulator Example (VB.NET)

This example shows how to insert a plane with a manipulator.

```vb
  '--------------------------------------------------------------
 ' Preconditions:
 ' 1. In the IDE:
 '    a. Click Project > Add Reference > COM >
 '       SolidWorks.Interop.swpublished.
 '    b. Copy the code in  SolidWorksMacro.vb to your project
 '       and create a class and copy the code in  Class1.vb
 '       to that class.
 '    c. Open the Immediate window.
 ' 2. Ensure that the specified part document exists.
 '
 ' Postconditions:
 ' 1. Part document opens.
 ' 2. Plane with manipulator is displayed.
 ' 3. Distance, angles, height, and width of the plane are
 '    printed to the Immediate window.
 ' 4. Click and hold the right-mouse button and drag the
 '    plane up and down, which calls the handler. The handle
 '    index is printed to the Immediate window at each drag.
 ' 5. Click and hold the right-mouse button and rotate the plane,
 '    which calls the handler. The handle index
 '    is printed to the Immediate window at each rotation.
 '
 ' NOTE: Because the part document is used elsewhere, do not
 ' save any changes when closing the document.
 '---------------------------------------------------------------

' SolidWorksMacro.vb
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics
 Imports SolidWorks.Interop.swpublished

 Partial  Class SolidWorksMacro

     Public  WithEvents swHdlr  As Class1
     Public swManipulator As Manipulator
     Public swPlaneManipulator As PlaneManipulator

     Public  Sub Main()

         Dim swModelDoc As ModelDoc2
         Dim swModelViewMgr As ModelViewManager

         Dim fileName  As  String
         Dim errors As  Integer
         Dim warnings As  Integer

         swHdlr = New Class1

         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
         swModelDoc = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent,  "", errors, warnings)

         ' Create the plane with a manipulator
         swModelViewMgr = swModelDoc.ModelViewManager
         swManipulator = swModelViewMgr.CreateManipulator(swManipulatorType_e.swPlaneManipulator, swHdlr)
         swPlaneManipulator = swManipulator.GetSpecificManipulator

         ' Set the distance of plane
         swPlaneManipulator.Distance = 0.04
         Debug.Print("Distance = " & swPlaneManipulator.Distance)

         'Set the angles of plane
         swPlaneManipulator.XAngle = 2 * PiVal() / 180
         Debug.Print("X = " & swPlaneManipulator.XAngle)

         swPlaneManipulator.YAngle = 10 * PiVal() / 180
         Debug.Print("Y = " & swPlaneManipulator.YAngle)

         ' Set the height and width of plane
         swPlaneManipulator.Height = 0.1
         Debug.Print("Height = " & swPlaneManipulator.Height)

         swPlaneManipulator.Width = 0.075
         Debug.Print("Width = " & swPlaneManipulator.Width)

         ' Set the color of plane manipulator
         swPlaneManipulator.Color = RGB(255, 0, 0)

         ' Update the plane's properties
         swPlaneManipulator.Update()

         ' Show the plane with the manipulator
         swManipulator.Show(swModelDoc)

     End  Sub

     Function PiVal() As  Double
         ' Set PI
         PiVal = 4 * System.Math.Atan(1)
     End  Function

     '''  <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     '''  </summary>

     Public swApp As SldWorks

 End   Class
```

[Back to top](#top)

```vb
 'Class1.vb
```

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swpublished
Imports System
Imports System.Diagnostics
Imports System.Runtime

<System.Runtime.InteropServices.ComVisibleAttribute(True)> _
Public Class Class1

Implements SwManipulatorHandler2

Public Sub SwManipulatorHandler2_**OnUpdateDrag**(ByVal pManipulator As Object, ByVal handleIndex As Long, ByVal newPosMathPt As Object)
'Public Sub SwManipulatorHandler2_OnUpdateDrag(ByVal pManipulator As Object, ByVal handleIndex As Long, ByVal newPosMathPt As Object) Implements SolidWorks.Interop.swpublished.SwManipulatorHandler.OnUpdateDrag
Debug.Print("SwManipulatorHandler2_OnUpdateDrag")
Debug.Print(" HandleIndex = " & handleIndex)
Dim swRetManip As PlaneManipulator
swRetManip = pManipulator

If (handleIndex = 8) Then
Dim retDist As Double
retDist = swRetManip.**Distance**
Else
Dim angleX As Double
Dim angleY As Double
angleX = swRetManip.**XAngle**
angleY = swRetManip.**YAngle**
End If

End Sub

Public Function SwManipulatorHandler2_OnDelete(ByVal pManipulator As Object) As Boolean
End Function

Public Sub SwManipulatorHandler2_OnDirectionFlipped(ByVal pManipulator As Object)
End Sub

Public Function SwManipulatorHandler2_OnDoubleValueChanged(ByVal pManipulator As Object, ByVal Id As Long, ByVal Value As Double) As Boolean
End Function

Public Sub SwManipulatorHandler2_OnEndNoDrag(ByVal pManipulator As Object, ByVal handleIndex As Long)
End Sub

Public Sub SwManipulatorHandler2_OnHandleRmbSelected(ByVal pManipulator As Object, ByVal handleIndex As Long)
End Sub

Public Function SwManipulatorHandler2_OnHandleLmbSelected(ByVal pManipulator As Object) As Boolean
End Function

Public Sub SwManipulatorHandler2_OnHandleSelected(ByVal pManipulator As Object, ByVal handleIndex As Long)
End Sub

Public Sub SwManipulatorHandler2_OnItemSetFocus(ByVal pManipulator As Object, ByVal Id As Long)
End Sub

Public Function SwManipulatorHandler2_OnLmbSelected(ByVal pManipulator As Object) As Boolean
End Function

Public Function SwManipulatorHandler2_OnStringValueChanged(ByVal pManipulator As Object, ByVal Id As Long, ByVal Value As String) As Boolean
End Function

Public Sub SwManipulatorHandler2_OnEndDrag(ByVal pMani As Object, ByVal index As Long)
End Sub

Public Function OnDelete(ByVal pManipulator As Object) As Boolean Implements SolidWorks.Interop.swpublished.ISwManipulatorHandler2.OnDelete
End Function

Public Sub OnDirectionFlipped(ByVal pManipulator As Object) Implements SolidWorks.Interop.swpublished.ISwManipulatorHandler2.OnDirectionFlipped
End Sub

Public Function OnDoubleValueChanged(ByVal pManipulator As Object, ByVal handleIndex As Integer, ByRef Value As Double) As Boolean Implements SolidWorks.Interop.swpublished.ISwManipulatorHandler2.OnDoubleValueChanged
End Function

Public Sub OnEndDrag(ByVal pManipulator As Object, ByVal handleIndex As Integer) Implements SolidWorks.Interop.swpublished.ISwManipulatorHandler2.OnEndDrag
End Sub

Public Sub OnEndNoDrag(ByVal pManipulator As Object, ByVal handleIndex As Integer) Implements SolidWorks.Interop.swpublished.ISwManipulatorHandler2.OnEndNoDrag
End Sub

Public Function OnHandleLmbSelected(ByVal pManipulator As Object) As Boolean Implements SolidWorks.Interop.swpublished.ISwManipulatorHandler2.OnHandleLmbSelected
End Function

Public Sub OnHandleRmbSelected(ByVal pManipulator As Object, ByVal handleIndex As Integer) Implements SolidWorks.Interop.swpublished.ISwManipulatorHandler2.OnHandleRmbSelected
End Sub

Public Sub OnHandleSelected(ByVal pManipulator As Object, ByVal handleIndex As Integer) Implements SolidWorks.Interop.swpublished.ISwManipulatorHandler2.OnHandleSelected
End Sub

Public Sub OnItemSetFocus(ByVal pManipulator As Object, ByVal handleIndex As Integer) Implements SolidWorks.Interop.swpublished.ISwManipulatorHandler2.OnItemSetFocus
End Sub

Public Function OnStringValueChanged(ByVal pManipulator As Object, ByVal handleIndex As Integer, ByRef Value As String) As Boolean Implements SolidWorks.Interop.swpublished.ISwManipulatorHandler2.OnStringValueChanged
End Function

Public Sub OnUpdateDrag(ByVal pManipulator As Object, ByVal handleIndex As Integer, ByVal newPosMathPt As Object) Implements SolidWorks.Interop.swpublished.ISwManipulatorHandler2.OnUpdateDrag
End Sub

End Class

[Back to top](#top)
