---
title: "Construct 2D PolyLine Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_2D_PolyLine_Example_CSharp.htm"
---

# Construct 2D PolyLine Example (C#)

This example shows how to construct a 2D PolyLine in a drawing document.

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
// Postconditions: A message box pops up when a 2D PolyLine is
// inserted in the drawing document.
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
        PolyLine dsPolyLine = default(PolyLine);
        double[] coordinates = new double[8];
        bool closed;
```

```
        //Connect to DraftSight
        dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
	dsApp.AbortRunningCommand(); //abort any command currently running in DraftSight to avoid nested commands
```

```
        //Get active document
        dsDoc = dsApp.GetActiveDocument();
```

```
        if (dsDoc != null)
        {
            //Get model space
            dsModel = dsDoc.GetModel();
```

```
            //Get Sketch Manager
            dsSketchManager = dsModel.GetSketchManager();
```

```
            //2D PolyLine parameters
            coordinates[0] = 0.0;
            coordinates[1] = 2.0;
            coordinates[2] = 0.0;
            coordinates[3] = 0.0;
            coordinates[4] = 6.0;
            coordinates[5] = 0.0;
            coordinates[6] = 6.0;
            coordinates[7] = 2.0;
            closed = true;
```

```
            //Add a 2D PolyLine
            dsPolyLine = dsSketchManager.InsertPolyline2D(coordinates, closed);
```

```
            if (dsPolyLine != null)
            {
                MessageBox.Show("2D PolyLine was added to drawing.");
            }
        }
        else
        {
            MessageBox.Show("There are no open documents in DraftSight.");
        }
    }
}
```
