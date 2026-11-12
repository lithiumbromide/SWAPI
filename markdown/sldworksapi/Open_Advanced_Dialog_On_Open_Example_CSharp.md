---
title: "Open Advanced Dialog on Document Open Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Advanced_Dialog_On_Open_Example_CSharp.htm"
---

# Open Advanced Dialog on Document Open Example (C#)

This example shows how to display an advanced dialog box before opening a document.

```vb
//----------------------------------------------------------------------
 // Preconditions: Verify that the specified model document to open exists.
 //
 // Postconditions:
 // 1. Displays the Configure Document dialog box before the model
 //    document opens.
 // 2. Click OK to close the dialog box.
 // 3. Close the document without saving.
 //---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;

    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 myDoc = default(ModelDoc2);
            DocumentSpecification openDocParams = default(DocumentSpecification);
            openDocParams = (DocumentSpecification)swApp.GetOpenDocSpec("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\motionstudies\\valve_cam.sldasm");
            openDocParams.DocumentType = (int)swDocumentTypes_e.swDocASSEMBLY;
            openDocParams.InteractiveAdvancedOpen = true;
            myDoc = swApp.OpenDoc7(openDocParams);
        }
        public SldWorks swApp;
    }
```
