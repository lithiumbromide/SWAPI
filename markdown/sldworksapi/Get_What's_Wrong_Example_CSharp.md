---
title: "Get What's Wrong Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_What's_Wrong_Example_CSharp.htm"
---

# Get What's Wrong Example (C#)

This example shows how to get the What's Wrong information for a document.

```vb
//-----------------------------------
//
// Preconditions: Model document is active. Examine the Immediate
//      window after running this macro to see the What's Wrong
//      items in the model document.
//
// Postconditions: None
//
//------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace GetWhatsWrongCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {

        ModelDoc2 swModel = default(ModelDoc2);
        ModelDocExtension swModelDocExt = default(ModelDocExtension);
        object oFeatures;
        object oErrorCodes;
        object oWarnings;
        object[] Features = null;
        int[] ErrorCodes = null;
        bool[] Warnings = null;
        bool boolstatus = false;
        int i = 0;
        int nbrWhatsWrong = 0;
        Feature swFeature = default(Feature);

        swModel = (ModelDoc2)swApp.ActiveDoc;
        swModelDocExt = (ModelDocExtension)swModel.Extension;

        nbrWhatsWrong = swModelDocExt.GetWhatsWrongCount();
        Debug.Print("Number of What's Wrong items: " + nbrWhatsWrong);
        Debug.Print("");
        if (nbrWhatsWrong > 0) {
            boolstatus = swModelDocExt.GetWhatsWrong(out oFeatures, out oErrorCodes, out oWarnings);
            Features = (object[])oFeatures;
            ErrorCodes = (int[])oErrorCodes;
            Warnings = (bool[])oWarnings;
            for (i = 0; i < Features.Length; i++) {
                swFeature = (Feature)Features[i];
                Debug.Print(" Name of feature: " + swFeature.GetTypeName2());
                Debug.Print(" Error: " + ErrorCodes[i]);
                Debug.Print(" Did SOLIDWORKS Design flag this item as a warning ? " + Warnings[i]);
                Debug.Print("");
            }
        }
        else {
            Debug.Print("No What's Wrong items.");
        }

    }
        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
