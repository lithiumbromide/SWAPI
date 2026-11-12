---
title: "Compare Selected Objects and Their Persistent Reference IDs Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_CSharp.htm"
---

# Compare Selected Objects and Their Persistent Reference IDs Example (C#)

This example shows how to determine if two selected entities are the same entities and if those entities have the same persistent IDs.

**NOTE**: Using [IModelDocExtension::IsSamePersistentID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsSamePersistentID.html) and [ISldWorks::IsSame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsSame.html) might be helpful when your application is passed two entities that it didn't select, and your application needs to know if they're the same entity.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open a part document is open and select two
//    different entities (e.g., face, edge, vertex, etc.).
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Compares the selected entities.
// 2. Examine the code and Immediate window.
//------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {

            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            object selObj1 = null;
            object selObj2 = null;
            object selObjPID1 = null;
            object selObjPID2 = null;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swModelDocExt = swModel.Extension;

            // Get the selected objects
            selObj1 = swSelMgr.GetSelectedObject6(1, -1);
            selObj2 = swSelMgr.GetSelectedObject6(2, -1);
            Debug.Print("Compare the selected objects:");
            switch (swApp.IsSame(selObj1, selObj2))
            {
                case 0:
                    Debug.Print(" Selected objects are not the same.");
                    break;
                case 1:
                    Debug.Print(" Selected objects are the same.");
                    break;
                case -1:
                    Debug.Print(" Unable to determine if selected objects are the same.");
                    break;
            }

            Debug.Print("");

            Debug.Print("Compare the same objects:");
            switch (swApp.IsSame(selObj1, selObj1))
            {
                case 0:
                    Debug.Print(" Selected objects are not the same.");
                    break;
                case 1:
                    Debug.Print(" Selected objects are the same.");
                    break;
                case -1:
                    Debug.Print(" Unable to determine if selected objects are the same.");
                    break;
            }

            Debug.Print("");

            // Get the persistent reference IDs of the
            // selected objects
            selObjPID1 = swModelDocExt.GetPersistReference3(selObj1);
            selObjPID2 = swModelDocExt.GetPersistReference3(selObj2);
            Debug.Print("Compare the persistent reference IDs of the selected objects:");
            switch (swModelDocExt.IsSamePersistentID(selObjPID1, selObjPID2))
            {
                case 0:
                    Debug.Print(" Selected objects do not have the same persistent reference ID.");
                    break;
                case 1:
                    Debug.Print(" Selected objects do have the same persistent reference ID.");
                    break;
                case -1:
                    Debug.Print(" Unable to determine if the selected objects have the same persistent reference ID.");
                    break;
            }

            Debug.Print("");

            Debug.Print("Compare the persistent reference IDs of the same objects:");
            switch (swModelDocExt.IsSamePersistentID(selObjPID1, selObjPID1))
            {
                case 0:
                    Debug.Print(" Selected objects do not have the same persistent reference ID.");
                    break;
                case 1:
                    Debug.Print(" Selected objects do have the same persistent reference ID.");
                    break;
                case -1:
                    Debug.Print(" Unable to determine if the selected objects have the same persistent reference ID.");
                    break;
            }
        }
        public SldWorks swApp;
    }
}
```
