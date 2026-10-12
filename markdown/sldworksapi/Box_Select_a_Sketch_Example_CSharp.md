---
title: "Box Select a Sketch Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Box_Select_a_Sketch_Example_CSharp.htm"
---

# Box Select a Sketch Example (C#)

This example shows how to box select all of the entities in a sketch block.

//-----------------------------------------------------------------------------
// Preconditions: Open `public_documents`**\samples\tutorial\blocks\piston_mechanism.sldblk**.
//
// Postconditions:
// 1. Opens and box selects **Sketch1**.
// 2. Examine the list of selected entities
// in the PropertyManager page.
// 3. Interactively quit editing the sketch without
// saving any changes.
// 4. Close the document.
//--------------------------------------

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
namespace SketchBoxSelect_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            bool boolstatus = false;
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = swModel.Extension;
            // Select the sketch and open it
            boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
            swModel.EditSketch();
            swModel.ViewZoomtofit2();

            // Box select the sketch
            boolstatus = swModelDocExt.SketchBoxSelect("-0.663893", "1.322001", "0.000000", "-0.395073", "0.698568", "0.000000");
        }
        public SldWorks swApp;
    }
}
```
