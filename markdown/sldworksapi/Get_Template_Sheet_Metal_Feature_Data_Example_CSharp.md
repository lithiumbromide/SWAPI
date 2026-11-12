---
title: "Get Sheet Metal Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Template_Sheet_Metal_Feature_Data_Example_CSharp.htm"
---

# Get Sheet Metal Feature Data Example (C#)

This example shows how to get the sheet metal feature data from a sheet metal part created in SOLIDWORKS 2013 or later.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a sheet metal part created in SOLIDWORKS 2013 or later.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Inspect the Immediate window to see whether a fixed face reference is selected.
 // 2. Inspect the selection in the graphics window.
 // 3. Press F5 to finish the macro.
 //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace GetTemplateSheetMetal_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelExt = default(ModelDocExtension);
             SelectData swSelData = null;
             Feature swSheetMetalTemplFeature = default(Feature);
             SheetMetalFeatureData swSheetMetal = default(SheetMetalFeatureData);
             Face2 swFixedFace = default(Face2);
             Entity swEntity = default(Entity);
             bool bRet = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelExt = swModel.Extension;

             swSheetMetalTemplFeature = (Feature)swModelExt.GetTemplateSheetMetal();
             swSheetMetal = (SheetMetalFeatureData)swSheetMetalTemplFeature.GetDefinition();

             // Roll back the model
             bRet = swSheetMetal.AccessSelections(swModel, null);
             swFixedFace = (Face2)swSheetMetal.FixedReference;

             if ((swFixedFace != null))
             {
                 Debug.Print("A fixed face or fixed edge is selected.");
                 swEntity = (Entity)swFixedFace;
                 bRet = swEntity.Select4(false, swSelData);
                 System.Diagnostics.Debugger.Break();
             }
             else
             {
                 // A fixed face or fixed edge is not required,
                 // so Null is a valid value
                 Debug.Print("There is no fixed face or fixed edge in this sheet metal part.");
             }

             // Cancel changes and roll forward the model
             swSheetMetal.ReleaseSelectionAccess();
         }

         public SldWorks swApp;
     }
 }
```
