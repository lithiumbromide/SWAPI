---
title: "Get Sketch Point's Selection Mark Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Points_Selection_Mark_Example_CSharp.htm"
---

# Get Sketch Point's Selection Mark Example (C#)

This example shows how to get the selection mark of a sketch point.

```
//------------------------------------------------
// Preconditions:
// 1. Open a part containing a sketch point.
// 2. Select the sketch containing the sketch point.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Gets the selection mark of the sketch point.
// 2. Examine the Immediate window.
//-----------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GetReferencePointCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Feature swFeat = default(Feature);
            Sketch swSketch = default(Sketch);
            object[] sketchPoints = null;
            SketchPoint swSketchPt = default(SketchPoint);
            SelectData swSelData = default(SelectData);
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swSketch = (Sketch)swFeat.GetSpecificFeature2();
            sketchPoints = (object[])swSketch.GetSketchPoints2();
            swSketchPt = (SketchPoint)sketchPoints[0];

            // Get selection mark of sketch point
            swSelData = (SelectData)swSelMgr.CreateSelectData();
            status = swSketchPt.Select4(true, swSelData);
            Debug.Print("Selection mark of sketch point: " + swSelData.Mark);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
