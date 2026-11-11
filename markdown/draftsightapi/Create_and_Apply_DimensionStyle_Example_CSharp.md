---
title: "Create and Apply DimensionStyle Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Apply_DimensionStyle_Example_CSharp.htm"
---

# Create and Apply DimensionStyle Example (C#)

This example shows how to create, activate, and apply a new DimensionStyle. This example also shows how to create arc length, jogged, rotated, radius, and diameter Dimensions for circles, arcs, and a line.

```
//-------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
// 4. Add references to System and System.Windows.Forms.
// 5. Set a breakpoint at:
//    dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);
// 6. Start DraftSight and open a document.
// 7. Click Start Debugging.
//
// Postconditions:
// 1. A new DimensionStyle named SampleDimStyle is created and
//    activated.
// 2. Arc length, jogged, rotated, radius, and diameter dimensions
//    are created for circles, arcs, and a line, using the new
//    DimensionStyle.
// 3. Examine the Output or Immediate window.
// 4. Click Continue.
// 5. Examine the drawing.
//------------------------------------------------------------
```

```
using System;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System.Diagnostics;
```

```
namespace AddArcLengthAndJoggedDimension
{
    class Program
    {
        private static DraftSight.Interop.dsAutomation.Application dsApp;
```

```
        static void Main(string[] args)
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
            //Get DimensionStyle manager
            DimensionStyleManager dsDimStyleManager = dsDoc.GetDimensionStyleManager();
```

```
            //Create DimensionStyle named SampleDimStyle
            dsCreateObjectResult_e createDimStyleResult;
            string dimStyleName = "SampleDimStyle";
            DimensionStyle dsDimStyle;
            dsDimStyleManager.CreateDimensionStyle(dimStyleName, out dsDimStyle, out createDimStyleResult);
            if(dsCreateObjectResult_e.dsCreateObjectResult_Error == createDimStyleResult ||
               dsCreateObjectResult_e.dsCreateObjectResult_AlreadyExists == createDimStyleResult ||
               null == dsDimStyle)
            {
                MessageBox.Show("Failed to create " + dimStyleName + " DimensionStyle, or DimensionStyle already exists.");
                return;
            }
```

```
            SetDimensionStyleSettings(dsDimStyle);
```

```
            //Activate DimensionStyle
            dsDimStyle.Activate();
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
            //Draw arc length Dimension
            DrawArcLengthDimension(dsSketchMgr);
```

```
            //Draw jogged Dimension for circle and arc
            DrawJoggedDimension(dsSketchMgr);
```

```
            //Draw rotated Dimension
            DrawRotatedDimension(dsSketchMgr);
```

```
            //Draw radius Dimension for circle and arc
            DrawRadialDimension(dsSketchMgr);
```

```
            //Draw diameter Dimension for circle and arc
            DrawDiameterDimension(dsSketchMgr);
```

```
            //Zoom to fit
            dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);
        }
```

```
        private static void SetDimensionStyleSettings(DimensionStyle dsDimStyle)
        {
            //Get DimensionStyle arrows options
            DimensionStyleArrowsOptions dsArrowsDimStyleOptions = dsDimStyle.GetDimensionStyleArrowsOptions();
```

```
            //Set start and end arrow types
            dsArrowsDimStyleOptions.SetStartArrow(dsDimensionArrowType_e.dsDimensionArrowType_ClosedBlank, string.Empty);
            dsArrowsDimStyleOptions.SetEndArrow(dsDimensionArrowType_e.dsDimensionArrowType_ClosedBlank, string.Empty);
```

```
            //Get DimensionStyle line options
            DimensionStyleLineOptions dsLineDimStyleOptions = dsDimStyle.GetDimensionStyleLineOptions();
```

```
            //Set Dimension line color
            Color dsColor = dsLineDimStyleOptions.DimensionLineColor;
            dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Green);
            dsLineDimStyleOptions.DimensionLineColor = dsColor;
```

```
            //Set extension line color
            dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Yellow);
            dsLineDimStyleOptions.ExtensionLineColor = dsColor;
```

```
            //Get DimensionStyle radius and diameter Dimension options
            DimensionStyleRadialDiameterDimensionOptions dsRadialAndDiameterDimStyleOptions = dsDimStyle.GetDimensionStyleRadialDiameterDimensionOptions();
```

```
            //Set jog angle 45 degrees (in radians)
            dsRadialAndDiameterDimStyleOptions.RadiusDimensionJogAngle = Math.PI / 4;
```

```
            //Set center mark
            double markSize = 0.05;
            dsRadialAndDiameterDimStyleOptions.SetCenterMarkDisplay(dsDimensionCenterMarkDisplay_e.dsDimensionCenterMarkDisplay_AsMark, markSize);
```

```
            //Get Dimension style text options
            DimensionStyleTextOptions dsTextOptions = dsDimStyle.GetDimensionStyleTextOptions();
```

```
            //Frame Dimension text
            dsTextOptions.FrameDimensionText = true;
```

```
            //Set text position
            dsTextOptions.HorizontalPosition = dsDimensionTextHorizontalPosition_e.dsDimensionTextHorizontalPosition_Centered;
            dsTextOptions.VerticalPosition = dsDimensionTextVerticalPosition_e.dsDimensionTextVerticalPosition_Centered;
```

```
            //Set text alignment
            dsTextOptions.Alignment = dsDimensionTextAlignment_e.dsDimensionTextAlignment_AlignWithDimensionLines;
        }
```

```
        private static void DrawArcLengthDimension(SketchManager dsSketchMgr)
        {
            //Add arc to drawing
            double centerX = -8;
            double centerY = 1;
            double centerZ = 0;
            double radius = 5;
            double startAngle = Math.PI / 6;
            double endAngle = Math.PI;
            CircleArc dsArc = dsSketchMgr.InsertArc(centerX, centerY, centerZ, radius, startAngle, endAngle);
```

```
            //Add arc length Dimension
            double[] dimensionPosition = new double[] { -6, 6, 0 };
            string dimensionTextOverride = string.Empty;
            ArcLengthDimension dsArcLengthDim = dsSketchMgr.InsertArcLengthDimension(dsArc, dimensionPosition, dimensionTextOverride);
```

```
            //Print information about arc length Dimension
            PrintArcLengthDimProperties(dsArcLengthDim);
```

```
            //Add a partial arc length Dimension
            double[] firstPoint = new double[] { -4, 3, 0 };
            double[] secondPoint = new double[] { -7, 6, 0 };
            dimensionPosition[0] = -6;
            dimensionPosition[1] = 7;
            ArcLengthDimension dsArcLengthPartialDim = dsSketchMgr.InsertArcLengthDimensionPartial(dsArc, firstPoint, secondPoint, dimensionPosition, dimensionTextOverride);
```

```
            //Print information about partial arc length Dimension
            PrintArcLengthDimProperties(dsArcLengthDim);
        }
```

```
        private static void DrawJoggedDimension(SketchManager dsSketchMgr)
        {
            //Draw a circle
            double centerX = -7, centerY = -5, centerZ = 0;
            double radius = 3;
            Circle dsCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius);
```

```
            //Add jogged Dimension to circle
            double[] centerPositionOverride = new double[] { -12, -8, 0 };
            double[] jogLinePosition = new double[] { -11, -8, 0 };
            double[] dimensionPosition = new double[] { -10, -7.5, 0 };
            string dimensionTextOverride = string.Empty;
            JoggedDimension dsJoggedDimForCircle = dsSketchMgr.InsertJoggedDimensionCircle(dsCircle, centerPositionOverride, jogLinePosition, dimensionPosition, dimensionTextOverride);
```

```
            //Print information about jogged Dimension
            PrintJoggedDimProperties(dsJoggedDimForCircle);
```

```
            //Draw an arc
            centerX = 2;
            centerY = -6;
            double arcRadius = 3;
            double startAngle = 0.0;
            double endAngle = Math.PI / 3;
            CircleArc dsArc = dsSketchMgr.InsertArc(centerX, centerY, centerZ, arcRadius, startAngle, endAngle);
```

```
            //Add jogged Dimension to arc
            centerPositionOverride[0] = 7;
            centerPositionOverride[1] = -3;
            jogLinePosition[0] = 7;
            jogLinePosition[1] = -4;
            dimensionPosition[0] = 5.5;
            dimensionPosition[1] = -4.5;
            JoggedDimension dsJoggedDimForArc = dsSketchMgr.InsertJoggedDimensionArc(dsArc, centerPositionOverride, jogLinePosition, dimensionPosition, dimensionTextOverride);
```

```
            //Print information about jogged Dimension
            PrintJoggedDimProperties(dsJoggedDimForArc);
        }
```

```
        private static void DrawRadialDimension(SketchManager dsSketchMgr)
        {
            //Draw a circle
            double centerX = 2, centerY = 2, centerZ = 0;
            double radius = 3;
            Circle dsCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius);
```

```
            //Draw an arc
            centerX = 10;
            centerY = 2;
            double arcRadius = 3;
            double startAngle = 0.0;
            double endAngle = Math.PI / 3;
            CircleArc dsArc = dsSketchMgr.InsertArc(centerX, centerY, centerZ, arcRadius, startAngle, endAngle);
```

```
            //Add radius Dimension to circle
            double[] dimPosition = new double[] { 7, 6, 0 };
            string dimTextOverride = string.Empty;
            RadialDimension dsRadialCircleDim = dsSketchMgr.InsertRadialDimensionCircle(dsCircle, dimPosition, dimTextOverride);
```

```
            //Print information about radius Dimension
            PrintRadialDimProperties(dsRadialCircleDim);
```

```
            //Add radius Dimension to arc
            dimPosition[0] = 16;
            dimPosition[1] = 3;
            RadialDimension dsRadialArcDim = dsSketchMgr.InsertRadialDimensionArc(dsArc, dimPosition, dimTextOverride);
```

```
            //Print information about radius Dimension
            PrintRadialDimProperties(dsRadialArcDim);
        }
```

```
        private static void DrawDiameterDimension(SketchManager dsSketchMgr)
        {
            //Draw a circle
            double centerX = 2, centerY = 2, centerZ = 0;
            double radius = 3;
            Circle dsCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius);
```

```
            //Draw an arc
            centerX = 10;
            centerY = 2;
            double arcRadius = 3;
            double startAngle = 0.0;
            double endAngle = Math.PI / 3;
            CircleArc dsArc = dsSketchMgr.InsertArc(centerX, centerY, centerZ, arcRadius, startAngle, endAngle);
```

```
            //Add diameter Dimension to circle
            double[] dimPosition = new double[] { 3, 8, 0 };
            //No text override - empty string
            string dimTextOverride = string.Empty;
            DiameterDimension dsDiameterCircleDim = dsSketchMgr.InsertDiameterDimensionCircle(dsCircle, dimPosition, dimTextOverride);
```

```
            //Print information about diameter Dimension
            PrintDiameterDimProperties(dsDiameterCircleDim);
```

```
            //Add diameter Dimension to arc
            dimPosition[0] = 14;
            dimPosition[1] = 6;
            DiameterDimension dsDiameterArcDim = dsSketchMgr.InsertDiameterDimensionArc(dsArc, dimPosition, dimTextOverride);
```

```
            //Print information about diameter Dimension
            PrintDiameterDimProperties(dsDiameterArcDim);
        }
```

```
        private static void DrawRotatedDimension(SketchManager dsSketchMgr)
        {
            //Draw line
            double startX = 10;
            double startY = -5;
            double startZ = 0;
            double endX = 14;
            double endY = -5;
            double endZ = 0;
            Line dsLine = dsSketchMgr.InsertLine(startX, startY, startZ, endX, endY, endZ);
```

```
            //Draw rotated Dimension
            double[] extLine1Point = new double[] {startX, startY, startZ };
            double[] extLine2Point = new double[] { endX, endY, endZ };
            double[] dimensionLinePosition = new double[] { 16, -6, 0 };
            string dimTextOverride = string.Empty;
```

```
            //Angle 45 degrees (in radians)
            double rotationAngle = Math.PI / 4;
            RotatedDimension dsRotatedDim = dsSketchMgr.InsertRotatedDimension(extLine1Point, extLine2Point, dimensionLinePosition, dimTextOverride, rotationAngle);
```

```
            //Print information about rotated Dimension
            PrintRotatedDimProperties(dsRotatedDim);
        }
```

```
        private static void PrintArcLengthDimProperties(ArcLengthDimension dsArcLengthDim)
        {
            Debug.Print(Environment.NewLine + "  Arc length Dimension parameters...");
```

```
            //Get general Dimension object, which contains common Dimension properties,
            //and print them
            GeneralDimension dsGeneralDim = dsArcLengthDim.GetGeneralDimension();
            PrintGeneralDimProperties(dsGeneralDim);
```

```
            //Print specific parameters for arc length Dimension
            Debug.Print("    ArcSymbolType = " + dsArcLengthDim.ArcSymbolType);
            Debug.Print("    HasLeader = " + dsArcLengthDim.HasLeader);
            Debug.Print("    IsPartial = " + dsArcLengthDim.IsPartial);
```

```
            double x, y, z;
            //Get center point
            dsArcLengthDim.GetCenterPoint(out x, out y, out z);
            Debug.Print("    Center point (" + x + "," + y + "," + z + ")");
```

```
            //Get arc point
            dsArcLengthDim.GetArcPoint(out x, out y, out z);
            Debug.Print("    Arc point (" + x + "," + y + "," + z + ")");
```

```
            //Get extension line 1 point
            dsArcLengthDim.GetExtensionLine1Point(out x, out y, out z);
            Debug.Print("    Extension line 1 point (" + x + "," + y + "," + z + ")");
```

```
            //Get extension line 2 point
            dsArcLengthDim.GetExtensionLine2Point(out x, out y, out z);
            Debug.Print("    Extension line 2 point (" + x + "," + y + "," + z + ")");
        }
```

```
        private static void PrintRadialDimProperties(RadialDimension dsRadialDim)
        {
            Debug.Print(Environment.NewLine + "  Radius Dimension parameters...");
```

```
            //Get general Dimension object, which contains common Dimension properties,
            //and print them
            GeneralDimension dsGeneralDim = dsRadialDim.GetGeneralDimension();
            PrintGeneralDimProperties(dsGeneralDim);
```

```
            //Print specific parameters for radius Dimension
            double x, y, z;
            //Get center point
            dsRadialDim.GetCenterPoint(out x, out y, out z);
            Debug.Print("    Center point (" + x + "," + y + "," + z + ")");
```

```
            //Get defining point
            dsRadialDim.GetDefiningPoint(out x, out y, out z);
            Debug.Print("    Defining point (" + x + "," + y + "," + z + ")");
```

```
            //Print leader length value
            Debug.Print("    Leader length = " + dsRadialDim.LeaderLength);
        }
```

```
        private static void PrintDiameterDimProperties(DiameterDimension dsDiameterDim)
        {
            Debug.Print(Environment.NewLine + "  Diameter Dimension parameters...");
```

```
            //Get general Dimension object, which contains common Dimension properties,
            //and print them
            GeneralDimension dsGeneralDim = dsDiameterDim.GetGeneralDimension();
            PrintGeneralDimProperties(dsGeneralDim);
```

```
            //Print specific parameters for diameter Dimension
            double x, y, z;
            //Get defining point
            dsDiameterDim.GetDefiningPoint(out x, out y, out z);
            Debug.Print("    Defining point (" + x + "," + y + "," + z + ")");
```

```
            //Get far defining point
            dsDiameterDim.GetFarDefiningPoint(out x, out y, out z);
            Debug.Print("    Far defining point (" + x + "," + y + "," + z + ")");
```

```
            //Print leader length value
            Debug.Print("    Leader length = " + dsDiameterDim.LeaderLength);
        }
```

```
        private static void PrintJoggedDimProperties(JoggedDimension dsJoggedDim)
        {
            Debug.Print(Environment.NewLine + "  Jogged Dimension parameters...");
```

```
            //Get general Dimension object, which contains common Dimension properties,
            //and print them
            GeneralDimension dsGeneralDim = dsJoggedDim.GetGeneralDimension();
            PrintGeneralDimProperties(dsGeneralDim);
```

```
            //Print specific parameters for jogged Dimension
            Debug.Print("    Jog angle = " + dsJoggedDim.JogAngle);
```

```
            double x, y, z;
            //Get center point
            dsJoggedDim.GetCenterPoint(out x, out y, out z);
            Debug.Print("    Center point (" + x + "," + y + "," + z + ")");
```

```
            //Get chord point
            dsJoggedDim.GetChordPoint(out x, out y, out z);
            Debug.Print("    Chord point (" + x + "," + y + "," + z + ")");
```

```
            //Get jog point
            dsJoggedDim.GetJogPoint(out x, out y, out z);
            Debug.Print("    Jog point (" + x + "," + y + "," + z + ")");
```

```
            //Get override center point
            dsJoggedDim.GetOverrideCenterPoint(out x, out y, out z);
            Debug.Print("    Override center point (" + x + "," + y + "," + z + ")");
        }
```

```
        private static void PrintRotatedDimProperties(RotatedDimension dsRotatedDim)
        {
            Debug.Print(Environment.NewLine + "  Rotated Dimension parameters...");
```

```
            //Get general Dimension object, which contains common Dimension properties,
            //and print them
            GeneralDimension dsGeneralDim = dsRotatedDim.GetGeneralDimension();
            PrintGeneralDimProperties(dsGeneralDim);
```

```
            //Print specific parameters for rotated Dimension
            Debug.Print("    Rotation angle = " + dsRotatedDim.Rotation);
```

```
            double x, y, z;
            //Get Dimension line point
            dsRotatedDim.GetDimensionLinePoint(out x, out y, out z);
            Debug.Print("    Dimension line point (" + x + "," + y + "," + z + ")");
```

```
            //Get extension line 1 point
            dsRotatedDim.GetExtensionLine1Point(out x, out y, out z);
            Debug.Print("    Extension line 1 point (" + x + "," + y + "," + z + ")");
```

```
            //Get extension line 2 point
            dsRotatedDim.GetExtensionLine2Point(out x, out y, out z);
            Debug.Print("    Extension line 2 point (" + x + "," + y + "," + z + ")");
        }
```

```
        private static void PrintGeneralDimProperties(GeneralDimension dsGeneralDim)
        {
            //Get general Dimension object, which contains common Dimension properties,
            //and print them
            Debug.Print("    Dimension style = " + dsGeneralDim.DimensionStyle);
            Debug.Print("    Handle = " + dsGeneralDim.Handle);
            Debug.Print("    Measurement = " + dsGeneralDim.Measurement.ToString());
            Debug.Print("    Related = " + dsGeneralDim.Related.ToString());
            Debug.Print("    Text override = " + dsGeneralDim.TextOverride);
            Debug.Print("    TextRotation = " + dsGeneralDim.TextRotation);
```

```
            //Get text position
            double x, y;
            dsGeneralDim.GetTextPosition(out x, out y);
            Debug.Print("    Text position (" + x + "," + y + ")");
        }
    }
}
```
