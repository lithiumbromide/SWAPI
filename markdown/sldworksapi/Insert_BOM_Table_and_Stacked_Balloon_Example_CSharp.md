---
title: "Insert BOM Table and Stacked Balloon Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_BOM_Table_and_Stacked_Balloon_Example_CSharp.htm"
---

# Insert BOM Table and Stacked Balloon Example (C#)

This example shows how to insert a bill of materials table and a stacked balloon annotation in an assembly document.

```vb
 //--------------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
 //
 // Postconditions:
 // 1. Inserts a parts-only BOM table.
 // 2. Inserts a stacked balloon annotation.
 // 3. Inspect the Immediate Window for the name of the configuration used to create
 //    the table and the name of the annotation.
 //
 // NOTE: Because this document is used do not save any changes.
 //-------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace StackedBalloon_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             BomTableAnnotation swBOMAnnotation = default(BomTableAnnotation);
             BomFeature swBOMFeature = default(BomFeature);
             Note swNote = default(Note);
             StackedBalloonOptions StackedBalloonParams = default(StackedBalloonOptions);
             bool boolstatus = false;
             int BomType = 0;
             string Configuration = null;
             string TemplateName = null;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModel.Extension;

             // Insert BOM table
             TemplateName =  "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\bom-standard.sldbomtbt";
             BomType = (int)swBomType_e.swBomType_PartsOnly;
             Configuration = "Default";
             swBOMAnnotation = swModelDocExt.InsertBomTable2(TemplateName, 40, 30, BomType, Configuration, false);
             swBOMFeature = swBOMAnnotation.BomFeature;

             // Print the name of the configuration used for the BOM table
             Debug.Print("Name of configuration used for BOM table: " + swBOMFeature.Configuration);

             // Select a face on which to attach the stacked balloons
             boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.02268677135385, 0.0082159933431, 0.01133567172189,  false, 0,  null, 0);

             StackedBalloonParams = swModel.Extension.CreateStackedBalloonOptions();
             StackedBalloonParams.BalloonsPerLine = 10;
             StackedBalloonParams.StackDirection = (int)swStackedBalloonDirection_e.swStackedBalloonDir_Right;
             StackedBalloonParams.Style = (int)swBalloonStyle_e.swBS_Circular;
             StackedBalloonParams.Size = (int)swBalloonFit_e.swBF_5Chars;
             StackedBalloonParams.UpperTextContent = (int)swBalloonTextContent_e.swBalloonTextItemNumber;
             StackedBalloonParams.ShowQuantity =  true;
             StackedBalloonParams.QuantityPlacement = (int)swBalloonQuantityPlacement_e.swBalloonQuantityPlacement_Top;
             StackedBalloonParams.QuantityDenotationText =  "PLACES";
             StackedBalloonParams.QuantityOverride =  false;
             StackedBalloonParams.ItemNumberStart = 1;
             StackedBalloonParams.ItemNumberIncrement = 1;
             StackedBalloonParams.ItemOrder = (int)swBalloonItemNumbersOrder_e.swBalloonItemNumbers_DoNotChangeItemNumbers;

             swNote = swModel.Extension.InsertStackedBalloon2(StackedBalloonParams);

             boolstatus = swModel.Extension.SelectByID2("", "FACE", -0.01632926202666, 0.05356671136803, 0.008058200827065,  false, 0,  null, 0);
             boolstatus = swModel.Extension.SelectByID2("", "FACE", 0.02199792044968, 0.00911087426303, 0.01062976811426,  false, 0,  null, 0);
             boolstatus = swModel.Extension.SelectByID2("", "FACE", -0.01412287126243, 0.003109265420704, -0.003984592306182,  false, 0,  null, 0);

             swModel.ViewZoomtofit2();

             // Get whether balloon is a stacked balloon;
             // If so, print the name of the balloon

             if (swNote.IsStackedBalloon())
             {
                 Debug.Print("Name of stacked balloons note: " + swNote.GetName());
             }

             swModel.ForceRebuild3(true);
         }

         public SldWorks swApp;

     }
 }
```
