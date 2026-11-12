---
title: "Copy and Paste Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_and_Paste_Feature_Example_CSharp.htm"
---

# Copy and Paste Feature Example (C#)

This example shows how to copy and paste a feature in a part document.

```
//----------------------------------------------------------------
// Preconditions: Verify that the specified part document to
// open exists.
//
// Postconditions:
// 1. Displays the Copy Confirmation dialog after calling
//    IModelDoc2::Paste.
// 2. Click Delete.
// 3. Pastes the copied feature on the selected face.
//
// NOTE: Because this part is used elsewhere, do not save changes.
//----------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace EditCopyPasteModelDoc2CSharp.csproj
{
    partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        ModelDocExtension swModelDocExt;
        string fileName;
        bool status;
        int errors;
        int warnings;

        public void Main()
        {
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\testpart1.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            // Select the feature to copy
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swModel.EditCopy();

            swModel.ClearSelection2(true);

            // Select the face where to paste the copied feature
            status = swModelDocExt.SelectByID2("", "FACE", 0.0297472797980731, 0.0564587562103043, 0.00676585125080464, false, 0, null, 0);

            // Paste the copied feature on the selected face
            swModel.Paste();

            // Display the Copy Confirmation dialog
            // Click Delete
            // Pastes the copied feature on the selected face
```

//Zoom to selection, then zoom to fit
swModel.**ViewZoomToSelection**();
swModel.**ViewZoomtofit2**();

}

/// <summary>
/// The SldWorks swApp variable is pre-assigned for you.
/// </summary>

public SldWorks swApp;

}
}
