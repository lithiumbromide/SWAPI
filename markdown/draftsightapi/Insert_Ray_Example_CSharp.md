---
title: "Insert Ray Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Ray_Example_CSharp.htm"
---

# Insert Ray Example (C#)

This example shows how to insert a Ray in a drawing document.

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
// Postconditions: A message box pops up when a Ray is
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
        Ray dsRay = default(Ray);
        double startX = 0;
        double startY = 0;
        double startZ = 0;
        double throughX = 0;
        double throughY = 0;
        double throughZ = 0;
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
            //Ray parameters
            startX = 0.0;
            startY = 0.0;
            startZ = 0.0;
            throughX = 2.0;
            throughY = 3.0;
            throughZ = 0.0;
            //Insert a Ray
            dsRay = dsSketchManager.InsertRay(startX, startY, startZ, throughX, throughY, throughZ);
            if (dsRay != null)
            {
                MessageBox.Show("Ray was added to drawing.");
            }
        }
        else
        {
            MessageBox.Show("There are no open documents in DraftSight.");
        }
    }
}
```
