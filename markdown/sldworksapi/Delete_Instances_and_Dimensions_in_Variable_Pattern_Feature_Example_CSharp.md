---
title: "Delete Instances and Dimensions in Variable Pattern Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_CSharp.htm"
---

# Delete Instances and Dimensions in Variable Pattern Feature Example (C#)

This example shows how to:

- delete instances in a variable pattern feature.
- add and delete dimensions in the pattern table of a variable pattern feature.

```
//---------------------------------------------------------
// Preconditions:
// 1. Verify that the part exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the part and selects the variable pattern feature.
// 2. Accesses the variable pattern feature.
// 3. Deletes the last and fourth instance from the pattern table
//    and pattern.
// 4. Gets the number and names of the controlling dimensions.
// 5. Selects and adds two dimensions to the pattern table and
//    deletes the second dimension from the pattern table.
// 6. Rolls forward the modified variable pattern feature.
// 7. Examine the graphics area and Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//----------------------------------------------------------

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
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            DimPatternFeatureData swDimensionDrivenTablePatternFeat = default(DimPatternFeatureData);
	    DisplayDimension swDisplayDimension = default(DisplayDimension);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            int dimNbr = 0;
            int i = 0;
            string[] controllingDimNames = null;
            string controllingDimName = null;

            //Open part and select the variable pattern feature
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\bottle.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            status = swModelDocExt.SelectByID2("VarPattern1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swDimensionDrivenTablePatternFeat = (DimPatternFeatureData)swFeature.GetDefinition();

            //Roll back and access the variable pattern feature
            status = swDimensionDrivenTablePatternFeat.AccessSelections(swModel, null);

            //Delete the last instance of the variable pattern in the pattern table
            status = swDimensionDrivenTablePatternFeat.DeleteInstanceAt(-1);
            Debug.Print("Last instance of variable pattern deleted from pattern table? " + status);

            //Delete another instance of the variable pattern in the pattern table
            status = swDimensionDrivenTablePatternFeat.DeleteInstanceAt(3);
            Debug.Print("Fourth instance of variable pattern deleted from pattern table? " + status);

            //Get the number and names of the controlling dimensions
            dimNbr = swDimensionDrivenTablePatternFeat.GetControllingDimensionCount();
            Debug.Print("Number of controlling dimensions: " + dimNbr);
            Debug.Print("  Controlling dimension names: ");
            Array.Resize(ref controllingDimNames, dimNbr + 1);
            for (i = 0; i <= dimNbr - 1; i++)
            {
                controllingDimNames[i] = (string)swDimensionDrivenTablePatternFeat.GetControllingDimensionName(i);
                controllingDimName = (string)controllingDimNames[i];
 		Debug.Print("     " + controllingDimName);
            }
```

```
  //Select two display dimensions and add them to the pattern table
  status = swModelDocExt.SelectByID2("D1@Sketch2@bottle.SLDPRT", "DIMENSION", 0.0176517231321772, 0.0149650532369545, -0.0243235746513165, false, 0, null, 0);
  swDisplayDimension = (DisplayDimension)swSelMgr.GetSelectedObject6(1, -1);
  status = swDimensionDrivenTablePatternFeat.AddDimension();
  if (status)
  {
      Debug.Print("Added " + swDisplayDimension.GetNameForSelection() + " to pattern table");
  }

  swModel.ClearSelection2(true);

  status = swModelDocExt.SelectByID2("D2@Sketch2@bottle.SLDPRT", "DIMENSION", 0.019517663324148, 0.0297942417761803, -0.0237034236540374, false, 0, null, 0);
  swDisplayDimension = (DisplayDimension)swSelMgr.GetSelectedObject6(1, -1);
  status = swDimensionDrivenTablePatternFeat.AddDimension();
  if (status)
  {
      Debug.Print("Added " + swDisplayDimension.GetNameForSelection() + " to pattern table");
  }

  //Delete the just-added display dimension from the pattern table
  status = swDimensionDrivenTablePatternFeat.DeleteDimension(swDisplayDimension.GetNameForSelection());
  if (status)
  {
      Debug.Print("  Deleted " + swDisplayDimension.GetNameForSelection() + " from pattern table");
  }
```

```
            swDimensionDrivenTablePatternFeat.PropagateVisualProperties = true;

            //Roll forward the variable pattern feature
            swFeature.ModifyDefinition(swDimensionDrivenTablePatternFeat, swModel, null);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
