---
title: "Cut and Paste Sketch Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Cut_and_Paste_Sketch_Example_CSharp.htm"
---

# Cut and Paste Sketch Example (C#)

This example shows how to cut and paste a sketch to and from the Microsoft Windows Clipboard.

```
//----------------------------------------------------------------
// Preconditions: Verify that the specified part template exists.
//
// Postconditions:
// 1. Opens a new part document.
// 2. Creates a sketch containing three lines.
// 3. Press F5 to continue.
// 4. Cuts the sketch and places it on the Microsoft
//    Windows Clipboard.
// 5. Press F5 to continue.
// 6. Pastes the sketch from the Clipboard into the part
//    document.
//----------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace EditCutCSharp.csproj
{
    partial class SolidWorksMacro
    {

        ModelDoc2 swModel;
        ModelDocExtension swModelDocExt;
        SketchManager swSketchManager;
        SketchSegment swSketchSegment;
        bool status;

        int errors;

        public void Main()
        {
            // Create a new part document
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2015\\templates\\Part.prtdot", (int)swDwgPaperSizes_e.swDwgPaperAsize, 0, 0);
            swApp.ActivateDoc3("Part1", false, (int)swRebuildOnActivation_e.swRebuildActiveDoc, ref errors);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Create a sketch
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(-0.066124, 0.011735, 0.0, -0.039675, 0.011735, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(-0.039675, -0.008754, 0.0, -0.010245, -0.008754, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(-0.010245, -0.029989, 0.0, 0.022166, -0.029989, 0.0);
            swModel.ClearSelection2(true);
            swSketchManager.InsertSketch(true);

            System.Diagnostics.Debugger.Break();
            // Examine the graphics area to
            // verify that the sketch was created

            // Press F5 to continue executing the
            // macro

            // Select the sketch and place it on the Microsoft Windows Clipboard
            status = swModelDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.051595524691358, 0.0117347222222222, 0, false, 0, null, 0);
            swModel.EditCut();

            System.Diagnostics.Debugger.Break();
            // Examine the graphics area to
            // verify that the sketch was cut

            // Press F5 to continue executing the
            // macro

            // Paste the contents of the Clipboard into the
            // part document

            swModel.Paste();
            // Examine the graphics area to
            // verify that the sketch was pasted
            // into the document
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
