---
title: "Change Dimension Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Dimension_Example_CSharp.htm"
---

# Change Dimension Example (C#)

This example shows how to change a dimension value in a model.

#### NOTE: Most of the SOLIDWORKS API functions operate in meters. Thus, if you pass in XValue_Passed = 2.0 and your model units are millimeters, then it appears as a 2000.0 in the model. If you need to determine the units used in the model, you can use the IModelDoc2::LengthUnit property and perform the appropriate conversion.

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified assembly document to open exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the specified assembly document.
 // 2. Changes the specified dimension parameter of the selected feature.
 // 3. Examine the Immediate window.
 //
 // NOTE: Because the assembly document is used elsewhere,
 // do not save changes.
 //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;
 namespace Macro1CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         ModelDoc2 swModel;
         Feature swFeature;
         SelectionMgr swSelectionManager;
         Dimension swDim;
         string fileName;
         bool boolstatus;
         int errors;
         int warnings;

         public void Main()
         {
             fileName = "C:\\Users\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\assem2.sldasm";
             swModel = swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

             boolstatus = swModel.Extension.SelectByID2("LocalCirPattern1", "COMPPATTERN", 0, 0, 0, false, 0, null, 0);
             swSelectionManager = (SelectionMgr)swModel.SelectionManager;
             swFeature = (Feature)swSelectionManager.GetSelectedObject6(1, -1);

             swDim = (Dimension)swFeature.Parameter("D3");
            Debug.Print("D3@LocalCirPattern1 is " + swDim.SystemValue.ToString() + " before changing it.");

             // Change D3 of LocalCirPattern1 from 360 degrees to 270 degrees (4.72 radians)
             errors = swDim.SetSystemValue3(4.72, (int)swSetValueInConfiguration_e.swSetValue_InThisConfiguration, null);

             swModel.EditRebuild3();

             Debug.Print("D3@LocalCirPattern1 is " + swDim.SystemValue.ToString() + " after changing it.");

         }

         public SldWorks swApp;

     }
 }
```
