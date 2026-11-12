---
title: "Add Objects to Selection List Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Objects_to_Selection_List_Example_CSharp.htm"
---

# Add Objects to Selection List Example (C#)

This example shows how to populate the selection list with objects that have not been pre-selected through the user interface.

```vb
  // ----------------------------------------------------------------------------
  // Preconditions:
  // 1. Open Public_documents\SOLIDWORKS\SOLIDWORKS 2020\samples\tutorial\api\multi_local.sldprt.
  // 2. Open the Immediate window.
  //
  // Postconditions:
  // 1. Suspends the selection list containing Sketch2.
  // 2. Populates another selection list with six sketch objects.
  // 3. Gets the type of the last object in the selection list.
  // 4. Appends the last selection list of six objects to the previously suspended
  //    selection list that contains Sketch2, placing Sketch2 at the top of the
  //    combined and resumed selection list.
  // 5. Places Sketch2 in edit mode.
  // 6. Inspect the Immediate window and graphics area.
  // 7. Discard changes to the model.
  //
  // NOTE: Because the model is used elsewhere, do not save any changes.
  // ---------------------------------------------------------------------------
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

```vb
  namespace ResumeSelectionList_CSharp
 {
```

```vb
        partial   class   SolidWorksMacro
        {
            public   void Main()
           {
                ModelDoc2 swModel;
                SelectionMgr selMgr;
                SelectData selData;
                FeatureManager featMgr;
                Feature feat;
                DispatchWrapper[] arrObjIn =   new   DispatchWrapper[6];
                Feature[] selObjs =   new   Feature[6];
                object selObj;
                int featCount;
                int i;
                string typeName;
                int j;
                int numAdded;
                bool boolstatus;
                int ret;
                int count;
```

```vb
                swModel = (ModelDoc2)swApp.ActiveDoc;
                selMgr = (SelectionMgr)swModel.SelectionManager;
                selData = selMgr.CreateSelectData();
                featMgr = swModel.FeatureManager;
```

```vb
                featCount = featMgr.GetFeatureCount(true);
                feat = (Feature)swModel.FirstFeature();
                j = 0;
                for (i = 0; i <= featCount; i++)
               {
                    if ((feat !=   null))
```

```vb
                   {
```

```vb
                        typeName = feat.Name;
                        typeName = typeName.ToUpper();
```

```vb
                        if ("SKE" == typeName.Substring(0, 3))
                       {
                            selObjs[j] = feat;
                            arrObjIn[j] =   new   DispatchWrapper(selObjs[j]);
```

```vb
                            j = j + 1;
                       }
```

```vb
                        feat = (Feature)feat.GetNextFeature();
```

```vb
                   }
```

```vb
               }
```

```vb
                // Add one object to the current selection list
                boolstatus = swModel.Extension.SelectByID2("Sketch2",   "SKETCH", 0, 0, 0,   false, 0,   null, 0);
```

```vb
                // Start a new selection list
                ret = selMgr.SuspendSelectionList();
                Debug.Print("The current selection list with " + ret +   " object (Sketch2) is suspended.");
```

```vb
                // Add six objects to the new selection list
                numAdded = selMgr.AddSelectionListObjects((selObjs), selData);
                Debug.Print("A new selection list is started.");
```

```vb
                // Get number of objects in the new selection list (should be 6)
                count = selMgr.GetSelectedObjectCount();
                Debug.Print("The selection list now contains " + count +   " objects.");
```

```vb
                // Get the last object in the new selection list
                selObj = selMgr.GetSelectedObject6(count, -1);
                Debug.Print("The last object in the selection list is of swSelectType_e = " + selMgr.GetSelectedObjectType3(count, -1) +   ".");
```

```vb
                // Resume the previously suspended selection list (Sketch2), appending the new selection list to it
                selMgr.ResumeSelectionList2(true);
                Debug.Print("The previous selection list is resumed and appended with the new selection list.");
```

```vb
                // Get the number of objects in the selection list (should be 7)
                count = selMgr.GetSelectedObjectCount();
                Debug.Print("The selection list now contains " + count +   " objects, including Sketch2, which is at the top of the selection list.");
```

```vb
                // Edit sketch2
                swModel.EditSketch();
           }
            ///   <summary>
            ///       ''' The SldWorks swApp variable is pre-assigned for you.
            ///       '''   </summary>
            public   SldWorks swApp;
        }
  }
```
