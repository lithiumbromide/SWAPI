---
title: "Set Radial Dimension Leader Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Edit_Radial_Dimension_Example_CSharp.htm"
---

# Set Radial Dimension Leader Example (C#)

This example shows how to attach a radial dimension leader to an arc extension line.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Verify that the part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the part.
// 2. Edits the sketch and creates a fillet.
// 3. Attaches the radial dimension leader to the arc extension
//    line.
// 4. Gets whether the radial dimension leader is attached to
//    the arc extension line.
// 5. Examine the graphics area, then press F5.
// 6. Exits the sketch.
// 7. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//---------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchManager = default(SketchManager);
            SketchSegment swSketchSegment = default(SketchSegment);
            SelectionMgr swSelectionManager = default(SelectionMgr);
            DisplayDimension swDisplayDimension = default(DisplayDimension);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            //Open the part
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\box.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Edit the sketch and create a fillet
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
            swModel.EditSketch();
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Point1", "SKETCHPOINT", -0.0811067833265636, 0.0389478433654258, 0, false, 0, null, 0);
            swSketchManager = swModel.SketchManager;
            swSketchSegment = (SketchSegment)swSketchManager.CreateFillet(0.01, (int)swConstrainedCornerAction_e.swConstrainedCornerDeleteGeometry);
```

```
       	    //Select and set the radial dimension
            status = swModelDocExt.SelectByID2("D1@Sketch1@box.SLDPRT", "DIMENSION", -5.09218235791179E-02, 2.23786104078373E-02, 6.93106363229314E-03, false, 0, null, 0);
            swSelectionManager = (SelectionMgr)swModel.SelectionManager;
            swDisplayDimension = (DisplayDimension)swSelectionManager.GetSelectedObject6(1, -1);
            swDisplayDimension.ArcExtensionLineOrOppositeSide = true;
            Debug.Print ("Leader attached to arc extension line? " + swDisplayDimension.ArcExtensionLineOrOppositeSide);

            System.Diagnostics.Debugger.Break();
            //Examine the graphics area, then press F5

            //Exit the sketch
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
