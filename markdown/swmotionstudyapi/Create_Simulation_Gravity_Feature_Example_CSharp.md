---
title: "Create Simulation Gravity Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swmotionstudyapi/Create_Simulation_Gravity_Feature_Example_CSharp.htm"
---

# Create Simulation Gravity Feature Example (C#)

This example shows how to create a simulation gravity feature in a motion study.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
  // 1. Verify that the specified model document exists.
 // 2. In SOLIDWORKS, verify that View > MotionManager is selected.
  // 3. In the IDE, right-click the project name in the Project Explorer,
 //    click Add Reference, browse to install_dir\api\redist, and select
 //    SolidWorks.Interop.swmotionstudy.dll.
 // 4. Click OK.
 // 5. Open an Immediate window.
 //
 // Postconditions:
 // 1. Adds Gravity to the MotionManager design tree on the Motion Study 1 tab.
 // 2. Inspect the Immediate window.
 //
 // NOTE: Because the model is used elsewhere,
 // do not save changes when closing it.
  //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.swmotionstudy;
 using System.Runtime.InteropServices;

 namespace CreateSimGravFeat_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         ModelDocExtension swModelDocExt;
         MotionStudyManager swMotionMgr;
         MotionStudy swMotionStudy1;
         SimulationGravityFeatureData swGravityFeat;
         Feature swFeat;
         int longstatus;
         int longwarnings;

         public void Main()
         {
             swModel = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\beam_boltconnection.sldasm", 2, 0, "", ref longstatus, ref longwarnings);
             swApp.ActivateDoc2("beam_boltconnection", false, ref longstatus);
             swModel = (ModelDoc2)swApp.ActiveDoc;

             swModelDocExt = swModel.Extension;

             swMotionMgr = (MotionStudyManager)swModelDocExt.GetMotionStudyManager();
             swMotionStudy1 = swMotionMgr.GetMotionStudy("Motion Study 1");

             if ((swMotionStudy1 == null))
             {
                 Debug.Print("Motion Study 1 is not available");
             }

             swMotionStudy1.StudyType = (int)swMotionStudyType_e.swMotionStudyTypePhysicalSimulation;

             // Activate Motion Study 1
             swMotionStudy1.Activate();

             // Define feature data
             swGravityFeat = (SimulationGravityFeatureData)swMotionStudy1.CreateDefinition((int)swFeatureNameID_e.swFmAEMGravity);
             if (swGravityFeat == null)
             {
                 Debug.Print("Creation of feature data object failed");
             }
             swGravityFeat.ReverseDirection = false;
             swGravityFeat.Axis = 0;
             swGravityFeat.Strength = 12;

             // Create feature
             swFeat = (Feature)swMotionStudy1.CreateFeature(swGravityFeat);

             if (swFeat == null)
             {
                 Debug.Print("Creation of feature failed");
             }
             else
             {
                 Debug.Print("Name of the feature added: " + swFeat.Name);
             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
