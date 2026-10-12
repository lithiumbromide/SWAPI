---
title: "Get Route Properties of Selected Sketch Segment Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_RouteProperty_from_Selected_Sketch_Segment_Example_CSharp.htm"
---

# Get Route Properties of Selected Sketch Segment Example (C#)

This example shows how to get the route and covering properties of a sketch segment.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. In SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Routing.
 // 2. In Tools > Options > System Options > Routing > Routing File Locations,
 //    click Launch Routing Library Manager and set the locations of your
 //    SOLIDWORKS Routing files.
 // 3. In the IDE, right-click the project,
 //    click Add Reference, browse install_dir\api\redist, click
 //    SolidWorks.Interop.SwRoutingLib.dll, and click OK.
 // 4. Open public_documents\samples\tutorial\api\RoutingAssem1.sldasm.
 // 5. Add a covering to the longest cable.
 // 6. Open an Immediate window.
 //
 // Postconditions:
 // 1. Edits Route1@Harness1^RoutingAssem1-1@RoutingAssem1.
 // 2. Selects the Spline1 sketch segment.
 // 3. Attempts to set the length of Spline1.
 // 4. Prints the route and covering properties of Spline1.
 // 5. Inspect the Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.SWRoutingLib;
 using System.Runtime.InteropServices;

 namespace GetRouteProperties_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         ModelDocExtension swModelDoc;
         AssemblyDoc swTopLevelAssembly;
         RouteManager rtRouteManager;
         Covering rtCovering;
         bool bRetVal;

         RouteProperty rtRouteProperty;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDoc = swModel.Extension;
             swTopLevelAssembly = (AssemblyDoc)swModel;
             rtRouteManager = (RouteManager)swTopLevelAssembly.GetRouteManager();
             if (rtRouteManager == null)
             {
                 Debug.Print("No RouteManager found in top-level document: " + swModel.GetPathName());
                 return;
             }

             // Select the route
             bRetVal = swModelDoc.SelectByID2("Route1@Harness1^RoutingAssem1-1@RoutingAssem1", "ROUTEFABRICATED", 0, 0, 0, false, 0, null, 0);
             swModel.EditRoute();

             TestRoute(swModelDoc, rtRouteManager);

             rtRouteManager.ExitRoute();
             swTopLevelAssembly.EditAssembly();

         }

         private void TestRoute(ModelDocExtension swModelDoc, RouteManager rtRouteManager)
         {
             bRetVal = swModelDoc.SelectByID2("Spline1", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);

             if ((!(bRetVal == false)))
             {
                 rtRouteProperty = rtRouteManager.GetRouteProperty();

                 if ((rtRouteProperty != null))
                 {
                     double dOriginalLength = 0;
                     dOriginalLength = rtRouteProperty.GetFixedLength();

                     double dNewLength = 0;
                     dNewLength = dOriginalLength * 1.1;

                     int lResult = 0;
                     lResult = rtRouteProperty.SetFixedLength(dNewLength);

                     double dFinalLength = 0;
                     dFinalLength = rtRouteProperty.GetFixedLength();

                     Debug.Print("Spline1");
                     Debug.Print("  Fixed length? " + (dOriginalLength < dFinalLength));
                     if ((dOriginalLength < dFinalLength))
                     {
                         Debug.Print("  Original fixed length (T0): " + dOriginalLength);
                         Debug.Print("  Set fixed length result code as defined in swSetRouteFixedLengthError_e: " + lResult);
                         Debug.Print("  Final fixed length (T1): " + dFinalLength);
                     }

                     Debug.Print("  Bend radius: " + rtRouteProperty.BendRadius);
                     Debug.Print("  Minimum bend radius: " + rtRouteProperty.MinimumBendRadius);
                     Debug.Print("  Route type as defined in swRouteType_e: " + rtRouteProperty.RouteType);

                     if ((rtRouteProperty.HasCovering))
                     {
                         rtCovering = rtRouteProperty.GetCovering();
                         Debug.Print("  Covering properties:");
                         Debug.Print("    Name: " + rtCovering.Name);
                         Debug.Print("    Color: " + rtCovering.Color);
                         Debug.Print("    Outer diameter: " + rtCovering.OuterDiameter);
                         Debug.Print("    Part number: " + rtCovering.PartNumber);
                     }

                     Debug.Print("");

                 }

             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
