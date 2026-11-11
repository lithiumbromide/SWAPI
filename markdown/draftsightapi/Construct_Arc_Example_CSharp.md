---
title: "Construct Arc Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_Arc_Example_CSharp.htm"
---

# Construct Arc Example (C#)

This example shows how to construct an Arc.

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
// Postconditions: A message box pops up when an Arc is
// constructed in the drawing document.
//----------------------------------------------------------------
using DraftSight.Interop.dsAutomation;
using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;
```

```
static class Module1
{
    public static void Main()
    {
        DraftSight.Interop.dsAutomation.Application dsApp;
        Document dsDoc = default(Document);
        Model dsModel = default(Model);
        SketchManager dsSketchManager = default(SketchManager);
        CircleArc dsArc = default(CircleArc);
        double centerX = 0;
        double centerY = 0;
        double centerZ = 0;
        double radius = 0;
        double startAngle = 0;
        double endAngle = 0;
```

```
        //Connect to DraftSight
        dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
	dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands
        //Get active document
        dsDoc = dsApp.GetActiveDocument();
        if (dsDoc != null)
        {
            //Get model space
            dsModel = dsDoc.GetModel();

            //Get Sketch Manager
            dsSketchManager = dsModel.GetSketchManager();

            //Arc parameters (start and end angle values should be in radians)
            centerX = 0.0;
            centerY = 0.0;
            centerZ = 0.0;
            radius = 4.0;
            startAngle = 0.0;
	    endAngle = Math.PI;
```

```
            //Construct an Arc
            dsArc = dsSketchManager.InsertArc(centerX, centerY, centerZ, radius, startAngle, endAngle);

            if (dsArc != null)
            {
                MessageBox.Show("An Arc was added to drawing.");
            }
        }
        else
        {
            MessageBox.Show("There are no open documents in DraftSight.");
        }
    }
}
```
