---
title: "Unifying, Subtracting, and Intersecting Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Unifying_Subtracting_and_Intersecting_Entities_Example_CSharp.htm"
---

# Unifying, Subtracting, and Intersecting Entities Example (C#)

This example shows how to perform union, subtract, and intersect operations on 3D solids.

//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
// `install_dir`\**APISDK\tlb\DraftSight.Interop.dsAutomation.dll**
// 4. Start DraftSight.
// 5. Press F5 to debug the project.
//
// Postconditions:
// 1. Inserts 2D polylines and creates 3D polysolids from them.
// 2. Performs union, subtract, and intersect operations on the 3D polysolids.
// 3. Inspect the graphics area.
//----------------------------------------------------------------

```vb
 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Runtime.InteropServices;
 using DraftSight.Interop.dsAutomation;

 namespace BooleanConsoleApp1
 {
       class  Program
      {
            public  static  void Main(string[] args)
           {
              DraftSight.Interop.dsAutomation.Application dsApp;

               //Connect to DraftSight
              dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
               //Abort any command currently running in DraftSight
               //to avoid nested commands
              dsApp.AbortRunningCommand();

              Document dsDoc = dsApp.GetActiveDocument();
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

              ViewManager dsViewManager = dsDoc.GetViewManager();
               if (null != dsViewManager)
                   dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric);

              dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   null,   null);

               //Boolean - Union

              PolyLine dsPolyline;
              {
                  dsPolyline = dsSketchManager.InsertPolyline2D(
                   new  double[] { 0.8839, 7.3348, 0.8839, 6.0943, 9.3647, 6.0943, 9.3647, 7.3348 },
                    true);
              }

              PolyLine dsPolyline2;
              {
                  dsPolyline2 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 5.8839, 12.3348, 5.8839, 11.0943, 14.3647, 11.0943, 14.3647, 12.3348 },
                    true);
              }

              dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   null,   null);

              DispatchWrapper[] dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline);
              Solid3D dsSolid3D_1 = dsSketchManager.PolysolidByEntities(dsEntities, 4.0, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left);

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline2);
              Solid3D dsSolid3D_2 = dsSketchManager.PolysolidByEntities(dsEntities, 4.0, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left);

              dsEntities =  new DispatchWrapper[2];
              dsEntities[0] =   new DispatchWrapper(dsSolid3D_1);
              dsEntities[1] =   new DispatchWrapper(dsSolid3D_2);

              Object obj;
              dsSketchManager.UnionEntities(dsEntities,  out obj);

              dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   null,   null);

               //Boolean - Subtract

              PolyLine dsPolyline3;
              {
                  dsPolyline3 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 22.5070, 8.2407, 22.5070, 13.8125, 36.4164, 13.8125, 36.4164, 8.2407 },
                    true);
              }

              PolyLine dsPolyline4;
              {
                  dsPolyline4 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 30.7029, 12.4677, 30.7029, 10.2257, 28.4117, 10.2257, 28.4117, 12.4677 },
                    true);
              }

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline3);

              Object extrudes =   null;
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0,   out extrudes);
                            object[] dsExtrudeObjs = (object[])extrudes;

              DispatchWrapper[] dsEntities2 =   new DispatchWrapper[1];
              dsEntities2[0] =   new DispatchWrapper(dsPolyline4);

              extrudes =   null;
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities2, 4.0, 0,   out extrudes);
               object[] dsExtrudeObjs2 = (object[])extrudes;

              dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   null,   null);

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper((Extrusion) dsExtrudeObjs[0]);

              dsEntities2 =   new DispatchWrapper[1];
              dsEntities2[0] =   new DispatchWrapper((Extrusion) dsExtrudeObjs2[0]);
              dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   null,   null);

              dsSketchManager.SubtractEntities(dsEntities2, dsEntities,   out obj);

              dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   null,   null);

               //Boolean - Intersect

              PolyLine dsPolyline5;
              {
                  dsPolyline5 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 22.1780, 3.6354, 22.1780, -2.0369, 36.1998, -2.0369, 36.1998, 3.6354 },
                    true);
              }

              PolyLine dsPolyline6;
              {
                  dsPolyline6 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 36.1998, -2.0369, 36.1998, 2.1240, 30.3079, 2.1240, 30.3079, -2.0369 },
                    true);
              }

              dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   null,   null);

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline5);
              Solid3D dsSolid3D_3 = dsSketchManager.PolysolidByEntities(dsEntities, 4.0, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left);

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline6);
              Solid3D dsSolid3D_4 = dsSketchManager.PolysolidByEntities(dsEntities, 4.0, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left);

              dsEntities =   new DispatchWrapper[2];
              dsEntities[0] =   new DispatchWrapper(dsSolid3D_3);
              dsEntities[1] =   new DispatchWrapper(dsSolid3D_4);

              dsSketchManager.IntersectEntities(dsEntities,   out obj);

              dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   null,   null);
          }
      }
 }
```
