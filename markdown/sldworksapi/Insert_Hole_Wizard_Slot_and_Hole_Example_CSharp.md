---
title: "Insert Hole Wizard Slot and Hole Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Hole_Wizard_Slot_and_Hole_Example_CSharp.htm"
---

# Insert Hole Wizard Slot and Hole Example (C#)

This example shows how to use [IFeatureManager::HoleWizard5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~HoleWizard5.html) to insert a straight slot and a counterbore hole in a part.

```
//-----------------------------------------------
// Preconditions:
// 1. Verify that the specified part document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Creates a straight slot and a counterbore hole.
// 3. Prints the length of the slot to the
//    Immediate window.
// 4. To verify steps 2 and 3, examine the part in the
//    graphics area, the FeatureManager design tree, and
//    the Immediate window.
//
// NOTE: Because the part document is used elsewhere,
// do not save changes.
//------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

Namespace HoleWizard5FeatureManagerCSharp.csproj
{
    Partial Class SolidWorksMacro
    {

        public void Main()
        {

            ModelDoc2 swModel = default(ModelDoc2);
            FeatureManager swFeatureMgr = default(FeatureManager);
            Feature swFeature = default(Feature);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            string fileName = null;
            int errors = 0;
            int warnings = 0;
            bool status = false;
            int SlotType = 0;
            int HoleType = 0;
            int StandardIndex = 0;
            int FastenerTypeIndex = 0;
            string SSize = null;
            short EndType = 0;
            double ConvFactorLength = 0;
            double ConvFactorAngle = 0;
            double Diameter = 0;
            double Depth = 0;
            double Length = 0;
            double ScrewFit = 0;
            double DrillAngle = 0;
            double NearCsinkDiameter = 0;
            double NearCsinkAngle = 0;
            double FarCsinkDiameter = 0;
            double FarCsinkAngle = 0;
            double Offset = 0;
            string ThreadClass = null;
            double CounterBoreDiameter = 0;
            double CounterBoreDepth = 0;
            double HeadClearance = 0;
            double BotCsinkDiameter = 0;
            double BotCsinkAngle = 0;
            WizardHoleFeatureData2 swWizardHoleFeatData = default(WizardHoleFeatureData2);

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2020\\samples\\tutorial\\api\\block20.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Create a slot

            //Select the face where to create the slot
            status = swModelDocExt.SelectByID2("", "FACE", -0.000609805077203873, 0.0396239999998897, -0.00830387834611201, false, 0, null, 0);

            SlotType = (int)swWzdGeneralHoleTypes_e.swWzdHoleSlot;
            StandardIndex = (int)swWzdHoleStandards_e.swStandardAnsiInch;
            FastenerTypeIndex = (int)swWzdHoleStandardFastenerTypes_e.swStandardAnsiInchAllDrillSizes;
            SSize = "#97";
            EndType = (int)swEndConditions_e.swEndCondBlind;
            ConvFactorLength = 25.4 / 1000; 		//Convert inches to meters
            ConvFactorAngle = (22 / 7) / 180; 		//Convert degrees to radians
            Diameter = 0.5 * ConvFactorLength;
            Depth = 2 * ConvFactorLength;
            Length = 3 * ConvFactorLength;

            //Value1 to Value12 arguments; SOLIDWORKS Design
            //ignores parameters set to -1
            ScrewFit = -1;   		         //Value1
            DrillAngle = 100 * ConvFactorAngle;	//Value2
            NearCsinkDiameter = -1;         		//Value3
            NearCsinkAngle = -1;            		//Value4
            FarCsinkDiameter = -1;          		//Value5
            FarCsinkAngle = -1;             		//Value6
            Offset = -1;                    		//Value7
            //Value8 - Value12 all set to -1

            ThreadClass = "";

            swFeature = (Feature)swFeatureMgr.HoleWizard5(SlotType, StandardIndex, FastenerTypeIndex, SSize, EndType, Diameter, Depth, Length,
            ScrewFit, DrillAngle, NearCsinkDiameter, NearCsinkAngle, FarCsinkDiameter, FarCsinkAngle, Offset, -1, -1, -1, -1, -1,
            ThreadClass, false, false, false, false, false, false);
```

//Print length of slot to Immediate window
swWizardHoleFeatData = (WizardHoleFeatureData2)swFeature.**GetDefinition**();
Debug.Print("Length of slot: " + swWizardHoleFeatData.**Length** + " inches");

```
            //Create a counterbore hole

            //Select the face where to create the hole
            status = swModelDocExt.SelectByID2("", "FACE", -0.0060197480091233, 0.0396239999998329, 0.0270812377555103, false, 0, null, 0);

            HoleType = (int)swWzdGeneralHoleTypes_e.swWzdCounterBore;
            StandardIndex = (int)swWzdHoleStandards_e.swStandardAnsiInch;
            FastenerTypeIndex = (int)swWzdHoleStandardFastenerTypes_e.swStandardAnsiInchBinding;
            SSize = "#12";
            EndType = (int)swEndConditions_e.swEndCondThroughAll;
            ConvFactorLength = 25.4 / 1000;	//Convert inches to meters
            ConvFactorAngle = (22 / 7) / 180;	//Convert degrees to radians
            Diameter = 0.5 * ConvFactorLength;
            Depth = -1;
            Length = -1;

            //Value1 to Value12 arguments; SOLIDWORKS Design
            //ignores parameters set to -1
            CounterBoreDiameter = 0.6 * ConvFactorLength;	//Value1
            CounterBoreDepth = 0.2 * ConvFactorLength;		//Value2
            HeadClearance = -1;                     		//Value3
            ScrewFit = -1;                          		//Value4
            DrillAngle = -1;                        		//Value5
            NearCsinkDiameter = -1;                 		//Value6
            NearCsinkAngle = -1;                    		//Value7
            BotCsinkDiameter = -1;                          	//Value8
            BotCsinkAngle = -1;                             	//Value9
            FarCsinkDiameter = -1;                  		//Value10
            FarCsinkAngle = -1;                     		//Value11
            Offset = -1;                            		//Value12

            ThreadClass = "";

            swFeature = (Feature)swFeatureMgr.HoleWizard5(HoleType, StandardIndex, FastenerTypeIndex, SSize, EndType,
            Diameter, Depth, Length, CounterBoreDiameter, CounterBoreDepth, HeadClearance, ScrewFit, DrillAngle,
            NearCsinkDiameter, NearCsinkAngle, BotCsinkDiameter, BotCsinkAngle, FarCsinkDiameter, FarCsinkAngle,
            Offset, ThreadClass, false, false, false, false, false, false);

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
