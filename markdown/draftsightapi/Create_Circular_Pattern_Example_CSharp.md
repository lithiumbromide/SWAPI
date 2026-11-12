---
title: "Create Circular Pattern Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Circular_Pattern_Example_CSharp.htm"
---

# Create Circular Pattern Example (C#)

This example shows how to construct a circular pattern of Circles in a DraftSight drawing.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add references to System and System.Windows.Forms.
// 5. Start DraftSight and open a drawing document.
// 6. Run the macro.
//
// Postconditions:
// 1. Constructs three Circles.
// 2. Creates a circular pattern using the Circles.
// 3. Zooms the drawing to fit.
// 4. Examine the drawing.
//----------------------------------------------------------------
using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using DraftSight.Interop.dsAutomation;
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
		Circle dsCircle1 = default(Circle);
		Circle dsCircle2 = default(Circle);
		Circle dsCircle3 = default(Circle);
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
		if ((dsDoc != null)) {
			//Get model space
			dsModel = dsDoc.GetModel();
```

```
			//Get Sketch Manager
			dsSketchManager = dsModel.GetSketchManager();
```

```
			//Circle parameters
			double center1X = 0;
			double center2X = 0;
			double center3X = 0;
			center1X = 30.0;
			center2X = 60.0;
			center3X = 90.0;
```

```
			double center1Y = 0;
			double center2Y = 0;
			double center3Y = 0;
			center1Y = 30.0;
			center2Y = 60.0;
			center3Y = 90.0;
```

```
			double center1Z = 0;
			double center2Z = 0;
			double center3Z = 0;
			center1Z = 0.0;
			center2Z = 0.0;
			center3Z = 0.0;
```

```
			double radius1 = 0;
			double radius2 = 0;
			double radius3 = 0;
			radius1 = 10.0;
			radius2 = 10.0;
			radius3 = 10.0;
```

```
			//Draw the Circles
			dsCircle1 = dsSketchManager.InsertCircle(center1X, center1Y, center1Z, radius1);
			dsCircle2 = dsSketchManager.InsertCircle(center2X, center2Y, center2Z, radius2);
			dsCircle3 = dsSketchManager.InsertCircle(center3X, center3Y, center3Z, radius3);
```

```
			//Circular pattern parameters
			double angleBetween = 0;
			angleBetween = 3.14159265358979 / 2;  //90 degrees in radians
```

```
			double fillAngle = 0;
			fillAngle = 4.71238898; //270 degrees in radians
```

```
			int totalNumber = 0;
			totalNumber = 4;
```

```
			double elementBasePointX = 0;
			double elementBasePointY = 0;
			double axisPointX = 0;
			double axisPointY = 0;
			elementBasePointX = 0.0;
			elementBasePointY = 0.0;
			axisPointX = 0.0;
			axisPointY = 0.0;
```

```
			bool orientElementsAboutAxis = false;
			orientElementsAboutAxis = true;
```

```
			//Prepare list of entity types
			int[] dsEntityTypes = new int[3];
			dsEntityTypes[0] = (int)dsObjectType_e.dsCircleType;
			dsEntityTypes[1] = (int)dsObjectType_e.dsCircleType;
			dsEntityTypes[2] = (int)dsObjectType_e.dsCircleType;
```

```
			//Prepare list of entities
			DispatchWrapper[] dsEntities = new DispatchWrapper[3];
			dsEntities[0] = new DispatchWrapper(dsCircle1);
			dsEntities[1] = new DispatchWrapper(dsCircle2);
			dsEntities[2] = new DispatchWrapper(dsCircle3);
```

```
			//Create circular pattern
			dsSketchManager.PatternCircular(dsBasePatternOn_e.dsBasePatternOn_AngleBetweenAndElementsNumber, angleBetween, fillAngle, totalNumber, elementBasePointX, elementBasePointY, axisPointX, axisPointY, orientElementsAboutAxis, dsEntityTypes,
			dsEntities);
```

```
			//Zoom to fit
			dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);
```

```
		} else {
			MessageBox.Show("There are no open documents in DraftSight.");
```

```
		}
	}
```

```
}
```
