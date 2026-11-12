---
title: "Create Fatigue Study for Dynamic Harmonic Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Fatigue_Study_for_Dynamic_Harmonic_Study_Example_CSharp.htm"
---

# Create Fatigue Study for Dynamic Harmonic Study Example (C#)

This example shows how to create a fatigue study for a linear dynamic harmonic study.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Open public_documents\samples\Simulation Examples\Dynamics\ac_unit.sldasm.
 // 4. Activate Sample_Harmonic.
  // 5. Expand Parts in the Simulation design tree and apply Ductile Iron (SN)
  //    to all parts (right-click a part, click Apply/Edit Material,
 //    select SOLIDWORKS Materials > Iron > Ductile Iron (SN), and click Apply).
 // 6. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates study, HarmonicFatigue.
 // 2. Adds a fatigue event for step 15 of Sample_Harmonic.
 // 3. Analyzes HarmonicFatigue.
  // 4. Displays a message box with the damage percent error.
 // 5. Click OK in the message box.
  // 6. Prints the minimum and maximum fatigue values to the Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save any changes.
  //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.cosworks;
 using System.Runtime.InteropServices;
 namespace HarmonicFatigue_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback CWAddinCallBack = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWResults CWFeatObj = default(CWResults);
             CWFatigueStudyOptions FatigueOptions = default(CWFatigueStudyOptions);
             CWFatigueEvent FatigueEvent = default(CWFatigueEvent);
             int errCode = 0;
             object[] Damage = null;

             const double Tol = 0.05;
             //5% damage tolerance
             const double DamageMax = 63.68;
             //63.68% maximum damage

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (CWAddinCallBack == null)
                 ErrorMsg(swApp, "CWAddinCallBack object not found");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "COSMOSWORKS object not found");

             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "Failed to get active document");

             // Add default fatigue study results plot
             errCode = ActDoc.AddDefaultFatigueStudyPlot((int)swsFatigueStudyResultType_e.swsFatigueStudy_DamagePlot);

             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "Failed to get CWStudyManager object");

             // Create harmonic fatigue study
             Debug.Print("Creating HarmonicFatigue study...");

             Study = StudyMngr.CreateNewStudy3("HarmonicFatigue", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeFatigue, 2, out errCode);
             if (Study == null)
                 ErrorMsg(swApp, "Failed to create new study");

             errCode = Study.SetFatigueResultOptions(1, null);

             FatigueOptions = Study.FatigueStudyOptions;
             if (FatigueOptions == null)
                 ErrorMsg(swApp, "Failed to get CWFatigueStudyOptions object");

             FatigueEvent = FatigueOptions.AddFatigueEventForHarmonic("Sample_Harmonic", 0, 15, 100000, 150000, out errCode);
             FatigueEvent.SuppressUnSuppress();//suppress event
             FatigueEvent.SuppressUnSuppress();//unsuppress event

             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode );

             CWFeatObj = Study.Results;
             if (CWFeatObj == null)
                 ErrorMsg(swApp, "Failed to get CWResults object");

             // Get minimum and maximum fatigue values
             Damage = (object[])CWFeatObj.GetMinMaxFatigue(1, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get minimum and maximum fatigue. Error code as defined in swsResultsError_e: " + errCode);

             float dam = (float)Damage[3];

             // Report damage percent error if result maximum fatigue value is not within tolerance
             if ((dam < (1 - Tol) * DamageMax) | (dam > (1 + Tol) * DamageMax))
             {
                 ErrorMsg(swApp, "Damage % error = " + (((dam - DamageMax) / DamageMax) * 100));
             }

             Debug.Print("  Minimum fatigue is " + Damage[1] + " at node " + Damage[0] + ".");
             Debug.Print("  Maximum fatigue is " + Damage[3] + " at node " + Damage[2] + ".");

         }

         public void ErrorMsg(SldWorks SwApp, string Message)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```
