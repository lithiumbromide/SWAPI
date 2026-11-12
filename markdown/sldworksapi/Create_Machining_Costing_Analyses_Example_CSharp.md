---
title: "Create Machining Cost Analysis Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Machining_Costing_Analyses_Example_CSharp.htm"
---

# Create Machining Cost Analysis Example (C#)

## Create Machining Costing Analysis Example (C#)

This example shows how to create a machining Costing analysis.

```vb
  //-----------------------------------------------
 // Preconditions:
 // 1. Open:
 //    C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\costing\machined_part.sldprt
 // 2. Verify that the Costing templates exist by clicking Tools > Options >
 //    System Options > File Locations and select Costing templates in
 //    Show folders for in SOLIDWORKS Design. Click Cancel to close the dialog.
 // 3. Add a reference to SolidWorks.Interop.sldcostingapi.dll.
 // 4. Open the Immediate window.
 // 5. Run the macro.
 //
 // Postconditions:
  // 1. Creates machining Costing analysis, which
 //    might take one or more minutes to complete.
 // 2. Examine the Immediate window.
 //
 // NOTE: Because the part is used elsewhere, do not
 // save changes.
 //------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.sldcostingapi;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace SOLIDWORKSMachiningCostingCSharp.csproj
 {

     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             CostManager swCosting = default(CostManager);
             CostPart swCostingPart = default(CostPart);
             CostBody swCostingBody = default(CostBody);
             object swCostingModel = null;
             CostAnalysis swCostingAnalysis = default(CostAnalysis);
             CostAnalysisMachining swCostingMachining = default(CostAnalysisMachining);
             string machiningCostingTemplatePathName = null;
             string machiningCostingReportTemplateFolderName = null;
             int nbrMachiningCostingTemplate = 0;
             int nbrCommonCostingTemplate = 0;
             object[] commonCostingTemplates = null;
             object[] machiningCostingTemplates = null;
             int nbrCostingBodies = 0;
             object[] costingBodies = null;
             string costingBodyName = null;
             int i = 0;
              bool isBody =  false;
             CostFeature swCostingFeat = default(CostFeature);
             CostFeature swCostingNextFeat = default(CostFeature);
             CostFeature swCostingSubFeat = default(CostFeature);
             CostFeature swCostingNextSubFeat = default(CostFeature);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = (ModelDocExtension)swModel.Extension;

             // Get Costing templates names
             Debug.Print("Costing template folders:");
             machiningCostingTemplatePathName = swApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swFileLocationsCostingTemplates);
             Debug.Print("    Name of Costing template folder: " + machiningCostingTemplatePathName);
             machiningCostingReportTemplateFolderName = swApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swFileLocationsCostingReportTemplateFolder);
             Debug.Print("    Name of Costing report template folder: " + machiningCostingReportTemplateFolderName);
             Debug.Print("");

             // Get CostingManager
             swCosting = (CostManager)swModelDocExt.GetCostingManager();
             swCosting.WaitForUIUpdate();

             // Get the number of templates
             nbrMachiningCostingTemplate = swCosting.GetTemplateCount((int)swcCostingType_e.swcCostingType_Machining);
             nbrCommonCostingTemplate = swCosting.GetTemplateCount((int)swcCostingType_e.swcCostingType_Common);

             // Get names of templates
             machiningCostingTemplates = (object[])swCosting.GetTemplatePathnames((int)swcCostingType_e.swcCostingType_Machining);
             commonCostingTemplates = (object[])swCosting.GetTemplatePathnames((int)swcCostingType_e.swcCostingType_Common);

             Array.Resize(ref machiningCostingTemplates, nbrMachiningCostingTemplate + 1);
             Array.Resize(ref commonCostingTemplates, nbrCommonCostingTemplate + 1);

             Debug.Print("Costing templates:");

             // Print names of templates to Immediate window
             for (i = 0; i <= (nbrMachiningCostingTemplate - 1); i++)
             {
                 Debug.Print("    Name of machining Costing template: " + machiningCostingTemplates[i]);
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

             // Get Costing bodies
             nbrCostingBodies = swCostingPart.GetBodyCount();
             if ((nbrCostingBodies > 0))
             {
                 Debug.Print("Costing bodies:");
                 Debug.Print("    Number of Costing bodies: " + nbrCostingBodies);
                 costingBodies = (object[])swCostingPart.GetBodies();
                 for (i = 0; i <= (nbrCostingBodies - 1); i++)
                 {
                     swCostingBody = (CostBody)costingBodies[i];
                     costingBodyName = swCostingBody.GetName();
                     Debug.Print("    Name of Costing body: " + costingBodyName);
                     // Make sure body is machining body
                     if ((swCostingBody.GetBodyType() == (int)swcBodyType_e.swcBodyType_Machined))
                     {
                         isBody = true;
                         // Determine analysis status of Costing body
                         switch ((int)swCostingBody.BodyStatus)
                         {
                             case (int)swcBodyStatus_e.swcBodyStatus_NotAnalysed:
                                 // Create Costing analysis
                                 swCostingAnalysis = (CostAnalysis)swCostingBody.CreateCostAnalysis("c:\\program files\\solidworks corp\\solidworks\\lang\\english\\costing templates\\machiningtemplate_default(englishstandard).sldcts");
                                 Debug.Print("    Creating machining Costing analysis for: " + swCostingBody.GetName());
                                 break;
                             case (int)swcBodyStatus_e.swcBodyStatus_Analysed:
                                 // Get Costing analysis
                                 swCostingAnalysis = (CostAnalysis)swCostingBody.GetCostAnalysis();
                                 Debug.Print("    Getting machining Costing analysis for: " + swCostingBody.GetName());
                                 break;
                             case (int)swcBodyStatus_e.swcBodyStatus_Excluded:
                                 // Body excluded from Costing analysis
                                 Debug.Print("    Excluded from machining Costing analysis: " + swCostingBody.GetName());
                                 break;
                             case (int)swcBodyStatus_e.swcBodyStatus_AssignedCustomCost:
                                 // Body has an assigned custom Cost
                                 Debug.Print("    Custom cost assigned: " + swCostingBody.GetName());
                                 break;
                         }

                         Debug.Print("");

                     }
                 }
             }

              if (!isBody )
             {
                 Debug.Print ("");
                 Debug.Print ("No bodies in part! Exiting macro.");
                 return;
             }

             // Get machining Costing Analysis data
             swCostingMachining = (CostAnalysisMachining)swCostingAnalysis.GetSpecificAnalysis();
             Debug.Print("Machining Costing analysis: ");
             Debug.Print("    Current material: " + swCostingMachining.CurrentMaterial);
             Debug.Print("    Current material class: " + swCostingMachining.CurrentMaterialClass);
             Debug.Print("    Current plate thickness: " + swCostingMachining.CurrentPlateThickness);

             Debug.Print("");

             // Get Costing features
             Debug.Print("Costing features:");
             swCostingFeat = (CostFeature)swCostingAnalysis.GetFirstCostFeature();
             while ((swCostingFeat != null))
             {
                 Debug.Print("    Feature: " + swCostingFeat.Name);
                  Debug.Print("      Type: " + swCostingFeat.GetType());
                 Debug.Print("        Setup related: " + swCostingFeat.IsSetup);
                 Debug.Print("        Overridden: " + swCostingFeat.IsOverridden);
                 Debug.Print("        Combined cost: " + swCostingFeat.CombinedCost);
                 Debug.Print("        Combined time: " + swCostingFeat.CombinedTime);

                 swCostingSubFeat = swCostingFeat.GetFirstSubFeature();
                 while ((swCostingSubFeat != null))
                 {
                     Debug.Print("      Subfeature: " + swCostingSubFeat.Name);
                     Debug.Print("        Type: " + swCostingSubFeat.GetType());
                     Debug.Print("          Setup related: " + swCostingSubFeat.IsSetup);
                     Debug.Print("          Overridden: " + swCostingSubFeat.IsOverridden);
                     Debug.Print("          Combined cost: " + swCostingSubFeat.CombinedCost);
                     Debug.Print("          Combined time: " + swCostingSubFeat.CombinedTime);
                     swCostingNextSubFeat = (CostFeature)swCostingSubFeat.GetNextFeature();
                     swCostingSubFeat = null;
                     swCostingSubFeat = (CostFeature)swCostingNextSubFeat;
                     swCostingNextSubFeat = null;
                 }
                 swCostingNextFeat = swCostingFeat.GetNextFeature();
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
```
