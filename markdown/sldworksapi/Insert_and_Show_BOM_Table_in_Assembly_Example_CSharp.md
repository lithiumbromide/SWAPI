---
title: "Insert and Show BOM Table in Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Show_BOM_Table_in_Assembly_Example_CSharp.htm"
---

# Insert and Show BOM Table in Assembly Example (C#)

This example shows how to insert and show a BOM table in an assembly document.

```
//------------------------------------------------
// Preconditions:
// 1. Verify that the specified file to open and template exist.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Inserts an indented BOM table.
// 2. Inserts a split-circle stacked balloon, which uses the
//    BOM table item number for its upper text,
//    at the selected face.
// 3. Examine the BOM table, stacked balloon, and Immediate
//    window.
//
// NOTE: Because this assembly document is used elsewhere,
// do not save changes.
//-------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace IBomFeatureInsertBomTable3CSharp.csproj
{
    partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            BomTableAnnotation swBOMAnnotation = default(BomTableAnnotation);
            BomFeature swBOMFeature = default(BomFeature);
            StackedBalloonOptions StackedBalloonParams = default(StackedBalloonOptions);
            Note swNote = default(Note);
            bool boolstatus = false;
            int BomType = 0;
            int nbrType = 0;
            string Configuration = null;
            string TemplateName = null;
            int nErrors = 0;
            int nWarnings = 0;

            // Open assembly document
            swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\arm2.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref nErrors, ref nWarnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Insert BOM table
            TemplateName = "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\bom-standard.sldbomtbt";
            BomType = (int)swBomType_e.swBomType_Indented;
            Configuration = "Default";
            nbrType = (int)swNumberingType_e.swNumberingType_Detailed;

            swBOMAnnotation = (BomTableAnnotation)swModelDocExt.InsertBomTable4(TemplateName, 0, 0, BomType, Configuration, false, nbrType, true, true);
            swBOMFeature = (BomFeature)swBOMAnnotation.BomFeature;

            // Print the name of the configuration used for the BOM table
            Debug.Print("Name of configuration used for BOM table: " + swBOMFeature.Configuration);

            // Insert BOM balloon for the selected face
            boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.091853347996107, -0.0104709589619745, 0.00174830255600256, false, 0, null, 0);

            StackedBalloonParams = (StackedBalloonOptions)swModelDocExt.CreateStackedBalloonOptions();
            StackedBalloonParams.BalloonsPerLine = 10;
            StackedBalloonParams.StackDirection = (int)swStackedBalloonDirection_e.swStackedBalloonDir_Right;
            StackedBalloonParams.Style = (int)swBalloonStyle_e.swBS_SplitCirc;
            StackedBalloonParams.LowerTextContent = (int)swBalloonTextContent_e.swBalloonTextCustom;
            StackedBalloonParams.LowerText = "Lower Text";
            StackedBalloonParams.ShowQuantity = true;
            StackedBalloonParams.Size = (int)swBalloonFit_e.swBF_Tightest;
            StackedBalloonParams.QuantityPlacement = (int)swBalloonQuantityPlacement_e.swBalloonQuantityPlacement_Top;
            StackedBalloonParams.QuantityDenotationText = "Denotation Text";
            StackedBalloonParams.QuantityOverride = false;
            StackedBalloonParams.ItemNumberStart = 1;
            StackedBalloonParams.ItemNumberIncrement = 1;
            StackedBalloonParams.ItemOrder = (int)swBalloonItemNumbersOrder_e.swBalloonItemNumbers_DoNotChangeItemNumbers;

            swNote = (Note)swModelDocExt.InsertStackedBalloon2(StackedBalloonParams);

            swModel.ViewZoomtofit2();

            // Get whether balloon is a stacked balloon;
            // if so, print the name of the balloon

            if (swNote.IsStackedBalloon())
            {
                Debug.Print("Name of stacked balloon: " + swNote.GetName());

            }

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
