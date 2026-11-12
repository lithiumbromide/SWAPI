---
title: "Create Structural Costing Analysis Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swcostingapi/Create_Structural_Costing_Analysis_Example_CSharp.htm"
---

# Create Structural Costing Analysis Example (C#)

This example shows how to create a structural Costing analysis of a weldment part.

```
//------------------------------------------------
// Preconditions:
// 1. Specified part template exists.
// 2. Add a reference to SolidWorks.Interop.sldcostingapi.dll.
// 3. Open the Immediate window.
// 4. Run the macro.
//
// Postconditions:
// 1. Creates a weldment part.
// 2. Gets the CostingManager.
// 3. Gets the Costing part.
// 4. Sets the Costing manufacturing method
//    to structural and gets the Costing body.
// 5. Gets the common Costing analysis and the
//    structural Costing analysis.
// 6. Gets the material classes from the Costing template
//    and sets the material class.
// 7. Gets the material names from the Costing template
//    and sets the material for the material class.
// 8. Sets and gets structural Costing analysis
//    parameters.
// 9. Gets the total manufacturing cost.
//10. Examine the Immediate window to see the
//    results of steps 6 through 9.
//-------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using SolidWorks.Interop.sldcostingapi;
using System.Diagnostics;
using System;

namespace structuralCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchMgr = default(SketchManager);
            FeatureManager swFeatMgr = default(FeatureManager);
            SelectionMgr swSelMgr = default(SelectionMgr);
            CostManager swcCostMgr = default(CostManager);
            CostPart swcCostPart = default(CostPart);
            CostBody swcCostBody = default(CostBody);
            CostAnalysis swcCostAnalysis = default(CostAnalysis);
            CostAnalysisStructural swcStructuralAnalysis = default(CostAnalysisStructural);
            object swFeat = null;
            object[] sketchLines = null;
            StructuralMemberGroup[] groupArray = new StructuralMemberGroup[1];
            StructuralMemberGroup group1 = default(StructuralMemberGroup);
            SketchLine[] segment1 = new SketchLine[1];
            SketchLine[] segmentArray1 = new SketchLine[1];
            bool status = false;
            double totalCost = 0;
            string templateName = null;
            int materialClassCount = 0;
            string[] materialClasses = null;
            int materialCount = 0;
            string[] materials = null;
            int i = 0;
            int costMethod = 0;

            //Open new part
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2015\\templates\\Part.prtdot", 0, 0, 0);

            //Sketch a rectangle
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
            swSketchMgr = (SketchManager)swModel.SketchManager;
            sketchLines = (object[])swSketchMgr.CreateCornerRectangle(0, 0, 0, 0.0712674458144988, -0.0441036883594848, 0);
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);

            //Create a weldment feature
            swFeatMgr = (FeatureManager)swModel.FeatureManager;
            swFeat = (object)swFeatMgr.InsertWeldmentFeature();

            //Create a structural member
            status = swModelDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", 0, -0.00830721773633059, 0, true, 0, null, 0);
            group1 = (StructuralMemberGroup)swFeatMgr.CreateStructuralMemberGroup();
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", 0, 0.334864850338306, 0.393154025912395, true, 0, null, 0);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            segment1[0] = (SketchLine)swSelMgr.GetSelectedObject6(1, 0);
            group1.Segments = (segment1);
            group1.ApplyCornerTreatment = true;
            group1.CornerTreatmentType = 1;
            group1.GapWithinGroup = 0;
            group1.GapForOtherGroups = 0;
            group1.Angle = 0;
            groupArray[0] = group1;
            swFeat = (object)swFeatMgr.InsertStructuralWeldment4("c:\\program files\\solidworks corp\\solidworks\\lang\\english\\weldment profiles\\ansi inch\\rectangular tube\\3 x 2 x 0.25.sldlfp", 1, true, (groupArray));
            swModel.ClearSelection2(true);

            //Get CostingManager
            swcCostMgr = (CostManager)swModelDocExt.GetCostingManager();
            if (swcCostMgr == null)
            {
                Debug.Print("CostingManager is nothing.");
                return;
            }

            //Get Costing part
            swcCostPart = (CostPart)swcCostMgr.CostingModel;
            if (swcCostPart == null)
            {
                Debug.Print("Costing part is nothing.");
                return;
            }

            //Set the Costing manufacturing method
            //to structural and get the Costing body
            swcCostBody = (CostBody)swcCostPart.SetCostingMethod("", (int)swcMethodType_e.swcMethodType_Structural);
            if (swcCostBody == null)
            {
                Debug.Print("Costing body is nothing.");
                return;
            }

            //Get the common Costing analysis
            swcCostAnalysis = (CostAnalysis)swcCostBody.GetCostAnalysis();
            if (swcCostAnalysis == null)
            {
                Debug.Print("Failed to activate Costing analysis.");
                return;
            }

            //Get the structural Costing analysis
            swcStructuralAnalysis = (CostAnalysisStructural)swcCostAnalysis.GetSpecificAnalysis();
            if (swcStructuralAnalysis == null)
            {
                Debug.Print("Structural Costing analysis is nothing.");
                return;
            }

            //Get the material classes from the Costing template
            materialClassCount = swcStructuralAnalysis.GetMaterialClassesCount();
            if (materialClassCount == 0)
            {
                Debug.Print("No material classes for this structural Costing analysis.");
                return;
            }
            Debug.Print("Structural Costing Analysis");
            materialClasses = (string[])swcStructuralAnalysis.GetMaterialClasses();
            Debug.Print("  Valid material classes for this structural Costing Analysis: ");
            for (i = 0; i <= materialClassCount - 1; i++)
            {
                Debug.Print("    " + materialClasses[i]);
            }

            //Set the material class
            swcStructuralAnalysis.CurrentMaterialClass = materialClasses[0];
            Debug.Print("  Name of the material class for this structural Costing analysis: " + materialClasses[0]);

            //Get the material names from the Costing template
            templateName = swcCostAnalysis.CostingTemplateName;
            Debug.Print("  Costing template path and file name: " + templateName);
            materialCount = swcStructuralAnalysis.GetMaterialCount(materialClasses[0]);
            if (materialCount == 0)
            {
                Debug.Print("No materials for this structural Costing Analysis.");
                return;
            }
            Debug.Print("  Number of materials: " + materialCount);
            materials = (string[])swcStructuralAnalysis.GetMaterials(materialClasses[0]);
            Debug.Print("  Valid materials for this structural Costing Analysis: ");
            for (i = 0; i <= materialCount - 1; i++)
            {
                Debug.Print("    " + materials[i]);
            }
            swcStructuralAnalysis.CurrentMaterial = materials[0];
            Debug.Print("  Name of material for " + materialClasses[0] + " for this structural Costing analysis: " + materials[0]);

            //Set and get structural Costing analysis parameters
            //Get current profile
            Debug.Print("  Current profile:");
            Debug.Print("    Standard: " + swcStructuralAnalysis.CurrentProfileStandard);
            Debug.Print("    Type:     " + swcStructuralAnalysis.CurrentProfileType);
            Debug.Print("    Size:     " + swcStructuralAnalysis.CurrentProfileSize);

            //Get current cost method
            costMethod = swcStructuralAnalysis.CurrentCostMethodType;
            switch (costMethod)
            {
                case 0:
                    Debug.Print("  Current cost method: Unknown");
                    Debug.Print("  Exiting. Check the template.");
                    return;

                    break;
                case 1:
                    Debug.Print("  Current cost method: Per length");
                    break;
                case 2:
                    Debug.Print("  Current cost method: Per unit length");
                    break;
            }

            //Reset the shop rate to the default
            swcStructuralAnalysis.ShopRateApplied = true;
            swcStructuralAnalysis.ShopRate = 27.55;
            Debug.Print("  Shop rate applied: " + swcStructuralAnalysis.ShopRateApplied);
            Debug.Print("  Shop rate: $" + swcStructuralAnalysis.ShopRate);

            totalCost = swcCostAnalysis.GetTotalCostToManufacture();
            Debug.Print("Total structural cost to manufacture: $" + totalCost);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
