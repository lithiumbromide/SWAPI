---
title: "Create Highlight Selection set Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Highlight_Selection_Set_Example_CSharp.htm"
---

# Create Highlight Selection set Example (C#)

## Create Highlight Selection Set Example (C#)

This example shows how to create a highlight selection set.

```
//--------------------------------------------------------------
// Preconditions:
//  1. Create a C# Windows console project.
//  2. Copy and paste this example into the C# IDE.
//  3. Add a reference to:
//     install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
//  4. Add a reference to System.Windows.Forms.
//  5. Start DraftSight.
//  6. Press F5.
//
// Postconditions:
//  1. Connects to DraftSight.
//  2. Gets active document.
//  3. Gets Sketch Manager.
//  4. Inserts a Circle and an Arc.
//  5. Creates an instance of a highlight selection set.
//  6. Adds Arc to the highlight selection set.
//  7. Move the pointer over both the Arc and Circle. Only the Arc
//     is highlighted. Press F5 to continue.
//  8. Removes Arc from highlight selection set.
//  9. Adds Circle to highlight selection set.
// 10. Move the pointer over both the Arc and Circle. Only
//     the Circle is highlighted.
//--------------------------------------------------------------

using System;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace HighlightSetCSharp
{
    class Program
    {
        private static DraftSight.Interop.dsAutomation.Application dsApp;

        static void Main(string[] args)
        {
            //Connect to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            if (null == dsApp)
            {
                return;
            }

            //Abort any command currently running in DraftSight to avoid nested commands
            dsApp.AbortRunningCommand();

            //Get active document
            Document dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }

            //Get Sketch Manager
            SketchManager dsSketchMgr = dsDoc.GetModel().GetSketchManager();

            //Draw a Circle and Arc
            Circle dsCircle = dsSketchMgr.InsertCircle(5.0, 5.0, 0.0, 10.0);
            CircleArc dsCircleArc = dsSketchMgr.InsertArc(7.5, 7.5, 0.0, 10.0, 2.5, 5.0);
            dsApp.Zoom(dsZoomRange_e.dsZoomRange_Bounds, null, null);

            //Create highlight selection set
            DispatchWrapper[] dsEntities = new DispatchWrapper[1];
            dsEntities[0] = new DispatchWrapper(dsCircleArc);

            HighlightSet dsHighlightSet = dsDoc.CreateHighlightSet(dsEntities);
            dsHighlightSet.Highlight = true;
            dsDoc.Rebuild(dsRebuildType_e.dsRebuildType_AllViewports);

            System.Diagnostics.Debugger.Break();
            //Move pointer over the Arc and Circle
            //Only the Arc is highlighted
            //Press F5 to continue

            //Remove entities from highlight selection set
            dsHighlightSet.RemoveEntities(dsEntities);
            dsDoc.Rebuild(dsRebuildType_e.dsRebuildType_AllViewports);

            //Add Circle to highlight selection set
            dsEntities.Initialize();
            dsEntities[0] = new DispatchWrapper(dsCircle);
            dsHighlightSet.AddEntities(dsEntities);
            dsHighlightSet.Highlight = true;
            dsDoc.Rebuild(dsRebuildType_e.dsRebuildType_AllViewports);

            //Move pointer over the Arc and Circle
            //Only the Circle is highlighted

        }
    }
}
```
