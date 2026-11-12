---
title: "Get Features of Multibody Sheet Metal Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Features_of_Multibody_Sheet_Metal_Part_Example_CSharp.htm"
---

# Get Features of Multibody Sheet Metal Part Example (C#)

This example shows how to sort a cut-list folder of a multibody sheet metal part.

```
// ---------------------------------------------------------------------------
// Preconditions:
// 1. Open C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2020\samples\tutorial\api\weldment_box3.sldprt.
// 2. Inspect the cut list folder.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Gets the number and names of the features in the cut list bodies.
// 2. Sets the cut list sorting options.
// 3. Sorts the cut list.
// 4. Inspect the sorted cut list folder in the Immediate window.
// --------------------------------------------------------------------------
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Security;
using System.Text;
using System.Threading.Tasks;
using Microsoft.VisualBasic;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
```

```
using System.Windows;
using System.Windows.Forms;
```

```
namespace CutListSort_CSharp
{
```

```
        partial class SolidWorksMacro
        {
            public void Main()
            {
                ModelDoc2 swModel;
                Feature swFeat;
                BodyFolder swBodyFolder;
                SelectionMgr selMgr;
                Body2 swBody;
                object[] Bodies;
                object[] Features;
                CutListSortOptions CutListSortOptions;
                int i;
                int j;
                bool boolstatus;
```

```
                swModel = (ModelDoc2)swApp.ActiveDoc;
                selMgr = (SelectionMgr)swModel.SelectionManager;
```

```
                boolstatus = swModel.Extension.SelectByID2("Solid Bodies", "BDYFOLDER", 0, 0, 0, false, 0, null/* TODO Change to default(_) if this is not a reference type */, 0);
                swFeat = (Feature)selMgr.GetSelectedObject6(1, -1);
```

```
                swBodyFolder = (BodyFolder)swFeat.GetSpecificFeature2();
                swBodyFolder.SetAutomaticCutList(true);
                swBodyFolder.SetAutomaticUpdate(false);
                Bodies = (object[])swBodyFolder.GetBodies();
                Debug.Print("    Number of bodies: " + swBodyFolder.GetBodyCount());
                Debug.Print("    Cut list type: " + swBodyFolder.GetCutListType());
                Debug.Print("    Generate cut list automatically? " + swBodyFolder.GetAutomaticCutList());
                Debug.Print("    Automatically update cut list? " + swBodyFolder.GetAutomaticUpdate());
                for (i = 0; i <= (swBodyFolder.GetBodyCount() - 1); i++)
                {
                    swBody = (Body2)Bodies[i];
                    Features = (object[])swBody.GetFeatures();
                    Debug.Print("    Number of features in body #" + i + 1 + ": " + swBody.GetFeatureCount());
                    for (j = 0; j <= (swBody.GetFeatureCount() - 1); j++)
                        Debug.Print("       Name of feature: " + ((Feature)Features[j]).GetTypeName2());
                }
```

```
                // Sort the cut list
                CutListSortOptions = (CutListSortOptions)swBodyFolder.GetCutListSortOptions();
                CutListSortOptions.CollectIdenticalBodies = true;
                boolstatus = swBodyFolder.SortCutList(CutListSortOptions, false);
            }
            /// <summary>
            ///     ''' The SldWorks swApp variable is pre-assigned for you.
            ///     ''' </summary>
            public SldWorks swApp;
        }
```

```
}
```
