---
title: "Insert Hatch Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Hatch_Example_CSharp.htm"
---

# Insert Hatch Example (C#)

This example shows how to insert a Hatch in a drawing document.

```vb
 //--------------------------------------------------------------
 // Preconditions:
 // 1. Create a C# Windows console project.
 // 2. Copy and paste this example into the C# IDE.
 // 3. Add a reference to:
 //    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 // 4. Add references to System and System.Windows.Forms.
 // 5. Start DraftSight and open a drawing document.
 // 6. Start debugging the project.
 //
 // Postconditions: A Hatch is inserted in the drawing document
 // and zoomed to fit.
 //----------------------------------------------------------------

 using System;
 using System.Collections.Generic;
 using System.Text;
 using DraftSight.Interop.dsAutomation;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;
 using System.Diagnostics;

 namespace AddHatch
 {
     class Program
     {
         private static DraftSight.Interop.dsAutomation.Application dsApp;

         static void Main(string[] args)
         {
             //Connect to DraftSight application
             dsApp = ConnectToDraftSight();
             if (null == dsApp)
             {
                 return;
             }

             dsApp.AbortRunningCommand();  // abort any command currently running in DraftSight to avoid nested commands

             //Get active document
             Document dsDoc = dsApp.GetActiveDocument();
             if (null == dsDoc)
             {
                 MessageBox.Show("There are no open documents in DraftSight.");
                 return;
             }

             //Get model space
             Model dsModel = dsDoc.GetModel();

             //Get Sketch Manager
             SketchManager dsSketchMgr = dsModel.GetSketchManager();

             //Hatch parameters
             int[] boundaryPointCountArray = new int[] { 4 };
             double[] boundaryPoints = new double[]
             {
                 0, 0,
                 2, 0,
                 2, 2,
                 0, 2,
             };
             string patternName = "ANSI31";
             double patternScale = 1.0;
             double patternAngle = Math.PI / 4; // In radians

             //Insert Hatch
             Hatch dsHatch = dsSketchMgr.InsertHatchByBoundary(boundaryPointCountArray, boundaryPoints, patternName, patternScale, patternAngle);
             if (null != dsHatch)
             {
                 //Change color of Hatch
                 Color dsColor = dsHatch.Color;
                 dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Green);
                 dsHatch.Color = dsColor;

                 //Zoom to fit
                 dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);
             }
             else
             {
                 MessageBox.Show("Hatch entity was not added to the current drawing.");
             }
         }

         private static DraftSight.Interop.dsAutomation.Application ConnectToDraftSight()
         {
             DraftSight.Interop.dsAutomation.Application dsApp = null;

             try
             {
                 //Connect to DraftSight
                 dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
             }
             catch (Exception ex)
             {
                 MessageBox.Show("Failed to connect to DraftSight. Cause: " + ex.Message);
                 dsApp = null;
             }

             return dsApp;
         }
     }
 }
```
