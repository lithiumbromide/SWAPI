---
title: "Create a Flattened Route Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Create_a_Flattened_Route_Example_VB.htm"
---

# Create a Flattened Route Example (VBA)

This example shows how to create an annotation type flattened route and its drawing.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add SOLIDWORKS Routing as an add-in
 '   (in SOLIDWORKS select Tools > Add-Ins > SOLIDWORKS Routing).
 ' 2. Add the SOLIDWORKS <version> Routing Type Library as a reference
 '   (in the IDE select Tools > References).
 ' 3. In Tools > Options > System Options > Routing > Routing File Locations,
 '    add locations of your SOLIDWORKS Routing files.
 ' 4. Open public_documents\samples\tutorial\api\5connector.sldasm.
 ' 5. Ensure that the specified templates exist.
 '
 ' Postconditions:
 ' 1. FeatureManager design tree shows AnnotateFlattenedRoute1 and hides Route1.
 ' 2. Sheet1 of 5connector.SLDDRW has the a2 - landscape format and contains:
 '    * drawing view
 '    * five electrical connector tables
 '    * circuit-summary table
 '    * electrical BOM table.
 '
 ' NOTE: Because this assembly is used elsewhere,
 ' do not save any changes to it.
 '---------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.AssemblyDoc
 Dim boolstatus As Boolean
 Dim longstatus As Long

Sub main()
```

```vb
Set swApp = Application.SldWorks
Set Part = swApp.ActiveDoc
boolstatus = Part.Extension.SelectByID2("5connector.SLDASM", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
Dim RouteMgr As SWRoutingLib.RouteManager
Set RouteMgr = Part.GetRouteManager
longstatus = RouteMgr.CreateFlattenRoute(1, 1, 0#, 0#, 1, True, "<SldWorks_install_dir>\lang\english\sheetformat\a2 - landscape.slddrt", "install_dir\lang\english\bom-standard.sldbomtbt", "install_dir\lang\english\bom-circuit-summary.sldbomtbt", "install_dir\lang\english\connector-table.sldtbt", True)
```

```vb
End Sub
```
