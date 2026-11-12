---
title: "Create and Change Trace Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Change_Trace_Example_CSharp.htm"
---

# Create and Change Trace Example (C#)

This example shows how to create a Trace and change its vertex coordinates and thickness.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this code into the C# project.
// 3. Add a reference to
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add a reference to System.Windows.Forms.
// 5. Start DraftSight.
// 6. Press F5.
//
// Postconditions:
// 1. Connects to DraftSight.
// 2. Gets the active document.
// 3. Creates a Trace.
// 4. Sets the vertex coordinates of the Trace.
// 5. Sets the thickness of the Trace.
// 6. Gets the vertex coordinates of the Trace.
//    Click OK to close each message box.
// 7. Gets the thickness of the Trace.
//    Click OK to close the message box.
//----------------------------------------------------------------

using System;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace TraceCSharp
{
    class Program
    {

        static void Main()
        {
            DraftSight.Interop.dsAutomation.Application dsApp;

            //Connects to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            if (null == dsApp)
            {
                return;
            }

            //Aborts any command currently running in DraftSight
            //to avoid nested commands
            dsApp.AbortRunningCommand();

            //Gets active document
            Document dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }

            //Gets Sketch Manager
            SketchManager dsSketchMgr = dsDoc.GetModel().GetSketchManager();

            //Creates array for Trace vertex coordinates
            double[] CoordinatesArray =
            {
                0, 0, 0,
                5, 5, 0,
                -1, 10, 0,
                4, 8, 0
            };

            //Creates Trace
            Trace dsTrace = dsSketchMgr.InsertTrace(CoordinatesArray);

            //Sets the vertex coordinates of trace
            dsTrace.SetVertex1Coordinate(1.2, 2.0, 0.0);
            dsTrace.SetVertex2Coordinate(1.1, 2.3, 0.0);
            dsTrace.SetVertex3Coordinate(2.2, 1.0, 0.0);
            dsTrace.SetVertex4Coordinate(2.2, 3.0, 0.0);

            //Sets Trace thickness
            dsTrace.Thickness = 2.0;

            //Gets Trace vertex coordinates
            double X, Y, Z;
            dsTrace.GetVertex1Coordinate(out X, out Y, out Z);
            MessageBox.Show("GetVertex1Coordinate: (" + X + ", " + Y + ", " + Z + ")");

            dsTrace.GetVertex2Coordinate(out X, out Y, out Z);
            MessageBox.Show("GetVertex2Coordinate: (" + X + ", " + Y + ", " + Z + ")");

            dsTrace.GetVertex3Coordinate(out X, out Y, out Z);
            MessageBox.Show("GetVertex3Coordinate: (" + X + ", " + Y + ", " + Z + ")");

            dsTrace.GetVertex3Coordinate(out X, out Y, out  Z);
            MessageBox.Show("GetVertex4Coordinate: (" + X + ", " + Y + ", " + Z + ")");

            //Gets Trace thickness
            MessageBox.Show("Thickness: " + dsTrace.Thickness);
        }
    }
}
```
