---
title: "Convert Drawing Views to Sketch Blocks Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Convert_Drawing_Views_to_Sketches_Example_CSharp.htm"
---

# Convert Drawing Views to Sketch Blocks Example (C#)

This example shows how to convert drawing views to sketches and sketch blocks.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\ReplaceView.slddrw
 //
 // Postconditions:
 // 1. Converts Drawing View1 to a sketch.
 // 2.  Converts  Drawing View2 to a sketch block
 // 3.  Converts  Drawing View3 to a sketch block at a new position in the drawing.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace ConvertViewToSketch_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         bool boolstatus;
         DrawingDoc drawDoc;
         SelectionMgr selMan;
         View drview;
         double[] nPt = new double[3];
         object vPt;
         MathUtility swMathUtil;
         MathPoint insertionPt;

         MathPoint position;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             drawDoc = (DrawingDoc)Part;
             swMathUtil = (MathUtility)swApp.GetMathUtility();
             selMan = (SelectionMgr)Part.SelectionManager;

             boolstatus = Part.Extension.SelectByID2("Drawing View1",  "DRAWINGVIEW", 0, 0, 0,  false, 0,  null, 0);
             drview = (View)selMan.GetSelectedObject6(1, 0);
             boolstatus = drview.ReplaceViewWithSketch();

             Part.ClearSelection2(true);
             boolstatus = Part.Extension.SelectByID2("Drawing View2",  "DRAWINGVIEW", 0, 0, 0,  false, 0,  null, 0);
             drview = (View)selMan.GetSelectedObject6(1, 0);

             nPt[0] = 1.41;
             nPt[1] = 3.88;
             nPt[2] = 0;
             vPt = nPt;
             insertionPt = (MathPoint)swMathUtil.CreatePoint(vPt);
             boolstatus = drview.ReplaceViewWithBlock(insertionPt);

             Part.ClearSelection2(true);
             boolstatus = Part.Extension.SelectByID2("Drawing View3",  "DRAWINGVIEW", 0, 0, 0,  false, 0,  null, 0);
             drview = (View)selMan.GetSelectedObject6(1, 0);

             nPt[0] = 5.48;
             nPt[1] = 5.22;
             nPt[2] = 0;
             vPt = nPt;
             position = (MathPoint)swMathUtil.CreatePoint(vPt);
             boolstatus = drview.InsertViewAsBlock(insertionPt, position);

         }

         public SldWorks swApp;

     }
 }
```
