---
title: "Construct Ellipses and Elliptical Arcs Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_Ellipses_and_Elliptical_Arcs_Example_CSharp.htm"
---

# Construct Ellipses and Elliptical Arcs Example (C#)

This example shows how to construct Ellipses and elliptical Arcs.

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
// Postconditions: A message box pops up when an Ellipse or
// elliptical Arc is inserted in the drawing document.
//----------------------------------------------------------------
using DraftSight.Interop.dsAutomation;
using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;
```

```
static class Module1
{
```

```
    public static void Main()
	{
		DraftSight.Interop.dsAutomation.Application dsApp;
		Document dsDoc = default(Document);
		Model dsModel = default(Model);
		SketchManager dsSketchManager = default(SketchManager);
		EllipseArc dsEllipseRotation = default(EllipseArc);
		EllipseArc dsEllipseDistance = default(EllipseArc);
		EllipseArc dsEllipseArcDistance = default(EllipseArc);
		EllipseArc dsEllipseArcRotation = default(EllipseArc);
		double x1 = 0;
		double y1 = 0;
		double x2 = 0;
		double y2 = 0;
		double rotation = 0;
		double distanceToOtherAxis = 0;
		double startAngle = 0;
		double endAngle = 0;
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
```

```
			//Get Sketch Manager
			dsSketchManager = dsModel.GetSketchManager();
```

```
			//Ellipse rotation parameters (rotation parameter should be in radians)
			x1 = 0.0;
			y1 = 0.0;
			x2 = 10.0;
			y2 = 0.0;
			rotation = Math.PI / 4;      //45 degrees in radians
			//Draw an ellipse
			dsEllipseRotation = dsSketchManager.InsertEllipseRotation(x1, y1, x2, y2, rotation);
```

```
			//Ellipse distance parameters
			x1 = 0.0;
			y1 = 0.0;
			x2 = 10.0;
			y2 = 0.0;
			distanceToOtherAxis = 3.0;
			//Draw an ellipse
			dsEllipseDistance = dsSketchManager.InsertEllipseDistanceToOtherAxis(x1, y1, x2, y2, distanceToOtherAxis);
```

```
			//Elliptical Arc distance parameters (start and end angle parameters should be in radians)
			x1 = 0.0;
			y1 = 0.0;
			x2 = 10.0;
			y2 = 0.0;
			distanceToOtherAxis = 2.0;
			startAngle = 0.0;
			endAngle = Math.PI;  //180 degrees in radians
			//Draw an elliptical Arc
			dsEllipseArcDistance = dsSketchManager.InsertEllipseArcDistanceToOtherAxis(x1, y1, x2, y2, distanceToOtherAxis, startAngle, endAngle);
```

```
			//Ellipitcal Arc rotation parameters (rotation, start, and end angle parameters should be in radians)
			x1 = 0.0;
			y1 = 0.0;
			x2 = 10.0;
			y2 = 0.0;
			rotation = Math.PI / 4;   //45 degrees in radians
			startAngle = 0.0;
			endAngle = 3.14159265358979;
			//180 degrees in radians
			//Draw an elliptical Arc
			dsEllipseArcRotation = dsSketchManager.InsertEllipseArcRotation(x1, y1, x2, y2, rotation, startAngle, endAngle);
```

```
			if (dsEllipseRotation != null)
                        {
				MessageBox.Show("An ellipse using the specified axes end points and the angle of rotation was added to drawing.");
			}
```

```
			if (dsEllipseDistance != null)
                        {
				MessageBox.Show("An ellipse using the specified axes end points and radius of the perpendicular axis was added to drawing.");
			}
```

```
			if (dsEllipseArcDistance != null)
                        {
				MessageBox.Show("An elliptical Arc using the specified axes end points and radius of the perpendicular axis was added to drawing.");
			}
```

```
			if (dsEllipseArcRotation != null)
                        {
				MessageBox.Show("An elliptical Arc using the specified axes end points, angle of rotation, and start and end angles was added to drawing.");
			}
```

```
		}
                else
                {
			MessageBox.Show("There are no open documents in DraftSight.");
```

```
		}
```

```
	}
```

```
}
```
