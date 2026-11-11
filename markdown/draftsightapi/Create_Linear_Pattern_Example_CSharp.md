---
title: "Create Linear Pattern Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Linear_Pattern_Example_CSharp.htm"
---

# Create Linear Pattern Example (C#)

This example shows how to to create a linear pattern.

```
//-------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add references to System and System.Windows.Forms.
// 5. Start DraftSight and open a document.
// 6. Click Start Debugging.
//
// Postconditions:
// 1. Draws a Circle.
// 2. Draws a 2D PolyLine.
// 3. Creates a linear pattern using the Circle and 2D PolyLine
//    entities.
// 4. Zooms the drawing to fit.
// 5. Examine the drawing.
//------------------------------------------------------------
```

```vb
using System;
 using System.Collections.Generic;
 using System.Text;
 using DraftSight.Interop.dsAutomation;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;

 namespace PatternLinear
 {
     class Program
     {
         private static DraftSight.Interop.dsAutomation.Application dsApp;

         static void Main(string[] args)
         {
             //Connect to DraftSight application
             dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
             dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands

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

             //Draw a Circle
             double[] centerPoint = new double[] { 5, 5, 0 };
             double radius = 3;
             Circle dsCircle = dsSketchMgr.InsertCircle(centerPoint[0], centerPoint[1], centerPoint[2], radius);

             //Draw a 2D PolyLine
             double[] coordinatesArray = new double[]
             {
                 10, 4,
                 10, 6,
                 14, 6,
                 14, 4
             };
             bool closed = true;
             PolyLine dsPolyLine = dsSketchMgr.InsertPolyline2D(coordinatesArray, closed);

             //Linear pattern parameters
             int numberElementsOnVerticalAxis = 4;
             int numberElementsOnHorizontalAxis = 5;
             double spacingOnVerticalAxis = 20;
             double spacingOnHorizontalAxis = 40;
             double patternAngle = Math.PI / 4; //In radians

             //Prepare list of entity types
             int[] dsEntityTypes = new int[]
             {
                 (int)dsObjectType_e.dsCircleType,
                 (int)dsObjectType_e.dsPolyLineType
             };

             //Prepare list of entities
             DispatchWrapper[] dsEntities = new DispatchWrapper[]
             {
                 new DispatchWrapper(dsCircle),
                 new DispatchWrapper(dsPolyLine)
             };

             //Create linear pattern
             dsSketchMgr.PatternLinear(numberElementsOnVerticalAxis, numberElementsOnHorizontalAxis,
                                       spacingOnVerticalAxis, spacingOnHorizontalAxis, patternAngle,
                                       dsEntityTypes, dsEntities);

             //Zoom to fit
             dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);
         }
     }
 }
```
