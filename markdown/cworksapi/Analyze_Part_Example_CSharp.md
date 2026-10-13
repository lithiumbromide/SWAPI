---
title: "Analyze Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Analyze_Part_Example_CSharp.htm"
---

# Analyze Part Example (C#)

This example shows how to perform a static analysis of a part and plot nodal strain results.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
 //--------------------------------------------------------------------------
 // Preconditions:
 //  1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //     Tools > Add-ins > SOLIDWORKS Simulation > OK).
 //  2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //     (in the IDE, click Project > Add Reference > .NET >
 //     SolidWorks.Interop.cosworks > OK).
 //  3. Modify the path to solidworks materials.sldmat as needed.
 //  4. Ensure that the specified part exists.
 //  5. Open the Immediate window.
 //
 // Postconditions:
 //  1. Adds a default static study results plot.
 //  2. Creates study, Static_solid.
 //  3. Applies a material to the model.
 //  4. Applies restraints and pressure to the selected faces.
 //  5. Creates a mesh.
 //  6. Runs the analysis.
 //  7. Prints strain and stress results to the Immediate window.
 //  8. Creates a nodal equivalent strain plot of the results.
 //  9. Prints plot data to the Immediate window.
 // 10. Hides fixture and force symbols. Examine the graphics area
 //     to verify.
 // 11. Press F5 to continue.
 // 12. Shows fixture and force symbols. Examine the graphics area
 //     to verify.
 // 13. Inspect the plots.
  //
 // NOTE: Because this model is used elsewhere, do not save any changes.
 //-------------------------------------------------------------------------
```

```vb
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.cosworks;
 using System;
 using System.Diagnostics;
 using System.Runtime.InteropServices;

 namespace AnalyzePartCSharp.csproj
{

    partial class SolidWorksMacro
    {
        public void Main()
        {
            CosmosWorks COSMOSWORKS = default(CosmosWorks);
            CwAddincallback CWObject = default(CwAddincallback);
            CWModelDoc ActDoc = default(CWModelDoc);
            CWStudyManager StudyMngr = default(CWStudyManager);
            CWStudy Study = default(CWStudy);
            CWSolidManager SolidMgr = default(CWSolidManager);
            CWSolidComponent SolidComponent = default(CWSolidComponent);
            CWSolidBody SolidBody = default(CWSolidBody);
            CWMesh CwMesh = default(CWMesh);
            CWResults CWResult = default(CWResults);
            object stress = null;
            ModelDoc2 Part = default(ModelDoc2);
            CWLoadsAndRestraintsManager LBCMgr = default(CWLoadsAndRestraintsManager);
            CWPressure CWPressure = default(CWPressure);
            CWRestraint CWRes1 = default(CWRestraint);
            object pointer1 = null;
            object pointer2 = null;
            object pointer3 = null;
             object pointer4 = null;
            CWMaterial CWMat = default(CWMaterial);
            byte[] var1 = null;
            byte[] var2 = null;
            byte[] var3 = null;
             byte[] var4 = null;
            int returnValue = 0;
            string selection1 = null;
            string selection2 = null;
            string selection3 = null;
             string selection4 = null;
            int status = 0;
            int warnings = 0;
            int errCode = 0;
            int NSource = 0;
            double el = 0;
            double tl = 0;
             int errorCode = 0;
             object[] results = null;
             CWPlot plot = default(CWPlot);
             string plotName = "";
             int i = 0;
             Entity[] entity = new Entity[1];
             int nType = 0;
             int nBase = 0;
             int nContour = 0;
             bool BFlip = false;
             bool BSpecifyColorLimit = false;
             object VarColor = null;
             object[] vDispOptions = null;
             object[] vPlotPosFormatOptions = null;
             object[] vPlotSettings = null;
             string Name = "";
             object Color = null;
              object[] Var;
             object oSelect2 = null;
             bool boolstatus = false;

            // Open SOLIDWORKS part document
            Part = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\Tutor1.SLDPRT ", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref status, ref warnings);
            if (Part == null) ErrorMsg(swApp, "Failed to open C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\Tutor1.SLDPRT.");

             // Insert a coordinate system
             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.170849242404917, 0.0898492424049175, -0.031, false, 1, null, 0);
             boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.101612421576135, 0.0102144219597449, -0.000303238444132603, true, 2, null, 0);
             boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.16010192941178, 0.0163935978611676, -0.0391019294117427, true, 4, null, 0);
             boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.160121414911089, 0.00991414669255164, -0.0284339843419161, true, 8, null, 0);
             boolstatus = Part.InsertCoordinateSystem(false, false, false);

             selection1 = "233,35,0,0,1,0,0,0,255,254,255,0,0,0,0,0,131,0,0,0";
             StringtoArray(selection1, ref var2);
             oSelect2 = Part.Extension.GetObjectByPersistReference3((var2), out status);

            // Get SOLIDWORKS Simulation object
            CWObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
            if (CWObject == null) ErrorMsg(swApp, "No CwAddincallback object");
            COSMOSWORKS = (CosmosWorks)CWObject.CosmosWorks;
            if (COSMOSWORKS == null) ErrorMsg(swApp, "No CosmosWorks object");

            // Get active document
            ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
            if (ActDoc == null) ErrorMsg(swApp, "No active document");
              // Add default static study results plot
            errCode = ActDoc.AddDefaultStaticStudyPlot((int)swsDefaultStaticResultTypes_e.swsStaticResultElementalStrain, (int)  swsStaticResultElementalStrainComponentTypes_e.swsStaticElementalStrain_ENERGY);

             // Set default plot boundary color
             errCode = ActDoc.SetSimulationOptionDefaultPlotsBoundaryColorInRGB((int)swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_e.swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_ModelOrMesh, 0, 0, 255);
             errCode = ActDoc.SetSimulationOptionDefaultPlotsBoundaryColorInRGB((int)swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_e.swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_TranslucentSingleColor, 255, 0, 0);

             // Get default plot model or mesh boundary color
             object[] colorObj = null;
             colorObj = (object[])ActDoc.GetSimulationOptionDefaultPlotsBoundaryColorInRGB((int)swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_e.swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_ModelOrMesh, out errCode);
             Debug.Print("RGB values for model or mesh:");
             for (i = 0; i <= colorObj.GetUpperBound(0); i++)
             {
                 Debug.Print(colorObj[i].ToString());
             }

             // Create new static study
             StudyMngr = (CWStudyManager)ActDoc.StudyManager;
             if (StudyMngr == null) ErrorMsg(swApp, "No CWStudyManager object");
             Study = (CWStudy)StudyMngr.CreateNewStudy3("Static_solid", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeStatic, (int)swsMeshType_e.swsMeshTypeSolid, out errCode);
             if (Study == null) ErrorMsg(swApp, "No study object");

             // Set material from the SOLIDWORKS material library
             SolidMgr = (CWSolidManager)Study.SolidManager;
             if (SolidMgr == null) ErrorMsg(swApp, "No CWSolidManager object");
             SolidComponent = (CWSolidComponent)SolidMgr.GetComponentAt(0, out errCode);
             if (errCode != 0) ErrorMsg(swApp, "No solid component");
             SolidBody = (CWSolidBody)SolidComponent.GetSolidBodyAt(0, out errCode);
             if (errCode != 0) ErrorMsg(swApp, "No solid body");
             returnValue = SolidBody.SetLibraryMaterial("c:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Ductile Iron (SN)");
             if (returnValue == 0) ErrorMsg(swApp, "No material applied");
             CWMat = (CWMaterial)SolidBody.GetDefaultMaterial();
             NSource = CWMat.Source;

             // Get the PIDs of the faces
             // First two selections are the faces for restraints
             // Third selection is the face where pressure is applied
             // Fourth selection is the direction reference face
             selection1 = "216,14,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,21,0,109,111,76,80,97,116,116,101,114,110,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,84,0,117,0,116,0,111,0,114,0,49,0,123,228,186,50,11,128,255,254,255,62,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,87,0,111,0,114,0,107,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,84,0,117,0,116,0,111,0,114,0,49,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,97,23,28,65,0,0,0,0";
             selection1 = selection1 + ",2,0,1,0,0,0,0,0,0,0,1,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,17,0,0,0,156,231,186,50,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,14,0,0,0,88,231,186,50,3,0,0,0,1,0,0,0,0,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,6,0,0,0,211,228,186,50,1,0,0,0,255,255,255,255,0,0,17,128,0,0,5,128,8,0,6,0,0,0,211,228,186,50,0,0,0,0,255,255,255,255,0,0,0,0,0,0";
             StringtoArray(selection1, ref var1);
             pointer1 = Part.Extension.GetObjectByPersistReference3((var1), out status);

             selection2 = "216,14,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,84,0,117,0,116,0,111,0,114,0,49,0,123,228,186,50,11,128,255,254,255,62,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,87,0,111,0,114,0,107,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,84,0,117,0,116,0,111,0,114,0,49,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,97,23,28,";
             selection2 = selection2 + "65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,1,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,14,0,0,0,88,231,186,50,3,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,6,0,0,0,211,228,186,50,1,0,0,0,255,255,255,255,0,0,14,128,0,0,5,128,8,0,6,0,0,0,211,228,186,50,0,0,0,0,255,255,255,255,0,0,0,0,0,0";
             StringtoArray(selection2, ref var2);
             pointer2 = Part.Extension.GetObjectByPersistReference3((var2), out status);

             selection3 = "216,14,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,8,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,84,0,117,0,116,0,111,0,114,0,49,0,123,228,186,50,11,128,255,254,255,62,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,87,0,111,0,114,0,107,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,84,0,117,0,116,0,111,0,114,0,49,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,97,23,28,65,0,0,0,0,2,0,";
             selection3 = selection3 + "1,0,0,0,0,0,0,0,1,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,11,0,0,0,51,230,186,50,1,0,0,0,255,255,255,255,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,8,0,0,0,218,229,186,50,4,0,0,0,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,31,0,0,0,210,195,223,50,17,128,0,0,5,128,8,0,23,0,0,0,160,192,223,50,14,128,0,0,5,128,8,0,19,0,0,0,181,233,186,50,1,0,0,0,1,0,0,0,2,0,0,0,17,128,0,0,5,128,8,0,31,0,0,0,210,195,223,50,17,128,0,0,5,128,8,0,23,0,0,0,160,192,223,50,14,128,0,0,5,128,8,0,19,0,0,0,181,233,186,50,1,0,0,0,1,0,0,0,1,0,0,0,17,128,0,0,5,128,8,0,31,0,0,0,210,195,223,50,17,128,0,0,5,128,8,0,23,0,0,0,160,192,223,50,14,128,0,0,5,128,8,0,19,0,0,0,181,233,186,50,1,0,0,0,2,0,0,0,3,0,0,0,17,128,0,0,5,128,8,0,31,0,0,0,210,195,223,50,17,128,0,0,5,128,8,0,23,0,0,0,160,192,223,50,14,";
             selection3 = selection3 + "128,0,0,5,128,8,0,19,0,0,0,181,233,186,50,1,0,0,0,2,0,0,0,4,0,0,0,0,0,0,0,0,0";
             StringtoArray(selection3, ref var3);
             pointer3 = Part.Extension.GetObjectByPersistReference3((var3), out status);

             selection4 =  "189,35,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,10,0,0,0,0,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,77,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,116,0,117,0,116,0,111,0,114,0,49,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,6,116,0,117,0,116,0,111,0,114,0,49,0,2,0,0,123,228,186,50,255";
             selection4 = selection4 + ",254,255,0,0,97,23,28,65,1,0,0,0,0,0,0,0,1,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,97,23,28,65,6,0,0,0,211,228,186,50,1,0,0,0,255,255,255,255,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,13,0,0,0,1,231,186,50,1,0,0,0,3,128,0,0,5,128,8,0,8,0,0,0,218,229,186,50,1,0,0,0,255,255,255,255,12,128,0,0,5,128,8,0,6,0,0,0,211,228,186,50,2,0,0,0,12,128,0,0,5,128,8,0,6,0,0,0,211,228,186,50,3,0,0,0,12,128,0,0,5,128,8,0,6,0,0,0,211,228,186,50,4,0,0,0,12,128,0,0,5,128,8,0,6,0,0,0,211,228,186,50,5,0,0,0,12,128,0,0,5,128,8,0,6,0,0,0,211,228,186,50,6,0,0,0,12,128,0,0,5,128,8,0,13,0,0,0,1,231,186,50,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0";
             StringtoArray(selection4, ref var4);
             pointer4 = Part.Extension.GetObjectByPersistReference3((var4), out status);

             object[] varArray1 = { pointer1, pointer2 };
             object[] varArray2 = { pointer3 };

             // Add a restraint that uses reference geometry
             LBCMgr = Study.LoadsAndRestraintsManager;
             if (LBCMgr == null)
                 ErrorMsg(swApp, "No CWLoadsAndRestraintsManager object");
             CWRes1 = LBCMgr.AddRestraint(5, (varArray1), pointer4, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No restraint created");

             CWRes1.RestraintBeginEdit();
             CWRes1.SetTranslationComponentsValues(1, 1, 1, 1, 1, 1);
             errCode = CWRes1.RestraintEndEdit();

             Debug.Print("Coordinate system type as defined in swsCoordinateType_e: " + CWRes1.GetCoordinateType());
             Debug.Print("Restraint type as defined in swsRestraintType_e: " + CWRes1.RestraintType);
             Debug.Print("Units of translation as defined in swsLinearUnit_e: " + CWRes1.Unit);

             int bval1 = 0;
             int bval2 = 0;
             int bval3 = 0;
             int brev1 = 0;
             int brev2 = 0;
             int brev3 = 0;
             int brev4 = 0;
             int brev5 = 0;
             int brev6 = 0;
             double dval1 = 0;
             double dval2 = 0;
             double dval3 = 0;

             CWRes1.GetReverseDirections(out brev1, out brev2, out brev3, out brev4, out brev5, out brev6);
             CWRes1.GetTranslationComponentsValues(out bval1, out bval2, out bval3, out dval1, out dval2, out dval3);

             if (bval1 == 1)
             {
                 Debug.Print(" Translation along plane direction 1: " + dval1);
                 Debug.Print("      Reverse? (1=yes, 0=no): " + brev4);
             }
             if (bval2 == 1)
             {
                 Debug.Print(" Translation along plane direction 2: " + dval2);
                 Debug.Print("      Reverse? (1=yes, 0=no): " + brev5);
             }
             if (bval3 == 1)
             {
                 Debug.Print(" Translation along direction normal to the plane: " + dval3);
                 Debug.Print("      Reverse? (1=yes, 0=no): " + brev6);
             }

             // Apply a nonuniform pressure normal to the selected face
             CWPressure = LBCMgr.AddPressure(0, (varArray2), null, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No CWPressure object");
             CWPressure.PressureBeginEdit();
             CWPressure.Unit = 1;
             CWPressure.Value = 1000;
             CWPressure.IncludeNonUniformDistribution = 1;
             CWPressure.SetCoordinateSystem(oSelect2);
             CWPressure.CoordSystemType = (int)swsCoordinateType_e.swsCoordinateTypeCartesian;
             CWPressure.Equation = ".4*\"x\" + .8* \"y\" + .6* \"z\"";
             errCode = CWPressure.PressureEndEdit();
             if (errCode != 0)
                 ErrorMsg(swApp, "Pressure not set with error code as defined in swsPressureEndEditError_e: " + errCode);
             Debug.Print("Pressure type as defined in swsPressureType_e: " + CWPressure.PressureType);
             Debug.Print("Pressure: " + CWPressure.Value);
             Debug.Print("  Reverse direction? (true=yes, false=no) " + CWPressure.ReverseDirection2);
             Debug.Print("  Include nonuniform distribution of pressure? (1=yes, 0=no) " + CWPressure.IncludeNonUniformDistribution);

             if (CWPressure.IncludeNonUniformDistribution == 1)
             {
                 Debug.Print("  Equation: " + CWPressure.Equation);
                 Debug.Print("  Coordinate system type as defined in swsCoordinateType_e: " + CWPressure.CoordSystemType);
                 if (CWPressure.CoordSystemType == 1)
                 {
                     Debug.Print("  Equation linear units as defined in swsLinearUnit_e: " + CWPressure.EquationLinearUnit);
                 }
                 if (CWPressure.CoordSystemType == 2 | CWPressure.CoordSystemType == 3)
                 {
                     Debug.Print("  Equation angular units as defined in " + CWPressure.EquationAngularUnit);
                 }
             }

             // Mesh
             CwMesh = (CWMesh)Study.Mesh;
             if (CwMesh == null) ErrorMsg(swApp, "No mesh object");
             CwMesh.Quality = 1;
             CwMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
             errCode = Study.CreateMesh(0, el, tl);
             if (errCode != 0) ErrorMsg(swApp, "Mesh failed");

             // Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0) ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode);
             CWResult = (CWResults)Study.Results;
             if (CWResult == null) ErrorMsg(swApp, "No CWResults object");
             stress = CWResult.GetMinMaxStress(0, 0, 1, null, 0, out errCode);

             // Get strain and stress values for
             // first face selected for restraint
             DispatchWrapper[] dispWrapper = new DispatchWrapper[1];
             dispWrapper[0] = new DispatchWrapper((Entity)pointer1);
             string resultsString = null;

             Debug.Print("  Strain value by node:");
             results = (object[])CWResult.GetStrainForEntities3(true, (int)swsStrainComponent_e.swsStrainComponentESTRN, 1, null, dispWrapper, status, 0, false, out errCode);
             for (i = 0; i < results.Length; i++)
             {
                 resultsString = Convert.ToString(results[i]);
                 Debug.Print("    " + resultsString);
             }

             Debug.Print(" ");
             Debug.Print("  Stress value by node:");
             results = (object[])CWResult.GetStressForEntities3(true, (int)swsStressComponent_e.swsStressComponentVON, 1, null, dispWrapper, (int)swsStrengthUnit_e.swsStrengthUnitPascal, status, 0, false, out errCode);
             for (i = 0; i < results.Length; i++)
             {
                 resultsString = Convert.ToString(results[i]);
                 Debug.Print("    " + resultsString);
             }
```

```vb
// Create a nodal equivalent strain plot
```

plot = CWResult.**CreatePlot**(3, (int)swsStaticResultNodalStrainComponentTypes_e.swsStaticNodalStrain_ESTRN, (int)swsUnit_e.swsUnitSI, false, out errorCode);
errorCode = plot.**ActivatePlot**();
errorCode = plot.**GetPlotName**(out plotName);
errorCode = plot.**ApplyNameViewOrientation**("*Front");
results = (object[])plot.**GetMinMaxResultValues**(out errorCode);
errorCode = plot.**SetPlotTitle**("Nodal Equivalent Strain");
plot.**SetFOSPlot**(false);
plot.**Set2DPlanarRevolveAngle**(0.0);
plot.**SetNormalizeModeShape**(false);
plot.**ShowAs3DPlot**(true);
plot.**ShowTensorOrVector**(false);
plot.**ShowShellin3D**(false);
plot.**ShowNormalizeValuesFrom0To1**(true);
errorCode = plot.**ShowDeformedPlot**(true, (int)swsDeformType_e.swsAutomatic, 0.0, true);
plot.**ShowBeamProfile**(false);
plot.**ShowAvgResultsAcrossBoundaryForParts**(false

);

Debug.Print("Result plot created: " + plotName);
Debug.Print("Node " + results[0] + " " + "has minimum strain value: " + results[1]);
Debug.Print("Node " + results[2] + " " + "has maximum strain value: "

+ results[3]);

Debug.Print("Number of plots for these results: " + CWResult.**GetPlotCount**());
foreach (string Name_loopVariable in (string

[])CWResult.**GetPlotNames**())
{

```vb
    Name = Name_loopVariable;
```

Debug.Print("");
Debug.Print("Plot: " + Name);
errorCode = CWResult.**GetPlotColorOptions**(Name, out nType, out nBase, out nContour, out BFlip, out BSpecifyColorLimit, out VarColor);
Debug.Print("Plot color options:");
Debug.Print(" Color map as defined in swsColorChartOptionLegendTypeValue_e: " + nType);
Debug.Print(" Number of base colors in color map: " + nBase);
Debug.Print(" Number of gradient colors in color map: " + nContour);
Debug.Print(" Reverse the color mapping? " + BFlip);
Debug.Print(" Specify a color for values above the yield limit? " + BSpecifyColorLimit);
Debug.Print(" Color for values above the yield limit and user-defined colors (RGB): "

);

string rgb = "{";
int rgbInd = 1;
int ind = 1;
object[] ColorObj = (object[])VarColor;
int size = ColorObj.Length;
int[] intColor = new int

[size];

for (i=0; i<size; i++){
intColor[i] = (int

)ColorObj[i];
}

// Create RGB triplet for each color
foreach (int Color_loopVariable in

intColor)
{

```vb
        Color = Color_loopVariable;
```

if (rgbInd < 3){
rgb = rgb + Color + ","

;
rgbInd = rgbInd + 1;
}

else {
rgb = rgb + Color + "}";
rgbInd = 1;
if (!(ind == size)){
rgb = rgb + "{"

;
}
}
ind = ind + 1;
}

Debug.Print(" " + rgb);

```vb
    errorCode = CWResult.GetLegendContourColors(Name, out VarColor);
     Debug.Print("");
     Debug.Print("Legend colors {R,G,B}: ");
     rgb = "{";
     rgbInd = 1;
     ind = 1;
     ColorObj = (object[])VarColor;
     size = ColorObj.Length;
     intColor = new int[size];

     for (i = 0; i < size; i++)
     {
           intColor[i] = (int)ColorObj[i];
     }

     // Create RGB triplet for each color
     foreach (int Color_loopVariable in intColor)
     {

         Color = Color_loopVariable;

         if (rgbInd < 3)
         {
              rgb = rgb + Color + ",";
              rgbInd = rgbInd + 1;
         }

          else
          {
              rgb = rgb + Color + "}";
              rgbInd = 1;
              if (!(ind == size))
              {
                      rgb = rgb + "{";
               }
           }
                     ind = ind + 1;
     }

       Debug.Print(" " + rgb);

     vDispOptions = (object[])CWResult.GetPlotDisplayOptions(Name, out errorCode);
     Debug.Print("");
     Debug.Print("Plot display options:");
     Debug.Print(" Display the minimum value? " + vDispOptions[0]);
     Debug.Print(" Display the maximum value? " + vDispOptions[1]);
     Debug.Print(" Display the plot details? " + vDispOptions[2]);
     Debug.Print(" Display the legend? " + vDispOptions[3]);
     Debug.Print(" Display the minimum/maximum range only for parts? " + vDispOptions[4]);
     Debug.Print(" Allow a user-defined minimum/maximum? " + vDispOptions[5]);
     Debug.Print(" User-defined minimum: " + vDispOptions[6]);
     Debug.Print(" User-defined maximum: " + vDispOptions[7]);
    vPlotPosFormatOptions = (object[])CWResult.GetPlotPositionFormatOptions(Name, out errorCode);
     Debug.Print("");
     Debug.Print("Plot position/format options:");
     Debug.Print(" Percentage of the window width: " + vPlotPosFormatOptions[0]);
     Debug.Print(" Percentage of the window height: " + vPlotPosFormatOptions[1]);
     Debug.Print(" Chart thickness option as defined in swsColorChartWidthOptionValue_e: " + vPlotPosFormatOptions[2]);
     Debug.Print(" Chart number format as defined in swsColorChartNumberFormatOptionValue_e: " + vPlotPosFormatOptions[3]);
     Debug.Print(" Number of decimal places to display: " + vPlotPosFormatOptions[4]);
     Debug.Print(" Display chart numbers with a 1000 comma separator? " + vPlotPosFormatOptions[5]);
     Debug.Print(" Use different number format for small numbers? " + vPlotPosFormatOptions[6]);
     Debug.Print(" Number format for small numbers as defined in swsColorNumberFormatUseDiffNumberFormatOptionValue_e: " + vPlotPosFormatOptions[7]);
    vPlotSettings = (object[])CWResult.GetPlotSettings(Name, out errorCode);
     Debug.Print("");
     Debug.Print("Plot settings:");
     Debug.Print(" Display option for active fringe plot as defined in swsPlotFringeSettingsOptionValue_e: " + vPlotSettings[0]);
     Debug.Print(" Display option for model boundary as defined in swsPlotBoundarySettingsOptionValue_e: " + vPlotSettings[1]);
     Debug.Print(" R value for model/mesh color: " + vPlotSettings[2]);
     Debug.Print(" G value for model/mesh color: " + vPlotSettings[3]);
     Debug.Print(" B value for model/mesh color: " + vPlotSettings[4]);
     Debug.Print(" Superimpose the un-deformed model on the deformed model? " + vPlotSettings[5]);
     Debug.Print(" Deformed plot translucent option as defined in swsPlotDeformedShapeOptionSuperImposeValue_e: " + vPlotSettings[6]);
     Debug.Print(" R value for single translucent color: " + vPlotSettings[7]);
     Debug.Print(" G value for single translucent color: " + vPlotSettings[8]);
     Debug.Print(" B value for single translucent color: " + vPlotSettings[9]);
     Debug.Print(" Color intensity [0,1]: " + vPlotSettings[10]);

      object[] InputVar1 = {true,0,255,0,0,0.75,true,0,0,0,255,0.2};
      errorCode = CWResult.SetPlotSettingsOptionForHiddenAndExcludedBody(Name, InputVar1);

      Var = (object[])CWResult.GetPlotSettingsOptionForHiddenAndExcludedBody(Name, out errorCode);
      Debug.Print("");
      Debug.Print("  Show hidden bodies? (1 = true, 0 = false) " + Var[0]);
      Debug.Print("    Translucent color option as defined in swsPlotShowHiddenBodiesOptionValue_e: " + Var[1]);
      Debug.Print("    R value for single translucent color: " + Var[2]);
      Debug.Print("    G value for single translucent color: " + Var[3]);
      Debug.Print("    B value for single translucent color: " + Var[4]);
      Debug.Print("    Color intensity [0, 1]: " + Var[5]);
      Debug.Print("  Show excluded bodies? (1 = true, 0 = false) " + Var[6]);
      Debug.Print("    Translucent color option as defined in swsPlotShowExcludedBodiesOptionValue_e: " + Var[7]);
      Debug.Print("    R value for single translucent color: " + Var[8]);
      Debug.Print("    G value for single translucent color: " + Var[9]);
      Debug.Print("    B value for single translucent color: " + Var[10]);
      Debug.Print("    Color intensity [0, 1]: " + Var[11]);

 }

             // Hide fixture and force symbols
             Study.ShowOrHideFixtures = false;
             Study.ShowOrHideForce = false;

             System.Diagnostics.Debugger.Break();

             // Show fixture and force symbols
             Study.ShowOrHideFixtures = true;
             Study.ShowOrHideForce = true;
         }

         private void ErrorMsg(SldWorks SwApp, string Message)
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
