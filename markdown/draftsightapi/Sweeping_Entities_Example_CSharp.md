---
title: "Sweeping Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Sweeping_Entities_Example_CSharp.htm"
---

# Sweeping Entities Example (C#)

This example shows how to sweep 3D entities.

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
// 1. Inserts a 2D polyline and a path line.
// 2. Sweeps the 2D polyline along the path line to create a 3D solid.
// 3. Inserts a 2D polyline and a path line.
// 4. Sweeps the 2D polyline along the path line to create a 3D surface.
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

 namespace SweepEntitiesConsoleApp1
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
               // Sweep to solid
              PolyLine dsPolyline1;
              {
                  dsPolyline1 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 0.8839, 7.3348, 0.8839, 6.0943, 9.3647, 6.0943, 9.3647, 7.3348 },
                    true);
              }

              Line dsLine1;
              {
                  dsLine1 = dsSketchManager.InsertLine(1.6048, 1.4138, 0.0000, 1.9225, 7.8519, 0.0000);
              }

              DispatchWrapper[] dsEntitiesSo =   new DispatchWrapper[1];
              dsEntitiesSo[0] =   new DispatchWrapper(dsPolyline1);

              dsSketchManager.SweepEntitiesToSolid(dsEntitiesSo, dsLine1,   true,   false,   false, 0.0, 0.0, 0.0, 1.0, 0.0);

               // Sweep to surface
              PolyLine dsPolyline2;
              {
                  dsPolyline2 = dsSketchManager.InsertPolyline2D(
                    new  double[] { 10.8839, 17.3348, 10.8839, 16.0943, 19.3647, 16.0943, 19.3647, 17.3348 },
                    true);
              }

              Line dsLine2;
              {
                  dsLine2 = dsSketchManager.InsertLine(10.6048, 10.4138, 0.0000, 10.9225, 17.8519, 0.0000);
              }

              DispatchWrapper[] dsEntitiesSu =   new DispatchWrapper[1];
              dsEntitiesSu[0] =   new DispatchWrapper(dsPolyline2);

              dsSketchManager.SweepEntitiesToSurface(dsEntitiesSu, dsLine2,   true,   false,   false, 0.0, 0.0, 0.0, 1.0, 0.0);

              ViewManager dsViewManager = dsDoc.GetViewManager();
               if (null != dsViewManager)
                   dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric);
              application.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   null,   null);
           }
            private  static DraftSight.Interop.dsAutomation.Application ConnectToDraftSight()
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
