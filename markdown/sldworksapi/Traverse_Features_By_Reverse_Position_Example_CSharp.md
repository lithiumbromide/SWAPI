---
title: "Traverse Features By Reverse Position Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Features_By_Reverse_Position_Example_CSharp.htm"
---

# Traverse Features By Reverse Position Example (C#)

This example shows how to traverse backwards through the list of features in the FeatureManager design tree. Features are obtained by their position using IModelDoc2::FeatureByPositionReverse.

```
//-------------------------------------
// Preconditions:
// 1. A part document is open in SOLIDWORKS Design.
// 2. Open the Immediate window.
// 3. Run the macro.
//
// Postconditions: Examine the Immediate window for
// the position and names of the features in
// the FeatureManager design tree in reverse
// chronological order.
//--------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace TraverseFeatureByReverseCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        ModelDoc2 Part;
        Feature theFeature;
        int featCount;
        string featName;
        int i;

        public void Main()
        {
            Part = (ModelDoc2)swApp.ActiveDoc;

            featCount = Part.GetFeatureCount();
            for (i = featCount; i >= 1; i += -1)
            {
                theFeature = (Feature)Part.FeatureByPositionReverse(featCount - i);
                if ((theFeature != null))
                {
                    featName = theFeature.Name;
                    Debug.Print("Feature " + i.ToString() + " is " + featName);
                }
            }

            Part = null;

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;
    }
}
```
