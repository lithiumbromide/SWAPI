---
title: "Get Minimum Bend Radii of Wires Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_Minimum_Bend_Radii_of_Wires_Example_CSharp.htm"
---

# Get Minimum Bend Radii of Wires Example (C#)

This example shows how to get:

- minimum bend radius for the bundle of wires in each route segment,
- minimum bend radius for each route segment, and
- types of routes.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Add SOLIDWORKS Routing as an add-in
//   (in SOLIDWORKS select Tools > Add-Ins > SOLIDWORKS Routing).
// 2. Add Solidworks.interop.SwRoutingLib.dll as a reference
//   (in the IDE right-click the project,
//    select Add Reference, and browse install_dir\api\redist).
// 3. Open public_documents\samples\tutorial\api\RoutingAssem1.sldasm.
// 4. Open the Immediate window.
// 5. Run the macro.
//
// Postconditions: Examine the Immediate window.
//
// NOTE: Because the assembly document is used elsewhere, do not save
// any changes when closing it.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using SolidWorks.Interop.SWRoutingLib;
using System.Diagnostics;

namespace BundleMinimumBendRadiusCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDoc = default(ModelDocExtension);
            AssemblyDoc swTopLevelAssembly = default(AssemblyDoc);
            RouteManager rtRouteManager = default(RouteManager);
            bool bRetVal = false;

            // Get the active document
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDoc = (ModelDocExtension)swModel.Extension;

            // Downcast from model document to assembly document
            swTopLevelAssembly = (AssemblyDoc)swModel;

            // Get the RouteManager from the top-level assembly
            // Use selection tied to the current document, which is the
            // top-level assembly, so get the RouteManager from there
            // instead of from the route subassembly
            rtRouteManager = (RouteManager)swTopLevelAssembly.GetRouteManager();

            if (rtRouteManager == null)
            {
                Debug.Print("No RouteManager found in top-level document");
                return;
            }

            // Select route in subassembly
            bRetVal = swModelDoc.SelectByID2("Route1@Harness1^RoutingAssem1-1@RoutingAssem1", "ROUTEFABRICATED", 0, 0, 0, false, 0, null, 0);

            swModel.EditRoute();

            // Clear selection
            swModel.ClearSelection2(true);

            // Select the 3D Sketch
            bRetVal = swModelDoc.SelectByID2("3DSketch1@Harness1-RoutingAssem1-1@RoutingAssem1", "SKETCH", 0, 0, 0, false, 0, null, 0);

            // Edit the 3D Sketch
            Debug.Print("Spline1:");
            TestRoute(swModelDoc, rtRouteManager, "Spline1");
            Debug.Print("Spline2:");
            TestRoute(swModelDoc, rtRouteManager, "Spline2");

            // Stop editing
            swModel.Insert3DSketch2(true);

            // Return to editing the top-level assembly
            swTopLevelAssembly.EditAssembly();

        }
        private void TestRoute(ModelDocExtension swModelDoc, RouteManager rtRouteManager, string strSketchSegmentName)
        {
            // Select a sketch segment
            bool bRetVal = false;
            bRetVal = swModelDoc.SelectByID2(strSketchSegmentName, "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);

            if ((!(bRetVal == false)))
            {
                // Get the RouteProperty for the selected sketch segment
                ElectricalRouteProperty rtElecRouteProperty = default(ElectricalRouteProperty);
                rtElecRouteProperty = (ElectricalRouteProperty)rtRouteManager.GetRouteProperty();

                if ((rtElecRouteProperty != null))
                {
                    Debug.Print("  Bundle minimum bend radius      = " + rtElecRouteProperty.BundleMinimumBendRadius);
                    int rtProp = 0;
                    RouteProperty rtProperty = default(RouteProperty);
                    rtProperty = (RouteProperty)rtRouteManager.GetRouteProperty();
                    Debug.Print(" Minimum bend radius              = " + rtProperty.MinimumBendRadius);
                    rtProp = rtProperty.RouteType;
                    switch (rtProp)
                    {
                        case (int)swRouteType_e.swRouteType_Electrical:
                            Debug.Print("  Type                            = Electrical");
                            break;
                    }
                }
            }
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
