---
title: "Get Linearized Stress Results Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Linearized_Stress_Results_Example_CSharp.htm"
---

# Get Linearized Stress Results Example (C#)

This example shows how to get the stress results that are linearized along Stress Classification Lines for a pressure vessel study.

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 //  1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //     Tools > Add-ins > SOLIDWORKS Simulation > OK).
 //  2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 //     click  Tools > References > SOLIDWORKS Simulation version type library).
 //  3. Open  pubic_documents\Simulation Examples\pressurevessel.sldprt.
 //  4. Open the Immediate window.
 //  5. Mesh Ready-Solids using a curvature-based mesh with a maximum of 10 elements.
 //  6. Analyze Ready-Solids.
 //  7. Create Pressure Vessel Design 1 study, using a linear combination of
 //      Ready-Solids with Factor = 1.
 //  8. Analyze Pressure Vessel Design 1.
 //  9. Create a default von Mises stress plot of the results.
 //
 // Postconditions:
 //  1. Gets the following stress values linearized along Stress Classification Lines
 //     for the specified points on the planar section created by the Top plane:
 //     * Membrane stress
 //     * Bending (Point 1) stress
 //     * Membrane stress + bending (Point 1) stress
 //     * Bending (Point 2) stress
 //     * Membrane stress + Bending (Point 2) stress
 //     * Peak (Point 1)
 //     * Peak (Point 2)
 //  2. Inspect the Immediate window.
 //
 // NOTE: Because the model is used elsewhere, do not save any changes.
 // ---------------------------------------------------------------------------

 using System;
 using System.Diagnostics;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Windows;
 using System.Windows.Forms;

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.cosworks;

 namespace Macro1
 {
       public  partial  class   SolidWorksMacro
      {
            private  ModelDoc2 Part;
            private  CosmosWorks COSMOSWORKS;
            private  CwAddincallback CWObject;
            private  CWModelDoc ActDoc;
            private  CWStudyManager StudyMngr;
            private  CWStudy Study;
            private  CWResults CWResult;
            private  CWPlot CWPlot;
            private  Feature ReferenceGeometryDispatchObj2;
            private  object plotNames;
            private  object[] values;
            private  int errCode;
            private  bool boolCode;
            public  void Main()
           {
              Part = (ModelDoc2)swApp.ActiveDoc;
              CWObject = (CwAddincallback)swApp.GetAddInObject("CosmosWorks.CosmosWorks");
              COSMOSWORKS = CWObject.CosmosWorks;
              ActDoc = COSMOSWORKS.ActiveDoc;
              StudyMngr = ActDoc.StudyManager;
              Study = StudyMngr.GetStudy(4);
              StudyMngr.ActiveStudy = 4;

              CWResult = Study.Results;
              plotNames = CWResult.GetPlotNames();
              boolCode = CWResult.ActivatePlot("Stress1");

              CWPlot = CWResult.GetPlot("Stress1",   out errCode);

              boolCode = Part.Extension.SelectByID2("Top",  "PLANE", 0, 0, 0,   true, 0,   null, 0);
              ReferenceGeometryDispatchObj2 = (Feature)((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);

              values = (object[])CWPlot.GetLinearizedStressValuesAlongSCL(5, 0.29224, -1.08E-19, -0.00034826, 0.30464, -2.17E-19, -0.00054522, ReferenceGeometryDispatchObj2,  out errCode);

               Debug.Print("Linearized normal stresses in the X-direction:");
               Debug.Print("  Membrane:                     " + values[0]);
               Debug.Print("  Bending (Point 1):            " + values[1]);
               Debug.Print("  Membrane + Bending (Point 1): " + values[2]);
               Debug.Print("  Bending (Point 2):            " + values[3]);
               Debug.Print("  Membrane + Bending (Point 2): " + values[4]);
               Debug.Print("  Peak (Point 1):               " + values[5]);
               Debug.Print("  Peak (Point 2):               " + values[6]);
           }

            // The SldWorks swApp variable is pre-assigned for you.
            public  SldWorks swApp;

      }
 }
```
