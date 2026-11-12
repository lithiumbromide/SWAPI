---
title: "Create Aligned Linear and Ordinate Dimensions Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Aligned_Linear_And_Ordinate_Dimensions_Example_CSharp.htm"
---

# Create Aligned Linear and Ordinate Dimensions Example (C#)

This example shows how to create aligned linear and ordinate Dimensions for a closed PolyLine and Circles. A Leader and a geometric tolerance are also created.

```
//-------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
// 4. Add references to System and System.Forms.
// 5. Start DraftSight and open a document.
// 6. Click Start Debugging.
//
// Postconditions:
// 1. A closed PolyLine and four Circles are constructed.
// 2. Aligned linear and ordinate Dimensions are created.
//------------------------------------------------------------
using System;
using System.Runtime.InteropServices;
using DraftSight.Interop.dsAutomation;
using System.Windows.Forms;
```

```
namespace AlignedAndOrdinateDims_ToleranceAndLeader
{
    class Program
    {
        private static DraftSight.Interop.dsAutomation.Application dsApp;
```

```
        static void Main()
        {
            //Connect to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
	    dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands
```

```
            //Get active document
            Document dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }
```

```
            //Get model space
            Model dsModel = dsDoc.GetModel();
```

```
            //Get sketch manager
            SketchManager dsSketchMgr = dsModel.GetSketchManager();
```

```
            //Construct a closed PolyLine
            double[] coordinates = new double[] { 2, 2, 8, 2, 8, 8, 2, 8 };
            bool closed = true;
            PolyLine dsPolyline = dsSketchMgr.InsertPolyline2D(coordinates, closed);
```

```
            //Construct four Circles
            double centerX = 3.5;
            double centerY = 3.5;
            double centerZ = 0.0;
            double radius = 0.7;
            Circle dsFirstCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius);
```

```
            centerX = 6.5;
            Circle dsSecondCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius);
```

```
            centerX = 6.5;
            centerY = 6.5;
            Circle dsThirdCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius);
```

```
            centerX = 3.5;
            Circle dsFourthCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius);
```

```
            //Add aligned linear Dimensions
            double[] extLine1Point = new double[] { 2, 2, 0 };
            double[] extLine2Point = new double[] { 8, 2, 0 };
            double[] dimLinePoint = new double[] { 5, 1, 0 };
            string dimensionTextOverride = string.Empty;
            AlignedDimension dsFirstAlignedDim = dsSketchMgr.InsertAlignedDimension(extLine1Point, extLine2Point, dimLinePoint, dimensionTextOverride);
```

```
            extLine1Point[0] = 8;
            extLine1Point[1] = 2;
            extLine2Point[0] = 8;
            extLine2Point[1] = 8;
            dimLinePoint[0] = 9;
            dimLinePoint[1] = 5;
            AlignedDimension dsSecondAlignedDim = dsSketchMgr.InsertAlignedDimension(extLine1Point, extLine2Point, dimLinePoint, dimensionTextOverride);
```

```
            //Add ordinate Dimensions
            dsOrdinateDimensionMeasure_e measure = dsOrdinateDimensionMeasure_e.dsOrdinateDimensionMeasure_UseYAxis;
            double[] datumPosition = new double[] { 2, 2, 0 };
            double[] dimPosition = new double[] { 1, 2, 0 };
            OrdinateDimension dsFirstOrdinateDim = dsSketchMgr.InsertOrdinateDimension(datumPosition, dimPosition, dimensionTextOverride, measure);
```

```
            datumPosition[1] = 8;
            dimPosition[1] = 8;
            OrdinateDimension dsSecondOrdinateDim = dsSketchMgr.InsertOrdinateDimension(datumPosition, dimPosition, dimensionTextOverride, measure);
```

```
            //Add Leader
            double[] leaderCoordinates = new double[] { 6.5, 7.2, 0, 7.7, 8.6, 0 };
            double noteWidth = 1.0;
            string noteText = "4X";
            Leader dsLeader = dsSketchMgr.InsertLeader(leaderCoordinates, noteWidth, noteText);
```

```
            //Add a geometric tolerance
            double[] tolerancePosition = new double[]{ 8.2, 8.6, 0};
            string textString = "{\\Fgdt;j}%%v{\\Fgdt;n}0.7{\\Fgdt;m}";
            Tolerance dsTolerance = dsSketchMgr.InsertTolerance(tolerancePosition, textString);
```

```
            //Zoom to fit
            dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);
        }
    }
}
```
