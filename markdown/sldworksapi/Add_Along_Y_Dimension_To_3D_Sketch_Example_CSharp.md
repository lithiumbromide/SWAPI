---
title: "Add Along Y Dimension to 3D Sketch Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Along_Y_Dimension_To_3D_Sketch_Example_CSharp.htm"
---

# Add Along Y Dimension to 3D Sketch Example (C#)

This example shows how to add a display dimension along the y axis in a 3D sketch.

```
//----------------------------------------------------------------------------
// Preconditions: Verify that the specified part template exists.
//
// Postconditions:
// 1. Opens a new part document.
// 2. Creates a 3D sketch.
// 3. Click the green check mark in the Modify dimension dialog
//    (If you don't see the dialog, look for it behind other open windows).
// 4. Puts 3DSketch1 in edit mode; 3DSketch1 contains a spline and a
//    corner rectangle.
// 5. Displays the display dimension of 63.24 mm on the y axis starting at
//    (-0.1, 0, 0.01111142101618) while the sketch is in edit mode.
// 6. Examine the graphics area.
//----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 Part = default(ModelDoc2);
            DisplayDimension myDisplayDim = default(DisplayDimension);
            bool boolstatus = false;
            int longstatus = 0;

            longstatus = swApp.ResetUntitledCount(0, 0, 0);
            Part = (ModelDoc2)swApp.NewDocument("C:\\Documents and Settings\\All Users\\Application Data\\SOLIDWORKS\\SOLIDWORKS 2015\\templates\\Part.prtdot", 0, 0, 0);
            swApp.ActivateDoc2("Part1", false, ref longstatus);
            Part = (ModelDoc2)swApp.ActiveDoc;

            Part.SketchManager.Insert3DSketch(true);
            object vSkLines = null;
            vSkLines = (object)Part.SketchManager.CreateCornerRectangle(-0.05171778666374, 0.01933785938058, 0.03, 0.08445537697179, -0.04142795937025, -0.03);
            boolstatus = Part.Extension.SelectByID2("Right Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            Part.ClearSelection2(true);

            object pointArray = null;
            double[] points = new double[12];
            points[0] = 0;
            points[1] = -0.03591009660795;
            points[2] = 0.04608246573503;
            points[3] = 0;
            points[4] = 0.0147420284178;
            points[5] = 0.005170989573514;
            points[6] = 0;
            points[7] = -0.006478053228363;
            points[8] = -0.04282131900055;
            points[9] = 0;
            points[10] = -0.02294509596464;
            points[11] = -0.09396066420243;
            pointArray = (object) points;

            SketchSegment skSegment = default(SketchSegment);
            skSegment = (SketchSegment)Part.SketchManager.CreateSpline2((pointArray), true);
            Part.SketchManager.InsertSketch(true);
            boolstatus = Part.Extension.SelectByID2("3DSketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
            Part.EditSketch();
            boolstatus = Part.Extension.SelectByID2("Point5", "SKETCHPOINT", 0, -0.03591009660795, 0.04608246573503, false, 0, null, 0);
            boolstatus = Part.Extension.SelectByID2("Point4", "SKETCHPOINT", 0.08445537697179, 0.02732744880518, -0.01872625210654, true, 0, null, 0);
            myDisplayDim = (DisplayDimension)Part.SketchManager.AddAlongYDimension(-0.1, 0, 0.01111142101618);
            Part.ClearSelection2(true);

            Part.ViewZoomtofit2();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
