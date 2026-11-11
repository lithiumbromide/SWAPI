---
title: "Add Temporary Entities to Block Definition Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Add_Temporary_Entities_to_Block_Definition_Example_CSharp.htm"
---

# Add Temporary Entities to Block Definition Example (C#)

This example shows how to add temporary entities to a Block definition and Block Instance.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add references to System and System.Windows.Forms.
// 5. Start DraftSight and open a document.
// 6. Start debugging the project.
//
// Postconditions:
// 1. Creates Block definition with one element, a Circle.
// 2. Inserts Block instance.
// 3. Zooms to fit the drawing and execution stops.
// 4. Press F10 to step through the rest of the project
//    and examine the drawing after each call.
// 5. Creates temporary entities, two Circles.
// 6. Modifies temporary entities.
// 7. Adds temporary entities to Block definition and Block
//    instance.
//----------------------------------------------------------------

using System;

using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace TemporaryEntitiesCSharp
{
    class Program
    {
        public static void Main()
        {
            DraftSight.Interop.dsAutomation.Application dsApp;

            //Connect to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            if (null == dsApp)
            {
                return;
            }
```

```
            //Abort any command currently running in DraftSight
            //to avoid nested commands
            dsApp.AbortRunningCommand();

            //Get active document
            Document dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }

            SketchManager dsSketchMgr = dsDoc.GetModel().GetSketchManager();

            //Create Block definition with one element, a Circle
            Circle dsCircle = dsSketchMgr.InsertCircle(0, 0, 0, 5);
            DispatchWrapper[] dsEntities = new DispatchWrapper[1];
            int[] dsEntityTypes = new int[1];
            dsEntities[0] = new DispatchWrapper(dsCircle);
            dsEntityTypes[0] = (int)dsObjectType_e.dsCircleType;
            BlockDefinition dsBlkDef = dsDoc.CreateBlockDefinition("SampleBlock", "Sample block definition",
                0, 0, 0, dsEntityTypes, dsEntities, dsBlockDefinitionEntities_e.dsBlockDefinitionEntities_RemoveFromDrawing);

            dsSketchMgr.InsertBlock2("SampleBlock", 0, 0, 0, 1, 1, 1, 0);

            //Zoom to fit
            dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);

            //Examine the drawing
            //to verify that a Block instance
            //was inserted
            //Press F10 to continue
            System.Diagnostics.Debugger.Break();

            //Create temporary entities, which are not added to drawing

            //Turn temporary entity mode on
            dsApp.TemporaryEntityMode = true;

            //Create temporary Circles
            Circle dsTempCircle1 = dsSketchMgr.InsertCircle(0, 0, 0, 5);
            Circle dsTempCircle2 = dsSketchMgr.InsertCircle(0, 0, 0, 5);

            //Turn temporary entity mode off
            dsApp.TemporaryEntityMode = false;

            //Modify Circles, which you cannot see
            double PointOnCurveX = 0.0;
            double PointOnCurveY = 0.0;
            double PointOnCurveZ = 0.0;
            dsCircle.GetClosestPointOn(2.5, 2.5, 0, out PointOnCurveX, out PointOnCurveY, out PointOnCurveZ);
            dsTempCircle1.SetCenter(PointOnCurveX, PointOnCurveY, PointOnCurveZ);

            dsTempCircle1.GetClosestPointOn(PointOnCurveX + 2.5, PointOnCurveY + 2.5, PointOnCurveZ, out PointOnCurveX, out PointOnCurveY, out PointOnCurveZ);
            dsTempCircle2.SetCenter(PointOnCurveX, PointOnCurveY, PointOnCurveZ);

            //Zoom to fit
            dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);

            //Add temporary Circles to Block definition
            //Block instance updates accordingly
            dsBlkDef.AddTemporaryEntity(dsTempCircle1);
            dsBlkDef.AddTemporaryEntity(dsTempCircle2);

            //Zoom to fit
            dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);

        }
    }
}
```
