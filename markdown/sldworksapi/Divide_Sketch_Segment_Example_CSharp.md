---
title: "Divide Sketch Segment Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Divide_Sketch_Segment_Example_CSharp.htm"
---

# Divide Sketch Segment Example (C#)

This example shows how to divide a sketch segment into equally spaced sketch points.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Ensure that the specified template exists.
 //
 // Postconditions:
 // 1. Creates Sketch1.
 // 2. Divides the sketch's line into 99 equally spaced sketch points.
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
 namespace DivideSketchSegment_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         SketchSegment skSegment;
         SketchSegment SkSeg;
         bool boolstatus;
         int longstatus;

         public void Main()
         {
             Part = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2015\\templates\\Part.prtdot", 0, 0, 0);
             swApp.ActivateDoc2("Part1", false, ref longstatus);
             Part = (ModelDoc2)swApp.ActiveDoc;

             Part.SketchManager.InsertSketch(true);
             skSegment = Part.SketchManager.CreateLine(-0.067186, 0.00851, 0.0, 0.07118, 0.081524, 0.0);
             boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);

             Part = (ModelDoc2)swApp.ActiveDoc;
             boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0.0058451006543539, 0.017433416397686, -0.0149283857579217,  false, 0,  null, 0);

             SkSeg = (SketchSegment)((SelectionMgr)Part.SelectionManager).GetSelectedObject6(1, -1);
             boolstatus = SkSeg.EqualSegment((int)swSketchSegmentType_e.swSketchSegmentType_sketchpoints, 99);

             Part.ForceRebuild3(true);

             boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
             Part.EditSketch();
             Part.SketchManager.InsertSketch(true);

         }

         public SldWorks swApp;

     }

 }
```
