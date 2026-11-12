---
title: "Insert Lofted Bend Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Lofted_Bend_Feature_Example_CSharp.htm"
---

# Insert Lofted Bend Feature Example (C#)

This example shows how to insert a lofted bend feature in a sheet metal part and get the lofted bend feature data.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens a new part.
// 2. Creates a sketch on Front Plane, a reference plane parallel to
//    Front Plane, and a sketch on that reference plane.
// 3. Selects the sketches and inserts a lofted bend.
// 4. Inspect the Immediate window, FeatureManager design, and graphics area.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {

        ModelDoc2 Part;
        Feature feat;
        RefPlane refPlane;
        SketchSegment skSegment;
        LoftedBendsFeatureData lbfd;

        bool boolstatus;

        public void Main()
        {
            // Open new part and create a sketch, a reference plane, and another sketch
            // on that reference plane
            Part = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
            boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            Part.ClearSelection2(true);
            Part.SketchManager.InsertSketch(true);
            skSegment = (SketchSegment)Part.SketchManager.CreateLine(0.0, 0.0, 0.0, 0.024074, 0.024074, 0.0);
            skSegment = (SketchSegment)Part.SketchManager.CreateLine(0.024074, 0.024074, 0.0, 0.076952, 0.024074, 0.0);
            skSegment = (SketchSegment)Part.SketchManager.CreateLine(0.076952, 0.024074, 0.0, 0.101026, 0.0, 0.0);
            Part.ClearSelection2(true);
            Part.SketchManager.InsertSketch(true);
            boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
            refPlane = (RefPlane)Part.FeatureManager.InsertRefPlane(8, 0.05, 0, 0, 0, 0);
            Part.ClearSelection2(true);
            boolstatus = Part.Extension.SelectByID2("Plane1", "PLANE", 0, 0, 0, false, 0, null, 0);
            Part.SketchManager.InsertSketch(true);
            skSegment = (SketchSegment)Part.SketchManager.CreateLine(-0.031383, 0.0, 0.0, 0.047146, 0.060616, 0.0);
            skSegment = (SketchSegment)Part.SketchManager.CreateLine(0.047146, 0.060616, 0.0, 0.058036, 0.060616, 0.0);
            skSegment = (SketchSegment)Part.SketchManager.CreateLine(0.058036, 0.060616, 0.0, 0.129686, 0.002436, 0.0);
            Part.ClearSelection2(true);
            Part.SketchManager.InsertSketch(true);

            // Select the sketches for the lofted bend feature
            boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 1, null, 0);
            boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, true, 1, null, 0);

            // Insert a lofted bend feature with two bends
            feat = Part.FeatureManager.InsertSheetMetalLoftedBend2(0, 0.0007366, false, 0.0007366, true, (int)swLoftedBendFacetOptions_e.swBendsPerTransitionSegment, 0, 2, 0, 0);

            // Get lofted bend feature data
            lbfd = (LoftedBendsFeatureData)feat.GetDefinition();
            Debug.Print("Number of sketch profiles in this feature: " + lbfd.GetProfileCount());
            Debug.Print("Thickness: " + lbfd.Thickness);
            Debug.Print("Reverse thickness direction? " + lbfd.Direction);
            Debug.Print("Faceting option as defined in swLoftedBendFacetOptions_e: " + lbfd.FacetingOption);
            Debug.Print("Faceting option value: " + lbfd.FacetValue);
            Debug.Print("Formed? " + lbfd.FormedMethod);
            Debug.Print("Calculate facet transitions using vertexes? " + lbfd.ReferToEndPoint);

        }

        public SldWorks swApp;

    }
}
```
