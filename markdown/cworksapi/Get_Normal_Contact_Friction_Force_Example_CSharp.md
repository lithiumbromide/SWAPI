---
title: "Get Contact or Friction Forces Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Normal_Contact_Friction_Force_Example_CSharp.htm"
---

# Get Contact or Friction Forces Example (C#)

This example shows how to get the contact or friction forces for selected entities.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

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
 // Postconditions: Inspect the Immediate window for the x-, y-, z-component
 // and resultant contact forces for the selected entity.
 //
 // NOTE: Because this assembly document is used by
 // SOLIDWORKS Simulation tutorial, do not save any
 // changes when closing the document.
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

 namespace ContactForces_CSharp.csproj
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

             //Contact plane
             string selection1 = null;
             //Constants
             selection1 =   "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,84,2,0,0,58,1,0,0,120,1,125,81,193,78,194,64,16,125,168,16,141,26,53,154,112,245,194,17,18,79,38,158,4,132,72,132,104,90,78,132,164,41,237,86,80,218,154,186,68,61,152,244,232,7,248,27,94,252,5,255,139,250,134,210,4,37,233,108,118,103,247,205,190,217,157,55,31,199,192,38,128,100,158,84,26,80,176,225,227,20,47,152,64,99,204,221,24,33,166,196,159,81,197,25,46,49,90,222,177,184,147,136,134,67,31,112,40,238,52,121,114,218,98,198,67,206,194,114,150,229,133,164,128,93,248,97,219,118,148,161,60,203,145,160,88,73,22,249,3,237,253,231,179,242,213,249,238,103,62,165,157,144,214,10,92,97,154,179,200,235,184,134,122,178,156,52,86,146,148,134,229,72,250,125,185,247,170,111,71,15,202,209,41,116,68,168,105,234,104,18,220,95,219,129,59,85,132,231,73,189,137,11,12,209,70,11,117,122,15,209,162,112,41,97,189,152,33,26,57,165,90,44,90,228,209,204,147,47,96,13,38,186,184,194,29,12,244,177,19,243,31,7,249,140,13,224,237,102,208,91,136,";
             selection1 = selection1 +  "156,234,147,174,100,22,171,108,78,58,87,35,53,30,206,187,131,94,166,173,168,82,22,133,162,208,55,31,117,43,208,127,4,44,198,219,200,40,210,179,189,24,88,197,164,43,255,49,126,106,13,203,158,99,136,246,11,23,144,126,96,0,0,0,0,0,0,0,0";
             selection1 = selection1 +  ",Type=1";
             //Store constants in a collection
             PIDCollection.Add("selection1", selection1);

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
             CWStaticStudyOptions StudyOptions = null;
             CWResults CWFeatObj = default(CWResults);
             ModelDocExtension ActDocExt = default(ModelDocExtension);

             string sModelName = null;
             string sStudyName = null;
             string sStudyConfig = null;

             int longstatus = 0;
             int longwarnings = 0;
             int errCode = 0;
             int i = 0;

             double el = 0;
             double el_hold = 0;
             double tl = 0;
             double tl_hold = 0;

             bool bStudyFound = false;

             object[] DispArray1 = new object[1];
             object[] Force = null;

             int iMeshUnit = 0;
             int iSolverType = 0;
             int iNumberOfStudies = 0;
             int ix = 0;
             int iStudyType = 0;

             sModelName = "beam_boltconnection.sldasm";

             //SOLIDWORKS configuration that study is active under (Blank "" = use default)
             sStudyConfig =  "";
             sStudyName = "Study 1";

             Hashtable PIDCollection = new Hashtable();
             PIDCollection = PIDInitializer();

             Part = swApp.OpenDoc6("public_documents\\samples\\tutorial\\api\\beam_boltconnection.SLDASM", (int)swDocumentTypes_e.swDocASSEMBLY, 1, "", ref longstatus, ref longwarnings);
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
             Study = null;
             iNumberOfStudies = StudyMngr.StudyCount;
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
                 ErrorMsg(swApp, "Failed to find study named: " + sStudyName);
             }

             CWMesh = Study.Mesh;
             if (CWMesh == null) ErrorMsg(swApp, "No mesh object");

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
             //Using the curvature-based mesher?
             if (CWMesh.MesherType == (int)swsMesherType_e.swsMesherTypeAlternate)
             {
                 //Yes, set the min element size equal to the max element size
                 errCode = Study.CreateMesh(0, el, el);
             }
             else
             {
                 //No, using the standard mesher
                 errCode = Study.CreateMesh(0, el, tl);
             }
             if (errCode != 0)
             {
                 ErrorMsg(swApp, "CreateMesh failed: Error code = " +  Convert.ToString(errCode));

                 //Check the mesh state
                 VerifyLong(swApp, (int)swsMeshState_e.swsMeshStateExistsAndCurrent, CWMesh.MeshState, "MeshState indicates that mesh is not current and/or doesn't exist");

                 //Check the number of components that failed to mesh
                 VerifyLong(swApp, 0, CWMesh.GetNoOfFailedComponents(),  "GetNoOfFailedComponents indicates mesh failure occurred");

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
                 if (CWFeatObj == null) ErrorMsg(swApp, "Failed to get results object");

                 DispArray1[0] = SelectByPID(Part,  "selection1", PIDCollection);

                 Force = (object[])CWFeatObj.GetContactForcesAndFriction(1, null, (DispArray1), (int)swsNForceType_e.swsNForceTypeNormal, 0, out errCode);
                 if (errCode != 0) ErrorMsg(swApp, "Failed to get contact force result");

                 Debug.Print("  x, y, z, and resultant contact forces:");
                 for (i = 0; i <= Force.GetUpperBound(0); i++)
                 {
                     Debug.Print("    " + Force[i]);
                 }

             }
         }

         public SldWorks swApp;

     }
 }
```
