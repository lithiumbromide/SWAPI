---
title: "Get Frequencies in Mode Shape Plots Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Frequencies_in_Mode_Shape_Plots_Example_CSharp.htm"
---

# Get Frequencies in Mode Shape Plots Example (C#)

This example shows how to get frequencies for all mode shapes in amplitude plots.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that the specified model exists.
 //
 // Postconditions:
 // 1. Meshes the model.
 // 2. Analyzes the study.
  // 3. Gets the frequencies of all amplitude plot mode shapes.
  // 4. Displays a message box with the frequency for mode shape 2.
 // 5. Click OK.
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
 using System.Windows.Forms;
 namespace GetFreqOrTime_CSharp.csproj
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
         CWMesh mesh;
         int errorCode;
         int longstatus;
         int longwarnings;
         object[] TimeorFrequency;

         int ModeShapeNumber;

         const double MeshEleSize = 47.9; //mm
         const double MeshTol = 2.39; //mm

         public void Main()
         {
             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\Dynamics\\ac_unit.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, 1, "", ref longstatus, ref longwarnings);

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("CosmosWorks.CosmosWorks");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             ActDoc = COSMOSWORKS.ActiveDoc;
             StudyMngr = ActDoc.StudyManager;
             StudyMngr.ActiveStudy = 0;
             Study = StudyMngr.GetStudy(0);

             mesh = Study.Mesh;
             mesh.MesherType = 0;
             mesh.Quality = 0;
             errorCode = Study.CreateMesh(0, MeshEleSize, MeshTol);

             errorCode = Study.RunAnalysis();
             CWResult = Study.Results;

             ModeShapeNumber = 2;
             TimeorFrequency = (object[])CWResult.GetTimeOrFrequencyAtEachStep2(0, out errorCode);
             MessageBox.Show("Frequency for mode shape 2: " + TimeorFrequency[ModeShapeNumber - 1]);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```
