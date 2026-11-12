---
title: "Create 3D Contact Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_3D_Contact_Feature_Example_CSharp.htm"
---

# Create 3D Contact Feature Example (C#)

This example shows how to create a 3D Contact feature for use in motion studies.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
  // 1. Verify that the specified model document exists.
 // 2. In SOLIDWORKS Design, verify that View > MotionManager is selected.
  // 3. In the IDE, right-click the project name in the Project Explorer,
 //    click Add Reference, browse to install_dir\api\redist, and select
 //    SolidWorks.Interop.swmotionstudy.dll.
 // 4. Click OK.
 // 5. Open an Immediate window.
 //
 // Postconditions:
 // 1. Selects the components to study.
 // 2. Sets the static contact friction option.
 // 3. Adds Solid Body Contact1 to the MotionManager design tree on the
 //    Motion Study 1 tab.
 // 4. Inspect the Immediate window.
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

 namespace CreateSim3DContFeat_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             MotionStudyManager swMotionMgr = default(MotionStudyManager);
             MotionStudy swMotionStudy1 = default(MotionStudy);
             Simulation3DContactFeatureData swContFeat = default(Simulation3DContactFeatureData);
             bool boolstatus = false;
             Feature swFeat = default(Feature);
             int longstatus = 0;
             int longwarnings = 0;

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

             // Create the feature data object
             swContFeat = (Simulation3DContactFeatureData)swMotionStudy1.CreateDefinition((int)swFeatureNameID_e.swFmAEM3DContact);

             if (swContFeat == null)
             {
                 Debug.Print("Failed to create feature data object");
             }

             SelectionMgr swSelMgr = default(SelectionMgr);
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             // Select the components to study
             boolstatus = swModelDocExt.SelectByID2("Beam with holes-1@beam_boltconnection", "COMPONENT", 0, 0, 0, false, 0, null, 0);
             boolstatus = swModelDocExt.SelectByID2("Beam with holes-2@beam_boltconnection", "COMPONENT", 0, 0, 0, true, 0, null, 0);

             // Set the 3D Contact components
             Component[] ContactObj = new Component[2];
             ContactObj[0] = (Component)swSelMgr.GetSelectedObject6(1, -1);
             ContactObj[1] = (Component)swSelMgr.GetSelectedObject6(2, -1);

             swContFeat.ContactComponents = ContactObj;

             // Set the static contact friction option
             swContFeat.FrictionOption = (int)swMotionContactFrictionType_e.swMotionContactFrictionFull;

             // Create a 3D Contact feature
             swFeat = (Feature)swMotionStudy1.CreateFeature(swContFeat);

             boolstatus = swModelDocExt.SelectByID2("Solid Body Contact1", "SIMULATION_ELEMENT", 0, 0, 0, false, 0, null, 0);

             if (swFeat == null)
             {
                 Debug.Print("Failed to create feature");
             }
             else
             {
                 Debug.Print(swFeat.Name);
                 if (swContFeat.UseRestitutionCoefficient)
                 {
                     Debug.Print("  Use coefficient of restitution:");
                     Debug.Print("    Coefficient of restitution: " + swContFeat.RestitutionCoefficient);
                 }
                 else
                 {
                     Debug.Print("  Use impact force:");
                     Debug.Print("    Exponent of exponential force: " + swContFeat.Exponent);
                     Debug.Print("    Maximum damping coefficient: " + swContFeat.MaxDamping);
                     Debug.Print("    Penetration at which maximum damping is applied: " + swContFeat.Penetration);
                     Debug.Print("    Stiffness of material at boundary of interaction: " + swContFeat.Stiffness);
                 }
                 if (swContFeat.SpecifyMaterial)
                 {
                     Debug.Print("  Type of material as defined by swCosmosWorksMat:");
                     Debug.Print("    First object: " + swContFeat.get_MaterialID(0));
                     Debug.Print("    Second object: " + swContFeat.get_MaterialID(1));
                 }
                 if (swContFeat.FrictionOption == (int)swMotionContactFrictionType_e.swMotionContactFrictionFull)
                 {
                     Debug.Print("  Static contact friction:");
                     Debug.Print("    Coefficient: " + swContFeat.StaticFrictionCoefficient);
                     Debug.Print("    Velocity: " + swContFeat.StaticFrictionVelocity);
                 }
                 else
                 {
                     Debug.Print("  Dynamic contact friction:");
                     Debug.Print("    Coefficient: " + swContFeat.DynamicFrictionCoefficient);
                     Debug.Print("    Velocity: " + swContFeat.DynamicFrictionVelocity);
                 }

             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
