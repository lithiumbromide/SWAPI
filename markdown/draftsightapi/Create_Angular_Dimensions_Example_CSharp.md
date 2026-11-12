---
title: "Create Angular Dimensions Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Angular_Dimensions_Example_CSharp.htm"
---

# Create Angular Dimensions Example (C#)

## Create Angular Dimension Example (C#)

This example shows how to create angular Dimensions using 3 points, 2 lines, and an arc.

```
//-------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add references to System and System.Windows.Forms.
// 5. Set a breakpoint at:
//    dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);
// 6. Start DraftSight and open a document.
// 7. Click Start Debugging.
//
// Postconditions:
// 1. Angular Dimensions using 3 points, 2 lines, and an arc are created.
// 2. Examine the Output or Immediate window.
// 3. Click Continue.
// 4. Examine the drawing.
//------------------------------------------------------------
```

```
using System;
using System.Collections.Generic;
using System.Text;
using DraftSight.Interop.dsAutomation;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Windows.Forms;
```

```
namespace AddAngularDimension
{
    class Program
    {
        private static DraftSight.Interop.dsAutomation.Application dsApp;
```

```
        static void Main(string[] args)
        {
            //Connect to the DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
	    dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands
```

```
            //Get the active document
            Document dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }
```

```
            //Get the model space
            Model dsModel = dsDoc.GetModel();
```

```
            //Get the sketch manager
            SketchManager dsSketchMgr = dsModel.GetSketchManager();
```

```
            //Add an angular Dimension using three points
            AngularDimension dsAngular3PointDim = AddAngularDimensionUsing3Points(dsSketchMgr);
```

```
            //Print the angular Dimension's properties
            PrintAngularDimProperties(dsAngular3PointDim);
```

```
            //Add an angular Dimension using two lines
            AngularDimension dsAngular2LinesDim = AddAngularDimensionUsing2Lines(dsSketchMgr);
```

```
            //Print the angular Dimension's properties
            PrintAngularDimProperties(dsAngular2LinesDim);
```

```
            //Add an angular Dimension for the arc
            AngularDimension dsAngularArcDim = AddAngularDimensionForArc(dsSketchMgr);
```

```
            //Print the angular Dimension's properties
            PrintAngularDimProperties(dsAngularArcDim);
```

```
            //Zoom to fit
            dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);
        }
```

```
        private static AngularDimension AddAngularDimensionForArc(SketchManager dsSketchMgr)
        {
            //Draw an arc
            double centerX = 18, centerY = 2, centerZ = 0;
            double radius = 3;
            double startAngle = 0.0, endAngle = Math.PI / 2;
            CircleArc dsArc = dsSketchMgr.InsertArc(centerX, centerY, centerZ, radius, startAngle, endAngle);
```

```
            //Angular Dimension's position
            double[] dimPosition = new double[] { 20, 5, 0 };
```

```
            //Text override
            string dimTextOverride = "AngularDimArc";
```

```
            AngularDimension dsAngularDim = dsSketchMgr.InsertAngularDimensionArc(dsArc, dimPosition, dimTextOverride);
```

```
            Debug.Print(Environment.NewLine + "An angular Dimension for an arc was added.");
```

```
            return dsAngularDim;
        }
```

```
        private static AngularDimension AddAngularDimensionUsing2Lines(SketchManager dsSketchMgr)
        {
            //Draw two lines for an angular Dimension
            Line dsFirstLine = dsSketchMgr.InsertLine(7, 0, 0, 10, 3, 0);
            Line dsSecondLine = dsSketchMgr.InsertLine(12, 0, 0, 15, 2, 0);
```

```
            //Angular Dimension position
            double[] dimPosition = new double[] { 13, 4, 0 };
```

```
            //No text override - empty string
            string dimTextOverride = string.Empty;
```

```
            AngularDimension dsAngularDim = dsSketchMgr.InsertAngularDimension2Line(dsFirstLine, dsSecondLine, dimPosition, dimTextOverride);
```

```
            Debug.Print(Environment.NewLine + "An angular Dimension using two lines was added.");
```

```
            return dsAngularDim;
        }
```

```
        private static AngularDimension AddAngularDimensionUsing3Points(SketchManager dsSketchMgr)
        {
            //Angular Dimension parameters
            double[] centerPoint = new double[] { 0, 0, 0 };
            double[] angleStartPoint = new double[] { 2, 2, 0 };
            double[] angleEndPoint = new double[] { 2, 4, 0 };
            double[] dimPosition = new double[] { 5, 5, 0 };
```

```
            //No text override - empty string
            string dimTextOverride = string.Empty;
```

```
            AngularDimension dsAngular3PointDim = dsSketchMgr.InsertAngularDimension3Point(centerPoint, angleStartPoint, angleEndPoint, dimPosition, dimTextOverride);
```

```
            Debug.Print(Environment.NewLine + "An angular Dimension using three points was added.");
```

```
            return dsAngular3PointDim;
        }
```

```
        private static void PrintAngularDimProperties(AngularDimension dsAngularDim)
        {
            Debug.Print("  Angular Dimension parameters...");
```

```
            Debug.Print("    Type = " + dsAngularDim.Type.ToString());
```

```
            //Get general Dimension object, which contains common Dimension properties
            GeneralDimension dsGeneralDim = dsAngularDim.GetGeneralDimension();
```

```
            Debug.Print("    Dimension style = " + dsGeneralDim.DimensionStyle);
            Debug.Print("    Handle = " + dsGeneralDim.Handle);
            Debug.Print("    Measurement (in radians) = " + dsGeneralDim.Measurement.ToString());
            Debug.Print("    Related = " + dsGeneralDim.Related.ToString());
            Debug.Print("    Text override = " + dsGeneralDim.TextOverride);
            Debug.Print("    Text rotation = " + dsGeneralDim.TextRotation);
```

```
            //Get text position
            double x, y;
            dsGeneralDim.GetTextPosition(out x, out y);
            Debug.Print("    Text position (" + x + "," + y + ")");
```

```
            //Print specific parameters for angular Dimension
            double z;
            //Get center point
            dsAngularDim.GetCenterPoint(out x, out y, out z);
            Debug.Print("    Center point (" + x + "," + y + "," + z + ")");
```

```
            //Get arc point
            dsAngularDim.GetArcPoint(out x, out y, out z);
            Debug.Print("    Arc point (" + x + "," + y + "," + z + ")");
```

```
            //Get first line's start point
            dsAngularDim.GetLine1Point(out x, out y, out z);
            Debug.Print("    Line1's start point (" + x + "," + y + "," + z + ")");
```

```
            //Get first line end point
            dsAngularDim.GetLine1EndPoint(out x, out y, out z);
            Debug.Print("    Line1's end point (" + x + "," + y + "," + z + ")");
```

```
            //Get second line start point
            dsAngularDim.GetLine2Point(out x, out y, out z);
            Debug.Print("    Line2's start point (" + x + "," + y + "," + z + ")");
```

```
            //Get second line end point
            dsAngularDim.GetLine2EndPoint(out x, out y, out z);
            Debug.Print("    Line2's end point (" + x + "," + y + "," + z + ")");
        }
    }
}
```
