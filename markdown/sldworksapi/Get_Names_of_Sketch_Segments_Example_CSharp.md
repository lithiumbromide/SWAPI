---
title: "Get Names of Sketch Segments Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_of_Sketch_Segments_Example_CSharp.htm"
---

# Get Names of Sketch Segments Example (C#)

This example shows how to get the names of the sketch segments in a sheet metal bend.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a sheet metal part or a drawing containing a bend.
 // 2. Unsuppress the flat pattern for the bend.
 // 3. Select a bend feature in the FeatureManager design tree.
 // 4. Ensure that the namespace matches the name of your C# project.
 //
 // Postconditions: Inspect the Immediate window for information about each
 // sketch segment in the bend feature.
 //--------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 namespace FlatPatternSketchSegments_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             MathUtility swMathUtil = default(MathUtility);
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             OneBendFeatureData swOneBend = default(OneBendFeatureData);
             Object[] vSketchSegs = null;
             SketchSegment swSketchSeg = default(SketchSegment);
             Sketch swSketch = default(Sketch);
             Feature swSketchFeat = default(Feature);
             SketchLine swSketchLine = default(SketchLine);
             SketchPoint swSkStartPt = default(SketchPoint);
             SketchPoint swSkEndPt = default(SketchPoint);
             SelectData swSelData = default(SelectData);
             double[] nPt = new double[3];
             MathPoint swStartPt = default(MathPoint);
             MathPoint swEndPt = default(MathPoint);
             MathTransform swSkXform = default(MathTransform);
             int[] vID = null;
             int i = 0;

             swMathUtil = (MathUtility)swApp.GetMathUtility();
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swSelData = swSelMgr.CreateSelectData();
             swOneBend = (OneBendFeatureData)swFeat.GetDefinition();
             Debug.Print("Type of bend (swBendType_e): " + swOneBend.GetType());
             Debug.Print("Number of sketch segments: " + swOneBend.GetFlatPatternSketchSegmentCount2());
             vSketchSegs = (Object[])swOneBend.FlatPatternSketchSegments2;

             for (i = 0; i <= vSketchSegs.GetUpperBound(0); i++)
             {
                 swSketchSeg = (SketchSegment)vSketchSegs[i];
                 swSketch = swSketchSeg.GetSketch();
                 swSketchLine = (SketchLine)swSketchSeg;
                 swSkStartPt = (SketchPoint)swSketchLine.GetStartPoint2();
                 swSkEndPt = (SketchPoint)swSketchLine.GetEndPoint2();
                 vID = (int[])swSketchSeg.GetID();

                 // Get sketch feature
                 swSketchFeat = (Feature)swSketch;
                 swSkXform = swSketch.ModelToSketchTransform;
                 swSkXform = (MathTransform)swSkXform.Inverse();

                 nPt[0] = swSkStartPt.X;
                 nPt[1] = swSkStartPt.Y;
                 nPt[2] = swSkStartPt.Z;
                 swStartPt = (MathPoint)swMathUtil.CreatePoint(nPt);
                 swStartPt = (MathPoint)swStartPt.MultiplyTransform(swSkXform);
                 double[] swStartPtArrayData;
                 swStartPtArrayData = (double[])swStartPt.ArrayData;

                 nPt[0] = swSkEndPt.X;
                 nPt[1] = swSkEndPt.Y;
                 nPt[2] = swSkEndPt.Z;
                 swEndPt = (MathPoint)swMathUtil.CreatePoint(nPt);
                 swEndPt = (MathPoint)swEndPt.MultiplyTransform(swSkXform);
                 double[] swEndPtArrayData;
                 swEndPtArrayData = (double[])swEndPt.ArrayData;

                 Debug.Print("File = " + swModel.GetPathName());
                 Debug.Print("  Feature = " + swFeat.Name +  " [" + swFeat.GetTypeName2() + "]");
                 Debug.Print("    Sketch             = " + swSketchFeat.Name);
                 Debug.Print("    SegID              = [" + vID[0] +  ", " + vID[1] + "]");
                 Debug.Print("    Start with respect to sketch   = (" + swSkStartPt.X * 1000.0 + ", " + swSkStartPt.Y * 1000.0 + ", " + swSkStartPt.Z * 1000.0 + ") mm");
                 Debug.Print("    End with respect to sketch   = (" + swSkEndPt.X * 1000.0 + ", " + swSkEndPt.Y * 1000.0 + ", " + swSkEndPt.Z * 1000.0 + ") mm");
                 Debug.Print("    Start with respect to model    = (" + swStartPtArrayData[0] * 1000.0 + ", " + swStartPtArrayData[1] * 1000.0 + ", " + swStartPtArrayData[2] * 1000.0 + ") mm");
                 Debug.Print("    End with respect to model    = (" + swEndPtArrayData[0] * 1000.0 + ", " + swEndPtArrayData[1] * 1000.0 + ", " + swEndPtArrayData[2] * 1000.0 + ") mm");
             }
         }

         public SldWorks swApp;

     }
 }
```
