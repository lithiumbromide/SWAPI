---
title: "Insert Sketch Text and Hole Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Sketch_Text_and_Hole_Example_VBNET.htm"
---

# Insert Sketch Text and Hole Example (VB.NET)

This example shows how to insert sketch text and a hole at the selected point on a face.

```vb
  '----------------------------------------------------------------------------
  ' Preconditions: Open a model document and select a face.
 '
 ' Postconditions:
 ' 1. Creates a hole and inserts the specified text on the
 '    face at its point of selection.
 ' 2. Examine the graphics area and FeatureManager design tree.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swSelMgr As SelectionMgr
     Dim swMathPt As MathPoint
     Dim selFace As Face2
     Dim selEnt As Entity
     Dim selPt As Object
     Dim NewPt As Object
     Dim swMathUtil As MathUtility
     Dim swMathTrans As MathTransform
     Dim selData As SelectData
     Dim swSketchMgr As SketchManager
     Dim skText As SketchText
     Dim ptArr(2) As Double
     Dim params As Object
     Dim holeFeat As Feature
     Dim swFeatMgr As FeatureManager
     Dim boolstatus As Boolean

     Function TransformPoint(ByVal Sketch1 As Sketch, ByVal X As Double, ByVal Y As Double, ByVal Z As Double) As Object

         ptArr(0) = X
         ptArr(1) = Y
         ptArr(2) = Z

         swMathUtil = swApp.GetMathUtility
         swMathPt = swMathUtil.CreatePoint((ptArr))

         params = swMathPt.ArrayData

         swMathTrans = Sketch1.ModelToSketchTransform
         swMathPt = swMathPt.MultiplyTransform(swMathTrans)

         NewPt = swMathPt.ArrayData

         TransformPoint = NewPt

     End Function

     Sub main()

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         selFace = swSelMgr.GetSelectedObject6(1, -1)
         selEnt = selFace

         selPt = swSelMgr.GetSelectionPoint2(1, -1)

         selData = swSelMgr.CreateSelectData

         selData.X = selPt(0)
         selData.Y = selPt(1)
         selData.Z = selPt(2)

         swSketchMgr = swModel.SketchManager

         swSketchMgr.InsertSketch(True)

         selPt = TransformPoint(swModel.IGetActiveSketch2, selPt(0), selPt(1), selPt(2))

         skText = swModel.InsertSketchText(selPt(0), selPt(1), selPt(2), "Hole", 0, 0, 0, 100, 100)

         params = skText.GetCoordinates

         swSketchMgr.InsertSketch(True)

         boolstatus = selEnt.Select4(False, selData)

         swFeatMgr = swModel.FeatureManager
         holeFeat = swFeatMgr.SimpleHole2(0.001, True, False, False, 0, 0, 0.001, 0.001, False, False, False, False, 0, 0, False, False, False, False, True, True, False, False, False)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
