---
title: "Create and Delete Selection Sets Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Delete_Selection_Sets_Example_CSharp.htm"
---

# Create and Delete Selection Sets Example (C#)

This example shows how to:

- create selection sets.
- get the Selection Sets folder.
- get the selection sets in the Selection Sets folder.
- get and then delete the items in the selection sets, which deletes the selection sets.

```
//--------------------------------------------------------------------
// Preconditions:
// 1. Verify that the assembly to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the assembly.
// 2. Creates two selection sets.
// 3. Traverses the FeatureManager design tree. If the feature is the
//    Selection Sets folder, then:
//    a. Gets its name.
//    b. Gets each selection set in the Selection Sets folder.
//    c. Gets and then deletes each selection set item in the
//       selection set, which deletes the selection set.
// 4. Examine the Immediate window.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//--------------------------------------------------------------------
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
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExtension = default(ModelDocExtension);
            SelectionSet swSelectionSet1 = default(SelectionSet);
            SelectionSet swSelectionSet2 = default(SelectionSet);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\wrench.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            Debug.Print("File = " + swModel.GetPathName());
            swModelDocExtension = swModel.Extension;

            //Create a selection set
            status = swModelDocExtension.SelectByID2("arm1-1@wrench", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExtension.SelectByID2("arm2-1@wrench", "COMPONENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExtension.SelectByID2("clamp2-1@wrench", "COMPONENT", 0, 0, 0, true, 0, null, 0);
            swSelectionSet1 = (SelectionSet)swModelDocExtension.SaveSelection(out errors);
            Debug.Print("  First selection set created (1 = succeeded; 0 = failed)? " + errors);
            swModel.ClearSelection2(true);

            //Create another selection set
            status = swModelDocExtension.SelectByID2("centerlink-1@wrench", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExtension.SelectByID2("screw-1@wrench", "COMPONENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExtension.SelectByID2("screw-1@wrench", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swSelectionSet2 = (SelectionSet)swModelDocExtension.SaveSelection(out errors);
            Debug.Print("  Second selection set created (1 = succeeded; 0 = failed)? " + errors);
            swModel.ClearSelection2(true);

            //Traverse the model to get Selection Sets folder
            TraverseModelFeatures(swModel);

        }

        public void TraverseFeatureFeatures(Feature swFeat)
        {
            SelectionSetFolder swSelectionSetFolder = default(SelectionSetFolder);
            object[] selectionSetArray = null;
            object[] selectionSetItemArray = null;
            int[] selectionSetItemArrayTypes = null;
            SelectionSet swSelectionSet = default(SelectionSet);
            SelectionSetItem swSelectionSetItem = default(SelectionSetItem);
            int i = 0;
            int j = 0;

            while ((swFeat != null))
            {
                if (swFeat.Name == "Selection Sets")
                {
                    Debug.Print("    " + swFeat.Name + " [" + swFeat.GetTypeName() + "]");
                    //Get Selection Sets folder
                    swSelectionSetFolder = (SelectionSetFolder)swFeat.GetSpecificFeature2();
                    //Get selection sets in Selection Sets folder
                    selectionSetArray = (object[])swSelectionSetFolder.GetSelectionSets();
                    for (i = 0; i < selectionSetArray.GetLength(0); i++)
                    {
                        swSelectionSet = (SelectionSet)selectionSetArray[i];
                        Debug.Print("      Selection set[" + i + "] name: " + swSelectionSet.GetName());
                        //Get the items in this selection set
                        selectionSetItemArray = (object[])swSelectionSet.GetSelectionSetItems();
                        selectionSetItemArrayTypes = (int[])swSelectionSet.GetSelectionSetItemTypes();
                        for (j = 0; j < selectionSetItemArray.GetLength(0); j++)
                        {
                            swSelectionSetItem = (SelectionSetItem)selectionSetItemArray[j];
                            Debug.Print(" Item[" + j + "] in this selection set is this entity type as defined in swSelectType_e: " + selectionSetItemArrayTypes[j]);
                            //Delete each item in this selection set
                            swSelectionSetItem.RemoveFromSelectionSet();
                            Debug.Print("        Selection set item[" + j + "] deleted");
                        }
                    }
                }
                swFeat = (Feature)swFeat.GetNextFeature();
            }

        }

        public void TraverseModelFeatures(ModelDoc2 swModel)
        {
            Feature swFeat = default(Feature);

            swFeat = (Feature)swModel.FirstFeature();
            TraverseFeatureFeatures(swFeat);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
