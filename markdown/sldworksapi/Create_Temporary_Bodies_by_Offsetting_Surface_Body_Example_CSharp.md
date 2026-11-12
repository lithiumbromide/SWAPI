---
title: "Create Temporary Bodies by Offsetting a Surface Body Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Temporary_Bodies_by_Offsetting_Surface_Body_Example_CSharp.htm"
---

# Create Temporary Bodies by Offsetting a Surface Body Example (C#)

This example shows how to create two temporary bodies by offsetting a surface body.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document template exists.
// 2. Add a reference to Microsoft.VisualBasic (right-click the name of
//    the project in the Project Explorer, click Add Reference, the .NET tab >
//    Microsoft.VisualBasic > OK.
//
// Postconditions:
// 1. Opens a new part document.
// 2. Creates a surface body.
// 3. Selects an edge on the surface body to offset.
// 4. Creates two temporary bodies of the surface
//    body using the selected edge.
// 5. Examine the graphics area.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using Microsoft.VisualBasic;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            FeatureManager swFeatureManager = default(FeatureManager);
            SketchSegment sketchSegment = default(SketchSegment);
            SketchManager swSketchManager = default(SketchManager);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionManager = default(SelectionMgr);
            Edge swEdge = default(Edge);
            Body2 swBody = default(Body2);
            Body2 newBody1 = default(Body2);
            Body2 newBody2 = default(Body2);
            object pointArray = null;
            double[] points = new double[12];
            bool status = false;

            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2015\\templates\\Part.prtdot", 0, 0, 0);
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swSketchManager = (SketchManager)swModel.SketchManager;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelectionManager = (SelectionMgr)swModel.SelectionManager;

            //Create extruded surface body
            points[0] = -0.0720746414289124;
            points[1] = -0.0283600245263074;
            points[2] = 0;
            points[3] = -0.0514715593755;
            points[4] = -0.00345025084396866;
            points[5] = 0;
            points[6] = 0;
            points[7] = 0;
            points[8] = 0;
            points[9] = 0.0872558597840225;
            points[10] = 0.0521037067517796;
            points[11] = 0;
            pointArray = points;
            sketchSegment = (SketchSegment)swSketchManager.CreateSpline((pointArray));
            swSketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 4, null, 0);
            swFeatureManager.FeatureExtruRefSurface2(true, false, false, 0, 0, 0.0508, 0.00254, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, false, false, false,
            false);
            swSelectionManager.EnableContourSelection = false;

            //Offset selected edge and create two temporary bodies
            status = swModelDocExt.SelectByID2("", "EDGE", -0.00623752003605205, 0.000329492391927033, 0.050581684437077, false, 0, null, 0);
            swEdge = (Edge)swSelectionManager.GetSelectedObject6(1, -1);
            swBody = (Body2)swEdge.GetBody();
            swBody = (Body2)swBody.Copy();
            //Using a copy of the selected surface body, create two new temporary bodies
            newBody1 = (Body2)swBody.MakeOffset(0.01, false);
            newBody2 = (Body2)swBody.MakeOffset(0.01, true);
            //Display and color the new temporary body blue
            newBody1.Display3(swModel, Information.RGB(0, 0, 255), (int)swTempBodySelectOptions_e.swTempBodySelectOptionNone);
            //Display and color the new temporary body red
            newBody2.Display3(swModel, Information.RGB(255, 0, 0), (int)swTempBodySelectOptions_e.swTempBodySelectOptionNone);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
