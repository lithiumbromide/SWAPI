---
title: "Create Swept Flange Using Gauge Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Swept_Flange_Using_Gauge_Table_Example_CSharp.htm"
---

# Create Swept Flange Using Gauge Table Example (C#)

This example shows how to create a swept flange using a bend table on a non-sheet metal part.

// ====================================================================================

// Preconditions:

// 1. Ensure that the paths to templates and gauge tables are valid.

// 2. Open an Immediate window.

// 3. Press F5 repeatedly and inspect the Immediate window and FeatureManager design tree as instructed.

//

// Postconditions:

```vb
 // 1. Creates Sketch1 for the sweep path.
 // 2. Creates Sketch2 for the sweep profile.
 // 3. Creates Swept Flange1 using a gauge table installed with SOLIDWORKS.
```

// 4. Displays gauge table parameters.

```vb
 // 5. Modifies Swept Flange1 to override the gauge number, bend radius, and gauge thickness.
```

// 6. Displays new gauge parameters.

// ============================================

```vb
 using System;
 using System.Collections.Generic;
 using System.Diagnostics;
 using System.Globalization;
 using System.IO;
 using System.Linq;
 using System.Reflection;
 using System.Runtime.CompilerServices;
 using System.Security;
 using System.Text;
 using System.Threading.Tasks;
 using Microsoft.VisualBasic;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace CreateSweptFlangeUsingGaugeTable_CSharp
 {
     public partial class SolidWorksMacro
     {
         public void Main()
         {

                 PartDoc swPart;
                 ModelDoc2 swModel;
                 Feature swFeat;
                 FeatureManager swFeatMgr;
                 SweptFlangeFeatureData swSweptFlangeFeatureData;
                 SweptFlangeFeatureData featData;
                 SheetMetalGaugeTableParameters smGaugeTableParam;
                 SketchSegment skSegment;
                 RefPlane myRefPlane;
                 int swFeatNameID;
                 Feature[] swSketch = new Feature[1];
                 bool boolstatus;
                 int errCode;
                 double swSheetWidth;
                 double swSheetHeight;
                 string gaugePath = null;
                 int gaugeCount;
                 string[] gaugeNumbers;
                 int i;
                 int radiiCount;
                 double[] radii;
                 string newgaugePath = null;

                 swSheetWidth = 0;
                 swSheetHeight = 0;
                 swModel = (ModelDoc2)swApp.NewDocument(@"E:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\Tutorial\part.prtdot", 0, swSheetWidth, swSheetHeight);

                 swPart = (PartDoc)swModel;
                 swModel = (ModelDoc2)swApp.ActiveDoc;

                 skSegment = swModel.SketchManager.Create3PointArc(-0.058601, -0.015313, 0.0, -0.003828, -0.021603, 0.0, 0.002265, -0.05642, 0.0);
                 swModel.ClearSelection2(true);
                 swModel.SketchManager.InsertSketch(true); // Sketch1
                 swModel.ClearSelection2(true);

                 boolstatus = swModel.Extension.SelectByID2("Point2@Sketch1", "EXTSKETCHPOINT", -0.003828, -0.021603, 0, true, 0, null, 0);
                 boolstatus = swModel.Extension.SelectByID2("Arc1@Sketch1", "EXTSKETCHSEGMENT", 0.00285760095397308, -0.0342380271903227, 0, true, 1, null, 0);

                 myRefPlane = (RefPlane)swModel.FeatureManager.InsertRefPlane(4, 0, 2, 0, 0, 0);

                 boolstatus = swModel.Extension.SelectByID2("Plane1", "PLANE", 0.0103901931573406, -0.00917038599747196, -0.00622490227027586, true, 0, null, 0);

                 swModel.SketchManager.InsertSketch(true);
                 skSegment = swModel.SketchManager.CreateLine(0.0, 0.0, 0.0, 0.0, 0.018316, 0.0);
                 skSegment = swModel.SketchManager.CreateLine(0.0, 0.018316, 0.0, 0.008362, 0.035435, 0.0);
                 swModel.ClearSelection2(true);
                 swModel.SketchManager.InsertSketch(true); // Sketch2

                 swFeatNameID = (int)swFeatureNameID_e.swFmSweptFlange;
                 swFeatMgr = swModel.FeatureManager;
                 swSweptFlangeFeatureData = (SweptFlangeFeatureData)swFeatMgr.CreateDefinition(swFeatNameID);

                 swModel.ClearSelection2(true);

                 // Select the sweep path
                 boolstatus = swModel.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
                 swSketch[0] = (Feature)((SelectionMgr)(swModel.SelectionManager)).GetSelectedObject6(1, -1);

                 swSweptFlangeFeatureData.Path = swSketch;

                 // Select the sweep profile
                 boolstatus = swModel.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, false, 0, null, 0);
                 swSweptFlangeFeatureData.Profile = (Feature)((SelectionMgr)(swModel.SelectionManager)).GetSelectedObject6(1, -1);

                 errCode = swSweptFlangeFeatureData.GetErrorCodes();
                 Debug.Print("Swept flange definition error code: " + System.Convert.ToString(errCode));

                 System.Diagnostics.Debugger.Break(); // Inspect the Immediate window for the swept flange definition error

                 swSweptFlangeFeatureData.UseMaterialSheetMetalParameters = false;
                 swSweptFlangeFeatureData.UseGaugeTable = true;

                 Debug.Print("Use gauge table? " + System.Convert.ToString(swSweptFlangeFeatureData.UseGaugeTable));

                 smGaugeTableParam = (SheetMetalGaugeTableParameters)swSweptFlangeFeatureData.GetGaugeTableParameters();
                 boolstatus = smGaugeTableParam.GetGaugeTablePath(gaugePath);

                 if (boolstatus == false)
                     smGaugeTableParam.SetGaugeTablePath(@"E:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\LANG\ENGLISH\SHEET METAL GAUGE TABLES\BEND ALLOWANCE MM SAMPLE.XLS");

                 boolstatus = smGaugeTableParam.GetGaugeTablePath(gaugePath);
                 Debug.Print("Got gauge table path? " + System.Convert.ToString(boolstatus));
                 Debug.Print("Gauge table path: " + gaugePath);
                 Debug.Print("Process: " + smGaugeTableParam.Process);

                 gaugeCount = smGaugeTableParam.GetGaugeNumberCount();
                 Debug.Print("Gauge number count: " + System.Convert.ToString(gaugeCount));

                 Debug.Print("Available gauge numbers: ");

                 gaugeNumbers = (string[])smGaugeTableParam.GetAvailableGaugeNumbers();

                 for (i = 0; i <= gaugeCount - 1; i++)
                     Debug.Print(gaugeNumbers[i]);
                 Debug.Print("Current gauge number: " + smGaugeTableParam.GetCurrentGaugeNumber());

                 System.Diagnostics.Debugger.Break(); // Inspect the Immediate window for the current gauge number

                 radiiCount = smGaugeTableParam.GetRadiiCount();
                 Debug.Print("Bend radii count: " + System.Convert.ToString(smGaugeTableParam.GetRadiiCount()));

                 Debug.Print("Available bend radii: ");
                 radii = (double[])smGaugeTableParam.GetAvailableRadii();
                 for (i = 0; i <= radiiCount - 1; i++)
                     Debug.Print(radii[i].ToString());
                 Debug.Print("Current bend radius: " + System.Convert.ToString(smGaugeTableParam.GetCurrentRadius()));
                 Debug.Print("Thickness: " + System.Convert.ToString(smGaugeTableParam.GetThickness()));
                 Debug.Print("Override thickness? " + System.Convert.ToString(smGaugeTableParam.OverrideThickness));
                 Debug.Print("Override bend radius? " + System.Convert.ToString(smGaugeTableParam.OverrideRadius));
                 Debug.Print("Reverse direction? " + System.Convert.ToString(smGaugeTableParam.ReverseDirection));

                 System.Diagnostics.Debugger.Break(); // Inspect the Immediate window for current bend radius and current gauge thickness

                 swSweptFlangeFeatureData.SetGaugeTableParameters(smGaugeTableParam);

                 swFeat = swFeatMgr.CreateFeature(swSweptFlangeFeatureData);

                 errCode = swSweptFlangeFeatureData.GetErrorCodes();
                 Debug.Print("Swept flange creation error code: " + System.Convert.ToString(errCode));
                 swModel.ClearSelection2(true);

                 System.Diagnostics.Debugger.Break(); // Inspect the Immediate window for the swept flange creation status
                                                      // Observe Sheet-Metal, Swept Flange1, and Flat-Pattern in the FeatureManager design tree

                 // Set new gauge number and override gauge thickness and bend radius
                 featData = (SweptFlangeFeatureData)swFeat.GetDefinition();
                 smGaugeTableParam = (SheetMetalGaugeTableParameters)featData.GetGaugeTableParameters();

                 smGaugeTableParam.ReverseDirection = true;
                 smGaugeTableParam.SetCurrentGaugeNumber("Gauge 3");
                 smGaugeTableParam.SetThickness(0.006, true);
                 smGaugeTableParam.SetRadius(0.006, true);

                 featData.SetGaugeTableParameters(smGaugeTableParam);
                 boolstatus = swFeat.ModifyDefinition(featData, swModel, null)
                 Debug.Print("Swept flange modification status: " + System.Convert.ToString(boolstatus));

                 System.Diagnostics.Debugger.Break(); // Inspect the Immediate window for the swept flange modification status

                 // Get new gauge number
                 boolstatus = featData.AccessSelections(swModel, null);
                 smGaugeTableParam = (SheetMetalGaugeTableParameters)featData.GetGaugeTableParameters();

                 boolstatus = smGaugeTableParam.GetGaugeTablePath(newgaugePath);
                 Debug.Print("Got gauge table path? " + System.Convert.ToString(boolstatus));
                 Debug.Print("Gauge table path: " + newgaugePath);

                 Debug.Print("Process: " + smGaugeTableParam.Process);

                 gaugeCount = smGaugeTableParam.GetGaugeNumberCount();
                 Debug.Print("Gauge number count: " + System.Convert.ToString(gaugeCount));
                 Debug.Print("Available gauge numbers: ");
                 gaugeNumbers = (string[])smGaugeTableParam.GetAvailableGaugeNumbers();

                 for (i = 0; i <= gaugeCount - 1; i++)
                     Debug.Print(gaugeNumbers[i]);
                 Debug.Print("Current gauge number: " + smGaugeTableParam.GetCurrentGaugeNumber());

                 System.Diagnostics.Debugger.Break(); // Inspect the Immediate window for the new gauge number

                 // Get new bend radius and gauge thickness
                 radiiCount = smGaugeTableParam.GetRadiiCount();
                 Debug.Print("Bend radii count: " + System.Convert.ToString(radiiCount));

                 Debug.Print("Available bend radii: ");
                 radii = (double[])smGaugeTableParam.GetAvailableRadii();
                 for (i = 0; i <= radiiCount - 1; i++)
                     Debug.Print(radii[i].ToString());
                 Debug.Print("Current bend radius: " + System.Convert.ToString(smGaugeTableParam.GetCurrentRadius()));

                 Debug.Print("Thickness: " + System.Convert.ToString(smGaugeTableParam.GetThickness()));
                 Debug.Print("Override thickness? " + System.Convert.ToString(smGaugeTableParam.OverrideThickness));
                 Debug.Print("Override bend radius? " + System.Convert.ToString(smGaugeTableParam.OverrideRadius));
                 Debug.Print("Reverse direction? " + System.Convert.ToString(smGaugeTableParam.ReverseDirection));

                 featData.ReleaseSelectionAccess();

                 System.Diagnostics.Debugger.Break(); // Inspect the Immediate window for the new bend radius and gauge thickness
             }

     // The SldWorks swApp variable is pre-assigned for you.
     public SldWorks swApp;

     }
 }
```
