---
title: "Create Countersink Slot Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Countersink_Slot_Example_CSharp.htm"
---

# Create Countersink Slot Example (C#)

This example shows how to create a countersink slot using the hole wizard.

```
//-------------------------------------------------
// Preconditions:
// 1. SOLIDWORKS Design is running.
// 2. Open the Immediate window.
// 3. Run the macro.
//
// Postconditions:
// 1. Creates a model and a countersink
//    slot in the model using the hole wizard.
// 2. Examine the Immediate window.
//-------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace HoleWizard5FeatureManagerCSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatMgr = default(FeatureManager);
            Feature swFeat = default(Feature);
            SketchManager swSketchMgr = default(SketchManager);
            WizardHoleFeatureData2 swWizardHoleFeatData = default(WizardHoleFeatureData2);
            object sketchLines = null;
            int status = 0;
            bool boolstatus = false;
            double[] P1 = new double[3];
            double[] P2 = new double[3];
            double[] P3 = new double[3];

            // Create the model for the countersink slot
            swApp.ResetUntitledCount(0, 0, 0);
            swModel = (ModelDoc2)swApp.NewDocument("C:\\Documents and Settings\\All Users\\Application Data\\SOLIDWORKS\\SOLIDWORKS 2014\\templates\\Part.prtdot", 0, 0, 0);
            swApp.ActivateDoc2("Part1", false, ref status);
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSketchMgr = swModel.SketchManager;
            swModelDocExt = swModel.Extension;
            swFeatMgr = swModel.FeatureManager;
            sketchLines = swSketchMgr.CreateCornerRectangle(-0.05096498314664, 0.05060941349678, 0, 0.1021670127265, -0.05037236706354, 0);
            boolstatus = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swFeat = swFeatMgr.FeatureExtrusion2(true, false, false, 0, 0, 0.381, 0.381, false, false, false,
            false, 0.01745329251994, 0.01745329251994, false, false, false, false, true, true, true,
            0, 0, false);

            //Create three points for the reference plane
            P1[0] = -0.0141556764402858;
            P1[1] = 0.00194061273859598;
            P1[2] = 0;
            P2[0] = -0.0141556764402858;
            P2[1] = 0.00194061273859598;
            P2[2] = 1;
            P3[0] = -0.149976101832345;
            P3[1] = -0.988792859011662;
            P3[2] = 0;
            //Create the reference plane
            swModel.CreatePlaneFixed2(P1, P2, P3, false);
            //Select reference plane
            boolstatus = swModelDocExt.SelectByID2("Plane1", "PLANE", -0.0156784487003801, -0.00916715285390111, 0.0558270998665543, false, 0, null, 0);
            // Create the countersink slot
            swFeat = swFeatMgr.HoleWizard5((int)swWzdGeneralHoleTypes_e.swWzdCounterSinkSlot, (int)swWzdHoleStandards_e.swStandardAnsiMetric, (int)swWzdHoleStandardFastenerTypes_e.swStandardAnsiMetricFlatHead82, "M2", (int)swEndConditions_e.swEndCondThroughAll, 0.0102, 0.010312189893273, 1, 0.0044, 1.57079632679489, 0.000152189893272978,
            0, 2.05948851735331, 0, 0, 0, 1, 0, 0, 0, "",
            false, true, true, true, true, false);

            swWizardHoleFeatData = (WizardHoleFeatureData2)swFeat.GetDefinition;
            Debug.Print("Length of countersink slot: " + swWizardHoleFeatData.Length;

        }
        public SldWorks swApp;
    }
}
```
