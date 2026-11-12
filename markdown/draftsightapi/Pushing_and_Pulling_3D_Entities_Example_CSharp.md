---
title: "Pushing and Pulling 3D Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Pushing_and_Pulling_3D_Entities_Example_CSharp.htm"
---

# Pushing and Pulling 3D Entities Example (C#)

This example shows how to pull out a 3D entity.

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
// 1. Inserts a 2D polyline and a circle.
// 2. Creates a point on the 2D polyline.
// 3. Pulls out a 3D entity from the point on the 2D polyline.
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

 namespace PushPullEntitiesConsoleApp1
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
                    new  double[] { 308.611, 244.543, 308.611, 133.606, 440.093, 133.606, 440.093, 244.543 },
                    true);
              }

              Circle dsCircle;
              {
                  dsCircle = dsSketchManager.InsertCircle(60.029, 196.265, 0.0, 100.0);
              }

              MathUtility dsMathUtility = application.GetMathUtility();
              MathPoint InternalPoint = dsMathUtility.CreatePoint(308.611, 244.543, 0.0);

               bool bRetVal = dsSketchManager.PushPullEntities(InternalPoint, 300);

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
