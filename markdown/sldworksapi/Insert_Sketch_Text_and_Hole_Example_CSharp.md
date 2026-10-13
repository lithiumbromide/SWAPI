---
title: "Insert Sketch Text and Hole Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Sketch_Text_and_Hole_Example_CSharp.htm"
---

# Insert Sketch Text and Hole Example (C#)

This example shows how to insert sketch text and a hole at the selected point on a face.

```vb
  //----------------------------------------------------------------------------
  // Preconditions: Open a model document and select a face.
 //
 // Postconditions:
 // 1. Creates a hole and inserts the specified text on the
 //    face at its point of selection.
 // 2. Examine the graphics area and FeatureManager design tree.
  //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace InsertSketchText_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         SelectionMgr swSelMgr;
         MathPoint swMathPt;
         Face2 selFace;
         Entity selEnt;
         double[] selPt;
         object NewPt;
         MathUtility swMathUtil;
         MathTransform swMathTrans;
         SelectData selData;
         SketchManager swSketchMgr;
         SketchText skText;
         double[] ptArr = new double[3];
         object @params;
         Feature holeFeat;
         FeatureManager swFeatMgr;

         bool boolstatus;

         public object TransformPoint(Sketch Sketch1, double X, double Y, double Z)
         {

             ptArr[0] = X;
             ptArr[1] = Y;
             ptArr[2] = Z;

             swMathUtil = (MathUtility)swApp.GetMathUtility();
             swMathPt = (MathPoint)swMathUtil.CreatePoint((ptArr));

             @params = swMathPt.ArrayData;

             swMathTrans = Sketch1.ModelToSketchTransform;
             swMathPt = (MathPoint)swMathPt.MultiplyTransform(swMathTrans);

             NewPt = swMathPt.ArrayData;

             return NewPt;

         }

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             selFace = (Face2)swSelMgr.GetSelectedObject6(1, -1);
             selEnt = (Entity)selFace;

             selPt = (double[])swSelMgr.GetSelectionPoint2(1, -1);

             selData = swSelMgr.CreateSelectData();

             selData.X = selPt[0];
             selData.Y = selPt[1];
             selData.Z = selPt[2];

             swSketchMgr = swModel.SketchManager;

             swSketchMgr.InsertSketch(true);

             selPt = (double[])TransformPoint(swModel.IGetActiveSketch2(), selPt[0], selPt[1], selPt[2]);

             skText = (SketchText)swModel.InsertSketchText(selPt[0], selPt[1], selPt[2], "Hole", 0, 0, 0, 100, 100);

             @params = skText.GetCoordinates();

             swSketchMgr.InsertSketch(true);

             boolstatus = selEnt.Select4(false, selData);

             swFeatMgr = swModel.FeatureManager;
             holeFeat = swFeatMgr.SimpleHole2(0.001, true, false, false, 0, 0, 0.001, 0.001, false, false,
             false, false, 0, 0, false, false, false, false, true, true,
             false, false, false);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```
