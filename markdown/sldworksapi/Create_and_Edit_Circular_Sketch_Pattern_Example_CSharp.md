---
title: "Create and Edit Circular Sketch Pattern Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Edit_Circular_Sketch_Pattern_Example_CSharp.htm"
---

# Create and Edit Circular Sketch Pattern Example (C#)

This example shows how to create and edit a circular sketch pattern.

//------------------------------------------------------------
// Preconditions: Verify that the specified part document template
// exists.
//
// Postconditions:
// 1. Opens a new part document and creates a sketch.
// 2. Inserts a circular sketch pattern of four instances.
// 3. Closes the sketch.
// 4. Opens the circular sketch pattern for editing.
// 5. Deletes an instance of the circular sketch pattern, leaving
// three instances.
// 6. Examine the graphics area.
//------------------------------------------------------------

```vb
using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 namespace Macro1CSharp.csproj
 {
     partial class SolidWorksMacro
    {
         public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             SketchManager swSketchMgr = default(SketchManager);
             SketchSegment swSketchSegment = default(SketchSegment);
             object vSkLines = null;
             bool boolstatus = false;
             int longstatus = 0;

             // Reset the counts for untitled documents for this macro
             swApp.ResetUntitledCount(0, 0, 0);

             // Create a part document
             swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
             swApp.ActivateDoc2("Part1", false, ref longstatus);
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSketchMgr = swModel.SketchManager;
             swModelDocExt = swModel.Extension;
            // Sketch a circle
             swSketchSegment = swSketchMgr.CreateCircle(0.0, 0.0, 0.0, 0.045549, 0.013926, 0.0);

             // Clear any selections and change
             // the view orientation to Front
             swModel.ClearSelection2(true);
             swModel.ShowNamedView2("*Front", 1);

             // Create a rectangle
             vSkLines = swSketchMgr.CreateCornerRectangle(-0.005867589431389, 0.03694408160504, 0, 0.004563680668858, 0.02673012963188, 0);
             // Create a circular sketch pattern
             // using the rectangle
             boolstatus = swSketchMgr.CreateCircularSketchStepAndRepeat(0.03184378021964, 4.732863934409, 4, 1.570796326795, true, "", true, true, true);
             swModel.ClearSelection2(true);

             // Close the sketch and rebuild
             swSketchMgr.InsertSketch(true);

             // Select an entity in the circular sketch pattern
             // and open the circular sketch pattern to edit it
             boolstatus = swModelDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.002390499397973, 0.03694408160504, 0, false, 0, null, 0);

             swModel.EditSketch();

             // Delete an instance of the circular
             // sketch pattern and close the sketch
              boolstatus = swSketchMgr.EditCircularSketchStepAndRepeat(0.03184378021964, 4.732863934409, 3, 1.570796326795, true, "", true, true, true, "Line2_Line1_Line4_Line3_");
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);
        }
        public SldWorks swApp;
    }
}
```
