---
title: "Insert Sketch Text and Hole Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Sketch_Text_and_Hole_Example_VB.htm"
---

# Insert Sketch Text and Hole Example (VBA)

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
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swMathPt As SldWorks.MathPoint
 Dim selFace As Face2
 Dim selEnt As Entity
 Dim selPt As Variant
 Dim NewPt As Variant
 Dim swMathUtil As SldWorks.MathUtility
 Dim swMathTrans As SldWorks.MathTransform
 Dim selData As SldWorks.SelectData
 Dim swSketchMgr As SldWorks.SketchManager
 Dim skText As SketchText
 Dim ptArr(2) As Double
 Dim params As Variant
 Dim holeFeat As SldWorks.Feature
 Dim swFeatMgr As SldWorks.FeatureManager
 Dim boolstatus As Boolean

Function TransformPoint(ByVal Sketch1 As SldWorks.Sketch, ByVal X As Double, ByVal Y As Double, ByVal Z As Double) As Variant
    ptArr(0) = X
     ptArr(1) = Y
     ptArr(2) = Z

    Set swMathUtil = swApp.GetMathUtility
     Set swMathPt = swMathUtil.CreatePoint((ptArr))
    params = swMathPt.ArrayData
    Set swMathTrans = Sketch1.ModelToSketchTransform
     Set swMathPt = swMathPt.MultiplyTransform(swMathTrans)
    NewPt = swMathPt.ArrayData
    TransformPoint = NewPt
End Function

Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set selFace = swSelMgr.GetSelectedObject6(1, -1)
     Set selEnt = selFace

    selPt = swSelMgr.GetSelectionPoint2(1, -1)

    Set selData = swSelMgr.CreateSelectData

    selData.X = selPt(0)
     selData.Y = selPt(1)
     selData.Z = selPt(2)

    Set swSketchMgr = swModel.SketchManager

    swSketchMgr.InsertSketch True

    selPt = TransformPoint(swModel.IGetActiveSketch2, selPt(0), selPt(1), selPt(2))

    Set skText = swModel.InsertSketchText(selPt(0), selPt(1), selPt(2), "Hole", 0, 0, 0, 100, 100)

    params = skText.GetCoordinates

    swSketchMgr.InsertSketch True

    boolstatus = selEnt.Select4(False, selData)

    Set swFeatMgr = swModel.FeatureManager
     Set holeFeat = swFeatMgr.SimpleHole2(0.001, True, False, False, 0, 0, 0.001, 0.001, False, False, False, False, 0, 0, False, False, False, False, True, True, False, False, False)

End Sub
```
