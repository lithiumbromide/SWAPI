---
title: "Create Tracker Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Tracker_Example_CSharp.htm"
---

# Create Tracker Example (C#)

This example shows how to create a tracker and add a temporary entity to the tracker.

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
// 1. Creates a temporary Circle for the tracker.
// 2. Creates a tracker and adds the temporary Circle to the
//    the tracker.
// 3. Examine the pointer in the drawing to verify.
// 4. Prompts you to click in the drawing to insert a Circle.
// 5. Inserts a Circle in the drawing at the point where you clicked.
//----------------------------------------------------------------

using System;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace TrackerCSharp
{
    class Program
    {
        private static DraftSight.Interop.dsAutomation.Application dsApp;
        private static Circle dsTempCircle;

        static void Main(string[] args)
        {
            //Connect to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            // Abort any command currently running in DraftSight to avoid nested commands
            dsApp.AbortRunningCommand();

            if (null == dsApp)
            {
                return;
            }

            //Get active document
            Document dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }

            //Get Sketch Manager
            SketchManager dsSketchMgr = dsDoc.GetModel().GetSketchManager();

            //Create temporary Circle
            dsApp.TemporaryEntityMode = true;
            dsTempCircle = dsSketchMgr.InsertCircle(0, 0, 0, 10);
            dsApp.TemporaryEntityMode = false;

            //Create tracker and add temporary Circle
            Tracker dsTracker = dsApp.CreateTracker();
            dsTracker.AddTemporaryEntity(dsTempCircle);

            //Prompt for point where to insert Circle
            //Before prompt, add tracker to command message
            CommandMessage dsCmdMsg = dsApp.GetCommandMessage();
            dsCmdMsg.AddTracker(dsTracker);

            double X = 0.0;
            double Y = 0.0;
            double Z = 0.0;
            dsTracker.UpdateNotify += new _ITrackerEvents_UpdateNotifyEventHandler(dsTracker_UpdateNotify);
            bool res = dsCmdMsg.PromptForPoint("Click to insert Circle", out X, out Y, out Z);
            dsTracker.UpdateNotify -= new _ITrackerEvents_UpdateNotifyEventHandler(dsTracker_UpdateNotify);

            if (res == true)
            {
                //Set the center of the Circle where user clicked
                dsTempCircle.SetCenter(X, Y, Z);
                //Add temporary Circle to drawing
                dsSketchMgr.AddTemporaryEntity(dsTempCircle);
            }
            //Remove tracker from command message if no longer needed
            dsCmdMsg.RemoveTracker(dsTracker);
        }

        private static void dsTracker_UpdateNotify(MathPoint CursorPosition)
        {
            if (CursorPosition == null)
                return;

            double x = 0.0, y = 0.0, z = 0.0;
            CursorPosition.GetPosition(out x, out y, out z);

            dsTempCircle.SetCenter(x, y, z);

        }
    }
}
```
