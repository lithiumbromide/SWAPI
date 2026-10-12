---
title: "Convert Edges and Inner Loops of Face to Sketch Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Convert_Edges_and_Inner_Loops_of_Face_to_Sketch_Entities_Example_CSharp.htm"
---

# Convert Edges and Inner Loops of Face to Sketch Entities Example (C#)

This example shows how to convert the edges and inner loops of a selected face to sketch entities on a sketch plane.

```
//------------------------------------------------------------------------
// Preconditions: Open public_documents\samples\tutorial\api\cover_plate.slprt.
//
// Postconditions:
// 1. Creates an offset plane named Plane1.
// 2. Opens a sketch on Plane1.
// 3. Selects a face on the part.
// 4. Converts the edges and inner loops of the selected face to sketch
//    entities and creates Sketch2.
// 5. Examine the graphics area and FeatureManager design tree.
//
// NOTE: Because this part is used elsewhere, do not save changes.
//------------------------------------------------------------------------
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
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatureManager = default(FeatureManager);
            RefPlane swRefPlane = default(RefPlane);
            SketchManager swSketchManager = default(SketchManager);
            bool boolstatus = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swSketchManager = (SketchManager)swModel.SketchManager;

            //Create offset plane
            boolstatus = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
            swRefPlane = (RefPlane)swFeatureManager.InsertRefPlane(8, 0.05, 0, 0, 0, 0);
            swModel.ClearSelection2(true);

            //Open sketch on Plane1
            boolstatus = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchManager.InsertSketch(true);

            //Select face whose edges and inner loops to convert
            boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.0456486773091456, 0.085157409722342, 0, false, 0, null, 0);

            //Convert edges and inner loops of selected face to sketch entities
            boolstatus = swSketchManager.SketchUseEdge3(false, true);

            //Clear the selections and close the sketch
            swModel.ClearSelection2(true);
            swSketchManager.InsertSketch(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
