---
title: "Get the Remote Load Forces Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Remote_Load_Forces_Example_CSharp.htm"
---

# Get the Remote Load Forces Example (C#)

This example shows how to get the forces applied to selected entities as a result of transferring a remote load.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Modify the path to the specified model.
 // 4. Open the Immediate window.
 //
 // Postconditions: Inspect the Immediate window for the remote load forces.
 //
 // NOTE: Because this assembly document is used by
 // SOLIDWORKS Simulation tutorial, do not save any
 // changes when closing the document.
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
 namespace GetRemoteForces_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public bool VerifyLong(SldWorks SwApp, long lExpected, long lActual, string sMessage)
         {
             bool functionReturnValue = false;
             //This function will compare two long values for equivalence.
             //If they are different, an error message is reported with {sMessage}
             //as title, and the function returns false.
             //If equivalent, the function returns true.
             functionReturnValue =  true;
             if (lActual != lExpected)
             {
                 ErrorMsg(SwApp, sMessage +  ": Expected = " + Convert.ToString(lExpected) + " , Actual = " + Convert.ToString(lActual));
                 functionReturnValue = false;
             }
             return functionReturnValue;
         }

         public bool VerifyTolerance(SldWorks SwApp, double dExpected, double dActual, double dTol, string sMessage)
         {
             bool functionReturnValue = false;
             //This function will compare two double values to ensure that the actual
             //value is within the specified tolerance range
             //of the expected value. If the actual is not within the tolerance
             //range, an error message is reported with {sMessage}
             //as title, and the function returns false. Otherwise, the function
             //returns true to indicate equivalence/success.
             functionReturnValue =  true;
             if ((dActual < ((1 - dTol) * dExpected)) | (dActual > ((1 + dTol) * dExpected)))
             {
                 ErrorMsg(SwApp, sMessage +  ": Expected = " + Convert.ToString(dExpected) + " , Actual = " + Convert.ToString(dActual) + " , Tolerance = " + Convert.ToString(dTol) + " percent");
                 functionReturnValue = false;
             }
             return functionReturnValue;
         }

         public object SelectByPID(ModelDoc2 Part, string PIDName, Hashtable PIDCollection)
         {
             object functionReturnValue = null;
             byte[] PID = null;
             string[] PIDVariant = null;
             string PIDString = null;
             int i = 0;
             object SelObj = null;

             //Get the value mapped to the PIDName key from the hashtable
             PIDString =  "";
             IDictionaryEnumerator enumerator = (IDictionaryEnumerator)PIDCollection.GetEnumerator();
             enumerator.Reset();
             while (enumerator.MoveNext())
             {
                 if ((string)enumerator.Key == PIDName)
                 {
                     PIDString = (string)enumerator.Value;
                     break;
                 }
             }

             //Parse the string into an array
             PIDVariant = PIDString.Split(new char[] { ',' });
             int sizeArray = PIDVariant.Length;
             PID = new byte[sizeArray];

             //Change to a byte array
             for (i = 0; i < PIDVariant.Length - 1; i++)
             {
                 PID[i] = Convert.ToByte(PIDVariant[i]);
             }

             //Select the entity
             SelObj = Part.Extension.GetObjectByPersistReference((PID));
             functionReturnValue = SelObj;
             SelObj = null;
             return functionReturnValue;
         }

         public Hashtable PIDInitializer()
         {
             Hashtable PIDCollection = new Hashtable();
             string selection1 = null;

             //Constants
             selection1 =   "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,161,1,0,0,16,1,0,0,120,1,109,80,77,75,195,64,20,156,42,181,181,234,65,40,232,197,163,224,69,239,182,232,197,84,44,20,34,155,30,60,8,33,110,54,98,219,36,18,183,224,69,200,143,232,111,240,230,69,252,7,30,253,79,141,243,92,226,7,184,135,157,125,51,243,102,121,175,215,5,86,1,84,203,138,55,177,106,96,3,105,126,30,105,163,76,18,234,198,23,13,52,5,197,201,243,244,190,216,127,25,190,142,107,116,109,59,210,86,228,105,48,181,131,204,6,243,34,25,198,202,220,135,218,201,107,34,171,80,203,15,91,124,15,30,173,127,51,49,218,58,106,155,212,89,96,139,187,236,246,34,202,226,153,33,189,172,14,60,244,112,141,75,20,200,49,129,129,134,101,29,32,101,61,101,45,90,68,213,226,129,111,69,70,20,75,28,17,35,196,56,162,123,4,143,62,133,49,214,75,166,118,254,243,173,0,31,39,125,31,184,218,237,28,186,57,221,205,134,150,199,192,132,113,115,204,24,94,159,231,214,49,246,88,188,157,246,125,217,143,140,214,149,209,178,88,246,247,103,5,205,178,253,23";
             selection1 = selection1 +  "7,173,119,10,108,150,220,236,47,165,78,254,193,79,249,139,99,22,0,0,0,0,0,0,0,0";
             selection1 = selection1 +  ",Type=1";

             //Store constants in a collection
             PIDCollection.Add(selection1, "selection1");

             return PIDCollection;
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

             double FRES = 0;
             double Tol1 = 0;
             double UResMax = 0;

             bool bStudyFound = false;

             object[] DispArray1 = new object[1];
             object[] Force = null;
             int iMeshUnit = 0;
             int iSolverType = 0;
             int iNumberOfStudies = 0;
             int ix = 0;
             int iStudyType = 0;

             sModelName = "K:\\api\\HELP\\Sample Macros\\Simulation\\2013\\RemoteForces\\Parts\\Remoteload.sldprt";

             //SOLIDWORKS configuration that study is active under (Blank "" = use default)
             sStudyConfig =  "";
             sStudyName = "Study 1";

             iSolverType = (int)swsSolverType_e.swsSolverTypeFFEPlus;

             Hashtable PIDCollection = new Hashtable();
             PIDCollection = PIDInitializer();

             Part = swApp.OpenDoc6(sModelName, (int)swDocumentTypes_e.swDocPART, 1, "", ref longstatus, ref longwarnings);
             if (Part == null) ErrorMsg(swApp, "Failed to open: " + sModelName);

             // Get the SOLIDWORKS Simulation object
             COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (COSMOSObject == null) ErrorMsg(swApp, "COSMOSObject object not found.");
             COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
             if (COSMOSWORKS == null) ErrorMsg(swApp, "COSMOSWORKS object not found.");

             //Get active document
             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null) ErrorMsg(swApp, "No active document");

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
             if (StudyMngr == null) ErrorMsg(swApp, "StudyMngr object not there");

             //Find the study
             bStudyFound =  false;
             iNumberOfStudies = StudyMngr.StudyCount;
             Study = null;
             for (ix = 0; ix <= iNumberOfStudies; ix++)
             {
                 StudyMngr.ActiveStudy = ix;
                 Study = StudyMngr.GetStudy(ix);
                 if (Study == null) ErrorMsg(swApp, "Failed to get study number: " + ix);
                 if (Study.Name == sStudyName)
                 {
                     bStudyFound = true;
                     break;
                 }
             }
             if (bStudyFound == false)
             {
                 ErrorMsg(swApp, "Failed to find Study named: " + sStudyName);
             }

             CWMesh = Study.Mesh;
             if (CWMesh == null) ErrorMsg(swApp, "No mesh object");

             //Check if need to use the default element size or tolerance

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
                 if (tl == 0)
                 {
                     tl = tl_hold;
                 }

             }

             //Create Mesh
             //Using the curvature-based mesher?
             if (CWMesh.MesherType == (int)swsMesherType_e.swsMesherTypeAlternate)
             {
                 //Yes, set the minimum element size equal to the maximum element size
                 errCode = Study.CreateMesh(0, el, el);
             }
             else
             {
                 //No, using the standard mesher
                 errCode = Study.CreateMesh(0, el, tl);
             }
             if (errCode != 0) ErrorMsg(swApp, "CreateMesh failed: Error code = " +  Convert.ToString(errCode));

             //Check the mesh state
             VerifyLong(swApp, (int)swsMeshState_e.swsMeshStateExistsAndCurrent, CWMesh.MeshState, "MeshState indicates that mesh is not current and/or doesn't exist");

             //Check the number of components that failed to mesh
             VerifyLong(swApp, 0, CWMesh.GetNoOfFailedComponents(), "GetNoOfFailedComponents indicates mesh failure occurred");

             //Get analysis type
             iStudyType = Study.AnalysisType;
             if (iStudyType == (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeStatic)
             {
                 StudyOptions = Study.StaticStudyOptions;
             }

             //Set solver type
             StudyOptions.SolverType = iSolverType;

             //Running analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0) ErrorMsg(swApp, "Analysis failed with error code " + errCode);

             //Getting results
             CWFeatObj = Study.Results;
             if (CWFeatObj == null) ErrorMsg(swApp, "Failed to get result object");

             DispArray1[0] = SelectByPID(Part,  "selection1", PIDCollection);

             Force = (object[])CWFeatObj.GetRemoteForces(1, null, (DispArray1), 0, out errCode);

             Debug.Print("Remote load forces:");
             Debug.Print("   Remote load force x-component: " + Force[0]);
             Debug.Print("   Remote load force y-component: " + Force[1]);
             Debug.Print("   Remote load force z-component: " + Force[2]);
             Debug.Print("   Resultant remote load force: " + Force[3]);

             if (errCode != 0) ErrorMsg(swApp, "Failed to get remote load force result");

             FRES = (double)Force[3];
             Tol1 = 0.1;
             UResMax = 100;
             //Check maximum resultant
             VerifyTolerance(swApp, UResMax, Convert.ToDouble(FRES), Tol1, "Resultant remote load force is beyond tolerance");

         }

         public SldWorks swApp;

     }
 }
```
