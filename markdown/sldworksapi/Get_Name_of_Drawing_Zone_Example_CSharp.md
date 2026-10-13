---
title: "Get Name of Drawing Zone Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Name_of_Drawing_Zone_Example_CSharp.htm"
---

# Get Name of Drawing Zone Example (C#)

This example shows how to get the name of a drawing zone for the specified x and y coordinates.

```
//-----------------------------------------------------------------------------
// Preconditions:
// 1. Verify that public_documents\samples\tutorial\api\assem20.slddrw exists.
// 2. Open the Immediate Window.
//
// Postconditions.
// 1. Opens the specified drawing.
// 2. Creates a new sheet named Test with four zones.
// 3. Gets the name of the drawing zone for the specified
//    x and y coordinates.
// 4. Examine the Immediate window.
//
// NOTE: Because the drawing is used elsewhere, do not save changes.
//---------------------------------------------------------------------------
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
            DrawingDoc swDraw = default(DrawingDoc);
            Sheet swSheet = default(Sheet);
            ModelDoc2 swModel = default(ModelDoc2);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            double x = 0;
            double y = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\assem20.slddrw";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swDraw = (DrawingDoc)swModel;

            swSheet = (Sheet)swDraw.GetCurrentSheet();
            swDraw.ActivateSheet(swSheet.GetName());

            // Create sheet Test with four zones
            status = swDraw.NewSheet4("Test", (int)swDwgPaperSizes_e.swDwgPaperAsize, (int)swDwgTemplates_e.swDwgTemplateAsize, 1, 1, true, "", 0, 0, "",
            0.5, 0.5, 0.5, 0.5, 2, 2);

            swModel.ForceRebuild3(true);

            swSheet = (Sheet)swDraw.GetCurrentSheet();
            swDraw.ActivateSheet(swSheet.GetName());

            // Set x and y coordinates on the sheet
            // whose drawing zone name to get
            x = 0.201705822198041;
            y = 0.0242677238302502;

            // Get the name of the drawing zone for x and y
            string drawingZoneName = null;
            drawingZoneName = swSheet.GetDrawingZone(x, y);
            Debug.Print("Drawing zone name for specified x and y coordinates: " + drawingZoneName);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
