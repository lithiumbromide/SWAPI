---
title: "Get Feature Type and Name Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Type_and_Name_of_Feature_Example_CSharp.htm"
---

# Get Feature Type and Name Example (C#)

This example shows how to get the feature type and name of the selected feature for use with IModelDocExtension::SelectByID2.

```vb
//-------------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
 // 2. Expand any component in the FeatureManager design tree
 //    and select one of its features.
 //
// Postconditions:
 // 1. Gets the selected feature's type and name.
 // 2. Examine the Immediate window.
 //
 // NOTE: Because this assembly document is used elsewhere, do not save changes.
 //-------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace GetNameForSelectionFeatureCSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             string featName = null;
             string featType = null;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swModelDocExt = (ModelDocExtension)swModel.Extension;

             // Get the selected feature
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);

             swModel.ClearSelection2(true);

             // Get the feature's type and name
             featName = swFeat.GetNameForSelection(out featType);
             swModelDocExt.SelectByID2(featName, featType, 0, 0, 0, true, 0, null, 0);

             // Print the feature's type and name
             // to the Immediate window
             Debug.Print("Feature type: " + featType);
             Debug.Print("Feature name: " + featName);
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;
     }
 }
```
