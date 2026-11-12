---
title: "Select Connector Using Highlight Search Tool Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Select_Connector_Using_Highlight_Search_Tool_Example_CSharp.htm"
---

# Select Connector Using Highlight Search Tool Example (C#)

This example shows how to select a connector using the SOLIDWORKS Routing Highlight Search tool.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
  // 1. Open an assembly document containing an electrical route and
 //    connector (3pin) female-1.
 // 2. In SOLIDWORKS, select Tools > Add-Ins > SOLIDWORKS Routing.
  // 3. In Tools > Options > System Options > Routing > Routing File Locations,
  //    click Launch Routing Library Manager and set the locations of your
 //    SOLIDWORKS Routing files.
 // 4. In the IDE, right-click the project,
 //    click Add Reference, browse install_dir\api\redist, select
 //    SolidWorks.Interop.SwRoutingLib.dll, and click OK.
 // 5. Open an Immediate window.
 //
 // Postconditions:
 // 1. Finds the specified component.
  // 2. Prints the number of instances of the specified component.
 // 3. Selects the component in the FeatureManager design tree.
  // 4. Prints the number of components attached to the selected component.
  // 5. Colors the selected component gray in the graphics area.
 // 6. Inspect the Immediate window, the FeatureManager design tree,
 //    and the graphics area.
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

 namespace SelectConnector_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         AssemblyDoc swAssemblyDoc;
         RouteManager rtRouteMgr;
         AdvancedRouteSelector rtAdvancedRouteSelector;
         long nbrConnectors;
         object selName;

         object attachNames;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swAssemblyDoc = (AssemblyDoc)swModel;

             // Get SOLIDWORKS RouteManager
             rtRouteMgr = (RouteManager)swAssemblyDoc.GetRouteManager();

             // Access the Highlight Search tool
             rtAdvancedRouteSelector = (AdvancedRouteSelector)rtRouteMgr.GetAdvancedRouteSelector();

             // Find the specified component and add it to the selection list
             nbrConnectors = rtAdvancedRouteSelector.Find("connector (3pin) female-1", (int)swRoutingSearchType_e.swRoutingComponentSearch, true, false);
             Debug.Print("Number of instances of the specified component in this assembly: " + nbrConnectors);

             // Get the number of components attached to the selected component
             Debug.Print("Number of components attached to the specified connector: " + rtAdvancedRouteSelector.getAttachedComponentsCount(0));

             // Color the selection gray
             rtAdvancedRouteSelector.SetSelectionColor(true, 0);

             // Select the component and return an array of its attached components
             attachNames = rtAdvancedRouteSelector.Select(0, false, null, (int)swAdvancedRouteSelectionOutput_e.swBoth, out selName);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
