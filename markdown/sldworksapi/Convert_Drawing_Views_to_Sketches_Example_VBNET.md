---
title: "Convert Drawing Views to Sketch Blocks Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Convert_Drawing_Views_to_Sketches_Example_VBNET.htm"
---

# Convert Drawing Views to Sketch Blocks Example (VB.NET)

This example shows how to convert drawing views to sketches and sketch blocks.

```vb
'----------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\api\ReplaceView.slddrw
 '
 ' Postconditions:
 ' 1. Converts Drawing View1 to a sketch.
 ' 2. Converts Drawing View2 to a sketch block
 ' 3. Converts Drawing View3 to a sketch block at a new position in the drawing.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim boolstatus As Boolean
     Dim drawDoc As DrawingDoc
     Dim selMan As SelectionMgr
     Dim drview As View
     Dim nPt(2) As Double
     Dim vPt As Object
     Dim swMathUtil As MathUtility
     Dim insertionPt As MathPoint
     Dim position As MathPoint

     Sub main()

         Part = swApp.ActiveDoc
         drawDoc = Part
         swMathUtil = swApp.GetMathUtility
         selMan = Part.SelectionManager

         boolstatus = Part.Extension.SelectByID2("Drawing View1",  "DRAWINGVIEW", 0, 0, 0,  False, 0,  Nothing, 0)
         drview = selMan.GetSelectedObject6(1, 0)
         boolstatus = drview.ReplaceViewWithSketch

         Part.ClearSelection2(True)
         boolstatus = Part.Extension.SelectByID2("Drawing View2",  "DRAWINGVIEW", 0, 0, 0,  False, 0,  Nothing, 0)
         drview = selMan.GetSelectedObject6(1, 0)

         nPt(0) = 1.41
         nPt(1) = 3.88
         nPt(2) = 0
         vPt = nPt
         insertionPt = swMathUtil.CreatePoint(vPt)
         boolstatus = drview.ReplaceViewWithBlock(insertionPt)

         Part.ClearSelection2(True)
         boolstatus = Part.Extension.SelectByID2("Drawing View3",  "DRAWINGVIEW", 0, 0, 0,  False, 0,  Nothing, 0)
         drview = selMan.GetSelectedObject6(1, 0)

         nPt(0) = 5.48
         nPt(1) = 5.22
         nPt(2) = 0
         vPt = nPt
         position = swMathUtil.CreatePoint(vPt)
         boolstatus = drview.InsertViewAsBlock(insertionPt, position)

     End Sub

     Public swApp As SldWorks

 End  Class
```
