---
title: "Get Minimum Radius of Bodies Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Minimum_Radius_of_Bodies_Example_CSharp.htm"
---

# Get Minimum Radius of Bodies Example (C#)

This example shows how to get the minimum radius of each body in a multibody part.

```
//----------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document
//    to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document as read only.
// 2. Gets the minimum radius of each body.
// 3. Examine the Immediate window.
//----------------------------------------------------
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
            PartDoc swPart = default(PartDoc);
            object[] bodies = null;
            Body2 abody = default(Body2);
            double radius = 0;
            string fileName = null;
            int errors = 0;
            int warnings = 0;
            int i = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\multibody\\multi_inter.sldprt";
            swPart = (PartDoc)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_ReadOnly, "", ref errors, ref warnings);
            bodies = (object[])swPart.GetBodies2((int)swBodyType_e.swAllBodies, false);
            i = 1;
            foreach (object vbody in bodies)
            {
                abody = (Body2)vbody;
                radius = abody.MinimumRadius();
                Debug.Print(abody.Name + "'s " + "minimum radius: " + radius);
                i = i + 1;
            }
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
