---
title: "Get Loaded Sheets Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Loaded_Sheets_Example_CSharp.htm"
---

# Get Loaded Sheets Example (C#)

This example shows how to determine which sheets in a drawing are loaded.

```
//----------------------------------------------
// Preconditions:
// 1. Click File > Open.
// 2. Browse to public_documents\samples\tutorial\advdrawings.
// 3. Select foodprocessor.slddrw.
// 4. Click Select sheets to open > Selected > Sheet1* (Load) > OK > Open.
// 5. Open the Immediate window.
//
// Postconditions:
// 1. Loads Sheet1 only.
// 2. Mouse over the Sheet2, Sheet3, and Sheet4 tabs and
//    examine the Immediate window to verify step 1.
//
// NOTE: Because this drawing is used elsewhere, do not save
// changes.
//----------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace IsLoadedSheetCSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            DrawingDoc swDraw = default(DrawingDoc);
            object[] vSheetName = null;
            int i = 0;
            bool bRet = false;
            string sheetName;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swDraw = (DrawingDoc)swModel;

            // Get the sheets in the drawing document
            vSheetName = (object[])swDraw.GetSheetNames();

            // Traverse the sheets and determine whether
            // they're loaded
            for (i = 0; i < vSheetName.Length; i++)
            {
                sheetName = (string)vSheetName[i];
                bRet = swDraw.ActivateSheet(sheetName);
                Sheet swSheet = default(Sheet);
                swSheet = (Sheet)swDraw.GetCurrentSheet();
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
