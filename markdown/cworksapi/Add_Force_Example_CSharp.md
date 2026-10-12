---
title: "Add Nonuniform Force Distribution Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Force_Example_CSharp.htm"
---

# Add Nonuniform Force Distribution Example (C#)

This example shows how to add a force of nonuniform distribution to a study.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Verify that the assembly exists.
 // 4. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the assembly.
 // 2. Inserts a coordinate system.
 // 3. Gets the Ready study.
 // 4. Adds a force of nonuniform distribution to Ready.
 // 5. Inspect the Immediate window.
 //
  // NOTE: Because this assembly document is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using SolidWorks.Interop.cosworks;
 using System.Diagnostics;
 using System.Collections;

 namespace AddForce_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {

             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback COSMOSObject = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             CWLoadsAndRestraintsManager LBCMgr = default(CWLoadsAndRestraintsManager);
             CWForce CWForce = default(CWForce);

             byte[] var1 = null;
             byte[] var2 = null;

             object oSelect1 = null;
             object oSelect2 = null;

             int status = 0;
             int warnings = 0;
             int errCode = 0;

             ArrayList PIDCollection = new ArrayList();
             bool boolstatus = false;

             object DistanceValues = null;
             object ForceValues = null;

             //Initialize PIDs
             PIDCollection = PIDInitializer();

             // Open document
             swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\mixedmesh-1.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref status, ref warnings);

             swModel = (ModelDoc2)swApp.ActiveDoc;

             swModelDocExt = (ModelDocExtension)swModel.Extension;

             // Insert a coordinate system
             boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.019197250673983, 0.167840898512935, -0.0353306093604147, false, 1, null, 0);
             boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.0180650048999951, 0.166100889103177, 0.123043418741133, true, 2, null, 0);
             boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.0476117249541517, 0.243477752733071, -0.0418878531492055, true, 4, null, 0);
             boolstatus = swModelDocExt.SelectByID2("", "EDGE", -0.0821419006116457, 0.165357357368464, -0.0411028452107871, true, 8, null, 0);
             boolstatus = swModel.InsertCoordinateSystem(false, false, false);

             // Get PIDs for the coordinate system object
             SelectByPID(1, PIDCollection, ref var2);
             oSelect2 = swModelDocExt.GetObjectByPersistReference3((var2), out status);

             // Get the SOLIDWORKS Simulation object
             COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (COSMOSObject == null) ErrorMsg(swApp, "COSMOSObject object not found");

             COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
             if (COSMOSWORKS == null) ErrorMsg(swApp, "COSMOSWORKS object not found");

             // Open and get active document
             ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
             if (ActDoc == null) ErrorMsg(swApp, "No active document");

             // Get the Ready study
             StudyMngr = (CWStudyManager)ActDoc.StudyManager;

             if (StudyMngr == null) ErrorMsg(swApp, "No CWStudyManager object");

             Study = StudyMngr.GetStudy(0);
             if (Study == null)
                 ErrorMsg(swApp, "No study found");

             // Get PIDs for the face to which the force is applied
             SelectByPID(0, PIDCollection, ref var1);
             oSelect1 = (object)swModelDocExt.GetObjectByPersistReference3((var1), out status);
             object[] DispArray1 = { oSelect1 };

             LBCMgr = (CWLoadsAndRestraintsManager)Study.LoadsAndRestraintsManager;
             double[] ComponentValues = {2.0, 3.0, 1.0, 1.5, 1.0, 1.0, 1.0};

             // Add force
             CWForce = LBCMgr.AddForce3((int)swsForceType_e.swsForceTypeNormal, 0, -1, 0, 0, 0, (DistanceValues), (ForceValues), true, false, 0, 0, 0, 1.0, (ComponentValues), false, false, (DispArray1), null, false, out errCode);
             if (errCode != 0)
                     ErrorMsg(swApp, "No force applied");

             // Edit force to be of nonuniform distribution
             CWForce.ForceBeginEdit();
             CWForce.IncludeNonUniformDistribution = 1;
             CWForce.SetCoordinateSystem(oSelect2);
             CWForce.EquationCoordinateSystemType = 1;
             CWForce.EquationLinearUnit = 0;
             CWForce.Equation = "\"x\" + \"y\" + \"z\"";
             CWForce.ForceEndEdit();

             Debug.Print("Force:");
             Debug.Print("  Type as defined in swsForceType_e: " + CWForce.ForceType);
             Debug.Print("  Units as defined in swsForceUnit_e: " + CWForce.Unit);
             Debug.Print("  Value: " + CWForce.NormalForceOrTorqueValue);
             Debug.Print("  Nonuniform distribution? (1=yes, 0=no) " + CWForce.IncludeNonUniformDistribution);
             if (CWForce.IncludeNonUniformDistribution == 1)
             {
                 Debug.Print("  Coordinate system type as defined in swsCoordinateType_e: " + CWForce.EquationCoordinateSystemType);
                 Debug.Print("  Equation linear units as defined in swsLinearUnit_e: " + CWForce.EquationLinearUnit);
                 if (CWForce.EquationCoordinateSystemType == 2 | CWForce.EquationCoordinateSystemType == 3)
                 {
                     Debug.Print("  Equation angular units as defined in " + CWForce.EquationAngularUnit);
                 }
                 if (string.IsNullOrEmpty(CWForce.Equation))
                 {
                     Debug.Print("  Nonuniform force distribution equation not set.");
                 }
                 else
                 {
                     Debug.Print("  Nonuniform force distribution equation: " + CWForce.Equation);
                 }
             }

         }

         private void ErrorMsg(SldWorks SwApp, string Message)
         {

             swApp.SendMsgToUser2(Message, 0, 0);
             swApp.RecordLine("'*** WARNING - General");
             swApp.RecordLine("'*** " + Message);
             swApp.RecordLine("");

         }

         public ArrayList PIDInitializer()
         {

             // Initialize PIDs
             ArrayList PIDCollection = new ArrayList();

             string selection1 = null;
             string selection2 = null;

            // Face
             selection1 = "13,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,";
             selection1 = selection1 + "0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,24,0,0,0,26,50,104,66,4,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,0,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,11,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,0,0,0,0,0,0";

             // Coordinate System
             selection2 = "189,35,0,0,1,0,0,0,255,254,255,0,0,0,0,0,124,0,0,0";

             // Store constants in an array
             PIDCollection.Add(selection1);
             PIDCollection.Add(selection2);

             return PIDCollection;

         }

         private void SelectByPID(int indx, ArrayList PIDCollection, ref byte[] varEntity)
         {

             // Select by PID
             byte[] PID = null;
             string[] PIDVariant = null;
             string PIDString = null;
             int i = 0;

             // Get the string from the collection
             PIDString = "";
             PIDString = (string)PIDCollection[indx];

             // Parse the string into an array
             PIDVariant = PIDString.Split(new char[] { ',' });

             // Change the string array to a byte array
             int sizeArray = PIDVariant.Length;
             PID = new byte[sizeArray];

             for (i = 0; i < PIDVariant.Length - 1; i++)
             {
                 PID[i] = Convert.ToByte(PIDVariant[i]);
             }

             varEntity = PID;

         }

         /// <summary>

         /// The SldWorks swApp variable is pre-assigned for you.

         /// </summary>

         public SldWorks swApp;

     }

 }
```
