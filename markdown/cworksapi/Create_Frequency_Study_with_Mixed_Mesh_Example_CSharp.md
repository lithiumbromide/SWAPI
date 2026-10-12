---
title: "Create Frequency Study with Mixed Mesh Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Frequency_Study_with_Mixed_Mesh_Example_CSharp.htm"
---

# Create Frequency Study with Mixed Mesh Example (C#)

This example shows how to create a frequency study using a mixed mesh.

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
 // 4. Ensure that the specified model document exists.
 // 5. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the model.
 // 2. Creates a frequency mixed-mesh study.
 // 3. Applies material.
 // 4. Adds a fixed restraint.
 // 5. Adds a bonded contact set.
 // 6. Creates a mesh.
 // 7. Runs an analysis.
 // 8. Inspect the Immediate window.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 //---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.cosworks;
using System;
using System.Diagnostics;

namespace Macro1.csproj
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
            CWSolidManager SolidMgr = default(CWSolidManager);
            CWSolidComponent SolidComponent = default(CWSolidComponent);
            CWSolidBody SolidBody = default(CWSolidBody);
            CWShell Shell = default(CWShell);
            CWMesh CwMesh = default(CWMesh);
            CWResults CWResult = default(CWResults);
            ModelDoc2 Part = default(ModelDoc2);
            CWShellManager ShellMgr = default(CWShellManager);
            CWLoadsAndRestraintsManager LBCMgr = default(CWLoadsAndRestraintsManager);
            CWContactManager ContactMgr = default(CWContactManager);
            CWContactSet CWContactSet = default(CWContactSet);
            CWRestraint CWRes1 = default(CWRestraint);
            object pDisp1 = null;
            object pDisp2 = null;
            object oselect1 = null;
            object oselect2 = null;
            object oselect3 = null;
            object oselect4 = null;
            object oselect5 = null;
            object oselect6 = null;
            byte[] var1 = null;
            byte[] var2 = null;
            byte[] var3 = null;
            byte[] var4 = null;
            byte[] var5 = null;
            byte[] var6 = null;
            byte[] var8 = null;
            byte[] var9 = null;
            object[] Freq = null;
            string str1 = null;
            string str2 = null;
            string selection1 = null;
            string selection2 = null;
            string selection3 = null;
            string selection4 = null;
            string selection5 = null;
            string selection6 = null;
            int status = 0;
            int warnings = 0;
            int errCode = 0;
            double el = 0;
            double tl = 0;
            int j = 0;

            // Open document
            swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\mixedmesh-1.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref status, ref warnings);
            Part = (ModelDoc2)swApp.ActiveDoc;

            // Get the SOLIDWORKS Simulation object
            COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
            if (COSMOSObject == null) ErrorMsg("COSMOSObject object not found");
            COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
            if (COSMOSWORKS == null) ErrorMsg("COSMOSWORKS object not found");

            // Open and get active document
            ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
            if (ActDoc == null) ErrorMsg("No active document", true);

            // Create new frequency study
            StudyMngr = (CWStudyManager)ActDoc.StudyManager;
            if (StudyMngr == null) ErrorMsg("No CWStudyManager object");
            Study = (CWStudy)StudyMngr.CreateNewStudy3("Frequency_Mixed", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeFrequency, 0, out errCode);
            if (Study == null) ErrorMsg("Frequency study not created");

            // Get selections for restraint
            // Faces of the six holes in the solid
            selection1 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12";
            selection1 = selection1 + "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,16,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0";
            StringtoArray(selection1, ref var1);
            oselect1 = Part.Extension.GetObjectByPersistReference3((var1), out status);
            selection2 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12";
            selection2 = selection2 + "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,15,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0";
            StringtoArray(selection2, ref var2);
            oselect2 = Part.Extension.GetObjectByPersistReference3((var2), out status);
            selection3 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12";
            selection3 = selection3 + "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,14,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0";
            StringtoArray(selection3, ref var3);
            oselect3 = Part.Extension.GetObjectByPersistReference3((var3), out status);
            selection4 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12";
            selection4 = selection4 + "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,11,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,6,0,0,0,0,0,0,0,0,0,0,0,0,0";
            StringtoArray(selection4, ref var4);
            oselect4 = Part.Extension.GetObjectByPersistReference3((var4), out status);
            selection5 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12";
            selection5 = selection5 + "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,12,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,6,0,0,0,0,0,0,0,0,0,0,0,0,0";
            StringtoArray(selection5, ref var5);
            oselect5 = Part.Extension.GetObjectByPersistReference3((var5), out status);
            selection6 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12";
            selection6 = selection6 + "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,13,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,6,0,0,0,0,0,0,0,0,0,0,0,0,0";
            StringtoArray(selection6, ref var6);
            oselect6 = Part.Extension.GetObjectByPersistReference3((var6), out status);

            // Get selections for contact set
            // Shell edge
            str1 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,69,100,103,101,82,101,102,95,99,1,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109";
            str1 = str1 + ",0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,24,0,0,0,26,50,104,66,9,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,10,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,14,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,0,0,0,0,0,0,0,0,0,0,0,0";
            StringtoArray(str1, ref var8);
            pDisp1 = (object)Part.Extension.GetObjectByPersistReference3((var8), out status);
            // Solid face
            str2 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0";
            str2 = str2 + ",112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,24,0,0,0,26,50,104,66,11,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,0,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,10,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0";
            StringtoArray(str2, ref var9);
            pDisp2 = (object)Part.Extension.GetObjectByPersistReference3((var9), out status);

            // Create arrays
            object[] varArray2 = { oselect1, oselect2, oselect3, oselect4, oselect5, oselect6 };
            object[] varArray3 = { pDisp1 };
            object[] varArray4 = { pDisp2 };

            // Add bonded contact set
            ContactMgr = (CWContactManager)Study.ContactManager;
            if (errCode != 0) ErrorMsg("No CWContactManager object");
            CWContactSet = (CWContactSet)ContactMgr.CreateContactSet2((int)swsContactType_e.swsContactTypeBonded, 0, (varArray3), (varArray4), out errCode);
            if (errCode != 0) ErrorMsg("No CWContactSet object");
             Debug.Print(CWContactSet.ContactName + " is suppressed? (1=yes, 0=no) " + CWContactSet.State);

             // If contact set is suppressed, unsuppress it
             if (CWContactSet.State == 1)
                 errCode = ContactMgr.SuppressUnsuppressContactPair(CWContactSet.ContactName, 0);

            // Apply material to shell
            ShellMgr = Study.ShellManager;
            if (ShellMgr == null) ErrorMsg("No CWShellManager object");
            Shell = (CWShell)ShellMgr.GetShellAt(0, out errCode);
            status = Shell.SetLibraryMaterial("c:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Ductile Iron");
            if (status == 0) ErrorMsg("No material applied");

            // Define shell properties
            Shell.ShellBeginEdit();
            Shell.Formulation = 0;
            Shell.ShellUnit = 0;
            Shell.ShellThickness = 5.0;
            errCode = Shell.ShellEndEdit();
            if (errCode != 0) ErrorMsg("Shell not created");

            // Apply material to solid
            SolidMgr = (CWSolidManager)Study.SolidManager;
            if (SolidMgr == null) ErrorMsg("No CWSolidManager object");
            SolidComponent = (CWSolidComponent)SolidMgr.GetComponentAt(1, out errCode);
            if (errCode != 0) ErrorMsg("No solid component");
            SolidBody = (CWSolidBody)SolidComponent.GetSolidBodyAt(0, out errCode);
            if (errCode != 0) ErrorMsg("No solid body");
            status = SolidBody.SetLibraryMaterial2("c:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Ductile Iron");
            if (status == 0) ErrorMsg("No material applied");

            // Add fixed restraint
            LBCMgr = (CWLoadsAndRestraintsManager)Study.LoadsAndRestraintsManager;
            CWRes1 = (CWRestraint)LBCMgr.AddRestraint((int)swsRestraintType_e.swsRestraintTypeFixed, (varArray2), null, out errCode);
            if (errCode != 0) ErrorMsg("No fixed restraint created");

             // Set meshing
            CwMesh = (CWMesh)Study.Mesh;
            if (CwMesh == null) ErrorMsg("No CWMesh object");
            CwMesh.Quality = 1;
            CwMesh.GetDefaultElementSizeAndTolerance((int)swsLinearUnit_e.swsLinearUnitMillimeters, out el, out tl);
            errCode = Study.CreateMesh((int)swsLinearUnit_e.swsLinearUnitMillimeters, el, tl);
            if (errCode != 0) ErrorMsg("Mesh failed");

            // Run analysis
            errCode = Study.RunAnalysis();
            if (errCode != 0) ErrorMsg("Analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode);

            // Get results
            CWResult = (CWResults)Study.Results;
            if (CWResult == null) ErrorMsg("No CWResults object");
            Freq = CWResult.GetResonantFrequencies(out errCode);
            if (errCode != 0) ErrorMsg("No frequency result");
             Debug.Print("Resonant frequencies:");
            for (j = 0; j < Freq.Length; j++)
                {
                Debug.Print (Freq[j].ToString());
                }
        }

        private void ErrorMsg(string Message)
        {
            swApp.SendMsgToUser2(Message, 0, 0);
            swApp.RecordLine("'*** WARNING - General");
            swApp.RecordLine("'*** " + Message);
            swApp.RecordLine("");

        }

        private void StringtoArray(string inputSTR, ref byte[] varEntity)
        {
            string[] PIDArray = null;
            byte[] PID = null;
            int i;
            // Parse string into an array
            PIDArray = inputSTR.Split(new char[] { ',' });
            //Convert string array to byte array
            int sizeArray = PIDArray.Length;
            PID = new byte[sizeArray];
            for (i = 0; i < PIDArray.Length; i++)
            {
                PID[i] = Convert.ToByte(PIDArray[i]);
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
