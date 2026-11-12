---
title: "Cross-sectioning Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Cross-sectioning_Entities_Example_CSharp.htm"
---

# Cross-sectioning Entities Example (C#)

This example shows how to cross-section 3D entities.

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
// 1. Extrudes a 2D polyline into a 3D entity.
// 2. Creates a CircleArc and cross-sections the 3D entity using the CircleArc. (Color red)
// 3. Creates 3 MathPoints and cross-sections the 3D entity using them. (Color yellow)
// 4. Cross-sections the 3D entity using the Z axis. (Color green)
// 5. Creates a point on the active view plane and cross-sections the 3D entity
// using the view plane. (Color cyan)
// 6. Extrudes another 2D polyline into a 3D entity.
// 7. Creates another MathPoint and uses its planes to cross-section the 3D entity:
// a. XY plane (Color blue)
// b. YZ plane (Color magenta)
// c. XZ plane (Color green)
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
 using System.Diagnostics;

 namespace CrossSectionEntitiesConsoleApp1
 {
       class  Program
      {
            static DraftSight.Interop.dsAutomation.Application application;
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

              MathUtility dsMathUtility = application.GetMathUtility();
               if (null == dsMathUtility)
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

              CircleArc dsCircleArc;
              {
                  dsCircleArc = dsSketchManager.InsertArc(218.0505, 105.1495, 100.0, 108.73107098019408, 0.59905667591910, 3.74064932950889);
              }

              DispatchWrapper[] dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline);

              Object extrudes =   null;
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 50, 0,   out extrudes);

               object[] dsExtrudeObjs = (object[])extrudes;
              dsEntities =   new DispatchWrapper[dsExtrudeObjs.Length];
              Extrusion dsExtrusion =   null;
               int i = 0;
               foreach (object dsExtrudeObj  in dsExtrudeObjs)
              {
                  dsExtrusion = dsExtrudeObj  as Extrusion;
                  dsEntities[i] =   new DispatchWrapper(dsExtrusion);
                  ++i;
              }

              DispatchWrapper[] dsEntities_0 =   new DispatchWrapper[1];
              dsEntities_0[0] =   new DispatchWrapper(dsCircleArc);

               // CrossSectionEntitiesByEntity
               object regions =   null;
              dsSketchManager.CrossSectionEntitiesByEntity(dsEntities, dsEntities_0,   out regions);
              changeColorProperty(regions, 1);

              MathPoint FirstPoint = dsMathUtility.CreatePoint(307.848, 166.459, 150.0);
              MathPoint SecondPoint = dsMathUtility.CreatePoint(307.848, 166.459, 100.0);
              MathPoint ThirdPoint = dsMathUtility.CreatePoint(128.253, 43.84, 150.0);

              regions =   null;
               //CrossSectionEntitiesBy3Points
              dsSketchManager.CrossSectionEntitiesBy3Points(dsEntities, FirstPoint, SecondPoint, ThirdPoint,  out regions);
              changeColorProperty(regions, 2);

              regions =   null;
               //CrossSectionEntitiesByZAxis
              dsSketchManager.CrossSectionEntitiesByZAxis(dsEntities, FirstPoint, SecondPoint,  out regions);
              changeColorProperty(regions, 3);

              ViewManager dsViewManager = dsDoc.GetViewManager();
               if (null != dsViewManager)
                   dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric);

              regions =   null;
               //CrossSectionEntitiesByView
              MathPoint PointOnActiveViewPlane = dsMathUtility.CreatePoint(128.253, 43.84, 100.0);
              dsSketchManager.CrossSectionEntitiesByView(dsEntities, PointOnActiveViewPlane,  out regions);
              changeColorProperty(regions, 4);

              PolyLine dsPolyline1;
              {
                  dsPolyline1 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 515.202, 23.36, 515.202, -82.68, 367.471, -82.68, 367.471, 23.36 },
                    true);
              }

              dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline1);

              extrudes =   null;
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities, 50, 0,   out extrudes);

              dsExtrudeObjs = (object[])extrudes;
              dsEntities =   new DispatchWrapper[dsExtrudeObjs.Length];

              Extrusion dsExtrusion_extr =   null;
              i = 0;
               foreach (object dsExtrudeObj  in dsExtrudeObjs)
              {
                  dsExtrusion_extr = dsExtrudeObj  as Extrusion;
                  dsEntities[i] =   new DispatchWrapper(dsExtrusion_extr);
                  ++i;
              }

              PointOnActiveViewPlane = dsMathUtility.CreatePoint(515.202, -82.68, 50);

              regions =   null;
               //CrossSectionEntitiesByXY
              dsSketchManager.CrossSectionEntitiesByXY(dsEntities, PointOnActiveViewPlane,  out regions);
              changeColorProperty(regions, 5);

              regions =   null;
               //CrossSectionEntitiesByYZ
              dsSketchManager.CrossSectionEntitiesByYZ(dsEntities, PointOnActiveViewPlane,   out regions);
              changeColorProperty(regions, 6);

              regions =   null;
               //CrossSectionEntitiesByZX
              dsSketchManager.CrossSectionEntitiesByZX(dsEntities, PointOnActiveViewPlane,  out regions);
              changeColorProperty(regions, 3);

              application.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   null,   null);
           }
            public  static DraftSight.Interop.dsAutomation.Application ConnectToDraftSight()
           {

              DraftSight.Interop.dsAutomation.Application application =  null;

               try
              {
                 //Connect to DraftSight
                  application = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
              }
               catch (Exception ex)
              {
                  MessageBox.Show("Failed to connect to DraftSight. Cause: " + ex.Message);
                  application =   null;
              }

               return application;
           }
            public  static  void changeColorProperty(object regions,   int colorIndex)
           {
               object[] dsRegionsObjs = (object[])regions;

              Region dsRegion =   null;
               foreach (object dsRegionObj  in dsRegionsObjs)
              {
                  dsRegion = dsRegionObj  as Region;

                  Color dsColor = application.GetColorByIndex(colorIndex);
                  dsRegion.Color = dsColor;
              }
           }
      }
 }
```
