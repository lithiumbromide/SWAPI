---
title: "Insert Weldment Cut List Example #2 (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_Cut_List2_Example_CSharp.htm"
---

# Insert Weldment Cut List Example #2 (C#)

This example shows how to insert a weldment cut list into the FeatureManager design tree.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\assemblymates\bracket.sldprt.
// 2. Click Tools > Options > System Options > FeatureManager >
//    Solid Bodies > Show > OK.
// 3. Expand the Solid Bodies(1) folder in the FeatureManager design tree
//    and note its contents.
//
// Postconditions:
// 1. Inserts a cut-list-item folder feature containing the specified
//    weldment body.
// 2. Expand the Cut-List-Item1 folder in the Solid Bodies(1) folder
//    in the the FeatureManager design tree to verify step 1.
//
// NOTE: Because this part is used elsewhere,
// do not save changes.
//----------------------------------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
namespace InsertWeldmentCutList2_CSharp.csproj
{
    partial class SolidWorksMacro
    {

        ModelDoc2 Part;
        Body2[] obj = new Body2[1];
        Object[] v;
        long i;

        public void Main()
        {
            Part = (ModelDoc2)swApp.ActiveDoc;
            v = (object[])((PartDoc)Part).GetBodies2(0, true);
            for (i = 0; i <= v.GetUpperBound(0); i++)
            {
                obj[i] = (Body2)v[i];
            }
            Feature cutListFeature = default(Feature);
            cutListFeature = Part.FeatureManager.InsertWeldmentCutList2(obj);
        }
        public SldWorks swApp;
    }
}
```
