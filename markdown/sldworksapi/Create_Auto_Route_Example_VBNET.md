---
title: "Create Auto Route Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Auto_Route_Example_VBNET.htm"
---

# Create Auto Route Example (VB.NET)

This example shows how to connect two points using the Auto Route interface.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. In SOLIDWORKS Design, click Tools > Add-Ins > SOLIDWORKS Routing.
 ' 2. In the IDE, right-click the project, select Add Reference,
 '      browse  install_dir\api\redist, and click
 '    SolidWorks.Interop.SWRoutingLib.dll).
 ' 3. In Tools > Options > System Options > Routing > Routing File Locations,
 '    add the locations of your SOLIDWORKS Design routing files.
 ' 4. Open a routing assembly that contains Route1 and two sketch points.
 ' 5. Modify the swModel.Extension.SelectByID2 parameters to select two sketch
 '    points through which to auto route.
 ' 6. Select the assembly that contains Route1 in the FeatureManager design tree.
 ' 7. Open an Immediate Window.
 '
 ' Postconditions: Auto Route connects the selected sketch points.
 '
 ' NOTE: Because the assembly is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.SWRoutingLib
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()
         Dim swModel As ModelDoc2
         Dim swTopLevelAssembly As AssemblyDoc
         Dim rtRouteManager As RouteManager
         Dim autoRoute As autoRoute
         Dim resultCode, boolstatus As Integer

         swModel = swApp.ActiveDoc
         swTopLevelAssembly = swModel

         ' Get the RouteManager from the top-level assembly
         rtRouteManager = swTopLevelAssembly.GetRouteManager
         If rtRouteManager Is Nothing Then
             Debug.Print("No RouteManager found in top-level document: " & swTopLevelAssembly.GetPathName)
             Exit Sub
         End If

         rtRouteManager.EditRoute()
         autoRoute = rtRouteManager.GetAutoRoute
         autoRoute.ShowGuidelines()
         boolstatus = swModel.Extension.SelectByID2("Point3", "SKETCHPOINT", -0.457835, 0.10795, -0.2032, True, 0, Nothing, 0)
         boolstatus = swModel.Extension.SelectByID2("Point8", "SKETCHPOINT", -0.218948, 0.0508, -0.470281, True, 0, Nothing, 0)
         resultCode = autoRoute.CreatePointToPointAutoRoute(2)
         rtRouteManager.ExitRoute()
         swTopLevelAssembly.EditAssembly()

     End Sub

     Public swApp As SldWorks

 End  Class
```
