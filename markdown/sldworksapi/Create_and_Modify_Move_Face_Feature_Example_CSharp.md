---
title: "Create and Modify Move Face Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Modify_Move_Face_Feature_Example_CSharp.htm"
---

# Create and Modify Move Face Feature Example (C#)

This example shows how to create a Move Face feature by translating a face on a part.

```vb
  //---------------------------------------------------------------------------
 // Preconditions: Verify that the specified part exists.
 //
 // Postconditions:
 // 1. Creates Move Face1 in the FeatureManager design tree.
 // 2. Modifies the translation parameters of Move Face1.
 //
 // NOTE: Because the part is used elsewhere, do not save any changes.
  //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace InsertMoveFace3_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         ModelDocExtension swModelDocExt;
         FeatureManager swFeatMgr;
         Feature swFeat;
         MoveFaceFeatureData swMoveFaceFeat;
         object transParams;
         bool boolstatus;
         double[] triadParams = new double[3];
         int fileerror;

         int filewarning;

         public void Main()
         {
             // Open the SOLIDWORKS Design document
             swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\assemblymates\\knee.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref fileerror, ref filewarning);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModel.Extension;
             swFeatMgr = swModel.FeatureManager;

             // Translation parameters
             triadParams[0] = 0;
             triadParams[1] = 0.05;
             triadParams[2] = 0;

             transParams = triadParams;

             // Select face to move
             boolstatus = swModel.Extension.SelectByID2("", "FACE", 0.04239074672171, 0.01587499999999, 0.3283508339712, false, 1, null, 0);

             // Create the Move Face feature by
             // translating the selected face
             swFeat = (Feature)swFeatMgr.InsertMoveFace3((int)swMoveFaceType_e.swMoveFaceTypeTranslate, false, 0, 0, (transParams), null, (int)swEndConditions_e.swEndCondBlind, 0);

             // Modify the Move Face feature
             swMoveFaceFeat = (MoveFaceFeatureData)swFeat.GetDefinition();

             // Roll back the Move Face feature
             swMoveFaceFeat.AccessSelections(swModel, null);

             triadParams[0] = 0;
             triadParams[1] = 0.1;
             triadParams[2] = 0;

             transParams = triadParams;

             swMoveFaceFeat.TriadTranslationParameters = (transParams);

             // Roll back the part with the modified Move Face feature
             swFeat.ModifyDefinition(swMoveFaceFeat, swModel, null);

         }

         public SldWorks swApp;

     }
 }
```
