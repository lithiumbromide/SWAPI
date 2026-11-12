---
title: "Create Full Symmetrical Angular Dimension Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Full_Symmetrical_Angular_Dimension_Example_CSharp.htm"
---

# Create Full Symmetrical Angular Dimension Example (C#)

This example shows how to create a full symmetrical angular dimension between a centerline and a line.

```
//---------------------------------------------------------
// Preconditions: Verify that the specified part document template
// exists.
//
// Postconditions:
// 1. Opens a new part document.
// 2. Opens a sketch.
// 3. Creates a centerline and three lines in
//    the open sketch.
// 4. Selects the centerline and one of the lines.
// 5. Suppresses the dimension dialog.
// 6. Creates a full symmetrical angular dimension for
//    the entities selected in step 4.
// 7. Unsuppresses the dimension dialog.
// 8. Examine the graphics area to verify step 6.
//----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace AddSymmetricDimensionCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SketchManager swSketchMgr = default(SketchManager);
            SketchSegment swSketchSegment = default(SketchSegment);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            DisplayDimension swDisplayDimension = default(DisplayDimension);
            bool status = false;

            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2015\\templates\\Part.prtdot", 0, 0, 0);

            //Sketch a centerline and three lines
            swSketchMgr = (SketchManager)swModel.SketchManager;
            swSketchMgr.InsertSketch(true);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateCenterLine(0.0, 0.043667, 0.0, 0.0, -0.050556, 0.0);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(-0.102, 0.039667, 0.0, -0.086223, 0.011, 0.0);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(0.142445, 0.066556, 0.0, 0.100889, -0.032333, 0.0);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(0.085334, 0.036556, 0.0, 0.049658, -0.048341, 0.0);

            //Select the centerline and one of the lines
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", -0.000222223294397278, 0.0223334410869282, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0.113556103437018, -0.00144445141358242, 0, true, 0, null, 0);
            swModel.ClearSelection2(true);

            //Suppress the dimension dialog box
            swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swInputDimValOnCreate, false);

            //Create a full symmetrical angular dimension
            status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", -0.000222223294397278, 0.0223334410869282, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0.113556103437018, -0.00144445141358242, 0, true, 0, null, 0);
            swDisplayDimension = (DisplayDimension)swModelDocExt.AddSymmetricDimension(0.0832913738352659, 0.112403597688285, 0);
            swModel.ClearSelection2(true);

            //Unsuppress the dimension dialog box
            swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swInputDimValOnCreate, true);

            swModel.ViewZoomtofit2();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
