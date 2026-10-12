---
title: "Save Model as Bitmap Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Model_as_Bitmap_Example_CSharp.htm"
---

# Save Model as Bitmap Example (C#)

## Save Model as BMP Example (C#)

This example shows how to save the current view of a model as a bitmap.

```
//-----------------------------------------------------------------------------------
// Preconditions:
// 1. Open:
//    C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cstick.sldprt
// 2. Run macro.
//
// Postconditions: Current view of the model is saved as C:\cstick.bmp.
//------------------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace SaveBMPCSharp.csproj
{

    partial class SolidWorksMacro
    {

        public void Main()
        {

            ModelDoc2 swModel = default(ModelDoc2);
            bool returnVal = false;
            string fileName = null;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            fileName = "c:\\cstick.bmp";

            // Save as bitmap and use current window size
            returnVal = swModel.SaveBMP(fileName, 0, 0);

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }
}
```
