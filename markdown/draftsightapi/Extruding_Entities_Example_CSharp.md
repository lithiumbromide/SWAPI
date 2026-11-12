---
title: "Extruding Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Extruding_Entities_Example_CSharp.htm"
---

# Extruding Entities Example (C#)

This example shows how to extrude 3D entities.

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
// 1. Extrudes 2D entities to both 3D solids and 3D surfaces by
// both heights and paths.
// 2. Inspect the graphics area.
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

 namespace ExtrudeEntitiesConsoleApp1
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
                    new  double[] { 128.253, 166.459, 128.253, 43.84, 307.848, 43.84, 307.848, 166.459 },
                    true);
              }

              Circle dsCircle;
              {
                  dsCircle = dsSketchManager.InsertCircle(221.87613941018759, 159.34343163538875, 0.00000000000000, 103.39978537214083);
              }

              DispatchWrapper[] dsEntities =   new DispatchWrapper[2];
              dsEntities[0] =   new DispatchWrapper(dsPolyline);
              dsEntities[1] =   new DispatchWrapper(dsCircle);

               // Extrude entities to solid by height
              Object extrudes =   null;
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 20, 0,   out extrudes);
               object[] dsExtrudeObjs = (object[])extrudes;

               // Change the properties of extrusion
              Extrusion dsExtrusion =   null;
               foreach (object dsExtrudeObj  in dsExtrudeObjs)
              {
                  dsExtrusion = dsExtrudeObj  as Extrusion;
                  dsExtrusion.Height = 30;

                  Color dsColor = application.GetColorByIndex(2);
                  dsExtrusion.Color = dsColor;
              }

              Line dsLine;
              {
                  dsLine = dsSketchManager.InsertLine(550.0, 122.0, 0.0, 431.0, 70.0, 0.0);
              }

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsLine);

               // Extrude entities to surface by height
              extrudes =   null;
              dsSketchManager.ExtrudeEntitiesToSurfaceByHeight(dsEntities, 20, 0,   out extrudes);

              ExtrudedSurface dsExtrudedSurface =   null;
              dsExtrudeObjs = (object[])extrudes;
               foreach (object dsExtrudedSurfaceObj  in dsExtrudeObjs)
              {
                  dsExtrudedSurface = dsExtrudedSurfaceObj  as ExtrudedSurface;
                  dsExtrudedSurface.Height = 50;
              }

              PolyLine dsPolyline1;
              {
                  dsPolyline1 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 515.202, 23.36, 515.202, -82.68, 367.471, -82.68, 367.471, 23.36 },
                    true);
              }

              Line dsLinePath;
              {
                  dsLinePath = dsSketchManager.InsertLine(734.317, 74.52, 0.0, 734.317, 74.52, -309.475);
              }

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline1);

              DispatchWrapper[] dsPathEntities =   new DispatchWrapper[1];
              dsPathEntities[0] =   new DispatchWrapper(dsLinePath);

              // Extrude entities to solid by path
              extrudes =   null;
              dsSketchManager.ExtrudeEntitiesToSolidByPath(dsEntities, dsPathEntities, 0,   out extrudes);

              PolyLine dsPolyline2;
              {
                  dsPolyline2 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 659.732, 89.273, 659.732, 16.042, 555.531, 16.042, 555.531, 89.273 },
                    true);
              }

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline2);

               // Extrude entities to surface by path
              extrudes =   null;
              dsSketchManager.ExtrudeEntitiesToSurfaceByPath(dsEntities, dsPathEntities, 0,  out extrudes);

              ViewManager dsViewManager = dsDoc.GetViewManager();
               if (null != dsViewManager)
                   dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric);

              application.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   null,   null);
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
                  dsApp =  null;
              }

               return dsApp;
           }
      }
 }
```
