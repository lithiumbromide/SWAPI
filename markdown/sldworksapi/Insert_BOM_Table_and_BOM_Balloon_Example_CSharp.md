---
title: "Insert BOM Table and BOM Balloon Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_BOM_Table_and_BOM_Balloon_Example_CSharp.htm"
---

# Insert BOM Table and BOM Balloon Example (C#)

This example shows how to insert a BOM table and a BOM balloon in a drawing document.

```
//------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Inserts a parts-only BOM table.
// 2. Inserts a split-circle BOM balloon, which uses the BOM
//    table item number for its upper text,
//    to the selected edge.
// 3. Zoom to area and examine both the BOM table and BOM
//    balloon to verify.
//
// NOTE: Because this drawing document is used elsewhere,
// do not save any changes.
//-------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace InsertBOMBalloonModelDocExtension_CSharp.csproj
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
            bool boolstatus = false;
            int AnchorType = 0;
            int BomType = 0;
            string Configuration = null;
            string TableTemplate = null;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swDrawing = (DrawingDoc)swModel;
            swModelDocExt = swModel.Extension;
            boolstatus = swDrawing.ActivateView("Drawing View1");
            swView = (View)swDrawing.ActiveDrawingView;

            // Insert parts-only BOM table
            AnchorType = (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft;
            BomType = (int)swBomType_e.swBomType_PartsOnly;
            Configuration = "";
            TableTemplate = "";
            swBOMAnnotation = swView.InsertBomTable2(false, 0.4, 0.3, (int)AnchorType, (int)BomType, Configuration, TableTemplate);
            swBOMFeature = swBOMAnnotation.BomFeature;

            // Print the name of the configuration used for the BOM table
            Debug.Print("Name of configuration used for BOM table: " + swBOMFeature.Configuration);

            // Insert BOM balloon for the selected edge
            boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.1205506330468, 0.261655309417, -0.0004000000000133, false, 0, null, 0);
            swNote = (Note)swModelDocExt.InsertBOMBalloon((int)swBalloonStyle_e.swBS_SplitCirc, (int)swBalloonFit_e.swBF_Tightest, (int)swBalloonTextContent_e.swBalloonTextItemNumber, "", (int)swBalloonTextContent_e.swBalloonTextCustom, "Lower text", (int)swBalloonFit_e.swBF_UserDef, true, 2, "Denotation Text"
            );
            // Get whether balloon is a BOM balloon;
            // if so, print the name of the BOM balloon
            if (swNote.IsBomBalloon())
            {
                Debug.Print("Name of BOM balloon: " + swNote.GetName());
            }
        }
        public SldWorks swApp;
    }
}
```
