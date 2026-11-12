---
title: "Construct InfiniteLine Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_InfiniteLine_Example_CSharp.htm"
---

# Construct InfiniteLine Example (C#)

This example shows how to construct an InfiniteLine.

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
// Postconditions: A message box pops up when an InfiniteLine is
// constructed in the drawing document.
//----------------------------------------------------------------
using DraftSight.Interop.dsAutomation;
using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;
static class Module1
{
    public static void Main()
    {
        DraftSight.Interop.dsAutomation.Application dsApp;
        Document dsDoc = default(Document);
        Model dsModel = default(Model);
        SketchManager dsSketchManager = default(SketchManager);
        InfiniteLine dsInfiniteLine = default(InfiniteLine);
        double x1 = 0;
        double y1 = 0;
        double z1 = 0;
        double x2 = 0;
        double y2 = 0;
        double z2 = 0;
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
```

```
           //InfiniteLine parameters
            x1 = 0.0;
            y1 = 0.0;
            z1 = 0.0;
            x2 = 1.0;
            y2 = 5.0;
            z2 = 0.0;
```

```
            //Construct an InfiniteLine
            dsInfiniteLine = dsSketchManager.InsertInfiniteLine(x1, y1, z1, x2, y2, z2);
            if (dsInfiniteLine != null)
            {
                MessageBox.Show("InfiniteLine was added to drawing.");
            }
        }
        else
        {
            MessageBox.Show("There are no open documents in DraftSight.");
        }
    }
}
```
