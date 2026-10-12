---
title: "Get Connector Forces, Moments, and Torques Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_the_Pin,_Bolt,_or_Bearing_Connector_Forces_Example_CSharp.htm"
---

# Get Connector Forces, Moments, and Torques Example (C#)

This example shows how to get the shear forces, axial forces, bending moments, and torques for a selected connector.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Modify the path to the specified model.
 // 4. Open the Immediate window.
 //
 // Postconditions: Inspect the Immediate window for
 // the connector forces, moments, and torques.
 //
 // NOTE: Because this assembly document is elsewhere,
 //  do not save any changes when closing the document.
 //-------------------------------------------------------------------------
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
 namespace GetConnectorForces_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public bool VerifyTolerance(SldWorks SwApp, double dExpected, double dActual, double dTol, string sMessage)
         {
             bool functionReturnValue = false;
             //This function will compare two double values to ensure that the actual
             //value is within the specified tolerance range
             //of the expected value. If the actual is not within the tolerance range,
             //an error message is reported with {sMessage}
             //as title, and the function returns false.
             //Otherwise, the function returns true to indicate equivalence/success.

             functionReturnValue =  true;
             if ((dActual < ((1 - dTol) * dExpected)) | (dActual > ((1 + dTol) * dExpected)))
             {
                 ErrorMsg(SwApp, sMessage +  ": Expected = " + Convert.ToString(dExpected) + " , Actual = " + Convert.ToString(dActual) + " , Tolerance = " + Convert.ToString(dTol) + " percent");
                 functionReturnValue = false;
             }
             return functionReturnValue;
         }

         public void ErrorMsg(SldWorks SwApp, string Message)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");
         }

         public void Main()
         {
             ModelDoc2 Part = default(ModelDoc2);

             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback COSMOSObject = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWMesh CWMesh = default(CWMesh);
             CWStaticStudyOptions StudyOptions = default(CWStaticStudyOptions);
             CWResults CWFeatObj = default(CWResults);
             ModelDocExtension ActDocExt = default(ModelDocExtension);

             string sModelName = null;
             string sStudyName = null;
             string sStudyConfig = null;

             int longstatus = 0;
             int longwarnings = 0;
             int errCode = 0;

             double el = 0;
             double el_hold = 0;
             double tl = 0;
             double tl_hold = 0;

             double UResMax = 0;
             double Tol1 = 0;

             bool bStudyFound = false;

             object[] Force = new object[16];

             int iMeshUnit = 0;
             int iSolverType = 0;
             int iNumberOfStudies = 0;
             int ix = 0;
             int iStudyType = 0;

             //Model names
             sModelName =  "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\beam_boltconnection.sldasm";

             //SOLIDWORKS configuration for which study is active (Blank "" = use default)
             sStudyConfig =  "";
             //Study name
             sStudyName =  "Study 1";

             iSolverType = (int)swsSolverType_e.swsSolverTypeDirectSparse;
             //Solver type

             Part = (ModelDoc2)swApp.OpenDoc6(sModelName, (int)swDocumentTypes_e.swDocASSEMBLY, 1, "", ref longstatus, ref longwarnings);
             if (Part == null) { ErrorMsg(swApp, "Failed to open: " + sModelName); }

             // Get the SOLIDWORKS Simulation object
             COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (COSMOSObject == null) ErrorMsg(swApp, "COSMOSObject object not found.");
             COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
             if (COSMOSWORKS == null) ErrorMsg(swApp, "COSMOSWORKS object not found.");

             //Get Active document
             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null) { ErrorMsg(swApp, "No active document"); }

             //If needed, rebuild the model
             ActDocExt = Part.Extension;
             if ((ActDocExt.NeedsRebuild == true))
             {
                 Part.ForceRebuild3(false);
             }

             //If needed, change the SOLIDWORKS configuration to activate the study
             if (!string.IsNullOrEmpty(sStudyConfig))
             {
                 Part.ShowConfiguration2(sStudyConfig);
             }

             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null) { ErrorMsg(swApp, "StudyMngr object not there"); }

             //Find the study
             bStudyFound =  false;
             iNumberOfStudies = StudyMngr.StudyCount;
             Study = null;
             for (ix = 0; ix <= iNumberOfStudies; ix++)
             {
                 StudyMngr.ActiveStudy = ix;
                 Study = StudyMngr.GetStudy(ix);
                 if (Study == null) { ErrorMsg(swApp, "Failed to get study number: " + ix); }
                 if (Study.Name == sStudyName)
                 {
                     bStudyFound = true;
                     break;
                 }
             }
             if (bStudyFound == false)
             {
                 ErrorMsg(swApp, "Failed to find study named: " + sStudyName);
             }

             //Create mesh
             CWMesh = Study.Mesh;
             if (CWMesh == null) { ErrorMsg(swApp, "No mesh object"); }

             //Check to use the default element size or tolerance

             if (((el == 0) | (tl == 0)))
             {
                 //Get the default element size and tolerance
                 CWMesh.GetDefaultElementSizeAndTolerance(iMeshUnit, out el_hold, out tl_hold);

                 //If element size was not entered, use the default
                 if (el == 0)
                 {
                     el = el_hold;
                 }

                 //If tolerance size was not entered, use the default
                 tl = 0.025;
                 if (tl == 0)
                 {
                     tl = tl_hold;
                 }
             }

             //Create Mesh
             if (CWMesh.MesherType == (int)swsMesherType_e.swsMesherTypeAlternate)
             {
                 //Using the curvature-based mesher; set the min element size equal to the max element size
                 errCode = Study.CreateMesh(0, el, el);
             }
             else
             {
                 //Using the standard mesher
                 errCode = Study.CreateMesh(0, el, tl);
             }
             if (errCode != 0) { ErrorMsg(swApp, "CreateMesh failed: Error code = " +  Convert.ToString(errCode)); }

             //Get analysis type
             iStudyType = Study.AnalysisType;
             if (iStudyType == (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeStatic)
             {
                 StudyOptions = Study.StaticStudyOptions;
             }

             if (StudyOptions == null) { ErrorMsg(swApp, "Failed to get StudyOptions object"); }

             //Set solver type
             StudyOptions.SolverType = iSolverType;

             //Running Analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0) { ErrorMsg(swApp,  "Analysis failed with error code " + errCode); }

             //Getting Results
             CWFeatObj = Study.Results;
             if (CWFeatObj == null) { ErrorMsg(swApp, "Failed to get result object"); }

             Force = (object[])CWFeatObj.GetConnectorForces2(1, "Counterbore with Nut-1", 0, out errCode);

             if (errCode != 0) { ErrorMsg(swApp, "Failed to get connector force result"); }

             Debug.Print("Connector forces, moments, and torques for Counterbore with Nut-1:");
             Debug.Print("   Shear force x-component: " + Force[0].ToString());
             Debug.Print("   Shear force y-component: " + Force[1].ToString());
             Debug.Print("   Shear force z-component: " + Force[2].ToString());
             Debug.Print("   Resultant shear force: " + Force[3].ToString());
             Debug.Print("   Axial force x-component: " + Force[4].ToString());
             Debug.Print("   Axial force y-component: " + Force[5].ToString());
             Debug.Print("   Axial force z-component: " + Force[6].ToString());
             Debug.Print("   Resultant axial force: " + Force[7].ToString());
             Debug.Print("   Bending moment x-component: " + Force[8].ToString());
             Debug.Print("   Bending moment y-component: " + Force[9].ToString());
             Debug.Print("   Bending moment z-component: " + Force[10].ToString());
             Debug.Print("   Resultant bending moment: " + Force[11].ToString());
             Debug.Print("   Torque x-component: " + Force[12].ToString());
             Debug.Print("   Torque y-component: " + Force[13].ToString());
             Debug.Print("   Torque z-component: " + Force[14].ToString());
             Debug.Print("   Resultant torque: " + Force[15].ToString());

             //Check max resultant bending moment
             UResMax = 0.467;
             Tol1 = 0.1;
             VerifyTolerance(swApp, UResMax,  Convert.ToDouble(Force[11]), Tol1, "Resultant bending moment is beyond tolerance");

         }

         public SldWorks swApp;
     }
 }
```
