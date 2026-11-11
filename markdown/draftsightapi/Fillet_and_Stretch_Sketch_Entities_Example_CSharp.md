---
title: "Fillet and Stretch Sketch Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Fillet_and_Stretch_Sketch_Entities_Example_CSharp.htm"
---

# Fillet and Stretch Sketch Entities Example (C#)

This example shows how to fillet and stretch sketch entities.

```vb
 //--------------------------------------------------------------
 //Preconditions:
 // 1. Create a C# Windows console project.
 // 2. Copy and paste this project into the C# IDE.
 // 3. Add a reference to:
 //    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.
 // 4. Add references to System and System.Windows.Forms.
 // 5. Start DraftSight and open a new drawing.
 // 6. Run the macro.
 //
 //Postconditions:
 //1. Two sets of sketch entities are created.
 //2. One set of sketch entities is filleted.
 //3. The other set of sketch entities is stretched.
 //----------------------------------------------------------------
 using System;
 using System.Collections.Generic;
 using System.Text;
 using DraftSight;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;

 namespace ModifyEntities
 {
     class Program
     {
         private static DraftSight.Application dsApp;
         private static DraftSight.Document dsDoc;

         static void Main(string[] args)
         {
             //Connect to DraftSight application
             dsApp = ConnectToDraftSight();
             if (null == dsApp)
             {
                 return;
             }

             dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands

             //Get active document
             dsDoc = dsApp.GetActiveDocument();
             if (null == dsDoc)
             {
                 MessageBox.Show("There are no opened documents in DraftSight.");
                 return;
             }

             //Get model space
             Model dsModel = dsDoc.GetModel();

             //Get sketch manager
             SketchManager dsSketchMgr = dsModel.GetSketchManager();

             //Fillet entities
             FilletEntities(dsSketchMgr);

             //Stretch entities
             StretchEntities(dsSketchMgr);
         }

         private static void StretchEntities(SketchManager dsSketchMgr)
         {
             //Stretch parameters
             double displacementX = 4;
             double displacementY = 6;
             double displacementZ = 0;
             DispatchWrapper[] dsEntities;
             double[] crossingBoxStartCorner;
             double[] crossingBoxEndCorner;

             //Prepare entities for stretch
             DrawEntitiesForStretch(dsSketchMgr, out dsEntities, out crossingBoxStartCorner, out crossingBoxEndCorner);

             //Zoom extents
             dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);

             MessageBox.Show("Entities before STRETCH.");

             //Stretch entities
             dsSketchMgr.StretchEntities(displacementX, displacementY, displacementZ, dsEntities,
                                         crossingBoxStartCorner, crossingBoxEndCorner);

             //Zoom extents
             dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);

             MessageBox.Show("Entities after STRETCH.");
         }

         private static void DrawEntitiesForStretch(SketchManager dsSketchMgr, out DispatchWrapper[] dsEntities,
                                                     out  double[] crossingBoxStartCorner, out double[] crossingBoxEndCorner)
         {
             //Initialize output entities array
             int entitiesIndex = 0;
             int entitiesCount = 3;
             dsEntities = new DispatchWrapper[entitiesCount];

             //Draw polyline
             bool closed = true;
             double[] coordinates = { 1, 1, 3, 1, 3, 3, 1, 3 };
             PolyLine dsPolyline = dsSketchMgr.InsertPolyline2D(coordinates, closed);

             //Add polyline to output array of entities
             dsEntities[entitiesIndex++] = new  DispatchWrapper(dsPolyline);

             //Draw line
             double[] startPoint = { 4, 1, 0 };
             double[] endPoint = { 4, 5, 0 };
             Line dsLine = dsSketchMgr.InsertLine(startPoint[0], startPoint[1], startPoint[2],
                                                  endPoint[0], endPoint[1], endPoint[2]);

             //Add line to output array of entities
             dsEntities[entitiesIndex++] = new  DispatchWrapper(dsLine);

             //Draw circle
             double radius = 1;
             double[] centerPoint = { 6, 2, 0 };
             Circle dsCircle = dsSketchMgr.InsertCircle(centerPoint[0], centerPoint[1], centerPoint[2], radius);

             //Add circle to output array of entities
             dsEntities[entitiesIndex++] = new  DispatchWrapper(dsCircle);

             //Specify crossing coordinates
             crossingBoxStartCorner =  new  double[] { 0.6, 2, 0 };
             crossingBoxEndCorner = new double[] { 8, 6, 0 };
         }

         private static void FilletEntities(SketchManager dsSketchMgr)
         {
             double[] firstPointOnEntityDblArray;
             DispatchWrapper[] firstEntityArray;
             double[] secondPointOnEntityDblArray;
             DispatchWrapper[] secondEntityArray;

             //Prepare entities for fillet
             DrawEntitiesForFillet(dsSketchMgr, out firstPointOnEntityDblArray, out firstEntityArray,
                                   out secondPointOnEntityDblArray, out secondEntityArray);

             //Zoom extents
             dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);

             MessageBox.Show("Entities before FILLET.");

             //Set fillet radius
             double filletRadius = 1.5;
             SetFilletRadius(dsDoc, filletRadius);

             //Do fillet entities
             dsSketchMgr.FilletEntities(firstPointOnEntityDblArray, firstEntityArray,
                                        secondPointOnEntityDblArray, secondEntityArray);

             //Zoom extents
             dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);

             MessageBox.Show("Entities after FILLET.");
         }

         private static void DrawEntitiesForFillet(SketchManager dsSketchMgr, out double[] firstPointOnEntityDblArray, out DispatchWrapper[] firstEntityArray, out double[] secondPointOnEntityDblArray, out DispatchWrapper[] secondEntityArray)
         {
             //Count of entity pairs to fillet
             int count = 3;

             //Initialize output arrays
             firstPointOnEntityDblArray = new  double[count*3];
             firstEntityArray = new DispatchWrapper[count];
             secondPointOnEntityDblArray =  new double[count*3];
             secondEntityArray = new DispatchWrapper[count];
             int entityIndex = 0;
             int coordinateIndex = 0;

             //--------Draw the first pair of entities to fillet-----------------------

             //Draw a line
             double[] startPoint = { 0, 0, 0 };
             double[] endPoint = { 5, 0, 0 };
             Line dsLine = dsSketchMgr.InsertLine(startPoint[0], startPoint[1], startPoint[2],
                                                  endPoint[0], endPoint[1], endPoint[2]);

             //Add line entity to output arrays
             firstEntityArray[entityIndex] = new  DispatchWrapper(dsLine);
             firstPointOnEntityDblArray[coordinateIndex] = endPoint[0];
             firstPointOnEntityDblArray[coordinateIndex +1] = endPoint[1];
             firstPointOnEntityDblArray[coordinateIndex+ 2] = endPoint[2];

             //Draw an arc
             double radius = 1;
             double[] centerPoint = { 2, -1, 0 };
             double startAngle = Math.PI;
             double endAngle = 1.5 * Math.PI;
             CircleArc dsArc = dsSketchMgr.InsertArc(centerPoint[0], centerPoint[1], centerPoint[2],
                                                     radius, startAngle, endAngle);

             //Add arc entity to output arrays
             secondEntityArray[entityIndex] = new DispatchWrapper(dsArc);
             secondPointOnEntityDblArray[coordinateIndex] = centerPoint[0] - radius;
             secondPointOnEntityDblArray[coordinateIndex + 1] = centerPoint[1];
             secondPointOnEntityDblArray[coordinateIndex + 2] = centerPoint[2];

             //Increase entity index
             entityIndex++;
             //Increase coordinate index
             coordinateIndex += 3;

             //--------Draw the second pair of entities to fillet----------------------

             //Draw a line
             startPoint =  new  double[] { 11, 0, 0 };
             endPoint = new double[] { 16, 0, 0 };
             dsLine = dsSketchMgr.InsertLine(startPoint[0], startPoint[1], startPoint[2],
                                             endPoint[0], endPoint[1], endPoint[2]);

             //Add line entity to output arrays
             firstEntityArray[entityIndex] = new  DispatchWrapper(dsLine);
             firstPointOnEntityDblArray[coordinateIndex] = endPoint[0];
             firstPointOnEntityDblArray[coordinateIndex + 1] = endPoint[1];
             firstPointOnEntityDblArray[coordinateIndex + 2] = endPoint[2];

             //Draw a circle
             centerPoint =  new  double[] { 18, -1, 0 };
             radius = 1;
             Circle dsCircle = dsSketchMgr.InsertCircle(centerPoint[0], centerPoint[1], centerPoint[2], radius);

             //Add circle entity to output arrays
             secondEntityArray[entityIndex] = new DispatchWrapper(dsCircle);
             secondPointOnEntityDblArray[coordinateIndex] = centerPoint[0] - radius;
             secondPointOnEntityDblArray[coordinateIndex + 1] = centerPoint[1];
             secondPointOnEntityDblArray[coordinateIndex + 2] = centerPoint[2];

             //Increase entity index
             entityIndex++;
             //Increase coordinate index
             coordinateIndex += 3;

             //--------Draw the third pair of entities to fillet-----------------------

             //Draw first circle
             centerPoint =  new  double[] { 7, -1, 0 };
             radius = 1;
             Circle dsFirstCircle = dsSketchMgr.InsertCircle(centerPoint[0], centerPoint[1], centerPoint[2], radius);

             //Add circle entity to output arrays
             firstEntityArray[entityIndex] = new  DispatchWrapper(dsFirstCircle);
             firstPointOnEntityDblArray[coordinateIndex] = centerPoint[0];
             firstPointOnEntityDblArray[coordinateIndex + 1] = centerPoint[1] + radius;
             firstPointOnEntityDblArray[coordinateIndex + 2] = centerPoint[2];

             //Draw second circle
             centerPoint[0] = 9;
             Circle dsSecondCircle = dsSketchMgr.InsertCircle(centerPoint[0], centerPoint[1], centerPoint[2], radius);

             //Add circle entity to output arrays
             secondEntityArray[entityIndex] = new DispatchWrapper(dsSecondCircle);
             secondPointOnEntityDblArray[coordinateIndex] = centerPoint[0];
             secondPointOnEntityDblArray[coordinateIndex + 1] = centerPoint[1] + radius;
             secondPointOnEntityDblArray[coordinateIndex + 2] = centerPoint[2];
         }

         private static void SetFilletRadius(Document dsDoc, double filletRadius)
         {
             dsSetCommandOptionResult_e setResult;
             dsCommandOptionDouble_e filletRadCommandOption =  dsCommandOptionDouble_e.dsCommandOptionDouble_SetFltRad;

             dsDoc.SetCommandOptionDouble(filletRadCommandOption, filletRadius, out setResult);
             if (dsSetCommandOptionResult_e.dsSetCommandOptionResult_Success != setResult)
             {
                 MessageBox.Show("Document.SetCommandOptionDouble() returns " + setResult.ToString() +  " after setting of " + filletRadCommandOption + " command option.");
             }
         }

         private static DraftSight.Application ConnectToDraftSight()
         {
             DraftSight.Application dsApp = null;

             try
             {
                 //Connect to DraftSight
                 dsApp = (DraftSight.Application)Marshal.GetActiveObject("DraftSight.Application");
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
