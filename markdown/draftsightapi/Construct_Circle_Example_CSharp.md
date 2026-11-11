---
title: "Construct Circle Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_Circle_Example_CSharp.htm"
---

# Construct Circle Example (C#)

This example shows how to construct a Circle.

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
// Postconditions: A message box pops up when a Circle is
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
		Circle dsCircle = default(Circle);
		double centerX = 0;
		double centerY = 0;
		double centerZ = 0;
		double radius = 0;
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
			//Circle parameters
			centerX = 1.0;
			centerY = 2.0;
			centerZ = 0.0;
			radius = 5.0;
			//Construct a Circle
			dsCircle = dsSketchManager.InsertCircle(centerX, centerY, centerZ, radius);
			if ((dsCircle != null))
                        {
                             MessageBox.Show("Circle was added to drawing.");
			}
		}
                else
                {
                        MessageBox.Show("There are no open documents in DraftSight.");
		}
```

```
	}
}
```
