---
title: "Create Drag Arrow Manipulator Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Drag_Arrow_Manipulator_Example_VBNET.htm"
---

# Create Drag Arrow Manipulator Example (VB.NET)

This example shows how to create a drag arrow manipulator, which is called a handle in the user interface.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part or assembly and select a face.
 ' 2. Select Project > Add Reference > .NET > SolidWorks.Interop.swpublished.
 ' 3.  De-select Tools > Options > Stop VSTA debugger on macro exit.
 ' 4. Copy the main class into SolidWorksMacro.vb of your VB.NET project.
 ' 5. Copy the handler class into Class1.vb of your VB.NET project.
 ' 6. Open an Immediate window.
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

'main class:
Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swpublished
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro
     Public swManip As Manipulator
     Public swDrag As DragArrowManipulator
     Public WithEvents swDragHdlr As New Class1
     Public Sub Main()

         Dim swFace As Face2
         Dim swMathUtil As MathUtility
         Dim swModel As ModelDoc2
         Dim swModViewMgr As ModelViewManager
         Dim swSelMgr As SelectionMgr
         Dim vPickPt As Object
         Dim swPickPt As MathPoint

         swMathUtil = swApp.GetMathUtility
         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFace = swSelMgr.GetSelectedObject6(1, 0)

         Dim nVector(2) As Double
         Dim vVector As Object
         nVector(0) = 0 : nVector(1) = 1 : nVector(2) = 0
         vVector = nVector

         Dim swN As MathVector
         swN = swMathUtil.CreateVector((vVector))

         vPickPt = swSelMgr.GetSelectionPoint2(1, -1)
         swPickPt = swMathUtil.CreatePoint((vPickPt))
         swModViewMgr = swModel.ModelViewManager

         swManip = swModViewMgr.CreateManipulator(1, swDragHdlr)
         swDrag = swManip.GetSpecificManipulator

         swDrag.AllowFlip =  True
         swDrag.ShowRuler =  True
         swDrag.ShowOppositeDirection =  True
         swDrag.Length = 0.02
         swDrag.Direction = swN
         swDrag.LengthOppositeDirection = 0.01
         swDrag.Origin = swPickPt
         swManip.Show(swModel)
         swDrag.Update()

         Dim origin As MathPoint
         origin = swDrag.Origin

         Dim pt As Object
         pt = origin.ArrayData

     End Sub
     Public swApp As SldWorks
 End  Class
```

'handler class:

```vb
Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swpublished
 Imports System
 Imports System.Diagnostics
 Imports System.Runtime
 <System.Runtime.InteropServices.ComVisibleAttribute(True)> _
 Public Class Class1
     Implements SwManipulatorHandler2

     Dim doneonce As Integer
     Const lenFact As Integer = 1
     Private Function OnHandleLmbSelected(ByVal pManipulator As Object) As  Boolean  Implements ISwManipulatorHandler2.OnHandleLmbSelected

         Debug.Print("SwManipulatorHandler2_OnHandleLmbSelected")

     End Function
     Private Function OnDelete(ByVal pManipulator As Object) As  Boolean  Implements ISwManipulatorHandler2.OnDelete

         Debug.Print("SwManipulatorHandler2_OnDelete")

     End Function
     Private Sub OnDirectionFlipped(ByVal pManipulator As Object) Implements ISwManipulatorHandler2.OnDirectionFlipped

         Debug.Assert(False)

         Debug.Print("SwManipulatorHandler2_OnDirectionFlipped")

     End Sub
     Private Function OnDoubleValueChanged(ByVal pManipulator As Object, ByVal Id As  Integer,  ByRef Value  As  Double)  As  Boolean  Implements ISwManipulatorHandler2.OnDoubleValueChanged

         'Debug.Assert False
         doneonce = doneonce + 1
         Debug.Print("SwManipulatorHandler2_OnDoubleValueChanged")

         Debug.Print("  ID               = " & Id)

         Debug.Print("  Value            = " & Value)
         Dim swTmpManipulator As DragArrowManipulator
         swTmpManipulator = pManipulator
         'Update origin
         Dim swMathPoint As MathPoint
         swMathPoint = swTmpManipulator.Origin
         Dim varMathPt As Object
         varMathPt = swMathPoint.ArrayData
         varMathPt(1) = varMathPt(1) + lenFact / 1000
         swMathPoint.ArrayData = varMathPt
         If (doneonce = 1) Then
             swTmpManipulator.FixedLength = True
         End If
         swTmpManipulator.Origin = swMathPoint

         swTmpManipulator.Update()
         Return True
     End Function
     Private Sub OnEndDrag(ByVal pManipulator As Object, ByVal handleIndex As Integer) Implements ISwManipulatorHandler2.OnEndDrag

         Dim swTmpManipulator As DragArrowManipulator
         swTmpManipulator = pManipulator
         swTmpManipulator.FixedLength = False
         doneonce = doneonce + 1
         Debug.Print("SwManipulatorHandler2_OnEndDrag")

         Debug.Print("  HandleIndex      = " & handleIndex)

         If (handleIndex = swDragArrowManipulatorOptions_e.swDragArrowManipulatorDirection2)  Then

             Debug.Print(" Direction1")

         Else

             Debug.Print(" Direction2")

         End If

     End Sub
     Private Sub OnEndNoDrag(ByVal pManipulator As Object, ByVal handleIndex As Integer) Implements ISwManipulatorHandler2.OnEndNoDrag

         Debug.Print("SwManipulatorHandler2_OnEndNoDrag")

     End Sub
     Private Sub OnHandleRmbSelected(ByVal pManipulator As Object, ByVal handleIndex As Integer) Implements ISwManipulatorHandler2.OnHandleRmbSelected

         Debug.Print("SwManipulatorHandler2_OnHandleRmbSelected")

         Debug.Print("  handleIndex      = " + handleIndex)

     End Sub
     Private Sub OnHandleSelected(ByVal pManipulator As Object, ByVal handleIndex As Integer) Implements ISwManipulatorHandler2.OnHandleSelected

         Debug.Print("SwManipulatorHandler2_OnHandleSelected")

         Debug.Print("  HandleIndex      = " + handleIndex)

     End Sub
     Private Sub OnItemSetFocus(ByVal pManipulator As Object, ByVal Id As  Integer)  Implements ISwManipulatorHandler2.OnItemSetFocus

         Debug.Assert(False)

         Debug.Print("SwManipulatorHandler2_OnItemSetFocus")

         Debug.Print("  ID               = " & Id)

     End Sub
     Private Function OnStringValueChanged(ByVal pManipulator As Object, ByVal Id As  Integer,  ByRef Value  As  String)  As  Boolean  Implements ISwManipulatorHandler2.OnStringValueChanged

         Debug.Assert(False)

         Debug.Print("SwManipulatorHandler2_OnStringValueChanged")

         Debug.Print("  ID               = " & Id)

         Debug.Print("  Value            = " & Value)

     End Function
     Private Sub OnUpdateDrag(ByVal pManipulator As Object, ByVal handleIndex As Integer, ByVal newPosMathPt As Object) Implements ISwManipulatorHandler2.OnUpdateDrag

         Debug.Print("SwManipulatorHandler2_OnUpdateDrag")

         Debug.Print("  HandleIndex      = " & handleIndex)

     End Sub

     Public Sub  New()

     End Sub
 End Class
```
