---
title: "Create Sheet Metal Costing Analysis Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swcostingapi/Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm"
---

# Create Sheet Metal Costing Analysis Example (C#)

This example shows how to create a sheet metal Costing analysis.

```vb
 //-----------------------------------------------
 // Preconditions:
 // 1. Open:
 //    C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\costing\sheet_metal_part.sldprt
 // 2. Verify that the Costing templates exist by clicking Tools > Options >
//    System Options > File Locations and select Costing templates in
//    Show folders for in SOLIDWORKS. Click Cancel to close the dialog.
// 3. Add a reference to SolidWorks.Interop.sldcostingapi.dll.
 // 4. Open the Immediate window.
// 5. Run the macro.
 //
// Postconditions:
 // 1. If prompted to save a temporary template with the costing data,
//    click Yes, browse to the folder where to save the temporary
//    template, type the name of the temporary template in File name,
//    and click Save.
// 2. Creates a sheet metal Costing analysis, which
//    can take one or more minutes to complete.
 // 3. Examine the Immediate window.
 //
// NOTE: Because the part is used elsewhere, do not
 // save any changes when closing it.
 //------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.sldcostingapi;
 using System.Runtime.InteropServices;
 using System.Diagnostics;
 using System;

 namespace SOLIDWORKSSheetMetalCostingCSharp.csproj
{

    partial class SolidWorksMacro
    {

        ModelDoc2 swModel;
        ModelDocExtension swModelDocExt;
        CostManager swCosting;
        CostPart swCostingPart;
        CostBody swCostingBody;
        object swCostingModel;
        CostAnalysis swCostingAnalysis;
        CostAnalysisSheetMetal swCostingSheetMetal;
        string sheetmetalCostingTemplatePathName;
        string sheetmetalCostingReportTemplateFolderName;
        int nbrSheetmetalCostingTemplate;
        int nbrCommonCostingTemplate;
        object[] commonCostingTemplates;
        object[] sheetmetalCostingTemplates;
        int nbrCostingBodies;
        object[] costingBodies;
        string costingBodyName;
        int i;
        bool isSheetMetalBody;
        CostFeature swCostingFeat;
        CostFeature swCostingNextFeat;
        CostFeature swCostingSubFeat;
        CostFeature swCostingNextSubFeat;
         TemplateOverrides swTemplateOverrides;
          int costingMethod;

        public void Main()
        {

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = swModel.Extension;

            // Get Costing templates names
            Debug.Print("Costing template folders:");
            sheetmetalCostingTemplatePathName = swApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swFileLocationsCostingTemplates);
            Debug.Print("    Name of Costing template folder: " + sheetmetalCostingTemplatePathName);
            sheetmetalCostingReportTemplateFolderName = swApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swFileLocationsCostingReportTemplateFolder);
            Debug.Print("    Name of Costing report template folder: " + sheetmetalCostingReportTemplateFolderName);
            Debug.Print("");

            // Get CostingManager
            swCosting = (CostManager)swModelDocExt.GetCostingManager();
            swCosting.WaitForUIUpdate();

            // Get the number of templates
            nbrSheetmetalCostingTemplate = swCosting.GetTemplateCount((int)swcCostingType_e.swcCostingType_SheetMetal);
            nbrCommonCostingTemplate = swCosting.GetTemplateCount((int)swcCostingType_e.swcCostingType_Common);

            // Get names of templates
            sheetmetalCostingTemplates = (object[])swCosting.GetTemplatePathnames((int)swcCostingType_e.swcCostingType_SheetMetal);
            commonCostingTemplates = (object[])swCosting.GetTemplatePathnames((int)swcCostingType_e.swcCostingType_Common);

            Array.Resize(ref sheetmetalCostingTemplates, nbrSheetmetalCostingTemplate + 1);
            Array.Resize(ref commonCostingTemplates, nbrCommonCostingTemplate + 1);

            Debug.Print("Costing templates:");

            // Print names of templates to Immediate window
            for (i = 0; i <= (nbrSheetmetalCostingTemplate - 1); i++)
            {
                Debug.Print("    Name of sheet metal Costing template: " + sheetmetalCostingTemplates[i]);
            }

            Debug.Print("");

            for (i = 0; i <= (nbrCommonCostingTemplate - 1); i++)
            {
                Debug.Print("    Name of common Costing template: " + commonCostingTemplates[i]);
            }

            Debug.Print("");

            // Get Costing part
            swCostingModel = (object)swCosting.CostingModel;
            swCostingPart = (CostPart)swCostingModel;

            // Create common Costing analysis
            swCostingAnalysis = (CostAnalysis)swCostingPart.CreateCostAnalysis("c:\\program files\\solidworks corp\\solidworks\\lang\\english\\costing templates\\multibodytemplate_default(englishstandard).sldctc");

            // Get common Costing analysis data
            Debug.Print("Common Costing analysis data:");
            Debug.Print("    Template name:  " + swCostingAnalysis.CostingTemplateName);
            Debug.Print("    Currency code: " + swCostingAnalysis.CurrencyCode);
            Debug.Print("    Currency name: " + swCostingAnalysis.CurrencyName);
            Debug.Print("    Currency separator: " + swCostingAnalysis.CurrencySeparator);
            Debug.Print("    Total manufacturing cost: " + swCostingAnalysis.GetManufacturingCost());
            Debug.Print("    Material costs: " + swCostingAnalysis.GetMaterialCost());
            Debug.Print("    Setup cost: " + swCostingAnalysis.GetSetupCost());
            Debug.Print("    Total cost to charge: " + swCostingAnalysis.GetTotalCostToCharge());
            Debug.Print("    Total cost to manufacture: " + swCostingAnalysis.GetTotalCostToManufacture());
            Debug.Print("    Lot size: " + swCostingAnalysis.LotSize);
            Debug.Print("    Total quantity: " + swCostingAnalysis.TotalQuantity);
            Debug.Print("");
```

// Override custom cost per bend and hem cost
swTemplateOverrides = (TemplateOverrides)swCostingPart.**TemplateOverrides**;
// Get Costing method
costingMethod = (int)swCostingPart.**GetCostingMethod**("");
if (costingMethod == (int)swcMethodType_e.swcMethodType_Sheetmetal){
// Get and set default and custom cost per bend and hem cost
Debug.Print("Custom cost per bend and hem cost");
Debug.Print(" Default custom cost per bend: $" + swTemplateOverrides.**CustomBendCost**);
Debug.Print(" Default custom hem cost: $" + swTemplateOverrides.**CustomHemCost**);
// Use custom cost per bend and hem cost
swTemplateOverrides.**UseCustomBendCost** = true;
swTemplateOverrides.**UseCustomHemCost** = true;
Debug.Print(" Use custom cost per bend? " + swTemplateOverrides.**UseCustomBendCost**);
Debug.Print(" Use custom hem cost? " + swTemplateOverrides.**UseCustomHemCost**);
// Set custom cost per bend and hem cost overrides
swTemplateOverrides.**CustomBendCost** = 4.55;
swTemplateOverrides.**CustomHemCost** = 2.17;
// Save and use custom cost per bend and hem cost overrides
swTemplateOverrides.**SaveCostingOverrideSettings**();
swTemplateOverrides.**ApplyOverrides**();
Debug.Print(" Custom cost per bend override: $" + swTemplateOverrides.**CustomBendCost**);
Debug.Print(" Custom hem cost override: $" + swTemplateOverrides.**CustomHemCost**);
Debug.Print(""

);

}

// Get Costing bodies
nbrCostingBodies = swCostingPart.**GetBodyCount**();
if ((nbrCostingBodies > 0))
{
Debug.Print("Costing bodies:");
Debug.Print(" Number of Costing bodies: " + nbrCostingBodies);
costingBodies = (object[])swCostingPart.**GetBodies**();
for (i = 0; i <= (nbrCostingBodies - 1); i++)
{
swCostingBody = (CostBody)costingBodies[i];
costingBodyName = (string)swCostingBody.**GetName**();
Debug.Print(" Name of Costing body: " + costingBodyName);
isSheetMetalBody = false;
// Make sure body is sheet metal
if ((swCostingBody.**GetBodyType**() == (int)swcBodyType_e.swcBodyType_SheetMetal))
{
isSheetMetalBody = true;
// Determine analysis status of Costing body
switch ((int)swCostingBody.BodyStatus)
{
case (int)swcBodyStatus_e.swcBodyStatus_NotAnalysed:
// Create Costing analysis
swCostingAnalysis = (CostAnalysis)swCostingBody.**CreateCostAnalysis**("c:\\program files\\solidworks corp\\solidworks\\lang\\english\\costing templates\\sheetmetaltemplate_default(englishstandard).sldcts");
Debug.Print(" Creating sheet metal Costing analysis for: " + swCostingBody.**GetName**());
break;
case (int)swcBodyStatus_e.swcBodyStatus_Analysed:
// Get Costing analysis
swCostingAnalysis = (CostAnalysis)swCostingBody.**GetCostAnalysis**();
Debug.Print(" Getting sheet metal Costing analysis for: " + swCostingBody.**GetName**());
break;
case (int)swcBodyStatus_e.swcBodyStatus_Excluded:
// Body excluded from Costing analysis
Debug.Print(" Excluded from sheet metal Costing analysis: " + swCostingBody.**GetName**());
break;
case (int)swcBodyStatus_e.swcBodyStatus_AssignedCustomCost:
// Body has an assigned custom Cost
Debug.Print(" Custom cost assigned: " + swCostingBody.**GetName**());
break;
}

Debug.Print("");

}

if (!isSheetMetalBody )
{
Debug.Print ("");
Debug.Print ("No sheet metal bodies in part! Exiting macro.");
return;
}
}
}

// Get sheet metal Costing Analysis data
swCostingSheetMetal = (CostAnalysisSheetMetal)swCostingAnalysis.**GetSpecificAnalysis**();
Debug.Print("Sheet metal Costing analysis: ");
Debug.Print(" Current material: " + swCostingSheetMetal.**CurrentMaterial**);
Debug.Print(" Current material class: " + swCostingSheetMetal.**CurrentMaterialClass**);
Debug.Print(" Current thickness: " + swCostingSheetMetal.**CurrentThickness**);
Debug.Print(" Material cost: " + swCostingSheetMetal.**MaterialCost**);
Debug.Print(" Material cost from template: " + swCostingSheetMetal.**MaterialCostFromTemplate**);
Debug.Print(" Type of blank size: " + swCostingSheetMetal.**BlankSizeType**);
Debug.Print(" Blank area from model: " + swCostingSheetMetal.**BlankAreaFromModel**);
Debug.Print(" Blank area, include any margins, from model: " + swCostingSheetMetal.**FinalAreaFromModel**);
Debug.Print("");

// Get Costing features
Debug.Print("Costing features:");
swCostingFeat = (CostFeature)swCostingAnalysis.**GetFirstCostFeature**();
while ((swCostingFeat != null))
{
Debug.Print(" Feature: " + swCostingFeat.**Name**);
Debug.Print(" Type: " + swCostingFeat.**GetType**());
Debug.Print(" Setup related: " + swCostingFeat.**IsSetup**);
Debug.Print(" Overridden: " + swCostingFeat.**IsOverridden**);
Debug.Print(" Combined cost: " + swCostingFeat.**CombinedCost**);
Debug.Print(" Combined time: " + swCostingFeat.**CombinedTime**);

swCostingSubFeat = (CostFeature)swCostingFeat.**GetFirstSubFeature**();
while ((swCostingSubFeat != null))
{
Debug.Print(" Subfeature: " + swCostingSubFeat.**Name**);
Debug.Print(" Type: " + swCostingSubFeat.**GetType**());
Debug.Print(" Setup related: " + swCostingSubFeat.**IsSetup**);
Debug.Print(" Overridden: " + swCostingSubFeat.**IsOverridden**);
Debug.Print(" Combined cost: " + swCostingSubFeat.**CombinedCost**);
Debug.Print(" Combined time: " + swCostingSubFeat.**CombinedTime**);
swCostingNextSubFeat = (CostFeature)swCostingSubFeat.**GetNextFeature**();
swCostingSubFeat = null;
swCostingSubFeat = (CostFeature)swCostingNextSubFeat;
swCostingNextSubFeat = null;
}
swCostingNextFeat = swCostingFeat.**GetNextFeature**();
swCostingFeat = null;
swCostingFeat = (CostFeature)swCostingNextFeat;
swCostingNextFeat = null;
}

}

/// <summary>
/// The SldWorks swApp variable is pre-assigned for you.
/// </summary>

public SldWorks swApp;

}
}
