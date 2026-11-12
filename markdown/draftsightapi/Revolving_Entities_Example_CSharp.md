---
title: "Revolving Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Revolving_Entities_Example_CSharp.htm"
---

# Revolving Entities Example (C#)

This example shows how to revolve 3D entities.

//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
// `install_dir`\**APISDK\tlb\DraftSight.Interop.dsAutomation.dll**
// 4. Add references to **System** and **System.Windows.Forms**.
// 5. Start DraftSight.
// 6. Press F5 to debug the project.
//
// Postconditions:
// 1. Inserts a 2D polyline, a circle, and an axis.
// 2. Revolves the 2D polyline and circle about the axis into a 3D solid.
// 3. Changes the color of the revolved entities.
// 4. Inserts a 2D polyline and a circle.
// 5. Revolves the 2D polyline and circle about the X axis into a 3D solid.
// 6. Inserts a 2D polyline and a circle.
// 7. Revolves the 2D polyline and circle about the specified axis
// and angle of revolution to a surface.
// 8. Inspect the graphics area.
//
// Optional: Open a new document, comment out the solid/surface revolve methods,
// uncomment the other solid/surface revolve methods, and rerun
// the macro.
//----------------------------------------------------------------

```vb
 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Runtime.InteropServices;
 using DraftSight.Interop.dsAutomation;
 using System.Windows.Forms;

 namespace RevolveEntitiesConsoleApp1
 {
       class  Program
      {
            static  void Main(string[] args)
           {
               //Connect to DraftSight application
              DraftSight.Interop.dsAutomation.Application application = ConnectToDraftSight();
               if (null == application)
              {
                   return;
              }

              application.AbortRunningCommand();   // abort any command currently running in DraftSight to avoid nested commands

              Document dsDoc = application.GetActiveDocument();
               if (null == dsDoc)
              {
                   return;
              }

              Model dsModel = dsDoc.GetModel();
               if (null == dsModel)
              {
                   return;
              }

              SketchManager dsSketchManager = dsModel.GetSketchManager();
               if (null == dsSketchManager)
              {
                   return;
              }

              PolyLine dsPolyline;
              {
                  dsPolyline = dsSketchManager.InsertPolyline2D(
                    new  double[] { -231.229, 148, -231.229, 76.963, -157.191, 76.963, -157.191, 148 },
                    true);

                  dsPolyline.Elevation = 100;
              }

              Circle dsCircle;
              {
                  dsCircle = dsSketchManager.InsertCircle(-199.212, 233.044, 0.0, 48.357);
              }

              Line dsLine;
              {
                  dsLine = dsSketchManager.InsertLine(-111.167, 282.069, 0, -111.167, 83.966, 0);
              }

              DispatchWrapper[] dsEntities =   new DispatchWrapper[2];
              dsEntities[0] =   new DispatchWrapper(dsPolyline);
              dsEntities[1] =   new DispatchWrapper(dsCircle);

              DispatchWrapper[] revolveArray =   new DispatchWrapper[1];
              revolveArray[0] =   new DispatchWrapper(dsLine);

               object revolves =   null;
                //Revolve entities to solid by object
              revolves = dsSketchManager.RevolveEntitiesToSolidByObject(dsEntities, revolveArray, 360.0);

               //Change the properties
              Revolve dsRevolve =   null;
               foreach (object dsRevolveObj  in (object[])revolves)
              {
                  dsRevolve = dsRevolveObj  as Revolve;
                  Color dsColor = application.GetColorByIndex(3);
                  dsRevolve.Color = dsColor;
              }

                //Revolve  entities to surface by object
               //revolves = dsSketchManager.RevolveEntitiesToSurfaceByObject(dsEntities, revolveArray, 360.0);

              PolyLine dsPolyline1;
              {
                  dsPolyline1 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 107.848, 158.077, 107.848, 74.014, 212.128, 74.014, 212.128, 158.077 },
                    true);

                  dsPolyline.Elevation = 100;
              }

              Circle dsCircle1;
              {
                  dsCircle1 = dsSketchManager.InsertCircle(153.603, 252.781, 0.0, 52.831);
              }

              dsEntities =   new DispatchWrapper[2];
              dsEntities[0] =   new DispatchWrapper(dsPolyline1);
              dsEntities[1] =   new DispatchWrapper(dsCircle1);

              revolves =   null;
                //Revolve  entities to solid by X axis
              revolves = dsSketchManager.RevolveEntitiesToSolidByXAxis(dsEntities, 360.0,   true);

                //Revolve  entities to surface by X axis
               //revolves = dsSketchManager.RevolveEntitiesToSurfaceByXAxis(dsEntities, 360.0, true);

              PolyLine dsPolyline2;
              {
                  dsPolyline2 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 435.587, 167.654, 435.587, 98.488, 483.471, 98.488, 483.471, 167.654 },
                    true);

                  dsPolyline.Elevation = 100;
              }

              Circle dsCircle2;
              {
                  dsCircle2 = dsSketchManager.InsertCircle(447.292, 270.87, 0.0, 41.116);
              }

              dsEntities =   new DispatchWrapper[2];
              dsEntities[0] =   new DispatchWrapper(dsPolyline2);
              dsEntities[1] =   new DispatchWrapper(dsCircle2);

              revolves =   null;
                //Revolve entities to solid by axis
               //revolves = dsSketchManager.RevolveEntitiesToSolidByAxis(dsEntities, 447.292, 270.87, 0.0,
               //483.471, 167.654, 0.0, 360.0 );

                //Revolve  entities to surface by axis
              revolves = dsSketchManager.RevolveEntitiesToSurfaceByAxis(dsEntities, 447.292, 270.87, 0.0,
                  483.471, 167.654, 0.0, 360.0);
           }
            public  static DraftSight.Interop.dsAutomation.Application ConnectToDraftSight()
           {

              DraftSight.Interop.dsAutomation.Application dsApp =  null;

               try
              {
                 //Connect to DraftSight
                 dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
              }
               catch (Exception ex)
              {
                  MessageBox.Show("Failed to connect to DraftSight. Cause: " + ex.Message);
                  dsApp =   null;
              }

               return dsApp;
           }
      }
 }
```
