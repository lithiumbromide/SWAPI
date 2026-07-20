---
title: "Place Note Behind Drawing Sheet Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Place_Note_Behind_Drawing_Sheet_Example_CSharp.htm"
---

# Place Note Behind Drawing Sheet Example (C#)

This example shows how to place a note behind a drawing sheet.

```
//----------------------------------------------------------
// Preconditions:
// 1. Verify that the specified drawing file to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Places the selected note, 2012-sm in the drawing template,
//    behind the drawing sheet.
// 2. To verify:
//    a. Examine the Immediate window.
//    b. Right-click the drawing and click
//       Edit Sheet Format.
//    c. Right-click 2012-sm and examine the
//       the short-cut menu to verify that Display
//       Note Behind Sheet is selected.
//    d. Exit drawing sheet edit mode.
//
// NOTE: Because this drawing is used elsewhere, do not
// save changes.
//-----------------------------------------------------------
```

```
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace NoteBehindSheetCSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            DrawingDoc swDrawing = default(DrawingDoc);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Note swNote = default(Note);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            // Open drawing
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2024\\samples\\tutorial\\api\\2012-sm.slddrw";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swDrawing = (DrawingDoc)swModel;

            // Put drawing template and sheet in edit mode
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Sheet1", "SHEET", 0.0399580396732789, 0.20594194865811, 0, false, 0, null, 0);
            swDrawing.EditTemplate();
            swDrawing.EditSheet2();

            swModel.ClearSelection2(true);

            // Select note to place behind the sheet
            status = swModelDocExt.SelectByID2("DetailItem3@Sheet Format1", "NOTE", 0.155548914819136, 0.017885845974329, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swNote = (Note)swSelectionMgr.GetSelectedObject6(1, -1);
            swNote.BehindSheet = true;
            Debug.Print("Was the selected note placed behind the sheet? " + status);

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
