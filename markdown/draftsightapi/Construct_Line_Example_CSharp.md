---
title: "Construct Line Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_Line_Example_CSharp.htm"
---

# Construct Line Example (C#)

This example shows how to construct a Line.

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
// Postconditions: A message box pops up when a Line is
// constructed and its color changed in the drawing document.
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
        Line dsLine = default(Line);
        Color dsColor = default(Color);
        double startX = 0;
        double startY = 0;
        double startZ = 0;
        double endX = 0;
        double endY = 0;
        double endZ = 0;
```

```
        //Connect to DraftSight
        dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
	dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands
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
            //Get Sketch Manager
            dsSketchManager = dsModel.GetSketchManager();
```

```
            //Line parameters
            startX = 1.0;
            startY = 1.0;
            startZ = 0.0;
            endX = 6.0;
            endY = 1.0;
            endZ = 0.0;
            //Construct a Line
            dsLine = (dsSketchManager.InsertLine(startX, startY, startZ, endX, endY, endZ);

            if (dsLine != null)
            {

                //Change line's color
                dsColor = dsLine.Color;
                dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Red);
                dsLine.Color = dsColor;

                MessageBox.Show("Line was added to drawing and its color changed to red.");
            }
        }
        else
        {
            MessageBox.Show("There are no open documents in DraftSight.");
        }
    }
}
```
