---
title: "Construct RichLine Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_RichLine_Example_CSharp.htm"
---

# Construct RichLine Example (C#)

This example shows how to construct a RichLine.

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
// Postconditions: A message box pops up when a RichLine is
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
        RichLine dsRichLine = default(RichLine);
        double[] coordinates = new double[6];
        bool closed;
        dsRichLineJustification_e justification = default(dsRichLineJustification_e);
        double scaleValue;
        string styleName;
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
```

```
            //Get Sketch Manager
            dsSketchManager = dsModel.GetSketchManager();

            //RichLine parameters
            coordinates[0] = 0.0;
            coordinates[1] = 0.0;
            coordinates[2] = 0.0;
            coordinates[3] = 7.0;
            coordinates[4] = 7.0;
            coordinates[5] = 0.0;
            scaleValue = 1.0;
            styleName = "Standard";
            closed = false;
            justification = dsRichLineJustification_e.dsRichLineJustification_Bottom;
```

```
            //Add a RichLine
            dsRichLine = dsSketchManager.InsertRichLine(coordinates, justification, scaleValue, styleName, closed);
```

```
            if (dsRichLine != null)
            {
                MessageBox.Show("RichLine was added to drawing.");
            }
        }
        else
        {
            MessageBox.Show("There are no open documents in DraftSight.");
        }
    }
}
```
