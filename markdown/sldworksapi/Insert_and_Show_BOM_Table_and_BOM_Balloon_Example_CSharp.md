---
title: "Insert and Show BOM Table and BOM Balloon Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_CSharp.htm"
---

# Insert and Show BOM Table and BOM Balloon Example (C#)

This example shows how to insert a Bill of Materials (BOM) table and balloon in a
drawing document.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Specified file and template exist.
 // 2. Open an Immediate Window.
//
// Postconditions:
// 1. Inserts an indented BOM table.
// 2. Inserts a BOM balloon annotation.
// 3. Inspect the Immediate Window for the BOM feature properties.
//
// NOTE: Because the drawing is used elsewhere, do not save any changes.
//---------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace IViewInsertBomTable4CSharp.csproj
 {

     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             DrawingDoc swDrawing = default(DrawingDoc);
             View swView = default(View);
             BomTableAnnotation swBOMAnnotation = default(BomTableAnnotation);
             BomFeature swBOMFeature = default(BomFeature);
             Note swNote = default(Note);
             BalloonOptions BomBalloonParams = default(BalloonOptions);
             bool boolstatus = false;
             int AnchorType = 0;
             int NbrType = 0;
             int BomType = 0;
             int nErrors = 0;
             int nWarnings = 0;
             string Configuration = null;
             string TableTemplate = null;

             swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw", (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref nErrors, ref nWarnings);
             swDrawing = (DrawingDoc)swModel;
             swModelDocExt = (ModelDocExtension)swModel.Extension;
             boolstatus = swDrawing.ActivateView("Drawing View1");
             swView = (View)swDrawing.ActiveDrawingView;

             // Insert indented BOM table
             AnchorType = (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft;
             BomType = (int)swBomType_e.swBomType_Indented;
             NbrType = (int)swNumberingType_e.swNumberingType_Detailed;
             TableTemplate = "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\bom-standard.sldbomtbt";
             Configuration = "";
             swBOMAnnotation = (BomTableAnnotation)swView.InsertBomTable6(false, 0.4, 0.3, AnchorType, BomType, Configuration, TableTemplate, false, NbrType, true, true, true);
             swBOMFeature = (BomFeature)swBOMAnnotation.BomFeature;

             Debug.Print("Type of BOM table as defined in swBomType_e: " + (int)swBOMFeature.TableType);
    Debug.Print("Numbering type of BOM table as defined in swNumberingType_e: " + (int)swBOMFeature.NumberingTypeOnIndentedBOM);
             Debug.Print("Value to display when a value is 0 as defined in swZeroQuantityDisplay_e: " + (int)swBOMFeature.ZeroQuantityDisplay);
             Debug.Print("Name of configuration used for BOM table: " + swBOMFeature.Configuration);
     Debug.Print("Display as one item? " + swBOMFeature.DisplayAsOneItem);
    Debug.Print("Sequence start number: " + swBOMFeature.SequenceStartNumber);
    Debug.Print("Keep missing items? " + swBOMFeature.KeepMissingItems);
    Debug.Print("  Strikeout missing items? " + swBOMFeature.StrikeoutMissingItems);
    Debug.Print("  Replace missing components as defined in swKeepReplacedCompOption_e: " + swBOMFeature.KeepReplacedCompOption);
    Debug.Print("Keep current item numbers when reordering rows? " + swBOMFeature.KeepCurrentItemNumbers);

             boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.1205506330468, 0.261655309417, -0.0004000000000133, false, 0, null, 0);

             BomBalloonParams = swModelDocExt.CreateBalloonOptions();
             BomBalloonParams.Style = (int)swBalloonStyle_e.swBS_Circular;
             BomBalloonParams.Size = (int)swBalloonFit_e.swBF_2Chars;
             BomBalloonParams.UpperTextContent = (int)swBalloonTextContent_e.swBalloonTextItemNumber;
             BomBalloonParams.ShowQuantity = true;
             BomBalloonParams.QuantityPlacement = (int)swBalloonQuantityPlacement_e.swBalloonQuantityPlacement_Right;
             BomBalloonParams.QuantityDenotationText = "PLACES";
             BomBalloonParams.QuantityOverride = false;
             BomBalloonParams.QuantityOverrideValue = "";
             BomBalloonParams.ItemNumberStart = 1;
             BomBalloonParams.ItemNumberIncrement = 1;
             BomBalloonParams.ItemOrder = (int)swBalloonItemNumbersOrder_e.swBalloonItemNumbers_DoNotChangeItemNumbers;

             swNote = (Note)swModelDocExt.InsertBOMBalloon2(BomBalloonParams);

             if (swNote.IsBomBalloon())
             {
                 Debug.Print("Name of BOM balloon: " + swNote.GetName());
             }

             swDrawing.ForceRebuild();

         }

         public SldWorks swApp;

     }
 }
```
