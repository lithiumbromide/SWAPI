---
title: "Creating Polysolid Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Creating_Polysolid_Entities_Example_CSharp.htm"
---

# Creating Polysolid Entities Example (C#)

This example shows how to create 3D polysolids.

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
// 1. Inserts a 2D polyline.
// 2. Creates a 3D polysolid using the 2D polyline.
// 3. Creates an array of coordinates.
// 4. Creates a 3D polysolid using the coordinates.
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

 namespace PolysolidConsoleApp1
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
                    new  double[] { 0.8839, 7.3348, 0.8839, 6.0943, 9.3647, 6.0943, 9.3647, 7.3348 },
                    true);
              }

              DispatchWrapper[] dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsPolyline);

              dsSketchManager.PolysolidByEntities(dsEntities, 4.0, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left);

               double[] coordinatesArray =   new   double[] { 0.6339, 3.9955, 9.3647, 3.9955 };

              dsSketchManager.PolysolidByCoordinates(coordinatesArray, 4.0, 0.25, dsPolySolidJustification_e.dsPolySolidJustification_Left);

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
