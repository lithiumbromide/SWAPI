---
title: "Add Remote Load Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Remote_Load_Example_CSharp.htm"
---

# Add Remote Load Example (C#)

This example shows how to add a remote load to a static study.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that the specified material library exists.
  // 4. Open public_documents\samples\tutorial\api\Mxd_asm.sldasm.
 //
 // Postconditions:
 // 1. Creates study, Static_Mixed6.
 // 2. Inspect the Immediate window for the remote load settings and
 //    analysis results.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using System.Runtime.InteropServices;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.cosworks;
 namespace AddRemoteLoad_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 Part = default(ModelDoc2);
             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback CWAddinCallBack = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWSolidManager SolidMgr = default(CWSolidManager);
             CWSolidComponent SolidComp = default(CWSolidComponent);
             CWSolidBody SolidBody = default(CWSolidBody);
             CWShellManager ShellMgr = default(CWShellManager);
             CWMaterial ShellMat = default(CWMaterial);
             CWLoadsAndRestraintsManager LBCMgr = default(CWLoadsAndRestraintsManager);
             CWContactManager CWContactMgr = default(CWContactManager);
             CWResults CWFeatObj = default(CWResults);
             CWStaticStudyOptions StaticOptions = default(CWStaticStudyOptions);
             int errCode = 0;
             int intStatus;
             object pDisp3 = null;
             object[] DispArray1 = new object[1];
             object[] DispArray2 = new object[1];
             object[] DispArray3 = new object[1];
             object[] DispArray4 = new object[1];
             object[] DispArray5 = new object[1];
             object[] Disp = null;
             object[] Stress = null;

             const double MeshEleSize = 4.48279654351123;
             //mm
             const double MeshTol = 0.224139827175561;
             //mm
             const double Tol1 = 0.05;
             //5%

             const double URESMax = 0.488;
             //mm
             const double VONMax = 93.8;
             //MPa

             Hashtable PIDCollection = new Hashtable();
             PIDCollection = PIDInitializer();

             Part = (ModelDoc2)swApp.ActiveDoc;

             string strMaterialLib = null;
             strMaterialLib = swApp.GetExecutablePath() +  "\\lang\\english\\sldmaterials\\solidworks materials.sldmat";

             DispArray1[0] = new DispatchWrapper(SelectByPID(Part, "selection1", PIDCollection));
             DispArray2[0] = new DispatchWrapper(SelectByPID(Part, "selection2", PIDCollection));
             DispArray3[0] = new DispatchWrapper(SelectByPID(Part, "selection1", PIDCollection));
             DispArray4[0] = new DispatchWrapper(SelectByPID(Part, "selection4", PIDCollection));
             DispArray5[0] = new DispatchWrapper(SelectByPID(Part, "selection5", PIDCollection));

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (CWAddinCallBack == null)
                 ErrorMsg(swApp, "CWAddinCallBack object not found");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "COSMOSWORKS object not found");

             //Get active document
             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "Failed to get active document");

             //Create new static study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "Failed to get CWStudyManager object");
             Study = StudyMngr.CreateNewStudy3("Static_Mixed6", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeStatic, 0, out errCode);
             if (Study == null)
                 ErrorMsg(swApp, "Failed to create new study");

             //Add materials
             SolidMgr = Study.SolidManager;
             if (SolidMgr == null)
                 ErrorMsg(swApp, "Failed to get SolidMgr object");
             SolidComp = SolidMgr.GetComponentAt(1,  out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get solid component");
             SolidBody = SolidComp.GetSolidBodyAt(0,  out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get solid body");
             intStatus = SolidBody.SetLibraryMaterial(strMaterialLib,  "AISI 1020");
             if (intStatus != 1)
                 ErrorMsg(swApp, "Failed to apply material");

             //Define shells
             ShellMgr = Study.ShellManager;
             if (ShellMgr == null)
                 ErrorMsg(swApp, "Failed to get CWShellManager object");
             CWShell CWShellObj = default(CWShell);
             CWShellObj = ShellMgr.GetShellAt(0,  out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp,  "Failed to get CWShell object");

             ShellMat = CWShellObj.GetDefaultMaterial();
             if (ShellMat == null)
                 ErrorMsg(swApp, "Failed to get default material for shell");
             ShellMat.MaterialUnits = 0;
             ShellMat.SetPropertyByName("EX", 120000000000.0, 0);
             ShellMat.SetPropertyByName("NUXY", 0.31, 0);
             errCode = CWShellObj.SetShellMaterial(ShellMat);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to apply material");

             CWShellObj.ShellBeginEdit();
             CWShellObj.Formulation = 0;
             CWShellObj.ShellUnit = 0;
             CWShellObj.ShellThickness = 3;
             errCode = CWShellObj.ShellEndEdit();
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create shell");
             CWShellObj = null;

             LBCMgr = Study.LoadsAndRestraintsManager;
             if (LBCMgr == null)
                 ErrorMsg(swApp, "No CWLoadsAndRestraintsManager object");

             //Create normal pressure
             CWPressure CWPressure = default(CWPressure);
             pDisp3 = SelectByPID(Part,  "selection3", PIDCollection);
             CWPressure = LBCMgr.AddPressure(1, (DispArray3), pDisp3,  out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create pressure");
             CWPressure.PressureBeginEdit();
             CWPressure.Unit = 1;
             CWPressure.Value = -12;
             errCode = CWPressure.PressureEndEdit();
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to apply pressure value");
             CWPressure = null;

             //Add fixed restraint
             CWRemoteLoad CWRemoteLoad = default(CWRemoteLoad);
             CWRemoteLoad = LBCMgr.AddRemoteLoad(0, (DispArray2), 0, 1.2, 1.5, 1.6, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create fixed remote load");
             CWRemoteLoad.RemoteLoadBeginEdit();
             CWRemoteLoad.SetLocationValues(4.5, 5.6, 6.7);
             CWRemoteLoad.RemoteLoadEndEdit();

             Debug.Print("Load type as defined in swsRemoteLoadType_e: " + CWRemoteLoad.LoadType);
             Debug.Print("Force unit as defined in swsForceUnit_e: " + CWRemoteLoad.ForceOrTranslationUnit);
             Debug.Print("Location unit as defined in swsLinearUnit_e: " + CWRemoteLoad.LocationUnit);
             Debug.Print("Moment unit as defined in swsMomentUnit_e: " + CWRemoteLoad.MomentOrRotationUnit);

             int binclude = 0;
             int bxvalue = 0;
             double dxvalue = 0;
             int byvalue = 0;
             double dyvalue = 0;
             int bzvalue = 0;
             double dzvalue = 0;
             CWRemoteLoad.GetForceOrTranslationValues2(out binclude, out bxvalue, out dxvalue, out byvalue, out dyvalue, out bzvalue, out dzvalue);
             Debug.Print("Include force in analysis? (-1=yes) " + binclude);
             Debug.Print("x-component of remote force? (-1=yes) " + bxvalue);
             Debug.Print("x-component value: " + dxvalue);
             Debug.Print("y-component of remote force? (-1=yes) " + byvalue);
             Debug.Print("y-component value: " + dyvalue);
             Debug.Print("z-component of remote force? (-1=yes) " + bzvalue);
             Debug.Print("z-component value: " + dzvalue);

             CWRemoteLoad.GetLocationValues(out dxvalue, out dyvalue, out dzvalue);
             Debug.Print("x-component of remote location: " + dxvalue);
             Debug.Print("y-component of remote location: " + dyvalue);
             Debug.Print("z-component of remote location: " + dzvalue);

             CWRemoteLoad.GetMomentOrRotationValues2(out binclude, out bxvalue, out dxvalue, out byvalue, out dyvalue, out bzvalue, out dzvalue);
             Debug.Print("x-component of remote moment? (-1=yes) " + bxvalue);
             Debug.Print("x-component value: " + dxvalue);
             Debug.Print("y-component of remote moment? (-1=yes) " + byvalue);
             Debug.Print("y-component value: " + dyvalue);
             Debug.Print("z-component of remote moment? (-1=yes) " + bzvalue);
             Debug.Print("z-component value: " + dzvalue);

             CWRemoteLoad = null;

             CWContactSet CWContactObj = default(CWContactSet);
             CWContactMgr = Study.ContactManager;
             CWContactObj = CWContactMgr.CreateContactSet(1, (DispArray4), (DispArray5), out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create contact object");
             CWContactObj = null;

             //Meshing
             CWMesh CWMeshObj = default(CWMesh);
             CWMeshObj = Study.Mesh;
             if (CWMeshObj == null)
                 ErrorMsg(swApp, "Failed to create mesh object");
             CWMeshObj.MesherType = 0;
             CWMeshObj.Quality = 0;
             errCode = Study.CreateMesh(0, MeshEleSize, MeshTol);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create mesh");
             CWMeshObj = null;

             //Set solver type to Automatic
             StaticOptions = Study.StaticStudyOptions;
             if (StaticOptions == null)
                 ErrorMsg(swApp, "Failed to get CWStaticStudyOptions object");
             StaticOptions.SolverType = 0;
             StaticOptions.UseSoftSpring = 1;
             StaticOptions.LargeDisplacement = 0;

             //Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode);

             //Get results
             CWFeatObj = Study.Results;
             if (CWFeatObj == null)
                 ErrorMsg(swApp, "Failed to get CWResults object");

             //Get min/max URES displacement
             Disp = (object[])CWFeatObj.GetMinMaxDisplacement(3, 0, null, 0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get displacement result");
             float dblDisp = (float)Disp[3];
             //Compare max resultant disp with URESMax
             if ((dblDisp < (1 - Tol1) * URESMax) | (dblDisp > (1 + Tol1) * URESMax))
             {
                 Debug.Print("URES displacement % error = " + (((dblDisp - URESMax) / URESMax) * 100));
             }

             //Get min/max von Mises stress
             Stress = (object[])CWFeatObj.GetMinMaxStress(9, 0, 0, null, 3, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get stress result");
             float dblStress = (float)Stress[3];
             //Compare max von Mises stress with VONMax
             if ((dblStress < (1 - Tol1) * VONMax) | (dblStress > (1 + Tol1) * VONMax))
             {
                 Debug.Print("VON Mises stress % error = " + (((dblStress - VONMax) / VONMax) * 100));
             }

             CWFeatObj = null;

         }

         public void ErrorMsg(SldWorks SwApp, string Message)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");
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
             return functionReturnValue;
         }

         public Hashtable PIDInitializer()
         {

             Hashtable PIDCollection = new Hashtable();
             string selection1 = null;
             string selection2 = null;
             string selection3 = null;
             string selection4 = null;
             string selection5 = null;

             //Constants
             selection1 =   "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,6,2,0,0,50,1,0,0,120,218,109,81,77,74,195,80,16,254,210,180,85,40,70,11,226,13,4,55,10,117,233,74,104,26,44,40,150,164,238,10,33,38,47,49,146,182,146,164,208,141,208,67,244,26,221,120,5,47,227,41,26,191,105,154,86,161,19,134,247,222,247,51,195,76,6,6,160,3,40,214,197,105,134,55,40,36,252,174,209,193,61,158,48,71,0,23,30,50,140,81,167,234,140,169,109,179,45,174,66,67,11,227,169,229,249,202,86,161,235,11,33,209,100,214,245,242,254,249,189,188,92,245,191,134,213,89,218,206,105,235,77,2,113,58,179,52,236,7,182,250,112,253,146,107,74,73,219,245,229,126,34,186,121,254,252,250,174,252,188,132,12,66,124,91,113,162,76,105,42,88,155,88,215,201,211,120,18,61,120,147,32,81,132,215,69,99,63,210,234,229,202,106,45,136,221,90,184,195,8,67,226,25,114,116,55,227,41,14,235,193,71,138,41,95,35,56,100,60,196,68,92,50,49,23,161,54,171,232,144,27,144,73,201,139,110,95,255,134,158,71,152,100,109,214,254,97,55,153,189,134,42,180,114,201";
             selection1 = selection1 +  ",71,38,245,33,43,204,232,201,241,55,46,152,149,15,219,229,202,88,142,138,198,189,32,82,187,21,53,22,199,59,177,252,21,99,241,31,211,14,96,181,3,152,190,107,253,11,105,183,117,188,0,0,0,0,0,0,0,0";
             selection1 = selection1 +  ",Type=1";

             selection2 =  "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,16,2,0,0,49,1,0,0,120,218,109,81,203,74,195,80,16,61,53,182,10,197,250,64,40,184,23,220,40,212,165,43,161,105,176,96,105,73,234,78,8,241,230,86,170,121,72,122,11,217,8,253,8,127,195,141,191,224,127,53,158,49,173,53,208,11,147,59,57,143,153,204,100,212,2,44,0,197,178,56,244,144,34,194,20,33,46,209,193,45,6,200,153,251,8,48,67,140,93,170,142,24,181,85,156,136,171,168,161,137,56,117,2,165,93,61,241,149,16,114,26,242,176,202,252,253,251,227,252,179,255,53,94,223,165,173,45,182,44,141,189,87,211,75,140,55,207,38,253,208,213,111,190,42,233,134,208,174,175,36,63,96,222,203,205,240,233,69,43,83,66,45,66,124,119,166,145,182,165,175,96,199,196,186,158,201,166,201,243,93,144,132,145,38,188,44,234,155,169,218,15,23,78,115,65,236,218,193,13,30,49,134,230,100,6,221,223,9,53,231,13,160,144,81,63,35,235,145,9,232,83,220,192,128,119,78,133,108,163,67,110,68,38,35,95,234,214,245,175,152,223,195,38,235,178,246,144,221,100,252,29,";
             selection2 = selection2 +  "252,63,236,190,103,179,210,132,21,230,244,153,10,123,198,16,159,181,218,237,169,76,158,132,178,222,202,134,234,139,253,63,237,218,107,45,170,184,252,138,214,22,108,155,118,243,141,63,69,114,115,194,0,0,0,0,0,0,0,0";
             selection2 = selection2 +  ",Type=1";

             selection3 =  "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,246,1,0,0,45,1,0,0,120,218,109,80,203,74,195,80,16,61,109,90,21,138,245,129,80,112,47,184,81,168,75,87,66,211,96,193,210,146,212,157,16,226,205,77,137,230,33,233,45,100,35,228,35,252,13,55,254,130,255,213,120,174,73,212,130,3,195,157,123,30,51,204,204,251,128,1,160,220,148,7,14,82,68,8,225,227,2,67,220,96,138,156,181,11,15,43,196,232,80,117,200,108,213,121,172,93,101,11,61,196,233,216,95,74,91,6,174,208,132,14,45,70,187,170,95,63,223,206,222,39,31,139,230,173,108,3,218,172,44,141,157,103,53,78,148,179,206,130,137,111,203,23,87,84,244,142,166,109,87,232,122,95,79,200,213,236,241,73,10,85,65,125,66,252,91,97,36,77,61,87,99,71,196,70,142,202,194,100,121,235,37,126,36,9,111,202,238,239,86,131,251,115,171,87,16,187,178,112,141,7,44,32,185,153,194,232,123,67,201,125,61,8,100,212,175,200,58,100,60,250,4,47,48,229,155,83,161,175,49,36,55,39,147,145,175,116,77,255,75,214,119,48,201,218,236,61,227,180,63,87,168,131,211,1";
             selection3 = selection3 +  "19,77,118,10,216,97,77,159,218,98,79,153,218,215,174,111,123,162,55,79,124,203,19,114,235,66,221,98,239,71,219,120,141,98,27,239,252,131,25,181,246,11,153,198,113,128,0,0,0,0,0,0,0,0";
             selection3 = selection3 +  ",Type=1";

             selection4 =  "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,242,1,0,0,46,1,0,0,120,218,109,81,65,74,195,80,16,125,209,68,133,98,180,32,222,64,112,163,80,151,174,132,198,96,65,177,36,117,87,8,241,231,39,70,146,84,146,20,186,17,114,8,175,209,141,87,240,50,158,162,241,253,38,105,21,156,48,252,255,223,155,55,195,188,140,77,96,23,64,189,170,143,10,188,64,34,225,119,129,1,110,240,128,5,2,120,240,81,32,133,206,170,99,166,214,102,95,169,106,13,61,164,179,219,32,146,142,12,61,161,8,21,6,83,223,105,238,239,95,31,103,203,209,231,164,59,27,217,137,146,101,129,237,11,233,206,243,112,20,56,242,205,19,13,183,71,206,118,60,161,238,135,170,110,81,62,62,191,74,81,54,144,73,136,111,59,78,164,165,134,42,172,79,108,232,150,121,156,69,119,126,22,36,146,240,170,54,182,43,45,159,206,237,94,69,236,202,198,53,166,152,16,47,80,98,184,94,79,114,89,31,2,57,102,124,77,225,146,241,17,19,241,200,196,52,66,174,173,24,144,27,147,201,201,171,186,109,255,75,106,238,97,145,117,216,251,155,211,212,238,173,5,1";
             selection4 = selection4 +  "73,101,156,190,111,177,62,100,135,57,53,37,126,199,41,179,211,53,209,45,230,202,40,85,22,111,76,50,170,131,77,185,250,123,102,245,23,211,254,193,244,182,233,15,36,113,114,226,0,0,0,0,0,0,0,0";
             selection4 = selection4 +  ",Type=1";

             selection5 =  "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,16,2,0,0,51,1,0,0,120,218,117,80,203,74,195,80,16,61,125,42,20,227,3,161,224,94,112,163,80,151,174,132,166,193,130,165,37,169,59,33,196,155,27,137,182,169,164,183,144,141,208,143,240,55,220,248,11,254,87,227,25,211,84,43,120,97,114,39,231,49,115,103,70,22,80,3,144,175,242,125,15,51,76,16,35,196,57,58,184,198,0,25,115,31,1,230,152,162,78,213,1,163,178,142,35,113,229,21,180,48,157,57,129,210,174,142,124,37,132,156,166,124,106,69,254,250,249,118,250,222,255,24,151,119,97,107,139,45,157,77,189,103,211,75,140,183,72,163,126,232,234,23,95,21,116,83,104,215,87,146,239,49,239,101,102,248,240,164,149,41,32,139,16,255,157,120,162,109,233,43,216,33,177,174,103,210,56,121,188,9,146,112,162,9,175,242,198,207,84,237,187,51,167,181,36,118,233,224,10,247,24,67,115,50,131,238,247,132,154,243,6,80,72,169,159,147,245,200,4,244,41,110,96,192,59,163,66,182,209,33,55,34,147,146,47,116,101,253,11,230,183,176,201,186,172,61,100,55,25,";
             selection5 = selection5 +  "191,138,223,135,221,119,108,86,138,88,97,65,159,217,98,79,24,226,171,174,119,123,44,147,39,161,172,119,107,67,141,229,238,70,91,122,107,203,109,92,182,111,253,193,42,255,104,235,155,23,124,1,69,120,115,197,0,0,0,0,0,0,0,0";
             selection5 = selection5 +  ",Type=1";

             //Store constants in a collection
             PIDCollection.Add("selection1", selection1);
             PIDCollection.Add("selection2", selection2);
             PIDCollection.Add("selection3", selection3);
             PIDCollection.Add("selection4", selection4);
             PIDCollection.Add("selection5", selection5);

             return PIDCollection;
         }

         public SldWorks swApp;

     }

 }
```
