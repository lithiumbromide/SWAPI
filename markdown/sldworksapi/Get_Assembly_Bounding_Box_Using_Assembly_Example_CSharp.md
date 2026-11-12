---
title: "Get Assembly Bounding Box Using Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Assembly_Bounding_Box_Using_Assembly_Example_CSharp.htm"
---

# Get Assembly Bounding Box Using Assembly Example (C#)

This example shows how to get the box bounding an assembly using the assembly.

```
//--------------------------------------------
// Preconditions:
// 1. Open an assembly document.
// 2. Open the Immediate window.
// 3. Run the macro.
//
// Postconditions:
// 1. Adds a 3D sketch to the assembly showing the bounding box.
// 2. Examine the graphics area and Immediate window to verify.
//
// NOTE: The assembly bounding box is approximated
// and is oriented with the assembly coordinate system.
//----------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GetBoxAssemblyCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            AssemblyDoc swAssy = default(AssemblyDoc);
            object Box = null;
            double[] BoxArray = new double[6];
            double X_max = 0;
            double X_min = 0;
            double Y_max = 0;
            double Y_min = 0;
            double Z_max = 0;
            double Z_min = 0;
            SketchManager swSketchMgr = default(SketchManager);
            SketchPoint[] swSketchPt = new SketchPoint[9];
            SketchSegment[] swSketchSeg = new SketchSegment[13];

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssy = (AssemblyDoc)swModel;

            Box = (object)swAssy.GetBox((int)swBoundingBoxOptions_e.swBoundingBoxIncludeRefPlanes);
            BoxArray = (double[])Box;

            // Initialize values
            X_max = BoxArray[3];
            X_min = BoxArray[0];
            Y_max = BoxArray[4];
            Y_min = BoxArray[1];
            Z_max = BoxArray[5];
            Z_min = BoxArray[2];

            swSketchMgr = (SketchManager)swModel.SketchManager;

            swSketchMgr.Insert3DSketch(true);
            swSketchMgr.AddToDB = true;

            // Draw points at each corner of bounding box
            swSketchPt[0] = swSketchMgr.CreatePoint(X_min, Y_min, Z_min);
            swSketchPt[1] = swSketchMgr.CreatePoint(X_min, Y_min, Z_max);
            swSketchPt[2] = swSketchMgr.CreatePoint(X_min, Y_max, Z_min);
            swSketchPt[3] = swSketchMgr.CreatePoint(X_min, Y_max, Z_max);
            swSketchPt[4] = swSketchMgr.CreatePoint(X_max, Y_min, Z_min);
            swSketchPt[5] = swSketchMgr.CreatePoint(X_max, Y_min, Z_max);
            swSketchPt[6] = swSketchMgr.CreatePoint(X_max, Y_max, Z_min);
            swSketchPt[7] = swSketchMgr.CreatePoint(X_max, Y_max, Z_max);

            // Draw bounding box
            swSketchSeg[0] = swSketchMgr.CreateLine(X_min, Y_min, Z_min, X_max, Y_min, Z_min);
            swSketchSeg[1] = swSketchMgr.CreateLine(X_max, Y_min, Z_min, X_max, Y_min, Z_max);
            swSketchSeg[2] = swSketchMgr.CreateLine(X_max, Y_min, Z_max, X_min, Y_min, Z_max);
            swSketchSeg[3] = swSketchMgr.CreateLine(X_min, Y_min, Z_max, X_min, Y_min, Z_min);
            swSketchSeg[4] = swSketchMgr.CreateLine(X_min, Y_min, Z_min, X_min, Y_max, Z_min);
            swSketchSeg[5] = swSketchMgr.CreateLine(X_min, Y_min, Z_max, X_min, Y_max, Z_max);
            swSketchSeg[6] = swSketchMgr.CreateLine(X_max, Y_min, Z_min, X_max, Y_max, Z_min);
            swSketchSeg[7] = swSketchMgr.CreateLine(X_max, Y_min, Z_max, X_max, Y_max, Z_max);
            swSketchSeg[8] = swSketchMgr.CreateLine(X_min, Y_max, Z_min, X_max, Y_max, Z_min);
            swSketchSeg[9] = swSketchMgr.CreateLine(X_max, Y_max, Z_min, X_max, Y_max, Z_max);
            swSketchSeg[10] = swSketchMgr.CreateLine(X_max, Y_max, Z_max, X_min, Y_max, Z_max);
            swSketchSeg[11] = swSketchMgr.CreateLine(X_min, Y_max, Z_max, X_min, Y_max, Z_min);

            swSketchMgr.AddToDB = false;
            swSketchMgr.Insert3DSketch(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
