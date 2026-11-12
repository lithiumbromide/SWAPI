---
title: "Create Auto Route Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Auto_Route_Example_CSharp.htm"
---

# Create Auto Route Example (C#)

This example shows how to connect two points using the Auto Route interface.

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 // 1. In SOLIDWORKS Design, click Tools > Add-Ins > SOLIDWORKS Routing.
 // 2. In the IDE, right-click the project, select Add Reference,
 //      browse  install_dir\api\redist, and click
 //    SolidWorks.Interop.SWRoutingLib.dll).
 // 3. In Tools > Options > System Options > Routing > Routing File Locations,
 //    add the locations of your SOLIDWORKS Design routing files.
 // 4. Open a routing assembly that contains Route1 and two sketch points.
 // 5. Modify the swModel.Extension.SelectByID2 parameters to select two sketch
 //    points through which to auto route.
 // 6. Select the assembly that contains Route1 in the FeatureManager design tree.
 // 7. Open an Immediate Window.
 //
 // Postconditions: Auto Route connects the selected sketch points.
 //
 // NOTE: Because the assembly is used elsewhere, do not save changes.
 //---------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.SWRoutingLib;
 using System;
 using System.Diagnostics;
 namespace CreateAutoRoute_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             AssemblyDoc swTopLevelAssembly = default(AssemblyDoc);
             RouteManager rtRouteManager = default(RouteManager);
             AutoRoute autoRoute = default(AutoRoute);
             int resultCode = 0;
             Boolean boolstatus = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swTopLevelAssembly = (AssemblyDoc)swModel;

             // Get the RouteManager from the top-level assembly
             rtRouteManager = (RouteManager)swTopLevelAssembly.GetRouteManager();
             if (rtRouteManager == null)
             {
                 Debug.Print("No RouteManager found in top-level document");
                 return;
             }

             rtRouteManager.EditRoute();
             autoRoute = (AutoRoute)rtRouteManager.GetAutoRoute();
             autoRoute.ShowGuidelines();
             boolstatus = swModel.Extension.SelectByID2("Point3", "SKETCHPOINT", -0.457835, 0.10795, -0.2032, true, 0, null, 0);
             boolstatus = swModel.Extension.SelectByID2("Point8", "SKETCHPOINT", -0.218948, 0.0508, -0.470281, true, 0, null, 0);
             resultCode = autoRoute.CreatePointToPointAutoRoute(2);
             rtRouteManager.ExitRoute();

             swTopLevelAssembly.EditAssembly();
         }

         public SldWorks swApp;

     }
 }
```
