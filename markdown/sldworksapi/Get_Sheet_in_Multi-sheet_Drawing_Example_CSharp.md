---
title: "Get Sheet in Multi-sheet Drawing Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sheet_in_Multi-sheet_Drawing_Example_CSharp.htm"
---

# Get Sheet in Multi-sheet Drawing Example (C#)

This example shows how to get each sheet in a multi-sheet drawing document regardless whether the sheet is loaded.

```
//----------------------------------------------------------------------
// Preconditions:
// 1. Click File > Open.
// 2. Open public_documents\samples\tutorial\advdrawings\foodprocessor.sldrw.
// 3. Click Select sheets to open > Selected > Sheet1* (load) > OK  >Open.
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Loads Sheet1 only.
// 2. Mouse over Sheet2, Sheet3, and Sheet4 tabs and examine the
//    Immediate window.
//
// NOTE: Because this drawing is used elsewhere, do not save changes.
//---------------------------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace SheetDrawingDocCSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            DrawingDoc swDraw = default(DrawingDoc);
            string[] vSheetName = null;
            int i = 0;
            bool bRet = false;
            string sheetName;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swDraw = (DrawingDoc)swModel;

            // Get the sheets in the drawing document
            vSheetName = (string[])swDraw.GetSheetNames();
            // Traverse the sheets and determine whether
            // they're loaded
            for (i = 0; i < vSheetName.Length; i++)
            {
                sheetName = (string)vSheetName[i];
                bRet = swDraw.ActivateSheet(sheetName);
                Sheet swSheet = default(Sheet);
                swSheet = (Sheet)swDraw.get_Sheet(vSheetName[i]);
                if ((swSheet.IsLoaded()))
                {
                    Debug.Print(vSheetName[i] + " is loaded.");
                }
                else
                {
                    Debug.Print(vSheetName[i] + " is not loaded.");
                }
            }
        }
        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
