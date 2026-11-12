---
title: "Get Factor of Safety Values for Composites Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Factor_of_Safety_Values_for_Composites_Example_CSharp.htm"
---

# Get Factor of Safety Values for Composites Example (C#)

This example shows how to get Factor of Safety results for specified entities having either composite or non-composite shells.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1.  Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //     Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2.  Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //     (in the IDE, click Project > Add Reference > .NET >
 //     SolidWorks.Interop.cosworks > OK).
  // 3.  Open public_documents\samples\tutorial\api\tjoint.sldprt.
 // 4.  Click the Ready - 8 plies tab.
 // 5.  Expand tjoint in the FeatureManager design tree.
 // 6.  Right-click SurfaceBody1 and click Edit Definition.
 // 7.  Select Thin and click the green arrow.
 // 8.  Right-click SurfaceBody2 and click Edit Definition.
 // 9.  Select Thin and click the green arrow.
 // 10. Open an Immediate window.
 //
 // Postconditions:
 // 1. Analyzes two studies:
 //    a. 8 plies with non-composite materials applied to surface bodies.
 //    b. 16 plies with composite materials applied to surface bodies.
 // 2. Inspect the Immediate window for the minimum and maximum factors of safety.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 // ---------------------------------------------------------------------------

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
 namespace GetMinMaxFOS_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         CosmosWorks COSMOSWORKS;
         CwAddincallback CWAddinCallBack;
         CWModelDoc ActDoc;
         CWStudyManager StudyMngr;
         CWStudy Study;
         CWResults CWResult;
         CWMesh CWMesh;
         SelectionMgr SelMgr;
         bool bIsCompositeOption;
         object[] varArray1 = new object[1];
         object Obj1;
         int NonCompositeCriterion;
         int CompositeFailureCriterion;
         int ShellFace;
         int PlyNum;
         int ShellFaceOption;
         int MinFOSVal;
         int swFactorOfSafetyDist;
         object[] FosVal;
         bool boolstatus;
         int errCode;
         double el;

         double tl;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;

             SelMgr = (SelectionMgr)Part.SelectionManager;
             boolstatus = Part.Extension.SketchBoxSelect(0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000);
             boolstatus = Part.Extension.SelectByID2("Surface-Trim1", "SURFACEBODY", -0.0533802776919856, 0.00381973755003173, 0.025111145036476, true, 0, null, 0);

             Obj1 = SelMgr.GetSelectedObject6(1, -1);
             varArray1[0] = Obj1;

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             ActDoc = COSMOSWORKS.ActiveDoc;
             StudyMngr = ActDoc.StudyManager;

             bIsCompositeOption = true;
             NonCompositeCriterion = (int)swsFOS_NonCompositeCriterion_e.swsFOSNonCompositeCriterion_VonMisesHencky;
             CompositeFailureCriterion = (int)swsFOS_CompositeCriterion_e.swsFOSCompositeCriterion_Tsai_Hill;
             PlyNum = 0; // Across all plies
             ShellFace = (int)swsFOS_ShellFaceOption_e.swsFOS_ShellFaceOption_TopFace;
             ShellFaceOption = (int)swsFOS_NormalShellFaceOption_e.swsFOS_NormalShellFaceOption_Top;
             MinFOSVal = 1;
             swFactorOfSafetyDist = (int)swsFOS_DistributionOpt_e.swsFOS_DistributionOpt_AreaBelowFOS;

             // Analyze study 1 (non-composite shells) and process results
             Debug.Print("Analyzing Study 1 with 8 plies...");
             StudyMngr.ActiveStudy = 1;
             Study = StudyMngr.GetStudy(1);

             // Create mesh
             CWMesh = Study.Mesh;
             if (CWMesh == null)
                 ErrorMsg(swApp, "No mesh object.", false);
             CWMesh.Quality = 1;
             CWMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
             errCode = Study.CreateMesh(0, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed.", true);

             // Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed.", true);
             CWResult = Study.Results;
             if (CWResult == null)
                 ErrorMsg(swApp, "No result object.", false);

             // For non-composite shells
             FosVal = (object[])CWResult.GetMinMaxFactorOfSafety2(true, null, (int)swsFOS_NonCompositeCriterion_e.swsFOSNonCompositeCriterion_Automatic, (int)swsFOS_ShellFaceOption_e.swsFOS_ShellFaceOption_TopFace, 0, out errCode);
             Debug.Print("  Non-composite shell:");
             Debug.Print("    Minimum FOS: " + FosVal[0].ToString());
             Debug.Print("    Maximum FOS: " + FosVal[1].ToString());

             // For non-composite shells and detail settings
             FosVal = (object[])CWResult.GetMinMaxFactorOfSafetyWithDetailSettings2(true, (varArray1), (int)swsFOS_NonCompositeCriterion_e.swsFOSNonCompositeCriterion_VonMisesHencky, true, 1000, (int)swsStrengthUnit_e.swsStrengthUnitPSI, (int)swsFactorOfSafetyStressLimitOption_e.swsFactorOfSafetyStressLimitOption_YieldStrength, 0, (int)swsFactorOfSafetyStressLimitOption_e.swsFactorOfSafetyStressLimitOption_UltimateStrength, 0,
             1, 1, false, ShellFaceOption, 0, out errCode);
             Debug.Print("  Non-composite shell and detail settings:");
             Debug.Print("    Minimum FOS: " + FosVal[0].ToString());
             Debug.Print("    Maximum FOS: " + FosVal[1].ToString());

             // Analyze study 2 (composite shells) and process results
             Debug.Print("");
             Debug.Print("Analyzing Study 2 with 16 plies...");
             StudyMngr.ActiveStudy = 2;
             Study = StudyMngr.GetStudy(2);

             // Create mesh
             CWMesh = Study.Mesh;
             if (CWMesh == null)
                 ErrorMsg(swApp, "No mesh object.", false);
             CWMesh.Quality = 1;
             CWMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
             errCode = Study.CreateMesh(0, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed.", true);

             // Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed.", true);
             CWResult = Study.Results;
             if (CWResult == null)
                 ErrorMsg(swApp, "No result object.", false);

             FosVal = (object[])CWResult.GetFactorOfSafetyForComposites(bIsCompositeOption, (varArray1), NonCompositeCriterion, CompositeFailureCriterion, PlyNum, ShellFace, ShellFaceOption, swFactorOfSafetyDist, MinFOSVal, out errCode);
             Debug.Print("  Composite shell:");
             Debug.Print("    Minimum FOS: " + FosVal[0].ToString());
             Debug.Print("    Maximum FOS: " + FosVal[1].ToString());

         }

         public void ErrorMsg(SldWorks SwApp, string Message, bool EndTest)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");

         }

         public SldWorks swApp;

     }

 }
```
