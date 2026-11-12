---
title: "Slicing Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Slicing_Entities_Example_CSharp.htm"
---

# Slicing Entities Example (C#)

This example shows how to slice 3D entities.

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
// 1. Extrudes several 3D entities.
// 2. Slices 3D entities by:
// - 3 points
// - A planar entity
// - A surface
// - XY plane
// - YZ plane
// - ZX plane
// - Z axis
// - A predefined view
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

 namespace SliceEntitiesConsoleApp1
 {
       class  Program
      {
            public  static DraftSight.Interop.dsAutomation.Application application;
            static  void Main(string[] args)
          {
               //Connect to DraftSight application
             application = ConnectToDraftSight();
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

              MathUtility dsMathUtility = application.GetMathUtility();
               if (null == dsMathUtility)
              {
                   return;
              }

              DispatchWrapper[] dsEntities;

               //Slice entities - 3 points

              PolyLine dsPolyline;
              {
                  dsPolyline = dsSketchManager.InsertPolyline2D(
                    new  double[] { 30.7029, 12.4677, 30.7029, 10.2257, 28.4117, 10.2257, 28.4117, 12.4677 },
                    true);
              }

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline);

              Object extrudes =   null;
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0,   out extrudes);
               object[] dsExtrudeObjs = (object[])extrudes;

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper((Extrusion)dsExtrudeObjs[0]);

              MathPoint FirstPoint = dsMathUtility.CreatePoint(28.4117, 10.2257, 4.0);
              MathPoint SecondPoint = dsMathUtility.CreatePoint(30.7029, 12.4677, 4.0);
              MathPoint ThirdPoint = dsMathUtility.CreatePoint(0.0, 0.0, 0.0);

              Object obj;
              dsSketchManager.SliceEntitiesBy3Points(dsEntities, FirstPoint, SecondPoint, ThirdPoint,  true, ThirdPoint,  out obj);

              changeColorProperty(obj, 1);

               //Slice Entities - Planar Entity

              PolyLine dsPolyline1;
              {
                  dsPolyline1 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 31.3452, 6.8946, 31.3452, 9.2404, 33.8880, 9.2404, 33.8880, 6.8946 },
                    true);
              }

              Circle dsCircle;
              {
                  dsCircle = dsSketchManager.InsertCircle(32.6166, 8.0675, 2.0000, 0.98);
              }

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline1);

              Object extrudes1 =   null;
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0,  out extrudes1);
               object[] dsExtrudeObjs1 = (object[])extrudes1;

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper((Extrusion)dsExtrudeObjs1[0]);

              DispatchWrapper[] dsEntityPlanar =   new DispatchWrapper[1];
              dsEntityPlanar[0] =   new DispatchWrapper(dsCircle);

              Object obj1;
              dsSketchManager.SliceEntitiesByPlanarEntity(dsEntities, dsEntityPlanar,  true, ThirdPoint,  out obj1);

              changeColorProperty(obj1, 2);

               //Slice Entity - Surface

              PolyLine dsPolyline2;
              {
                  dsPolyline2 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 34.5488, 3.2662, 34.5488, 5.8077, 37.1209, 5.8077, 37.1209, 3.2662 },
                    true);
             }
 Line dsLine;
              {
                  dsLine = dsSketchManager.InsertLine(35.8348, 3.2662, 0.0000, 35.8348, 5.8077, 0.0000);
              }

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline2);

              Object extrudes2 =   null;
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0,  out extrudes2);
               object[] dsExtrudeObjs2 = (object[])extrudes2;

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsLine);

              Object extrudesSur =   null;
              dsSketchManager.ExtrudeEntitiesToSurfaceByHeight(dsEntities, 4.0, 0,   out extrudesSur);
               object[] dsExtrudeObjsSur = (object[])extrudesSur;

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper((Extrusion)dsExtrudeObjs2[0]);

              DispatchWrapper[] dsEntitySurface =   new DispatchWrapper[1];
              dsEntitySurface[0] =   new DispatchWrapper((ExtrudedSurface)dsExtrudeObjsSur[0]);
              Object obj2;
              dsSketchManager.SliceEntitiesBySurface(dsEntities, dsEntitySurface,   true, ThirdPoint,   out obj2);

              changeColorProperty(obj2, 3);

               //Slice Entity - XY

              PolyLine dsPolyline3;
              {
                  dsPolyline3 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 37.9451, -0.4819, 37.9451, 2.3739, 40.6400, 2.3739, 40.6400, -0.4819 },
                    true);
              }
              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline3);

              Object extrudes3 =   null;
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0,   out extrudes3);
               object[] dsExtrudeObjs3 = (object[])extrudes3;

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper((Extrusion)dsExtrudeObjs3[0]);

              Object obj3;
              dsSketchManager.SliceEntitiesByXY(dsEntities, dsMathUtility.CreatePoint(37.9451, -0.4819, 2.0000),   true, ThirdPoint,   out obj3);

              changeColorProperty(obj3, 4);

               //Slice Entity - YZ

              PolyLine dsPolyline4;
              {
                  dsPolyline4 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 41.2617, -4.0399, 41.2617, -1.1841, 43.9566, -1.1841, 43.9566, -4.0399 },
                    true);
              }
              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline4);

              Object extrudes4 =   null;
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0,   out extrudes4);
               object[] dsExtrudeObjs4 = (object[])extrudes4;

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper((Extrusion)dsExtrudeObjs4[0]);

              Object obj4;
              dsSketchManager.SliceEntitiesByYZ(dsEntities, dsMathUtility.CreatePoint(42.60915, -4.0399, 4.0),   true, ThirdPoint,   out obj4);

              changeColorProperty(obj4, 5);

               //Slice Entity - ZX

              PolyLine dsPolyline5;
              {
                  dsPolyline5 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 44.7029, -7.6823, 44.7029, -4.8264, 47.3978, -4.8264, 47.3978, -7.6823 },
                    true);
              }
              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline5);

              Object extrudes5 =   null;
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0,   out extrudes5);
               object[] dsExtrudeObjs5 = (object[])extrudes5;

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper((Extrusion)dsExtrudeObjs5[0]);

              Object obj5;
              dsSketchManager.SliceEntitiesByZX(dsEntities, dsMathUtility.CreatePoint(44.7029, -6.25435, 4.0),   true, ThirdPoint,   out obj5);

              changeColorProperty(obj5, 6);

               //Slice Entity - Z Axis

              PolyLine dsPolyline6;
              {
                  dsPolyline6 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 48.0560, -11.3057, 48.0560, -8.4498, 50.7509, -8.4498, 50.7509, -11.3057 },
                    true);
              }
              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline6);

              Object extrudes6 =   null;
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0,   out extrudes6);
               object[] dsExtrudeObjs6 = (object[])extrudes6;

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper((Extrusion)dsExtrudeObjs6[0]);

              Object obj6;
              dsSketchManager.SliceEntitiesByZAxis(dsEntities, dsMathUtility.CreatePoint(49.4034, -11.3057, 0.0),
                  dsMathUtility.CreatePoint(50.7509, -11.3057, 2.0),   true, ThirdPoint,   out obj6);

              changeColorProperty(obj6, 2);

               //Slice Entity - View

              PolyLine dsPolyline7;
              {
                  dsPolyline7 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 51.3856, -14.8710, 51.3856, -12.0151, 54.0805, -12.0151, 54.0805, -14.8710 },
                    true);
              }
              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline7);

              Object extrudes7 =   null;
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0,   out extrudes7);
               object[] dsExtrudeObjs7 = (object[])extrudes7;

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper((Extrusion)dsExtrudeObjs7[0]);

              ViewManager dsViewManager = dsDoc.GetViewManager();
               if (null != dsViewManager)
                   dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric);

              Object obj7;
              dsSketchManager.SliceEntitiesByView(dsEntities, dsMathUtility.CreatePoint(52.7330, -14.8710, 0.0),   true, ThirdPoint,   out obj7);

              changeColorProperty(obj7, 3);

              application.Zoom(dsZoomRange_e.dsZoomRange_Fit,   null,   null);
           }
            public  static  void changeColorProperty(object solid,   int colorIndex)
           {
               object[] dsSolidsObjs = (object[])solid;

              Solid3D dsSolid =   null;
               foreach (object dsSolidObj  in dsSolidsObjs)
              {
                  dsSolid = dsSolidObj  as Solid3D;

                  Color dsColor = application.GetColorByIndex(colorIndex);
                  dsSolid.Color = dsColor;
              }
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
