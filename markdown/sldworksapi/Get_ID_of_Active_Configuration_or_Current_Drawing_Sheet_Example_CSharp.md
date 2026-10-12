---
title: "Get ID of Active Configuration or Current Drawing Sheet Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_CSharp.htm"
---

# Get ID of Active Configuration or Current Drawing Sheet Example (C#)

This example shows how to get the name and ID of the active configuration of a part or assembly or the current sheet of a drawing.

**NOTE:** A unique ID is assigned to each configuration and drawing. This ID does not change when the name of the configuration or drawing sheet is changed.

```
//-------------------------------------------------------
// Preconditions:
// 1. Open a part, assembly, or drawing document.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Changes either the active configuration's name or
//    the current sheet's name to Test. However, the
//    document's ID is unchanged.
// 2. Examine the Immediate window.
//------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            Configuration swConfig = default(Configuration);
            DrawingDoc swDrawingDoc = default(DrawingDoc);
            Sheet swSheet = default(Sheet);
            int nDocType = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;

            // Get type of model document
            if (swModel.GetType() == 1)
            {
                nDocType = (int)swDocumentTypes_e.swDocPART;
            }
            else if (swModel.GetType() == 2)
            {
                nDocType = (int)swDocumentTypes_e.swDocASSEMBLY;
            }
            else if (swModel.GetType() == 3)
            {
                nDocType = (int)swDocumentTypes_e.swDocDRAWING;
            }
            else
            {
                // Not a SOLIDWORKS Design model document,
                // so exit macro
                return;
            }

            // If a part or assembly document,
            // then get the name of it and its ID
            if (nDocType != (int)swDocumentTypes_e.swDocDRAWING)
            {
                swConfig = (Configuration)swModel.GetActiveConfiguration();
                if ((swConfig != null))
                {
                    Debug.Print("Active configuration's name = " + swConfig.Name + ", ID = " + swConfig.GetID());
                    // Change the active configuration's name
                    swConfig.Name = "Test";
                    // Test to see if the ID remains the same
                    // after changing the name of the configuration
                    Debug.Print("Active configuration's new name = " + swConfig.Name + ", ID = " + swConfig.GetID());
                }
                return;
            }

            // A drawing sheet must be active,
            // so get its name and ID
            swDrawingDoc = (DrawingDoc)swModel;
            swSheet = (Sheet)swDrawingDoc.GetCurrentSheet();
            if ((swSheet != null))
            {
                Debug.Print("Current sheet's name = " + swSheet.GetName() + ", ID = " + swSheet.GetID());
                // Change current sheet's name
                swSheet.SetName("Test");
                // Test to see if the ID remains the same
                // after changing the name of the sheet
                Debug.Print("Current sheet's new name = " + swSheet.GetName() + ", ID = " + swSheet.GetID());
            }

        }

        public SldWorks swApp;

    }

}
```
