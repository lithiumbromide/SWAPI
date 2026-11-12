---
title: "Create Auto Route Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Auto_Route_Example_VB.htm"
---

# Create Auto Route Example (VBA)

This example shows how to connect two points using the Auto Route interface.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. In SOLIDWORKS Design, click Tools > Add-Ins > SOLIDWORKS Routing.
 ' 2. In the IDE, click Tools > References and select
 '    SOLIDWORKS version Routing Type Library.
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
Dim swApp As SldWorks.SldWorks
 Option Explicit
Sub main()
```

```vb
Dim swModel As SldWorks.ModelDoc2
Dim swTopLevelAssembly As SldWorks.AssemblyDoc
Dim rtRouteManager As SWRoutingLib.RouteManager
Dim autoRoute As SWRoutingLib.autoRoute
Dim resultCode, boolstatus As Long
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swTopLevelAssembly = swModel
' Get the RouteManager from the top-level assembly
Set rtRouteManager = swTopLevelAssembly.GetRouteManager
If rtRouteManager Is Nothing Then
Debug.Print "No RouteManager found in top-level document: " & swTopLevelAssembly.GetPathName
Exit Sub
End If
rtRouteManager.EditRoute
Set autoRoute = rtRouteManager.GetAutoRoute
autoRoute.ShowGuidelines
boolstatus = swModel.Extension.SelectByID2("Point3", "SKETCHPOINT", -0.457835, 0.10795, -0.2032, True, 0, Nothing, 0)
boolstatus = swModel.Extension.SelectByID2("Point8", "SKETCHPOINT", -0.218948, 0.0508, -0.470281, True, 0, Nothing, 0)
resultCode = autoRoute.CreatePointToPointAutoRoute(swOrthogonalMode)
rtRouteManager.ExitRoute
swTopLevelAssembly.EditAssembly
```

```vb
End Sub
```
