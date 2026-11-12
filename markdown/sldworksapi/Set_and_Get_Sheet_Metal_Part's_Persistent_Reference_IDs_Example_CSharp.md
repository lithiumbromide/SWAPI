---
title: "Set and Get Sheet Metal Part's Persistent Reference IDs Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_CSharp.htm"
---

# Set and Get Sheet Metal Part's Persistent Reference IDs Example (C#)

This example shows how to set and get persistent reference IDs (PIDs) on a sheet metal part.

The entities in flattened and unflattened (folded) states of sheet metal in SOLIDWORKS Design do not have the same properties, making it difficult to track entities across states of sheet metal.

- [IModelDocExtension::GetFlattenSheetMetalPersistReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetFlattenSheetMetalPersistReference.html) returns a PID array for an entity in the flattened state of the sheet metal part.
- [IModelDocExtension::GetSheetmetalObjectsByPersistReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSheetMetalObjectsByPersistReference.html) uses the PID byte array to retrieve an array of objects that comprise the previously selected entity in the folded state of the part.

Together these methods provide a way to track entities across sheet metal states.

```
//------------------------------------------
// Preconditions:
// 1. Verify that the specified part exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens specified part document.
// 2. Unsuppresses the Flat-Pattern1 feature.
// 3. Gets the PIDs of the selected face on the
//    Flat-Pattern1 feature.
// 4. Suppresses the Flat-Pattern1 feature.
// 5. Uses the PIDs to retrieve and highlight the
//    array of objects that comprise the previously
//    selected face in the folded state of the part.
// 6. Examine the Immediate window, graphics area, and
//    FeatureManager design tree.
//
// NOTE: Because the part document is used elsewhere,
// do not save changes.
//--------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace EditSuppress2.csproj
{
    partial class SolidWorksMacro
    {

        ModelDoc2 swModel;
        ModelDocExtension swModelDocExt;
        SelectionMgr swSelectionMgr;
        Face2 swFace;
        SelectData swSelectData;
        byte[] pid;
        object selObj;
        object[] swObjList;
        string fileName;
        int errors;
        int warnings;
        bool boolstatus;
        int i;
        int j;

        public void Main()
        {

            // Open the specified sheet metal part
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\2012-sm.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            // Get flat-pattern feature
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            boolstatus = swModelDocExt.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);

            // Unsuppress (unfold) flat-pattern feature
            boolstatus = swModel.EditUnsuppress2();

            // Select the top face on the flattened sheet metal part
             boolstatus = swModelDocExt.SelectByID2("", "FACE", -3.46526388559596E-02, 0, 0.011695220708134, false, 0, null, 0)
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFace = (Face2)swSelectionMgr.GetSelectedObject6(1, -1);

            // Get the persistent reference IDs for the
            // the selected face on the flattened sheet
            // metal part
            pid = (byte[])swModelDocExt.GetFlattenSheetMetalPersistReference(swFace);

            // Print the PID values to the Immediate window
            for (j = pid.GetLowerBound(0); j <= pid.GetUpperBound(0); j++)
            {
                Debug.Print("PID = " + pid[j]);
            }

            // Suppress (fold) flat-pattern feature
            boolstatus = swModelDocExt.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
            swModel.EditSuppress2();

            // Use the persistent reference IDs to
            // retrieve an array of objects that comprise
            // the entity in the folded state of the part
            swObjList = (object[])swModelDocExt.GetSheetMetalObjectsByPersistReference((pid), out errors);

            if ((swObjList != null))
            {
                swModel.ClearSelection2(true);

                for (i = swObjList.GetLowerBound(0); i <= swObjList.GetUpperBound(0); i++)
                {
                    selObj = swObjList[i];

                    if (selObj == null)
                    {
                        Debug.Print("Persistent reference ID conversion error.");
                        return;
                    }
                    else
                    {
                        SelectObject(selObj, true);
                    }
                }
            }

            Debug.Print("The entities that comprise the previously selected entity in the folded state are selected.");

        }

        private void SelectObject(object selObj, bool append)
        {
            if (selObj is Entity)
            {
                Entity selObj1;
                selObj1 = (Entity)selObj;
                swSelectData = (SelectData)swSelectionMgr.CreateSelectData();
                selObj1.Select4(append, swSelectData);

            }
            else
            {
                Debug.Print("Need selection handle.");

            }
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;
    }
}
```
