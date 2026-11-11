---
title: "Insert Block Instance Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Block_Instance_Example_CSharp.htm"
---

# Insert Block Instance Example (C#)

This example shows how to insert a Block instance in a drawing document.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add references to System and System.Windows.Forms.
// 5. Start DraftSight and open a new document.
// 6. If C:\Block.dwg exists, then skip this step.
//    - or -
//    If C:\Block.dwg does not exist, then construct
//    some geometry in the drawing, save the drawing
//    as C:\Block.dwg, and open a new drawing document.
// 7. Start debugging the project.
//
// Postconditions: A message box pops up when a Block Instance is
// inserted in the drawing document.
//----------------------------------------------------------------
```

```
using DraftSight.Interop.dsAutomation;
using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;
```

```
static class Module1
{
        static void Main(string[] args)
        {
        DraftSight.Interop.dsAutomation.Application dsApp;
        Document dsDoc = default(Document);
        Model dsModel = default(Model);
        SketchManager dsSketchManager = default(SketchManager);
        BlockInstance dsBlockInstance = default(BlockInstance);
        string pathName;
        double insertX = 0;
        double insertY = 0;
        double insertZ = 0;
        double scaleX = 0;
        double scaleY = 0;
        double scaleZ = 0;
        double rotation = 0;
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
```

```
            //Block instance parameters (rotation value should be in radians)
            pathName = "C:\\Block.dwg";
            insertX = 0.0;
            insertY = 0.0;
            insertZ = 0.0;
            scaleX = 1.0;
            scaleY = 1.0;
            scaleZ = 1.0;
            rotation = 0.0;
            //Add a Block instance
            dsBlockInstance = dsSketchManager.InsertBlock2(pathName, insertX, insertY, insertZ, scaleX, scaleY, scaleZ, rotation);
            if (dsBlockInstance != null)
            {
                MessageBox.Show("A Block instance from '" + pathName + "' file was added to the drawing.");
            }
            else
            {
                MessageBox.Show(pathName + " file was not found.");
            }
        }
        else
        {
            MessageBox.Show("There are no open documents in DraftSight.");
        }
    }
}
```
