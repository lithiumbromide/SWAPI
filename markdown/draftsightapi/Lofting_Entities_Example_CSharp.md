---
title: "Lofting Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Lofting_Entities_Example_CSharp.htm"
---

# Lofting Entities Example (C#)

This example shows how to loft entities.

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
// 1. Inserts a 2D polyline, a circle, and a guide line.
// 2. Lofts the polyline and circle to solids using the guide line.
// 3. Inserts two 2D polylines and a path line.
// 4. Lofts the polylines to solids using the path line.
// 5. Inspect the graphics area.
//
// Optional: Open a new document. Comment out the two solid loft methods,
// uncomment the two surface loft methods, and rerun the macro.
//----------------------------------------------------------------

```vb
 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Runtime.InteropServices;
 using System.Reflection;
 using DraftSight.Interop.dsAutomation;
 using System.Windows.Forms;

 namespace LoftEntitiesConsoleApp1
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

                  dsPolyline.Elevation = 100;
              }

              Circle dsCircle;
              {
                  dsCircle = dsSketchManager.InsertCircle(221.87613941018759, 159.34343163538875, 0.00000000000000, 103.39978537214083);
              }

              Line dsLine;
              {
                  dsLine = dsSketchManager.InsertLine(432.58, 113.544, 0, 432.58, 113.544, -155.752);
              }

              DispatchWrapper[] dsEntities =   new DispatchWrapper[2];
              dsEntities[0] =   new DispatchWrapper(dsPolyline);
              dsEntities[1] =   new DispatchWrapper(dsCircle);

              DispatchWrapper[] dsGuideEntities =   new DispatchWrapper[1];
              dsGuideEntities[0] =   new DispatchWrapper(dsLine);

              Loft dsLoft;
              {
                   //Loft entities to solid by guides
                  dsLoft = dsSketchManager.LoftEntitiesToSolidByGuides(dsEntities,   false,
                      dsGuideEntities, dsLoftSurfaceNormalOption_e.dsLoftSurfaceNormalOption_SmoothFit,
                      dsLoftedSurfaceNormalOption_e.dsLoftedSurfaceNormalOption_SmoothFit, 0, 0, 0, 0);

                   //Loft entities to surface by guides
                   //LoftedSurface dsLoftedSurface = dsSketchManager.LoftEntitiesToSurfaceByGuides(dsEntities, false,
                   //    dsGuideEntities, dsLoftSurfaceNormalOption_e.dsLoftSurfaceNormalOption_SmoothFit,
                   //    dsLoftedSurfaceNormalOption_e.dsLoftedSurfaceNormalOption_SmoothFit, 0, 0, 0, 0);
              }

               if (null == dsLoft)
              {
                   return;
              }

              PolyLine dsPolyline1;
              {
                  dsPolyline1 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 486.181, 78.416, 486.181, 246.617, 675.147, 246.617, 675.147, 78.416 },
                    true);

                  dsPolyline1.Elevation = 100;
              }

              PolyLine dsPolyline2;
              {
                  dsPolyline2 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 546.401, 200.933, 546.401, 123.062, 675.147, 123.062, 675.147, 200.933 },
                    true);
              }

              Line dsLine1;
              {
                  dsLine1 = dsSketchManager.InsertLine(486.181, 246.617, 100, 546.401, 200.933, 0);
              }

              dsEntities =   new DispatchWrapper[2];
              dsEntities[0] =   new DispatchWrapper(dsPolyline1);
              dsEntities[1] =   new DispatchWrapper(dsPolyline2);

              DispatchWrapper[] dsPathEntities =   new DispatchWrapper[1];
              dsPathEntities[0] =   new DispatchWrapper(dsLine1);

              Loft dsLoft_1;
              {
                   // Loft entities to solid by path
                  dsLoft_1 = dsSketchManager.LoftEntitiesToSolidByPath(dsEntities,   false,
                      dsPathEntities, dsLoftSurfaceNormalOption_e.dsLoftSurfaceNormalOption_SmoothFit,
                      dsLoftedSurfaceNormalOption_e.dsLoftedSurfaceNormalOption_SmoothFit, 0, 0, 0, 0);

                   // Loft entities to surface by path
                  //LoftedSurface dsLoftedSurface = dsSketchManager.LoftEntitiesToSurfaceByPath(dsEntities, false,
                   //    dsPathEntities, dsLoftSurfaceNormalOption_e.dsLoftSurfaceNormalOption_SmoothFit,
                   //    dsLoftedSurfaceNormalOption_e.dsLoftedSurfaceNormalOption_SmoothFit, 0, 0, 0, 0);
              }

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
                  dsApp =   null;
              }

               return dsApp;
           }
      }
 }
```
