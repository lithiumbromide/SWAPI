---
title: "Get Names of Creators of Features Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_of_Creators_of_Features_Example_CSharp.htm"
---

# Get Names of Creators of Features Example (C#)

This example shows how to get the names of the creators of features in a part document.

```
//-------------------------------------------------
// Preconditions:
// 1. Verify that the specified part exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets the names of the features and their creators.
// 2. Examine the Immediate window.
//-------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace CloseDocCSharp.csproj
{

    partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            Feature swFeat = default(Feature);
            string Filename = null;
            int errors = 0;
            int warnings = 0;

            Filename = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\cstick.sldprt";

            // Open document
            swApp.OpenDoc6(Filename, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModel = (ModelDoc2)swApp.ActiveDoc;

            // Get first feature in this part document
            swFeat = (Feature)swModel.FirstFeature();

            // Iterate over features in this part document in
            // FeatureManager design tree
            while ((swFeat != null))
            {
                // Write the name of the feature and its
                // creator to the Immediate window
                Debug.Print("  Feature " + swFeat.Name + " created by " + swFeat.CreatedBy);

                // Get next feature in this part document
                swFeat = (Feature)swFeat.GetNextFeature();
            }

            swApp.CloseDoc(Filename);

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
