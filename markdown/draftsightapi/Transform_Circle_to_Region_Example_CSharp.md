---
title: "Transform Circle to Region Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Transform_Circle_to_Region_Example_CSharp.htm"
---

# Transform Circle to Region Example (C#)

This example shows how to transform a Circle to a Region.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
// 4. Add references to System and System.Windows.Forms.
// 5. Start DraftSight.
// 6. Open the Immediate window.
// 7. Press F5 to debug the project.
//
// Postconditions:
// 1. A Circle is constructed in the drawing document.
// 2. The Circle is transformed to a Region.
// 3. Whether the Region is visible and its perimeter value are
//    printed to the Immediate window.
//----------------------------------------------------------------
using DraftSight.Interop.dsAutomation;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.Diagnostics;
using System;

static class Module1
{

    public static void Main()
    {
        Document dsDoc = default(Document);
        Model dsModel = default(Model);
        SketchManager dsSketchManager = default(SketchManager);
        SelectionManager dsSelectionManager = default(SelectionManager);
        Circle dsCircle = default(Circle);
        double centerX = 0;
        double centerY = 0;
        double centerZ = 0;
        double radius = 0;
        double perimeter = 0;
        bool status = false;

        // Connect to DraftSight
        DraftSight.Interop.dsAutomation.Application dsApp = ConnectToDraftSight();
        if (null == dsApp)
        {
            return;
        }
```

```
        // Abort any command currently running in DraftSight to
        // avoid nested commands
        dsApp.AbortRunningCommand();

        // Get active document
        dsDoc = dsApp.GetActiveDocument();
        if (dsDoc == null)
        {
            MessageBox.Show("There are no open documents in DraftSight.");
            return;
        }

        // Get model space
        dsModel = dsDoc.GetModel();

        // Get Sketch Manager
        dsSketchManager = (SketchManager)dsModel.GetSketchManager();

        // Circle parameters
        centerX = 1.0;
        centerY = 2.0;
        centerZ = 0.0;
        radius = 5.0;

        // Construct a Circle
        dsCircle = dsSketchManager.InsertCircle(centerX, centerY, centerZ, radius);

        // Select the Circle
        status = dsCircle.Select(true);

        if (status)
        {
            // Get selected Circle
            dsSelectionManager = dsDoc.GetSelectionManager();
            dsObjectType_e objType;
            object dsObj = dsSelectionManager.GetSelectedObject(dsSelectionSetType_e.dsSelectionSetType_Current, 0, out objType);
            DispatchWrapper[] dsSelObj = new DispatchWrapper[1];
            dsSelObj[0] = new DispatchWrapper(dsObj);
            object dsSelObject = dsSelObj;

            // Transform Circle to Region
            object regions;
            dsSketchManager.InsertRegion(dsSelObject, out regions);
            object[] dsRegionObjs = (object[])regions;
            foreach (object regionObj in dsRegionObjs)
            {
                Region dsRegion = regionObj as Region;

                // Is Region visible?
                status = dsRegion.Visible;
                Debug.Print("Is Region visible? " + status);

                // Get perimeter of Region
                dsRegion.GetPerimeter(out perimeter);
                Debug.Print("Perimeter of Region: " + perimeter);
            }

        }

    }
    private static DraftSight.Interop.dsAutomation.Application ConnectToDraftSight()
    {
        DraftSight.Interop.dsAutomation.Application dsApp = null;

        try
        {
            // Connect to DraftSight
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
        }
        catch (Exception ex)
        {
            MessageBox.Show("Failed to connect to DraftSight. Cause: " + ex.Message);
            dsApp = null;
        }

        return dsApp;

    }
}
```
