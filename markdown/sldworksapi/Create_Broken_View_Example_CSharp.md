---
title: "Create Break View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Broken_View_Example_CSharp.htm"
---

# Create Break View Example (C#)

This example shows how to create and remove a broken view.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified file to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified drawing and selects Drawing View1.
// 2. Examine the drawing, then press F5.
// 3. Inserts break lines in Drawing View1.
// 4. Examine the drawing, then press F5.
// 5. Modifies the positions of the break lines and breaks the view.
// 6. Examine the drawing, then press F5.
// 7. Removes the break from Drawing View1.
// 8. Examine the drawing and the Immediate window.
//
// NOTE: Because this drawing document is used elsewhere,
// do not save changes.
//----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace BreakViewDrawingDocCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel;
            DrawingDoc swDrawingDoc;
            ModelDocExtension swModelDocExt;
            SelectionMgr swSelectionManager;
            SelectData swSelectData;
            View swView;
            BreakLine swBreakLine;
            string fileName;
            bool status;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\box.slddrw";
            swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swDrawingDoc = (DrawingDoc)swModel;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Activate and select the view to break

            status = swDrawingDoc.ActivateView("Drawing View1");

            status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, false, 0, null, 0);

            swSelectionManager = (SelectionMgr)swModel.SelectionManager;
            swSelectData = (SelectData)swSelectionManager.CreateSelectData();

            swView = (View)swSelectionManager.GetSelectedObject6(1, -1);

            System.Diagnostics.Debugger.Break();

// Examine the drawing; press F5

            // Insert the break lines

            swBreakLine = (BreakLine)swView.InsertBreak(0, -0.0291950859897372, 0.0198236302285804, 1);

            System.Diagnostics.Debugger.Break();

// Break lines inserted; press F5

            // Reset position of break lines

            status = swBreakLine.SetPosition(-0.03, 0.05);
            swModel.EditRebuild3

            Debug.Print("Break line: ");

            Debug.Print("
Selected: " + swBreakLine.Select(true, null));

            Debug.Print(" Style: " + swBreakLine.Style);

            Debug.Print(" Orientation: " + swBreakLine.Orientation);

            Debug.Print(" Position: " + swBreakLine.GetPosition(0));

            swDrawingDoc.BreakView();
```

System.Diagnostics.

Debugger.Break();
// Positions of the break lines are modified, and view is broken
// Press F5

status = swModelDocExt.**SelectByID2**(

"Drawing View1", "DRAWINGVIEW", 0, 0, 0, false, 0, null, 0);
swDrawingDoc.**UnBreakView**();

// Break is removed

}

/// <summary>
/// The SldWorks swApp variable is pre-assigned for you.
/// </summary>
public SldWorks swApp;
}
}
