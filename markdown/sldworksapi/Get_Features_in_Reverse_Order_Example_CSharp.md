---
title: "Get Features in Reverse Order Example C(#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Features_in_Reverse_Order_Example_CSharp.htm"
---

# Get Features in Reverse Order Example C(#)

## Get Features in Reverse Order Example (C#)

This example shows how to get the names and types of features in the FeatureManager design tree in reverse chronological order.

```
//--------------------------------------------
// Preconditions:
// 1. Open a part.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets the names and types of features
//    in the FeatureManager design tree
//    in reverse chronological order.
// 2. Examine the Immediate window and
//    FeatureManager design tree.
//--------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Runtime.InteropServices;
using System.Diagnostics;

namespace GetFeatureInReverseOrderCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            Feature swFeat = default(Feature);
            int i = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;

            Debug.Print("File = " + swModel.GetPathName());
            Debug.Print("");
            Debug.Print("Feature Name and Type");
            Debug.Print("=====================");
            for (i = 0; i <= swModel.GetFeatureCount() - 1; i++)
            {
                swFeat = (Feature)swModel.FeatureByPositionReverse(i);
                if ((swFeat != null))
                {
                    Debug.Print(swFeat.Name + " [" + swFeat.GetTypeName() + "]");
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
