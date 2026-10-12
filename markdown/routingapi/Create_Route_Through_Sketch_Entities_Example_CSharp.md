---
title: "Create Route Through Sketch Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Create_Route_Through_Sketch_Entities_Example_CSharp.htm"
---

# Create Route Through Sketch Entities Example (C#)

This example shows how to create a route by specifying sketch entity types and their IDs.

```
//--------------------------------------------
// Preconditions:
// 1. Add SOLIDWORKS Routing as an add-in
//    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Routing).
// 2. Add the SOLIDWORKS Routing interop assembly as a reference
//    (right-click the project in Project Explorer, click Add Reference,
//    browse install_dir\api\redist, and select
//    SolidWorks.Interop.SWRoutingLib.dll).
// 3. Open public_documents\tutorial\api\AutoRouteThroughSketchEntities.sldasm
// 4. Open the Immediate window.
// 5. Run the macro.
//
// Postconditions:
// 1. Creates a route using the sketch
//    points whose entity types and IDs were passed
//    to IAutoRoute::CreateRouteThroughSketchEntities.
// 2. Examine the the assembly document to verify.
// 3. Examine the Immediate window.
//
// NOTE: Because the assembly is used elsewhere,
// do not save any changes when closing it.
//-------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
using SolidWorks.Interop.SWRoutingLib;

namespace AutoRouteThroughPointsCSharp.csproj
{
    partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            AssemblyDoc swTopLevelAssembly = default(AssemblyDoc);
            RouteManager rtRouteManager = default(RouteManager);
            SelectionMgr swSelMgr = default(SelectionMgr);
            SketchPoint swSketchPt1 = default(SketchPoint);
            SketchPoint swSketchPt2 = default(SketchPoint);
            bool status = false;
            int routeStatus = 0;
            int[] sketchEntityTypes = new int[2];
            int[] sketchPt1IDs = new int[2];
            int[] sketchPt2IDs = new int[2];
            int[] sketchPtIDs = new int[2];

            // Get the active document
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;

            // Downcast from model document to assembly document
            swTopLevelAssembly = (AssemblyDoc)swModel;

            // Get the RouteManager from the top-level assembly
            rtRouteManager = (RouteManager)swTopLevelAssembly.GetRouteManager();

            if (rtRouteManager == null)
            {
                Debug.Print("No RouteManager found in top-level document");
                return;
            }

            // Get and edit the route
            status = swModelDocExt.SelectByID2("Route1@Harness_1-AutoRouteThroughSketchEntities-1@AutoRouteThroughSketchEntities", "ROUTEFABRICATED", 0, 0, 0, false, 0, null, 0);
            swModel.EditRoute();

            // Get the AutoRoute
            AutoRoute rtAutoRoute = default(AutoRoute);
            rtAutoRoute = (AutoRoute)rtRouteManager.GetAutoRoute();

            if (rtAutoRoute == null)
            {
                Debug.Print("No AutoRoute found");
                return;
            }

            //Assign the types of sketch entities to be sketch points
            sketchEntityTypes[0] = 0;
            sketchEntityTypes[1] = 0;

            // Get the IDs of the sketch points
            status = swModelDocExt.SelectByID2("Point3@3DSketch1@Harness_1-AutoRouteThroughSketchEntities-1@AutoRouteThroughSketchEntities", "EXTSKETCHPOINT", 0.0486125655897816, 0.0244300235589649, 0.0130597511505374, false, 0, null, 0);
            swSketchPt1 = (SketchPoint)swSelMgr.GetSelectedObject6(1, -1);
            sketchPt1IDs = (int[])swSketchPt1.GetID();
            Debug.Print("sketchPt1IDs: " + sketchPt1IDs[0] + ", " + sketchPt1IDs[1]);

            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Point7@3DSketch1@Harness_1-AutoRouteThroughSketchEntities-1@AutoRouteThroughSketchEntities", "EXTSKETCHPOINT", 0.145249999302905, -0.0158029634039849, -0.0222342355241044, false, 0, null, 0);
            swSketchPt2 = (SketchPoint)swSelMgr.GetSelectedObject6(1, -1);
            sketchPt2IDs = (int[])swSketchPt2.GetID();
            Debug.Print("sketchPt2IDs: " + sketchPt2IDs[0] + ", " + sketchPt2IDs[1]);

            // Create an array containing the first
            // member of each sketch point ID array
            // to pass to IAutoRoute::CreateRouteThroughSketchEntities
            sketchPtIDs[0] = sketchPt1IDs[0];
            sketchPtIDs[1] = sketchPt2IDs[0];

            // Create the Auto Route
            routeStatus = rtAutoRoute.CreateRouteThroughSketchEntities((int)swAutoRouteConversionMode_e.swOrthogonalAutoRouteMode, (int)swAutoRouteAutoTangencyMode_e.swAutoTangencyMode_ON, sketchEntityTypes, sketchPtIDs);

            // Clear selection
            swModel.ClearSelection2(true);

            // Return to editing the top-level assembly
            swTopLevelAssembly.EditAssembly();

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
