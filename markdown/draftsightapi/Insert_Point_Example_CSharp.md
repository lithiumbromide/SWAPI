---
title: "Insert Point Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Point_Example_CSharp.htm"
---

# Insert Point Example (C#)

This example shows how to insert a point in a drawing document.

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
// Postconditions: A message box pops up when a point is
// inserted in the drawing document. A SimpleNote is also
// added to the drawing that identifies where the point was inserted.
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
        Point dsPoint = default(Point);
        SimpleNote dsSimpleNote = default(SimpleNote);
        double x = 0;
        double y = 0;
        double z = 0;
        string noteValue;
        double angle = 0;
        double height;

        //Connect to DraftSight
        dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
	dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands
```

```
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
            //Point parameters (angle value should be passed in radians)
            x = 5.0;
            y = 5.0;
            z = 0.0;
```

```
            //Add a point
            dsPoint = dsSketchManager.InsertPoint(x, y, z);

            //SimplePoint parameters (angle value should be passed in radians)
            noteValue = "Sample text";
            height = 1.0;
            angle = Math.PI / 4; //45 degrees in radians
```

```
            //Add a simple note
            dsSimpleNote = dsSketchManager.InsertSimpleNote(x, y,z, height, angle, noteValue);
```

```
            if (dsPoint != null)
            {
                MessageBox.Show("Point was added to drawing where SimpleNote was added.");
            }
        }
        else
        {
            MessageBox.Show("There are no open documents in DraftSight.");
        }
    }
```

```
}
```
